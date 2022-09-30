import random
import string

from django.utils.text import slugify


def create_unique_slug(text: str, max_length: int = 64, id_length: int = 6) -> str:
    unique_id = "".join(random.choice(string.ascii_lowercase) for i in range(id_length))
    slug = slugify(text[: max_length - id_length - 1])
    return f"{slug}-{unique_id}"