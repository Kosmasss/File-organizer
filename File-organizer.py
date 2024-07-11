import os
import shutil
from datetime import datetime, timedelta
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str, help='Directory where the files are located')
parser.add_argument('months', type=int, help='Number of months to look back')
args = parser.parse_args()

# Get the directory and number of months from the command-line arguments
directory = args.directory
months = args.months

# Get the current date and time
current_date = datetime.now()

# Calculate the date months ago
months_ago = current_date - timedelta(days=months*30)

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    # Get the last modified date of the file
    last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
    # Check if the file hasn't been modified in the last months
    if last_modified_date < months_ago:
        # Move the file to the destination directory
        shutil.move(file_path, os.path.join(directory, 'archived', filename))