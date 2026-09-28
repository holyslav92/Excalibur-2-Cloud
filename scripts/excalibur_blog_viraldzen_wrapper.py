#!/usr/bin/env python3
"""Обёртка ViralDzen (vendored) — не меняем upstream, только CLI spawn."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def viraldzen_env(root: Path) -> dict[str, str]:
    env = os.environ.copy()
    pkg = root / "vendor" / "viraldzen"
    existing = env.get("PYTHONPATH", "")
    prefix = str(pkg)
    env["PYTHONPATH"] = f"{prefix}{os.pathsep}{existing}" if existing else prefix
    return env


def min_delay(delay: float) -> float:
    return max(0.7, float(delay))


def run_viraldzen(root: Path, args: list[str], *, delay: float | None = None) -> int:
    cmd = [sys.executable, "-m", "viraldzen", *args]
    if delay is not None:
        if "--delay" in args:
            # заменить значение после --delay
            out: list[str] = []
            skip_next = False
            for i, a in enumerate(args):
                if skip_next:
                    skip_next = False
                    out.append(str(min_delay(delay)))
                    continue
                if a == "--delay" and i + 1 < len(args):
                    out.append(a)
                    skip_next = True
                    continue
                out.append(a)
            cmd = [sys.executable, "-m", "viraldzen", *out]
        else:
            cmd.extend(["--delay", str(min_delay(delay))])
    proc = subprocess.run(
        cmd,
        cwd=root,
        env=viraldzen_env(root),
        check=False,
    )
    return int(proc.returncode)


def main() -> int:
    root = project_root()
    return run_viraldzen(root, sys.argv[1:], delay=0.7)


if __name__ == "__main__":
    raise SystemExit(main())
