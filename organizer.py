from pathlib import Path 
Category_Map = {
    "Images" : [".jpeg",".jpg",".gif",".png"],
    "Documents" : [".pdf",".docx",".txt",".xlsx",".csv"],
    "Audio" : [".mp3",".wav"],
    "Archives" : [".zip",".tar",".gz"]
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


if __name__ == "__main__":
    organize_folder(input("Enter Folder path"))

