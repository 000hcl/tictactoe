# Instructions

## Installation

1. Make sure poetry and python is installed.

2. Download the latest release

3. unzip into the directory of your choice

4. move the the unzipped directory with the terminal and execute a command:

## Commands:

Note: To run these commands poetry and python (3.6 or higher) are required.

1. Run to install dependencies:
```bash
poetry install 
```
2. Runs the program: (running main.py wihtout poetry should be possible)
``` bash
poetry run invoke start
```
---

Testing: (CURRENTLY MOST WILL FAIL)
```bash
poetry run invoke test
```

Coverage report:

(poetry run invoke coverage may be needed to run beforehand?)

```bash
poetry run invoke coverage-report
```
---

Lint:
```bash
poetry run invoke lint
```
