# Pyimg-converter

Convert file (`*.heic`, `*.tiff`, `*.jpg`, `*.pdf`) to images (`*.png`).

## Installation
```
pip install -r requirements.txt
```

## Usage
```py
from src.pyimg_converter import convert_from_path

input = 'sample.pdf'
images = convert_from_path(input) # list[PIL.Image]
```