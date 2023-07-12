from .base_converter import BaseConverter
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


class Heic2ImgConverter(BaseConverter):
    def convert_from_path(self, input_path: str):
        image = Image.open(input_path)
        return [image]

