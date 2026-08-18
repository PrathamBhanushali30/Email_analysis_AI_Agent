import re

def extract_urls(text):
    return re.findall(r'(https?://\S+)', text)