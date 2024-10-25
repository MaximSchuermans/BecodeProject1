# challenge-openspace-classifier

This is the repository for the first Becode project "challenge-openspace-classifier" made Kevin and Maxim. It is a simple python module that reads and excel file containing colleague names and
randomly assigns people to openspace tables.

## Installation

The code depends on several packages that should be installed through a virtual environment:

### Linux:

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage:
The main Class is openspace.py. To create a room, create an Openspace object in main.py.
A room contains by default 6 tables of 4 seats. The config.yaml file contains the Excel file that will be read.


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
