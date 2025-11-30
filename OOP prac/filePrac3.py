from pathlib import Path

path = Path("text_files/data.txt")

content = path.read_text()
print(content)