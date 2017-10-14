import os
from pathlib import Path

import click as clk


def requires_login(method):
    home = str(Path.home())
    if not os.path.isfile(os.path.join(home, '.papyrus', 'token')):
        clk.secho('You must login first', err=True, fg='red')
        exit()
    return method
