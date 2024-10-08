import os

# Define the specific file to delete
file_to_delete = 'consolidated_items.xml'

# Get a list of all items in the current working directory
for filename in os.listdir('.'):
    # Check if the item is a file that starts with 'repeater' or is 'consolidated_items.xml'
    if (filename.startswith('repeater') or filename == file_to_delete) and os.path.isfile(filename):
        # Delete the file
        os.remove(filename)
        print(f"Deleted {filename}")
