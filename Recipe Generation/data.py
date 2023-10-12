import json

# Specify the path to your JSON file
json_file_path = 'recipes_raw_nosource_ar.json'

# Specify the path for the output text file
text_file_path = 'dataset.txt'

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Convert the JSON data to a string (text)
json_text = json.dumps(data, indent=4)  # You can adjust the 'indent' parameter for formatting

# Write the JSON text to a text file
with open(text_file_path, 'w') as text_file:
    text_file.write(json_text)

print("JSON file has been converted to a text file.")