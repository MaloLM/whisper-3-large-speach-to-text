def add_newline_after_sentence(text):
    """
    Adds a newline after each sentence ending with a period (.).
    """
    sentences = text.split('. ')
    formatted_text = '.\n'.join(sentences).strip()
    return formatted_text


def format_output_text(text):
    formated_text = add_newline_after_sentence(text)
    return formated_text
