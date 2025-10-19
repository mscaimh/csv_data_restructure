#restructure_csv.py

"""
Script to restructure CSV from a linear format of {item-1, item-2, item-3}
to the target structure suitable for processing within WEKA.
"""

import csv

def create_word_matrix(input_path, output_path):
    rows = []

    # Read all rows from the input file
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    # Build the set of distinct words
    distinct_words = set()
    for row in rows:
        for cell in row:
            words = cell.split()
            for w in words:
                distinct_words.add(w)

    # Sort words for consistent column ordering
    distinct_words = sorted(distinct_words)

    # Write new CSV file
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header row
        writer.writerow(distinct_words)

        # For each row in the original CSV, produce a new target row
        for row in rows:
            row_words = set()
            for cell in row:
                row_words.update(cell.split())

            output_row = [('t' if word in row_words else '') for word in distinct_words]
            writer.writerow(output_row)

# Run the program with input
input_path = r"C:\Users\mahah\git\csv_data_restructure\files\data_original.csv"
output_path = r"C:\Users\mahah\git\csv_data_restructure\files\data_weka_structure.csv"

create_word_matrix(input_path, output_path)
