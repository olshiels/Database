import csv
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Read the CSV and convert to dictionary
def load_data():
    data = []  # Initialize the data list
    try:
        with open('database.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row = {key.strip(): value.strip() if value.strip() != '' else 'N/A' for key, value in row.items()}
                data.append(row)
    except FileNotFoundError:
        print("Error: The file 'database.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    # Get the data from the CSV
    data = load_data()

    # Get the search query and column name from the form (if any)
    search_query = request.args.get('search', '')
    search_column = request.args.get('column', 'Gene')  # Default to 'Gene' if not provided

    # Filter data based on search query and column selected
    if search_query:
        filtered_data = [row for row in data if search_query.lower() in row[search_column].lower()]
    else:
        filtered_data = data
    
    return render_template('index.html', data=data, filtered_data=filtered_data, search_query=search_query, search_column=search_column)

if __name__ == '__main__':
    app.run(debug=True)