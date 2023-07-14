from __future__ import annotations

from pathlib import Path

from .converter import get_converter

SUPPORTED_OUTPUT_FORMATS = tuple('png',)

def convert_from_path(input_path: str, output_path: str = None):
    """
    Converts a file to PNG format to a list of images.
    Saves it to the specified output if output path is provided.

    Args:
      input_path (str): path of input file
      output_path (str): specifies the path where the converted image(s) will be saved.
    If `output_path` is not provided, the converted image(s) will not be saved to a file.

    Returns:
      A list of images.
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f'Input path does not exist: {input_path}.')
    if not input_path.is_file():
        raise IsADirectoryError(f'Input path is not a file: {input_path}.')

    file_type = input_path.suffix[1:].lower()
    converter = get_converter(file_type)
    images = converter.convert_from_path(input_path)

    if output_path is not None:
        if Path(output_path).suffix[1:].lower() != '.png':
            raise ValueError(f'Output path must be in {SUPPORTED_OUTPUT_FORMATS} format.')

        if len(images) == 1:
            images[0].save(output_path)

        else:
            import math
            digit_count = int(math.log10(len(images))) + 1
            for i, image in enumerate(images, 1):
                _output_path = output_path[:-4] + f'-{i:0{digit_count}d}.png'
                image.save(_output_path)

    return images
