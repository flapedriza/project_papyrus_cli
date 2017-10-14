import click
import os

import errno
import requests
from pathlib import Path


@click.command()
@click.option('--mail', prompt='Please, enter your email address: ')
@click.option('--password', prompt='Please, enter your password: ', hide_input=True)
def login(mail, password):
    token = requests.post('http://localhost:8000/api/users/login', data={'username': mail,
                                                                         'password': password})
    if token.status_code != 200:
        click.secho('Invalid account data', fg='red')
        exit()
    click.echo(token.content)
    save_token(token.content['token'])
    click.secho('Login successful!', fg='green')


def save_token(token):
    path = os.path.join(Path.home(), '.papyrus', 'token')
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open('token', 'w+') as file:
        file.write(token)
