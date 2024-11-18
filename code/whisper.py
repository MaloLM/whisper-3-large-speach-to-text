import os
import torch
from utils.text_utils import format_output_text
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


class SpeechToTextInference:
    def __init__(self, language: str = 'english') -> None:
        """
        Initializes the inference class.

        :param pipeline: The speech-to-text pipeline object.
        :param supported_languages: A list of supported language codes.
        """
        self.language = language.lower()

        if self.language not in self.get_languages():
            raise ValueError(f"Unsupported language '{language}'. Supported languages are: "
                             f"{', '.join(self.languages)}.")

        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        self.model_id = "openai/whisper-large-v3"

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_id, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        model.to(self.device)

        self.processor = AutoProcessor.from_pretrained(self.model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )

    def get_languages(self):
        return ['english', 'chinese', 'german', 'spanish', 'russian', 'korean', 'french', 'japanese', 'portuguese', 'turkish', 'polish', 'catalan', 'dutch', 'arabic', 'swedish', 'italian', 'indonesian', 'hindi', 'finnish', 'vietnamese', 'hebrew', 'ukrainian', 'greek', 'malay', 'czech', 'romanian', 'danish', 'hungarian', 'tamil', 'norwegian', 'thai', 'urdu', 'croatian', 'bulgarian', 'lithuanian', 'latin', 'maori', 'malayalam', 'welsh', 'slovak', 'telugu', 'persian', 'latvian', 'bengali', 'serbian', 'azerbaijani', 'slovenian', 'kannada', 'estonian', 'macedonian', 'breton', 'basque', 'icelandic', 'armenian', 'nepali', 'mongolian', 'bosnian',
                'kazakh', 'albanian', 'swahili', 'galician', 'marathi', 'punjabi', 'sinhala', 'khmer', 'shona', 'yoruba', 'somali', 'afrikaans', 'occitan', 'georgian', 'belarusian', 'tajik', 'sindhi', 'gujarati', 'amharic', 'yiddish', 'lao', 'uzbek', 'faroese', 'haitian creole', 'pashto', 'turkmen', 'nynorsk', 'maltese', 'sanskrit', 'luxembourgish', 'myanmar', 'tibetan', 'tagalog', 'malagasy', 'assamese', 'tatar', 'hawaiian', 'lingala', 'hausa', 'bashkir', 'javanese', 'sundanese', 'cantonese', 'burmese', 'valencian', 'flemish', 'haitian', 'letzeburgesch', 'pushto', 'panjabi', 'moldavian', 'moldovan', 'sinhalese', 'castilian', 'mandarin']

    def inference(self, file_path: str):
        """
        Processes an audio file and transcribes it to text.

        :param file_path: Path to the audio file.
        :param language: Language for transcription.
        :return: Transcribed text.
        :raises ValueError: If the language is not supported or the file path is invalid.
        :raises FileNotFoundError: If the file does not exist.
        :raises RuntimeError: For errors during the transcription process.
        """
        if not file_path or not isinstance(file_path, str):
            raise ValueError(
                "Invalid file path. It must be a non-empty string.")

        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f"The file '{file_path}' does not exist or is inaccessible.")

        try:
            result = self.pipe(file_path, return_timestamps=True, generate_kwargs={
                               "language": self.language})

            text = format_output_text(result["text"])
            return text

        except Exception as e:
            raise RuntimeError(f"An error occurred during transcription: {e}")