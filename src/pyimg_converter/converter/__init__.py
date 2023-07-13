from __future__ import annotations

from .pdf2images import Pdf2ImgsConverter
from .pil_converter import PILConverter

SUPPORTED_CONVERTER = {
    'pdf': Pdf2ImgsConverter,
    'heic': PILConverter,
    'tiff': PILConverter,
    'png': PILConverter,
    'jpg': PILConverter,
}


def get_converter(file_type: str):
    converter = SUPPORTED_CONVERTER.get(file_type)

    if converter is None:
        raise ValueError(f'Unsupported file type: "{file_type}". Must be in {tuple(SUPPORTED_CONVERTER.keys())}.')

    return converter()
