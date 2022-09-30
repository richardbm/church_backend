import math
import re

from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from markdown_deux import markdown


def count_words(html_string: str) -> int:
    word_string = strip_tags(html_string)
    matching_words = re.findall(r"\w+", word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string: str, words_per_minute: int = 200) -> int:
    """
    It returns the amount of reading time expressed in minutes
    """
    count = count_words(html_string)
    read_time_min = math.ceil(count / float(words_per_minute))
    return int(read_time_min)


def get_markdown_from_html(content: str) -> str:
    markdown_text = markdown(content)
    return mark_safe(markdown_text)


def extract_short_description(content: str, max_length: int = 25):
    description = strip_tags(content)[:250]
    description = description.split(".\n")[0]
    if description[-1] == ".":
        description = description[:-1]
    return f"{description}..."
