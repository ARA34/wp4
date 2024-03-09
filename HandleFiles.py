from pathlib import Path


current_path = Path(".").resolve()


class FileCreationError(Exception):
    pass


def create_png_folder():
    """
    Creates a folder named 'data_images' to store data visualizations.
    """
    try:
        folder_path = str(current_path) + "/data_images"
        folder_path = Path(folder_path)
        if not folder_path.exists():
            folder_path.mkdir()
            print("Folder Initialized")
    except Exception as ex:
        raise FileCreationError("Folder Error: ", ex)


def sort_file(file_name: str):
    """
    Redirects an already created file to the data_image folder.
    Keep in mind the create_png_folder must be ran first.
    """
    try:
        file_path = str(current_path) + "/" + file_name + ".png"
        file_path = Path(file_path)

        target_path = current_path / Path("data_images") / file_path.name
        file_path.rename(target_path)
        print(f"Your data visualizetion file can be found at: {str(target_path)}")
    except Exception as ex:
        raise FileCreationError("File I/O problem: ", ex)


