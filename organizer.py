from pathlib import path 
Category_Map = {
    "Images" : [".jpeg",".jpg",".gif",".png"],
    "Documents" : [".pdf",".docx",".txt",".xlsx",".csv"],
    "Audio" : [".mp3",".wav"],
    "Archives" : [".zip",".tar",".gz"]
}

def organize_folder(target_directory):
    pass

if __name__ == "__main__":
    organize_folder(input("Enter Folder path"))