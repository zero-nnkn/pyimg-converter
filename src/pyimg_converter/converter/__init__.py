from .pdf2images import Pdf2ImgsConverter
from .heic2image import Heic2ImgConverter

SUPPORTED_CONVERTER = {
    'pdf': Pdf2ImgsConverter,
    'heic': Heic2ImgConverter,
}

def get_converter(file_type: str):
    converter = {
        'pdf': Pdf2ImgsConverter,
        'heic': Heic2ImgConverter,
    }.get(file_type)

    if converter is None:
        raise ValueError(f'Unsupported file type: {file_type}. Check {SUPPORTED_CONVERTER.keys()}')

    return converter()
