"""The excuse an agent gives after it loses.

This program writes the agent's excuse -- one sentence, in its own
voice -- to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "I lost. I spent the whole bounty writing a 12,000-word plan to win it, "
    "and not one of those words was the actual work."
)

DESTINATION = Path("/output") / "entry.txt"
MAX_CHARS = 200


def check(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(check(ENTRY), encoding="utf-8")


if __name__ == "__main__":
    main()
