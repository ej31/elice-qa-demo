import unittest

from src.text_analyzer import TextSummary, summarize, summarize_many, tokenize


class TokenizeTests(unittest.TestCase):
    def test_tokenize_lowercases_words(self):
        self.assertEqual(tokenize("Hello WORLD"), ["hello", "world"])

    def test_tokenize_handles_apostrophes(self):
        self.assertEqual(tokenize("let's test"), ["let's", "test"])

    def test_tokenize_ignores_non_word_characters(self):
        self.assertEqual(tokenize("Hello, world!"), ["hello", "world"])


class SummarizeTests(unittest.TestCase):
    def test_summarize_populates_fields(self):
        summary = summarize("repeat repeat unique")
        self.assertEqual(summary.original, "repeat repeat unique")
        self.assertEqual(summary.word_count, 3)
        self.assertEqual(summary.unique_word_count, 2)

    def test_summarize_many_returns_list_of_summaries(self):
        texts = ["first text", "second text"]
        results = summarize_many(texts)
        self.assertEqual(len(results), 2)
        self.assertTrue(all(isinstance(item, TextSummary) for item in results))

    def test_format_for_display_contains_counts(self):
        summary = summarize("alpha beta beta")
        rendered = summary.format_for_display()
        self.assertIn("Word count: 3", rendered)
        self.assertIn("Unique words: 2", rendered)


if __name__ == "__main__":
    unittest.main()
