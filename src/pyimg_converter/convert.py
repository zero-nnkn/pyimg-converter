from pathlib import Path
from .converter import get_converter


def convert_from_path(input_path: str, output_path: str = None):
    input_path = Path(input_path)
    assert input_path.exists(), f'Input path does not exist: {input_path}'
    assert input_path.is_file(), f'Input path is not a file: {input_path}'

    file_type = input_path.suffix[1:].lower()
    converter = get_converter(file_type)
    images = converter.convert_from_path(input_path)

    if output_path is not None:
        assert output_path[-4:].lower() == '.png', 'Output path must be in *.png format'

        if len(images) == 1:
            images[0].save(output_path)

        else:
            import math
            digit_count = int(math.log10(len(images))) + 1
            for i, image in enumerate(images, 1):
                _output_path = output_path[:-4] + f'-{i:0{digit_count}d}.png'
                image.save(_output_path)

    return images