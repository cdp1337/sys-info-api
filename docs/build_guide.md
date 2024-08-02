# Developer Build Guide

## Setup PyPA build system

`python3 -m pip install --upgrade build`

## Install Twine (used for uploads)

`python3 -m pip install --upgrade twine`

## Generate distribution

`python3 -m build`

## Upload distribution

`python3 -m twine upload dist/*`