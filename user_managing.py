import json

import click
import os

import errno
import requests
from pathlib import Path

API_URL = 'http://51.15.195.60/api'

@click.command()
@click.option('--mail', prompt='Please, enter your email address: ')
@click.option('--password', prompt='Please, enter your password: ', hide_input=True)
def login(mail, password):
    token = requests.post(API_URL +'/users/login/', data={'username': mail, 'password': password})
    if token.status_code != 200:
        click.secho('Invalid account data: '+str(token.content), fg='red')
        exit()
    res = json.loads(token.text)
    click.echo(res['token'])
    save_token(res['token'])
    click.secho('Login successful!', fg='green')


def save_token(token):
    path = os.path.join(str(Path.home()), '.papyrus')
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(os.path.join(path, 'token'), 'w+') as file:
        file.write(token)

@click.command()
@click.option('--user', prompt='Enter your email address', confirmation_prompt=True)
@click.password_option()
def register(user, password):
    token =requests.post(API_URL+'/users/register', data={'email':user, 'password': password})
    if token.status_code != 200:
        click.secho('Invalid account data: '+str(token.content), fg='red')
        exit()
    res = json.loads(token.text)
    save_token(res['token'])
    click.echo('User created successfully with token {}'.format(res['token']))
