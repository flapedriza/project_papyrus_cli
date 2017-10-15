from setuptools import setup, find_packages

setup(
    name='papyrus',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main', 'user_managing', 'task_commands'],
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points='''
        [console_scripts]
        #papyrus=main:cli
        papyrus=task_commands:clo
    '''
)
