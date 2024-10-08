import shutil
import os

# Specify the filename you want to move
filename = 'partOne.csv'  # Replace 'your_file.txt' with the actual file name

# Define the source and destination paths
source_path = r'C:\Users\nnaye\OneDrive\Documents'
destination_path = os.getcwd()  # Current working directory

# Create full file paths
source_file = os.path.join(source_path, filename)
destination_file = os.path.join(destination_path, filename)

# Move the file from source to destination
try:
    shutil.move(source_file, destination_file)
    print(f"File moved to {destination_file}")
except FileNotFoundError:
    print("The file does not exist in the source directory.")
except PermissionError:
    print("You do not have permission to move this file.")
except Exception as e:
    print(f"An error occurred: {e}")
