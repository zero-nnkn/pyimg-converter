# Pyimg-converter

Convert file (`*.heic`, `*.tiff`, `*.jpg`, `*.pdf`) to images (`*.png`).

## Installation
```
pip install -r requirements.txt
```

## Usage
```py
from src.pyimg_converter import convert_from_path

input_path = 'sample.pdf'
images = convert_from_path(input_path) # return a list[PIL.Image]

# If you want to save to a PNG file:
output_path = 'sample.png'
images = convert_from_path(input_path, output_path)
```