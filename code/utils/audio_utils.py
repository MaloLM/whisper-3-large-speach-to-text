import os

def is_audio_format_compatible(path):
    """
    .wav, .mp3, .flac
    """
    compatible_extensions = {'.wav', '.mp3', '.flac'}
    return os.path.splitext(path)[1].lower() in compatible_extensions
