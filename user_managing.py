import click
import requests

from main import cli


@cli.command()
@click.argument('user')
@click.argument('password')
def login(user, password):
    token = requests.post('localhost:8000/api/users/login', data={'user':user, 'password':password})
    click.echo(token.content)