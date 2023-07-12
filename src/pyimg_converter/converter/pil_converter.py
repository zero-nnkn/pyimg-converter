from PIL import Image

from .base_converter import BaseConverter


class PILConverter(BaseConverter):
    def convert_from_path(self, input_path: str):
        return Image.open(input_path)
