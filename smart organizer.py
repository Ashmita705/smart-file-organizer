from pathlib import Path
import shutil

folder_path = Path(input("Enter folder path: "))

for item in folder_path.iterdir():
    if item.is_dir():
        continue

    ext = item.suffix.lower()

    if ext in [".jpg", ".png"]:
        new_folder = folder_path / "Images"
    elif ext in [".pdf", ".txt"]:
        new_folder = folder_path / "Docs"
    elif ext == ".mp4":
        new_folder = folder_path / "Videos"
    elif ext == ".py":
        new_folder = folder_path / "Code"
    else:
        new_folder = folder_path / "Others"

    new_folder.mkdir(exist_ok=True)

    destination = new_folder / item.name
    shutil.move(str(item), str(destination))

    print(f"Moved {item.name} → {new_folder.name}")

print("Done")
