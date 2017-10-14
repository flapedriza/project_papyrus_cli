import json
from base64 import b64decode

import click as clk
import requests

from user_managing import login, register, API_URL


@clk.group()
def cli():
    pass


@clk.command()
@clk.argument('color', default='blue', required=False)
def start(color):
    clk.secho('Lleg� el bigoteeeeees', fg=color)


@clk.command()
def end():
    clk.echo('end')

@clk.command()
def get_tasks():
    token = None
    with open('/home/francesc/.papyrus/token') as file: # Need to check if file exists (check nneds_login decorator)
        token = 'Token '+file.read() # Obtain token from file
    tasks = requests.get(API_URL+'/core/tasks', headers={'Authorization':token}) # GET request
    son = json.loads(tasks.text) # Obtain dict from json
    clk.echo(son)

cli.add_command(login)
cli.add_command(register)
cli.add_command(start)
cli.add_command(end)
cli.add_command(get_tasks)
