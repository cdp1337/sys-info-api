# Developer Build Guide

## Setup PyPA build system

`python3 -m pip install --upgrade build`

## Install Twine (used for uploads)

`python3 -m pip install --upgrade twine`

## Generate distribution

`python3 -m build`

## Upload distribution

`python3 -m twine upload dist/*`




If using Jetbrains to run coverage tests:
sudo apt install libsqlite3-dev

https://github.com/pyenv/pyenv

curl https://pyenv.run | bash

pyenv install 3.9.16

~/.pyenv/versions/3.9.16/bin/python3 -m venv venv
source venv/bin/activate


Install package in editable mode
venv/bin/pip3 install -e .


sudo apt install lldpad
sudo apt install wireless-tools


apt install python3-pip

apt install pre-commit


Run tests: `pytest`

Lint code: `flake8 src`

Generate documentation: `lazydocs src --overview-file=api.md`

Install dev dependencies `pip install .[dev]`
