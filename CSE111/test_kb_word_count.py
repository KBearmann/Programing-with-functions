# Author: Keillor Behrmann
# Date: 7/17/
# Purpose: This file contains test functions for the kb_word_count.py program.
# How to Run: Execute the tests using pytest.

import pytest
from kb_word_count import kb_read_file, kb_count_words

def test_kb_read_file():
    """Tests the kb_read_file function to ensure it correctly reads data from a text file."""
    text = kb_read_file("test_input.txt")
    assert text == "Hello world! This is a test file. Hello again."
    text = kb_read_file("non_existent_file.txt")
    assert text == ""

def test_kb_count_words():
    """Test the kb_count_words function to ensure it accurately counts word occurrences in a string."""
    text = "Hello world! This is a test file. Hello again."
    word_counts = kb_count_words(text)
    expected_counts = {
        'hello': 2,
        'world': 1,
        'this': 1,
        'is': 1,
        'a': 1,
        'test': 1,
        'file': 1,
        'again': 1
    }
    assert word_counts == expected_counts

    text = "Python is so great! Python is very fun."
    word_counts = kb_count_words(text)
    expected_counts = {
        'python': 2,
        'is': 2,
        'great': 1,
        'fun': 1
    }
    assert word_counts == expected_counts

if __name__ == "__main__":
    pytest.main()
