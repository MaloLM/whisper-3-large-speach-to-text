def add_newline_after_sentence(text):
    """
    Adds a newline after each sentence ending with a period (.).

    Args:
        text (str): The input text where sentences are separated by periods.

    Returns:
        str: The formatted text with a newline after each sentence ending with a period.
    """
    sentences = text.split('. ')
    formatted_text = '.\n'.join(sentences).strip()
    return formatted_text


def format_output_text(text):
    """
    Formats the output text by adding a newline after each sentence ending with a period (.).

    Args:
        text (str): The input text to be formatted.

    Returns:
        str: The formatted text with a newline after each sentence ending with a period.
    """
    formatted_text = add_newline_after_sentence(text)
    return formatted_text
