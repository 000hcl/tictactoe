from invoke import task

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
