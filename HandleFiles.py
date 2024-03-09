from pathlib import Path
import matplotlib as plt

current_path = Path(".").resolve()


class FileCreationError(Exception):
    pass

def create_png_folder():
    try:
        folder_path = str(current_path) + "/data_images"
        folder_path = Path(folder_path)
        if not folder_path.exists():
            folder_path.mkdir()
            print("Folder Initialized")
    except Exception as ex:
        raise FileCreationError("Folder Error: ", ex)

def sort_file(file_name: str):
    try:
        file_path = str(current_path) + "/" + file_name + ".png"
        file_path = Path(file_path)

        target_path = current_path / Path("data_images") / file_path.name
        file_path.rename(target_path)
        print(f"Your data visualizetion file can be found at: {str(target_path)}")
    except Exception as ex:
        raise FileCreationError("File I/O problem: ", ex)

    # 

