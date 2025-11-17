from __future__ import annotations

from pathlib import Path

def read_from_file(path: str) -> list[tuple[str, str, str]]:
    contents = Path(path).read_text(encoding="utf-8").replace("\r", "").strip()

    if not contents:
        return []
    lines: list[str] = [line.strip() for line in contents.split("\n")]
    commands: list[tuple[str, str, str]] = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) != 3:
            raise ValueError("invalid command format")
        cmd, arg1, arg2 = parts
        commands.append((cmd, arg1, arg2))
    return commands