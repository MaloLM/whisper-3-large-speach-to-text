# import os
# from datetime import datetime


# def get_languages():
#     return ['english', 'chinese', 'german', 'spanish', 'russian', 'korean', 'french', 'japanese', 'portuguese', 'turkish', 'polish', 'catalan', 'dutch', 'arabic', 'swedish', 'italian', 'indonesian', 'hindi', 'finnish', 'vietnamese', 'hebrew', 'ukrainian', 'greek', 'malay', 'czech', 'romanian', 'danish', 'hungarian', 'tamil', 'norwegian', 'thai', 'urdu', 'croatian', 'bulgarian', 'lithuanian', 'latin', 'maori', 'malayalam', 'welsh', 'slovak', 'telugu', 'persian', 'latvian', 'bengali', 'serbian', 'azerbaijani', 'slovenian', 'kannada', 'estonian', 'macedonian', 'breton', 'basque', 'icelandic', 'armenian', 'nepali', 'mongolian', 'bosnian',
#             'kazakh', 'albanian', 'swahili', 'galician', 'marathi', 'punjabi', 'sinhala', 'khmer', 'shona', 'yoruba', 'somali', 'afrikaans', 'occitan', 'georgian', 'belarusian', 'tajik', 'sindhi', 'gujarati', 'amharic', 'yiddish', 'lao', 'uzbek', 'faroese', 'haitian creole', 'pashto', 'turkmen', 'nynorsk', 'maltese', 'sanskrit', 'luxembourgish', 'myanmar', 'tibetan', 'tagalog', 'malagasy', 'assamese', 'tatar', 'hawaiian', 'lingala', 'hausa', 'bashkir', 'javanese', 'sundanese', 'cantonese', 'burmese', 'valencian', 'flemish', 'haitian', 'letzeburgesch', 'pushto', 'panjabi', 'moldavian', 'moldovan', 'sinhalese', 'castilian', 'mandarin']


# def save_transcription(transcription: str, output_dir: str, filename: str):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

#     final_filename = f"{filename}_{timestamp}.txt"
#     final_path = os.path.join(output_dir, final_filename)

#     if os.path.exists(final_path):
#         print(f"Warning: The file "
#               "{final_path} already exists and will be overwritten.")

#     with open(final_path, 'w') as file:
#         file.write(transcription)

#     print(f"Transcription saved to '{final_path}'")


# def get_filename_without_extension(path):
#     base_name = os.path.basename(path)
#     file_name, _ = os.path.splitext(base_name)
#     return file_name


# def add_newline_after_sentence(text):
#     """
#     Adds a newline after each sentence ending with a period (.).
#     """
#     sentences = text.split('. ')
#     formatted_text = '.\n'.join(sentences).strip()
#     return formatted_text


# def is_file_path(path):
#     return os.path.isfile(path)


# def is_dir_path(path):
#     if not os.path.isdir(path):
#         raise NotADirectoryError(f"The path '{path}' is not a directory.")
#     return True


# def is_audio_format_compatible(path):
#     """
#     .wav, .mp3, .flac
#     """
#     compatible_extensions = {'.wav', '.mp3', '.flac'}
#     return os.path.splitext(path)[1].lower() in compatible_extensions


# def save_text_to_file_with_timestamp(text, directory="./texts"):
#     """
#     Saves the given text to a file with a timestamped filename.
#     Creates the file and directory if they do not exist.
#     """
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_name = os.path.join(directory, f"text_{timestamp}.txt")

#     os.makedirs(directory, exist_ok=True)

#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(text)

#     return file_name
