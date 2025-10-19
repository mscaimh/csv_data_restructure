#restructure_csv.py

"""
Script to restructure CSV from a linear format of {item-1, item-2, item-3}
to the target structure suitable for processing within WEKA.
"""

import csv

def create_word_matrix():
    rows = []

    # Read all rows from the input file
    print("Reading input file")
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    # Build the set of distinct words
    print("Extracting distinct words")
    distinct_words = set()
    for row in rows:
        for cell in row:
            distinct_words.add(cell.strip())

    # Sort words for consistent column ordering
    distinct_words = sorted(distinct_words)

    # Mapping numeric index to the distinct words
    print("Mapping numeric index to distinct words")
    word_indexes_map = dict()
    word_indexes = set()
    word_index = 0
    for word in distinct_words:
        word_indexes_map[word] = word_index
        word_indexes.add(word_index)
        word_index += 1

    print("Word:index mapping: ", word_indexes_map)

    # Write new CSV file
    print("Writing output file")
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header row
        writer.writerow(word_indexes)

        # For each row in the original CSV, produce a new target row
        for row in rows:
            row_words = set()
            row_words.update([cell.strip() for cell in row])

            output_row = [('t' if word in row_words else '') for word in distinct_words]
            writer.writerow(output_row)

# Run the program with input
input_path = r"C:\Users\mahah\git\csv_data_restructure\files\data_original.csv"
output_path = r"C:\Users\mahah\git\csv_data_restructure\files\data_weka_structure.csv"

create_word_matrix()
