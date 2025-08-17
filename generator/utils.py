
from urllib.parse import quote, urlencode
import uuid

BASE_URL = "https://image.pollinations.ai/prompt/"

def build_pollinations_url(prompt: str, size: str = "512") -> str:
    """
    Returns a direct image URL from Pollinations.
    Pollinations generates by GET, no API key needed.
    """
    encoded_prompt = quote(prompt.strip())
    width = height = int(size or 512)

    # Optional query params Pollinations supports (keep minimal & safe)
    params = {
        "width": width,
        "height": height,
        # "seed": 42,         # uncomment to make results repeatable
        # "model": "sdxl",    # you can try values if supported; safe to omit
        # Cache-buster so each click gives a fresh image
        "t": uuid.uuid4().hex
    }
    return f"{BASE_URL}{encoded_prompt}?{urlencode(params)}"
