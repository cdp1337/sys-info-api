# Developer Build Guide

## Setting up from source (for development)

Install code from git

```bash
git clone git@github.com:cdp1337/sys-info-api.git
cd sys-info-api
```

Pyenv is useful for installing different versions of Python for testing.
It is recommended to use 3.6 or 3.9 for this project, (for better legacy support)

https://github.com/pyenv/pyenv

```bash
# Install pyenv
curl https://pyenv.run | bash

# Install v 3.9.16 in ~/.pyenv
pyenv install 3.9.16

# Setup virtual environment in project directory for Py 3.9.16
~/.pyenv/versions/3.9.16/bin/python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install package in editable mode
venv/bin/pip3 install -e .[dev]
```

<!--

### Operating system specific requirements (DEV)

**Linux Mint 22**

```bash
sudo apt install git python3-venv
```

**Debian 12**

```bash
sudo apt install git python3-venv
```
-->

### Notes for Jetbrains / IntelliJ

If using Jetbrains to run coverage tests:

```bash
sudo apt install libsqlite3-dev
```


### Running tests

All tests in this platform are written with unittest and are compatible with pytest.

```bash
# Run all tests with pytest
pytest

# Example output
======================================= test session starts =======================================
platform linux -- Python 3.9.16, pytest-8.3.2, pluggy-1.5.0
benchmark: 4.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/charlie/Projects/sys-info-api
configfile: pyproject.toml
plugins: benchmark-4.0.0
collected 25 items                                                                                                                                                                                                                 

tests/common/test_cmd.py ..............                                                                                                                                                                                      [ 56%]
tests/test_common.py ......                                                                                                                                                                                                  [ 80%]
tests/test_data.py .                                                                                                                                                                                                         [ 84%]
tests/test_key_value_parser.py ..                                                                                                                                                                                            [ 92%]
tests/test_yum_repos.py ..                                                                                                                                                                                                   [100%]

======================================= 25 passed in 0.25s =======================================
```

The low-level `unittest` from Python can also be used for producing more detailed output.

```bash
# Run all tests with unittest
python -m unittest discover tests/

# Example output
......Loading test data from rocky-9.4-x86_64-20240817_004527
  Testing bin.arp.txt
  Testing bin.df.txt
  Skipping bin.dmibaseboard, test data not found
  Testing bin.dmibios.txt
  Skipping bin.dmicache, test data not found
  ...
Loading test data from linuxmint-22-x86_64-20240817_010653
  Testing bin.arp.txt
  Testing bin.df.txt
  Skipping bin.dmibaseboard, test data not found
  Testing bin.dmibios.txt
  Skipping bin.dmicache, test data not found
  ...
/home/charlie/Projects/sys-info-api/tests/data
.....
----------------------------------------------------------------------
Ran 11 tests in 0.094s

OK
```

### Linting code

Code linting of this project is done with `flake8` and is done automatically on pre-commit.

To manually lint code prior to commit:

```bash
flake8 src
```


## Managing build and distribution

To upload to PyPI, the following steps are useful:

### Setup PyPA build system

`python3 -m pip install --upgrade build`

### Install Twine (used for uploads)

`python3 -m pip install --upgrade twine`

### Generate distribution

`python3 -m build`

### Upload distribution

`python3 -m twine upload dist/*`


## Other tools? (@todo sort / categorize these)

sudo apt install lldpad
sudo apt install wireless-tools
sudo apt install pre-commit
Generate documentation: `lazydocs src --overview-file=api.md`
Install dev dependencies `pip install .[dev]`


Collectors: when writing a collector, try to ensure to use
low level classes when applicable when returning field data.

ie: when returning a date, use datetime.datetime instead of a string.
