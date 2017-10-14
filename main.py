import click as clk

from utils.decorators import requires_login


@clk.group()
def cli():
    clk.echo('usagdyusagdyu')

@requires_login
@cli.command()
@clk.argument('color', default='blue', required=False)
def start(color):
    clk.secho('Lleg� el bigoteeeeees', fg=color)


@cli.command()
def end():
    clk.echo('end')
