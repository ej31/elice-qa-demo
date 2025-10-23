import io
import unittest
from contextlib import redirect_stdout

from src.gugudan import generate_two_times_table, print_two_times_table


class GugudanTests(unittest.TestCase):
    def test_generate_two_times_table_contains_expected_lines(self):
        expected = [f"2 x {i} = {2 * i}" for i in range(1, 10)]
        self.assertEqual(list(generate_two_times_table()), expected)

    def test_print_two_times_table_writes_to_stdout(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_two_times_table()
        output = buffer.getvalue().strip().splitlines()
        self.assertEqual(output[0], "구구단 2단")
        self.assertEqual(output[1:], [f"2 x {i} = {2 * i}" for i in range(1, 10)])


if __name__ == "__main__":
    unittest.main()
