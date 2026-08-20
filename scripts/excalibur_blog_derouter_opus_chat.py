#!/usr/bin/env python3
"""Derouter REST chat/completions — единственный «мозг» текстовых ролей фабрики.

POST https://api.derouter.ai/openai/v1/chat/completions
Fallback: https://api.apikey.cloud/openai/v1/chat/completions

Auth: DEROUTER_API_KEY (Cloud Secrets only). Model: claude-opus-5 or DEROUTER_TEXT_MODEL.
Forbidden: mcp-derouter/start-mcp.sh, Cursor Composer/Auto fallback for role prose.

На успех пишет stamp JSON (model, endpoint, request id, usage) рядом со статьёй
или в memory/setup/ для smoke.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_API_KEY_ENV = "DEROUTER_API_KEY"
DEFAULT_MODEL_ENV = "DEROUTER_TEXT_MODEL"
DEFAULT_MODEL = "claude-opus-5"
PRIMARY_ENDPOINT = "https://api.derouter.ai/openai/v1/chat/completions"
FALLBACK_ENDPOINT = "https://api.apikey.cloud/openai/v1/chat/completions"
DEFAULT_TIMEOUT_SECONDS = 300
MIN_TIMEOUT_SECONDS = 60
DEFAULT_MAX_RETRIES = 1
DEFAULT_RETRY_WAIT_SECONDS = 5

VALID_ROLES = frozenset(
    {
        "scout",
        "research",
        "title",
        "writer",
        "sol",
        "description",
        "cover-text",
        "schema",
        "cover-scene",
        "smoke",
    }
)


class DerouterChatError(RuntimeError):
    """Fatal API or configuration error."""


class DerouterChatRetryable(DerouterChatError):
    """Retryable HTTP/network failure."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_text_arg(*, inline: str | None, path: str | None, label: str) -> str:
    if path:
        p = Path(path)
        if not p.is_file():
            raise DerouterChatError(f"{label} file not found: {path}")
        return p.read_text(encoding="utf-8")
    if inline is not None:
        return inline
    raise DerouterChatError(f"Provide --{label.replace(' ', '-')} or --{label.replace(' ', '-')}-file")


def resolve_model(override: str | None = None) -> str:
    if override and override.strip():
        model = override.strip()
    else:
        model = (os.environ.get(DEFAULT_MODEL_ENV) or DEFAULT_MODEL).strip()
    if not model:
        raise DerouterChatError(f"{DEFAULT_MODEL_ENV} empty; must stay Claude Opus 5 family")
    lower = model.lower()
    if "opus" not in lower:
        raise DerouterChatError(
            f"Model {model!r} is not Claude Opus family; set {DEFAULT_MODEL_ENV}=claude-opus-5"
        )
    return model


def is_retryable_http(status: int) -> bool:
    return status in {401, 403, 408, 429, 500, 502, 503, 504, 524}


