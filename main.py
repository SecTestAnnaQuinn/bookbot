#!/usr/bin/python3
from stats import word_count,letter_count,sorter
import sys

file_contents = None

def get_book_text(filepath):
	with open(filepath) as f:
		file_read = f.read()
	return file_read

def report_print(counts):
	for item in counts:
		if item["char"].isalpha():
			print(f"{item["char"]}: {item["num"]}")
	return
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	file_contents = get_book_text(path)
	words = word_count(file_contents)
	letters = letter_count(file_contents)
	sorted = sorter(letters)
	print(f"""============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
""")
	report_print(sorted)

main()
