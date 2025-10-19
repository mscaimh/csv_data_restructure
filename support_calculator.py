#calculate_support.py

"""
Calculating support
"""

import csv

def calculate_support():
    rows = []

    # Read all rows from the input file
    print("Reading input file")
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    # Iterate through the rows and count number of rows containing all elements
    print("Counting match count")
    count = 0;
    for row in rows:
        if input_items.issubset(set(row)):
            count = count + 1

    support = count / len(rows)

    print(f"Matches: {count}, Total rows: {len(rows)}, Support: {support}")

# Run the program with input
input_path = r"C:\Users\mahah\git\csv_data_restructure\files\data_original.csv"
input_items = {"shrimp", "almonds"}

calculate_support()
