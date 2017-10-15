

@clk.command()
@click.option('--name', prompt='Please, enter a task name: ')
@click.option('--deadline', prompt='Please, enter the task\'s deadline (format YYYY/MM/DD): ') # alt: date.time (infer format)
@click.option('--priority', type=click.IntRange(1, 3),
 prompt='Please, enter the task\'s priority (from 1=most to 3=least): ')
@click.option('--project', prompt='Please, enter the task\'s deadline: ')
def add_task()

project
title, description
prioridad
is_done
fecha de vencimiento
created / modified
tags
