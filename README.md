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


 md

## Evaluation criteria

| Criteria       | Indicator                                                                              | Yes/No |
| -------------- | -------------------------------------------------------------------------------------- | ------ |
| 1. Is complete | The student has realized all must-have features.                                       | 1      |
|                | There is a published GitHub repo available.                                            | 1      |
|                | The program runs until the end without any error.                                      | 1      |
|                | The program starts by running `python main.py` in the terminal.                      | 1      |
| 2. Is correct  | The code is well typed.                                                                | 1      |
|                | There is a docstring for every function/method/class.                                  | 1      |
|                | All the constraints are respected.                                                     | 1      |
| 3. Is great    | There is an interaction with the user.                                                 | 0      |
|                | The algorithm doesn't create table with alone people.                                  | 1      |
|                | The result is nicely displayed and can be saved in a file.                             | 1      |
|                | The program has been developped has a team using proper git flow and management system | 1      |
