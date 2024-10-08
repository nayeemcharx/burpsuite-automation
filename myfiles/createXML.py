import os
import re

def extract_items_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use a regex to extract everything between <item> and </item>
    items = re.findall(r'<item>.*?</item>', content, re.DOTALL)


    return items

def consolidate_items(directory):
    all_items = []
    
    # Iterate through all files in the current directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        items = extract_items_from_file(file_path)
        all_items.extend(items)
    # Define the output file path in the same directory
    output_file = os.path.join(directory, "consolidated_items.xml")
    
    # Write all extracted items to the output file
    with open(output_file, 'w') as output:
        output.write("<items>\n")
        for item in all_items:
            output.write(item + "\n")
        output.write("</items>")

# Example usage
directory_path = os.getcwd()  # Get the current working directory (where the script is located)
consolidate_items(directory_path)
