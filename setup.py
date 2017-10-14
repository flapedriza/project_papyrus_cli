from setuptools import setup

setup(
    name='papyrus',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        papyrus=main:cli
    '''
)