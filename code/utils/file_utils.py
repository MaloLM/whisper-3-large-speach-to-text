import os
from datetime import datetime


def is_file_path(path):
    """
    Checks if the given path is a file.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path is a file, False otherwise.
    """
    return os.path.isfile(path)


def is_dir_path(path):
    """
    Checks if the given path is a directory. Raises an error if it is not.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path is a directory.

    Raises:
        NotADirectoryError: If the path is not a directory.
    """
    return os.path.isdir(path)


def get_filename_without_extension(path):
    """
    Extracts the filename without its extension from the given path.

    Args:
        path (str): The file path.

    Returns:
        str: The filename without its extension.
    """
    base_name = os.path.basename(path)
    file_name, _ = os.path.splitext(base_name)
    return file_name


def save_text_to_file_with_timestamp(text, directory="./texts"):
    """
    Saves the given text to a file with a timestamped filename.
    Creates the file and directory if they do not exist.

    Args:
        text (str): The text to save.
        directory (str): The directory where the file will be saved. Defaults to "./texts".

    Returns:
        str: The path to the saved file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(directory, f"text_{timestamp}.txt")

    os.makedirs(directory, exist_ok=True)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)

    return file_name


def save_transcription(transcription: str, output_dir: str, filename: str):
    """
    Saves the transcription text to a file with a timestamped filename.
    Creates the directory if it does not exist.

    Args:
        transcription (str): The transcription text to save.
        output_dir (str): The directory where the file will be saved.
        filename (str): The base filename for the saved file.

    Returns:
        None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    final_filename = f"{filename}_{timestamp}.txt"
    final_path = os.path.join(output_dir, final_filename)

    if os.path.exists(final_path):
        print(f"Warning: The file {final_path}"
              "already exists and will be overwritten.")

    with open(final_path, 'w') as file:
        file.write(transcription)

    print(f"Transcription saved to '{final_path}'")
