from pathlib import Path

folder = Path("C:/Users/garri/OneDrive/Desktop/python programs")

files = 0
folders = 0
for item in folder.iterdir():
    if item.is_file():
        files += 1
    elif item.is_dir():
        folders += 1
    
print(f"Files: {files}\nFolders: {folders}\n\n")

for item in folder.iterdir():
    print(item)    