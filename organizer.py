from pathlib import Path 
import shutil
CATEGORY_MAP = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".svg", ".bmp", ".webp"],
    "Documents": [".pdf", ".txt", ".rtf", ".md"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx", ".key"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Executables": [".exe", ".dmg", ".sh", ".bat"]
}

def organize_folder(target_directory):
    base_dir = Path(target_directory)
    if not base_dir.exists():
        print("Error: File doesnt exists")
        return
    for item in base_dir.iterdir():
        file_extension = item.suffix.lower()

        target_category = None
        for category, extensions in Category_Map.items():
            if file_extension in extensions:
                target_category = category
                break
        
        if target_category:
            category_folder = base_dir/target_category
            category_folder.mkdir(exist_ok=True)
            destination_path = category_folder/item.name

            try:
                shutil.copy(str(item),str(destination_path))
                print(f"Moved: {item.name} -> {target_category}/")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")

if __name__ == "__main__":
    organize_folder(input("Enter Folder path"))

