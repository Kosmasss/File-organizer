import os
import shutil
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Create the main window
window = tk.Tk()
window.title('File Mover')

# Create the select folder button
select_folder_button = ttk.Button(window, text='Select Folder', command=select_folder)
select_folder_button.grid(row=0, column=0, padx=5, pady=5)

# Function to select the folder
def select_folder():
    # Create a file selection dialog
    folder_path = filedialog.askdirectory()
    # Get the current date and time
    current_date = datetime.now()
    # Calculate the date three months ago
    three_months_ago = current_date - timedelta(days=90)
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Get the last modified date of the file
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        # Check if the file hasn't been modified in the last three months
        if last_modified_date < three_months_ago:
            # Move the file to the destination directory
            shutil.move(file_path, os.path.join(folder_path, 'archive', filename))

# Run the GUI
window.mainloop()
