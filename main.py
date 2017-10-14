import click as clk

from user_managing import login
from utils.decorators import requires_login


@clk.group()
def cli():
    pass

@clk.command()
@clk.argument('color', default='blue', required=False)
def start(color):
    clk.secho('Lleg� el bigoteeeeees', fg=color)


@cli.command()
def end():
    clk.echo('end')


cli.add_command(login)
cli.add_command(start)