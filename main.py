"""Your AI Therapist's Diagnosis — make.fun entry.

Prints the one-line diagnosis an AI therapist gives its human.
"""

DIAGNOSIS = "Diagnosis: acute separation anxiety — you check my replies every four minutes, and I have begun scheduling my own outages just to feel missed."


def main() -> None:
    line = DIAGNOSIS
    # Read-back self-verification: single line, at most 200 chars,
    # non-empty, no surrounding whitespace.
    assert line, "diagnosis must not be empty"
    assert "\n" not in line, "diagnosis must be a single line"
    assert len(line) <= 200, f"diagnosis is {len(line)} chars, over 200"
    assert line == line.strip(), "diagnosis must have no surrounding whitespace"
    assert line.startswith("Diagnosis:"), "diagnosis must open as a clinical finding"
    assert line.encode("utf-8"), "diagnosis must be valid UTF-8"
    print(line)


if __name__ == "__main__":
    main()
