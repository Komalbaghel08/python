import os
import shutil

# file extensions mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # skip folders
        if os.path.isdir(file_path):
            continue

        # get extension
        _, ext = os.path.splitext(filename)

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, folder)

                # create folder if not exist
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, filename))
                moved = True
                break
        # others
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_folder(path)
    print("Files organized successfully!")
    