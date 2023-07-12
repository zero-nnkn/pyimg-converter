from .pdf2images import Pdf2ImgsConverter

SUPPORTED_CONVERTER = {
    'pdf': Pdf2ImgsConverter,
}

def get_converter(file_type: str):
    converter = {
        'pdf': Pdf2ImgsConverter,
    }.get(file_type)

    if converter is None:
        raise ValueError(f'Unsupported file type: {file_type}. Check {SUPPORTED_CONVERTER.keys()}')

    return converter()
