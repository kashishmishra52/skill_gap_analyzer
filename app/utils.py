import re

def clean_text(text):
    """
    Convert text to lowercase, remove punctuation, normalize whitespace.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text)     # normalize spacing
    return text.strip()
