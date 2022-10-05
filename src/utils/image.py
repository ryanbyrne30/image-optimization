from pathlib import Path
from PIL import Image


def convert_to_webp(image: str) -> str:
    """Converts image to a webp image with reduced quality and returns
    path of new image"""
    source = Path(image)
    destination = source.with_suffix(".webp")
    image = Image.open(image)
    image = image.convert("RGB")
    image.save(destination, "webp", optimize=True, quality=80)
    return str(destination)
