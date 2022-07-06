# URL encoder-decoder

## Introduction
This repository contains a python utility to encode / decode in URL format.  
Python code can be compiled, or used as lib in other projects


## References
* [**`Percent-encoding - MDN`**](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding)
* [**`RFC 3986`**](https://datatracker.ietf.org/doc/html/rfc3986)


## Usage
Here help of script (can be get calling `URLencdec -h`):
```
usage: URLencdec.py [-h] [--decode | --encode] [--file FILEPATH | --text TEXT]

URL encoder / decoder

options:
  -h, --help            show this help message and exit
  --decode, -d          decode
  --encode, -e          encode
  --file FILEPATH, -f FILEPATH
                        input file
  --text TEXT, -t TEXT  input text
```


## Build
**Prerequisites**:
* Install [PyInstaller](https://pyinstaller.org/en/stable/)

To build an executable, launch following commands:  
* **Windows**: `pyinstaller --noupx --clean --onefile --icon=build\URLencdec.ico --console src\URLencdec.py`
* **Linux**: `pyinstaller --noupx --clean --onefile --console src/URLencdec.py`


## Tests
Run into `src` folder (minimal) test with command:
`python3 -m unittest discover`
