# Author: Keillor Behrmann
# Date: 7/16/24
# Purpose: This program reads a text file and counts how often each word occurs in the file. 
# It then writes the word counts to an output file.
# How to Run: Execute the program in a Python environment. Ensure you have 'input.txt' in the same directory.
# Sources: https://www.youtube.com/watch?v=Uh2ebFW8OYM&ab_channel=CoreySchafer. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
import os

def kb_read_file(file_path):
    """Read the content of a text file and return it as a string.

    Returns:
        str: The content of the file.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return ""
    
    with open(file_path, 'r') as file:
        return file.read()

def kb_count_words(text):
    """Counts how often each word occurs in the text and return a dictionary.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    words = text.split()
    word_counts = {}
    for word in words:
        # Cleans the word by removing punctuation and changing it to lower case
        word = word.lower().strip(",.?!\"'()[]{}:;")
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def kb_write_word_counts(word_counts, output_path):
    """Write the word counts to a text file.

    """
    with open(output_path, 'w') as file:
        for word, count in sorted(word_counts.items()):
            file.write(f"{word}: {count}\n")

def kb_main():
    """Coordinate the reading, counting, and writing processes.

    """
    input_path = "input.txt"
    output_path = "output.txt"
    
    text = kb_read_file(input_path)
    if not text:
        return
    
    word_counts = kb_count_words(text)
    kb_write_word_counts(word_counts, output_path)
    
    print(f"Word counts have been written to {output_path}")

if __name__ == "__main__":
    kb_main()