def http_chat_post(
    endpoint: str,
    api_key: str,
    payload: dict[str, Any],
    *,
    timeout: int,
) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if is_retryable_http(exc.code):
            raise DerouterChatRetryable(
                f"Derouter HTTP {exc.code}: {body[:500]}", status=exc.code
            ) from exc
        raise DerouterChatError(f"Derouter HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise DerouterChatRetryable(f"Derouter network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise DerouterChatError(f"Derouter returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterChatError("Derouter returned a non-object JSON response")
    return parsed


def extract_assistant_text(response: dict[str, Any]) -> str:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        raise DerouterChatError("Derouter response missing choices")
    first = choices[0]
    if not isinstance(first, dict):
        raise DerouterChatError("Derouter choices[0] is not an object")
    message = first.get("message")
    if not isinstance(message, dict):
        raise DerouterChatError("Derouter choices[0].message missing")
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        raise DerouterChatError("Derouter returned empty assistant content")
    return content


def call_derouter_chat(
    *,
    system_prompt: str,
    user_prompt: str,
    model: str,
    timeout: int,
    max_retries: int,
) -> tuple[str, dict[str, Any], str]:
    api_key = os.environ.get(DEFAULT_API_KEY_ENV, "").strip()
    if not api_key:
        raise DerouterChatError(f"{DEFAULT_API_KEY_ENV} missing")

    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    endpoints = [PRIMARY_ENDPOINT, FALLBACK_ENDPOINT]
    last_error: Exception | None = None

    for endpoint in endpoints:
        attempts = max_retries + 1
        for attempt in range(attempts):
            try:
                response = http_chat_post(endpoint, api_key, payload, timeout=timeout)
                text = extract_assistant_text(response)
                return text, response, endpoint
            except DerouterChatRetryable as exc:
                last_error = exc
                if attempt < attempts - 1:
                    time.sleep(DEFAULT_RETRY_WAIT_SECONDS)
                    continue
                break
            except DerouterChatError as exc:
                last_error = exc
                break

    raise DerouterChatError(
        f"Derouter chat API unavailable after retry; last error: {last_error}"
    )


def role_blocker_label(role: str) -> str:
    mapping = {
        "scout": "SCOUT",
        "research": "RESEARCH",
        "title": "TITLE",
        "writer": "WRITER",
        "sol": "SOL",
        "description": "DESCRIPTION",
        "cover-text": "COVER-TEXT",
        "schema": "SCHEMA",
        "cover-scene": "COVER-SCENE",
        "smoke": "SMOKE",
    }
    return mapping.get(role, role.upper())


def print_blocker(role: str, reason: str) -> None:
    label = role_blocker_label(role)
    print(f"DEROUTER {label} BLOCKER", file=sys.stderr)
    print(f"reason: {reason}", file=sys.stderr)


def write_stamp(
    *,
    stamp_path: Path,
    role: str,
    model: str,
    endpoint: str,
    response: dict[str, Any],
    user_prompt_preview: str,
) -> None:
    usage = response.get("usage") if isinstance(response.get("usage"), dict) else {}
    stamp: dict[str, Any] = {
        "script": "scripts/excalibur_blog_derouter_opus_chat.py",
        "role": role,
        "model": model,
        "endpoint": endpoint,
        "request_id": response.get("id"),
        "usage": usage,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "provider": "derouter-rest",
        "user_prompt_chars": len(user_prompt_preview),
        "contract": "shared/derouter-opus-brain-contract.md",
    }
    stamp_path.parent.mkdir(parents=True, exist_ok=True)
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_stamp_path(*, article_dir: str | None, role: str, root: Path) -> Path:
    if article_dir:
        ad = Path(article_dir)
        if not ad.is_absolute():
            ad = root / ad
        return ad / f"derouter-opus-stamp-{role}.json"
    return root / "memory/setup/derouter-opus-stamp.json"


def run_chat(args: argparse.Namespace) -> int:
    role = args.role.strip().lower()
    if role not in VALID_ROLES:
        raise DerouterChatError(f"Invalid role {role!r}; expected one of {sorted(VALID_ROLES)}")

    root = project_root()
    model = resolve_model(args.model)
    timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))

    if role == "smoke" or args.smoke:
        system_prompt = "You are a connectivity test. Reply with exactly: pong"
        user_prompt = "ping"
        role = "smoke"
    else:
        system_prompt = load_text_arg(
            inline=args.system_prompt, path=args.system_file, label="system-prompt"
        )
        user_prompt = load_text_arg(
            inline=args.user_prompt, path=args.user_file, label="user-prompt"
        )

    try:
        text, response, endpoint = call_derouter_chat(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            model=model,
            timeout=timeout,
            max_retries=DEFAULT_MAX_RETRIES,
        )
    except DerouterChatError as exc:
        print_blocker(role, str(exc))
        return 2

    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = root / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        print(f"WROTE {out.relative_to(root) if out.is_relative_to(root) else out}")

    stamp_path = resolve_stamp_path(article_dir=args.article_dir, role=role, root=root)
    if args.stamp_path:
        stamp_path = Path(args.stamp_path)
        if not stamp_path.is_absolute():
            stamp_path = root / stamp_path
    write_stamp(
        stamp_path=stamp_path,
        role=role,
        model=model,
        endpoint=endpoint,
        response=response,
        user_prompt_preview=user_prompt[:200],
    )
    print(f"STAMP {stamp_path.relative_to(root) if stamp_path.is_relative_to(root) else stamp_path}")

    if role == "smoke":
        ok = "pong" in text.lower()
        print(f"SMOKE {'PASS' if ok else 'FAIL'}: {text.strip()[:80]}")
        return 0 if ok else 1

    preview = text.strip().replace("\n", " ")[:120]
    print(f"OK role={role} model={model} chars={len(text)} preview={preview!r}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Derouter Opus chat — единственный автор прозы текстовых ролей Excalibur BLOG"
    )
    parser.add_argument(
        "--role",
        required=True,
        choices=sorted(VALID_ROLES),
        help="Pipeline role (scout, writer, sol, …) or smoke",
    )
    parser.add_argument("--system-prompt", help="System prompt inline")
    parser.add_argument("--system-file", help="System prompt file (skill/agent md)")
    parser.add_argument("--user-prompt", help="User prompt inline")
    parser.add_argument("--user-file", help="User prompt file (assembled inputs)")
    parser.add_argument("--output", "-o", help="Write assistant text to this path")
    parser.add_argument(
        "--article-dir",
        help="Article dir for stamp: <dir>/derouter-opus-stamp-<role>.json",
    )
    parser.add_argument("--stamp-path", help="Override stamp JSON path")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Alias: --role smoke ping→pong connectivity test",
    )
    parser.add_argument(
        "--model",
        help="Override model id (default: DEROUTER_TEXT_MODEL or claude-opus-5)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.smoke:
        args.role = "smoke"
    try:
        return run_chat(args)
    except DerouterChatError as exc:
        role = getattr(args, "role", "unknown")
        print_blocker(role, str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
