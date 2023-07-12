from pathlib import Path
from .converter import get_converter


def convert_from_path(input_path: str):
    input_path = Path(input_path)
    assert input_path.exists(), f'Input path does not exist: {input_path}'
    assert input_path.is_file(), f'Input path is not a file: {input_path}'

    file_type = input_path.suffix[1:].lower()
    converter = get_converter(file_type)
    images = converter.convert_from_path(input_path)

    return images