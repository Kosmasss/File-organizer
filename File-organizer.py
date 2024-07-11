import os
import shutil
from datetime import datetime, timedelta

# Specify the directory where the files are located
directory = '/path/to/your/directory'

# Specify the directory where the files should be moved
destination_directory = '/path/to/destination/directory'

# Get the current date and time
current_date = datetime.now()

# Calculate the date three months ago
three_months_ago = current_date - timedelta(days=90)

# Loop through all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    # Get the last modified date of the file
    last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
    # Check if the file hasn't been modified in the last three months
    if last_modified_date < three_months_ago:
        # Move the file to the destination directory
        shutil.move(file_path, os.path.join(destination_directory, filename))
