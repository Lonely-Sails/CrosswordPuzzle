from os.path import exists
from json import dump, load

from Configures import *


class Config:
    config = {'level': 1}

    def __init__(self):
        if exists(CONFIGURE_PATH):
            self.load()
        self.level = self.config['level']

    def load(self):
        with open(CONFIGURE_PATH, encoding='Utf-8', mode='r') as file:
            self.config = load(file)

    def save(self):
        self.config['level'] = self.level
        with open(CONFIGURE_PATH, encoding='Utf-8', mode='w') as file:
            dump(self.config, file)
