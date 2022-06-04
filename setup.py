from setuptools import setup

APP = ['WPM.py']
DATA_FILES = ['text.txt']
OPTIONS = {'argv_emulation': True,
           'resources': ["text.txt"],
           'packages': ['curses'],
            }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
