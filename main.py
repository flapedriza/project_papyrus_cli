import click as clk
import os
from pathlib import Path


def requires_login(method):
    home = str(Path.home())
    if not os.path.isfile(os.path.join(home, '.papyrus', 'token')):
        clk.secho('You must login first', err=True, fg='red')
        exit()
    return method


@clk.group()
def cli():
    clk.echo('usagdyusagdyu')


@cli.command()
@requires_login
@clk.argument('color', default='blue', required=False)
def start(color):
    clk.secho('Lleg� el bigoteeeeees', fg=color)


@cli.command()
def end():
    clk.echo('end')
