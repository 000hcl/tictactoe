# 5 in a row tic-tac-toe

[Final release](https://github.com/000hcl/tictactoe/releases/tag/final)

## Documentation

[Project Specification](https://github.com/000hcl/tictactoe/blob/main/documentation/project_specification.md)

[instructions](https://github.com/000hcl/tictactoe/blob/main/documentation/user_guide.md)

[implementation](https://github.com/000hcl/tictactoe/blob/main/documentation/implementation.md)

[testing](https://github.com/000hcl/tictactoe/blob/main/documentation/testing.md)


## Weekly reports:
[week1](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week1.md)

[week2](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week2.md)


[week3](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week3.md)


[week4](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week4.md)


[week5](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week5.md)

[week6](https://github.com/000hcl/tictactoe/blob/main/documentation/weekly_reports/week6.md)



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

Testing (does not work): 
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
