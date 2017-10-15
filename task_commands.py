import click as clk
import task

API_URL = 'http://51.15.195.60/api'

@clk.command()
@click.option('--name', prompt='Please, enter a task name: ')
@click.option('--deadline', prompt='Please, enter the task\'s deadline (format YYYY/MM/DD): ') #
@click.option('--priority', type=click.IntRange(1, 3),
 prompt='Please, enter the task\'s priority (from 1=most to 3=least): ')
@click.option('--project', prompt='Please, enter the task\'s deadline: ')

@clk.command()
def add_task():

@clk.command()
def consult_task():

@clk.command()
def modify_task():

@clk.command()
def complete_task():

@clk.command()
def tasks_list():

def retrieve():

def update():
