import pypdfium2 as pdfium

from .base_converter import BaseConverter


class Pdf2ImgsConverter(BaseConverter):
    def convert_from_path(self, input_path: str):
        pdf = pdfium.PdfDocument(input_path)
        images = pdf.render(
            pdfium.PdfBitmap.to_pil,
            page_indices = [i for i in range(len(pdf))],
            scale = 1,
        )
        images = [img for img in images]
        return images