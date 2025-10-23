from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable, List


_TOKEN_PATTERN = re.compile(r"\b[\w']+\b")


@dataclass(frozen=True)
class TextSummary:
    """Structured information about a text snippet."""

    original: str
    tokens: List[str]

    @property
    def word_count(self) -> int:
        return len(self.tokens)

    @property
    def unique_word_count(self) -> int:
        return len(set(self.tokens))

    def format_for_display(self) -> str:
        return (
            "Text analysis summary:\n"
            f"  Original text: {self.original!r}\n"
            f"  Word count: {self.word_count}\n"
            f"  Unique words: {self.unique_word_count}"
        )


def tokenize(text: str) -> List[str]:
    """Split the input text into lowercase tokens."""
    return [match.group(0).lower() for match in _TOKEN_PATTERN.finditer(text)]


def summarize(text: str) -> TextSummary:
    tokens = tokenize(text)
    return TextSummary(original=text, tokens=tokens)


def summarize_many(texts: Iterable[str]) -> List[TextSummary]:
    return [summarize(text) for text in texts]


if __name__ == "__main__":
    sample_text = "GitHub Actions keeps continuous integration simple."
    summary = summarize(sample_text)
    print(summary.format_for_display())
