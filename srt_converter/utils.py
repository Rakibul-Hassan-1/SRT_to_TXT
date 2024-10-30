# srt_converter/utils.py
import re

def parse_srt_to_paragraph(srt_content):
    # Remove numeric indices
    srt_content = re.sub(r'^\d+\s*$', '', srt_content, flags=re.MULTILINE)
    # Remove timestamps
    srt_content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', srt_content)
    # Remove all redundant whitespaces and line breaks
    srt_content = re.sub(r'\s*\n\s*', ' ', srt_content).strip()
    return srt_content
