import click as clk
#import task
import os
from pathlib import Path
import requests
import json

API_URL = 'http://51.15.195.60/api'
global token

def get_token():
    path = os.path.join(str(Path.home()), '.papyrus', 'token')
    if not os.path.exists(os.path.dirname(path)):
        print("You need to be logged in")
        exit()
    with open(path,'r') as file:
        return file.read()

@clk.group()
def clo(): pass

@clk.command()
@clk.option('--name', help='Name of the task, required', prompt='Please, enter a task name')
@clk.option('--priority', type=clk.IntRange(1, 3),
 help='Priority of the task (from 1=most to 3=least), required',
 prompt='Please, enter the task\'s priority (from 1=most to 3=least)')
@clk.option('--deadline', help='A deadline for the task (format YYYYMMDD)')
@clk.option('--description', help='A description for the task')
@clk.option('--project', help='The project the task belongs to')
@clk.option('--tags', '-t', multiple=True, help='Any tag related to the task')
def add_task(name, priority, deadline, description, project, tags):
    token = get_token()

    year = int(deadline[0:4])
    month = int(deadline[4:6])
    day = int(deadline[6:8])
    deadline = datetime(year,month,day)

    new_task = Task(name,priority,'stub_user',deadline,description,project,tags)
    data = new_task.toDjango()

    token2 = requests.post(API_URL +'/core/tasks/', data=data)
    if token2.status_code != 200:
        click.secho('Invalid account data: '+str(token.content), fg='red')
        exit()

@clk.command()
def tasks_list(): pass

@clk.command()
def task_info(): pass

@clk.command()
def modify_task(): pass

@clk.command()
def complete_task(): pass

def retrieve(): pass

def update(): pass

clo.add_command(add_task)
