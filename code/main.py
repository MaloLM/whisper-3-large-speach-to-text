import argparse
from pathlib import Path
from whisper import SpeechToTextInference
from utils.audio_utils import is_audio_format_compatible
from utils.file_utils import get_filename_without_extension, is_dir_path, is_file_path, save_transcription


def main(input_dir, output_dir, language):

    stt = SpeechToTextInference(language=language)

    if is_dir_path(output_dir):
        if is_file_path(input_dir):
            transcription = stt.inference(input_dir)
            filename = get_filename_without_extension(input_dir)
            save_transcription(transcription, output_dir, filename)

        elif is_dir_path(input_dir):
            dir = Path(input_dir)
            for file_path in dir.iterdir():
                if file_path.is_file():
                    if is_audio_format_compatible(file_path):
                        transcription = stt.inference(str(file_path))
                        filename = get_filename_without_extension(
                            str(file_path))
                        save_transcription(transcription, output_dir, filename)
        else:
            raise FileNotFoundError(f"Given path {input_dir} was not found.")
    else:
        raise FileNotFoundError(f"Given path {output_dir} was not found.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Speech to Text Inference Script')
    parser.add_argument('input_dir', type=str,
                        help='Input directory or file path')
    parser.add_argument('output_dir', type=str, help='Output directory path')
    parser.add_argument('language', type=str,
                        help='Language for speech to text inference')

    args = parser.parse_args()

    is_dir_path(args.output_dir)

    main(args.input_dir, args.output_dir, args.language)

# Examples from project root:
# > python main.py ./inputs/test_sample.flac ./outputs french
# > python main.py ./inputs/ ./outputs french
