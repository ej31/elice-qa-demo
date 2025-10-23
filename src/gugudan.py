from __future__ import annotations

from typing import Iterable


def generate_two_times_table() -> Iterable[str]:
    """Return lines representing the 2-times multiplication table."""
    return [f"2 x {i} = {2 * i}" for i in range(1, 10)]


def print_two_times_table() -> None:
    """Print the 2-times multiplication table to the console."""
    print("구구단 2단")
    for line in generate_two_times_table():
        print(line)


if __name__ == "__main__":
    print_two_times_table()
