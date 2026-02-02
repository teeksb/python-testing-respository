import os
from datetime import datetime

def list_directory(path=''):  # the parameter here is an empty string whch usually means "current folder"
    """List contents of a directory with details."""
    print(f"Contents of {os.path.abspath(path)}:") #prints a title like contents of C: \...\Files: and converts the path into an absolute path
    print(f"{'Name':<30} {'Size':<10} {'Modified':<20} {'Type':<10}") #:<30 means left-align in a field 30 characters wide (so it lines up like a table)
    print("-" * 70)
    
    for item in os.listdir(path): #loop through directory content-returns a list of names inside that folder , item here is just the anme like ("students_grades.csv")
        full_path = os.path.join(path, item) #builds ful path to the item e,g path: "files" and item : house_prices.csv 
        mod_time = datetime.fromtimestamp(os.path.getmtime(full_path)) #gives the “modified time” as a timestamp (seconds since 1970)
        item_type = "Directory" if os.path.isdir(full_path) else "File"
        item_size = os.path.getsize(full_path)
        
        print(f"{item:<30} {item_size:<10,} {mod_time.strftime('%Y-%m-%d %H:%M'):<20} {item_type:<10}")

list_directory('Files')


