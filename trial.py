import csv
from flask import Flask, render_template

def load_data():
    data = []  # Initialize the data list
    try:
        with open('database.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)  # Append each row as a dictionary to the data list
    except FileNotFoundError:
        print("Error: The file 'database.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

data = load_data()
print(data)