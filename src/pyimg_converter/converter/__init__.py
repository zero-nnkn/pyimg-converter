from .pdf2images import Pdf2ImgsConverter
from .heic2image import Heic2ImgConverter
from .pil_converter import PILConverter

SUPPORTED_CONVERTER = {
    "pdf": Pdf2ImgsConverter,
    "heic": Heic2ImgConverter,
    "tiff": PILConverter,
    "png": PILConverter,
    "jpg": PILConverter,
}


def get_converter(file_type: str):
    converter = SUPPORTED_CONVERTER.get(file_type)

    if converter is None:
        raise ValueError(f"Unsupported file type: {file_type}. Check {SUPPORTED_CONVERTER.keys()}")

    return converter()
