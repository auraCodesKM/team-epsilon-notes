"""Turn notes into question/answer flashcards (heuristic: one card per sentence with 'is')."""

import sys


def flashcards(text: str) -> list[tuple[str, str]]:
    cards = []
    for sentence in text.replace("\n", " ").split("."):
        if " is " in sentence:
            term, _, rest = sentence.strip().partition(" is ")
            cards.append((f"What is {term}?", rest.strip()))
    return cards


if __name__ == "__main__":
    for q, a in flashcards(open(sys.argv[1]).read()):
        print(f"Q: {q}\nA: {a}\n")
