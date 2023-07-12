from PIL import Image
from pillow_heif import register_heif_opener

from .base_converter import BaseConverter

register_heif_opener()


class PILConverter(BaseConverter):
    def convert_from_path(self, input_path: str):
        return Image.open(input_path)
