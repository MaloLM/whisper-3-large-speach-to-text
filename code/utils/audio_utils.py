import os


def is_audio_format_compatible(path):
    """
    Checks if the given file path has a compatible audio format.

    Compatible audio formats are: .wav, .mp3, .flac.

    Args:
        path (str): The file path to check.

    Returns:
        bool: True if the file has a compatible audio format, False otherwise.
    """
    compatible_extensions = {'.wav', '.mp3', '.flac'}
    return os.path.splitext(path)[1].lower() in compatible_extensions
