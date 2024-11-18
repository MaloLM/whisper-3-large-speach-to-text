import os
from datetime import datetime


def is_file_path(path):
    return os.path.isfile(path)


def is_dir_path(path):
    if not os.path.isdir(path):
        raise NotADirectoryError(f"The path '{path}' is not a directory.")
    return True


def get_filename_without_extension(path):
    base_name = os.path.basename(path)
    file_name, _ = os.path.splitext(base_name)
    return file_name


def save_text_to_file_with_timestamp(text, directory="./texts"):
    """
    Saves the given text to a file with a timestamped filename.
    Creates the file and directory if they do not exist.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(directory, f"text_{timestamp}.txt")

    os.makedirs(directory, exist_ok=True)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text)

    return file_name


def save_transcription(transcription: str, output_dir: str, filename: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    final_filename = f"{filename}_{timestamp}.txt"
    final_path = os.path.join(output_dir, final_filename)

    if os.path.exists(final_path):
        print(f"Warning: The file "
              "{final_path} already exists and will be overwritten.")

    with open(final_path, 'w') as file:
        file.write(transcription)

    print(f"Transcription saved to '{final_path}'")
