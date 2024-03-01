from pathlib import Path

CURR_DIR = Path(".").resolve()
class FileCreationError(Exception):
    pass

def create_path(file_name:str):
    """
    Creates a file based on file_name if it doesn't already exist.
    """
    try:
        file_name = file_name + ".txt"
        file_path = CURR_DIR/file_name
        file_path = Path(file_path)
        if not file_path.exists():
            file_path.touch()
    except Exception as ex:
        raise FileCreationError("There was an error creating the file: ", ex)
    