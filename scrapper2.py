from bs4 import BeautifulSoup

# Sample HTML string (use the actual HTML content from above)
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON Data in HTML</title>
    <style>
        .data-item {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>JSON Data List</h1>
    <div id="data-container"></div>

    <script>
        // Sample JSON data
        const jsonData = [
            { "id": 1, "name": "Alice", "age": 25, "city": "New York" },
            { "id": 2, "name": "Bob", "age": 30, "city": "Los Angeles" },
            { "id": 3, "name": "Charlie", "age": 35, "city": "Chicago" }
        ];
    </script>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract the content of the <script> tag
script_content = soup.find('script').string

# Find the start and end of the JSON data within the script content
start_index = script_content.find('[')
end_index = script_content.find(']') + 1

# Extract the JSON string
json_string = script_content[start_index:end_index]

print("Extracted JSON String:", json_string)

import json

# The extracted JSON string from the previous step
#json_string = '[{ "id": 1, "name": "Alice", "age": 25, "city": "New York" }, { "id": 2, "name": "Bob", "age": 30, "city": "Los Angeles" }, { "id": 3, "name": "Charlie", "age": 35, "city": "Chicago" }]'

# Convert JSON string to Python object (list of dictionaries)
json_data = json.loads(json_string)

print("Converted Python Object:", json_data)
