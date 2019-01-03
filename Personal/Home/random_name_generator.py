# Python Imports
from os import path
import random

CURRENT_FILE_DIRECTORY = path.dirname(path.dirname(path.abspath(__file__)))
TEXT_FILE_DIRECTORY = path.join(CURRENT_FILE_DIRECTORY, 'static/txt')

class Generator:

    def __init__(self):

        self.FIRST_NAMES_FILE = path.join(TEXT_FILE_DIRECTORY, 'First_Names.txt')
        self.LAST_NAMES_FILE = path.join(TEXT_FILE_DIRECTORY, 'Last_Names.txt')

    def generate_random_first_name(self):

        first_names = open(self.FIRST_NAMES_FILE, 'rb')

        list_of_first_names = []
        formatted_list_of_first_names = []

        for name in first_names:
            list_of_first_names.append(name)

        first_names.close()

        for name in list_of_first_names:
            name = name.decode('utf-8')
            name = name.replace("\n", "")
            formatted_list_of_first_names.append(name)

        random_first_name = random.choice(formatted_list_of_first_names)

        return random_first_name
     
    def generate_random_last_name(self):

        last_names = open(self.LAST_NAMES_FILE, 'rb')

        list_of_last_names = []
        formatted_list_of_last_names = []

        for name in last_names:
            list_of_last_names.append(name)

        last_names.close()

        for name in list_of_last_names:
            name = name.decode('utf-8')
            name = name.replace("\n", "")
            formatted_list_of_last_names.append(name)

        random_last_name = random.choice(formatted_list_of_last_names)

        return random_last_name

    def generate_random_full_name(self):
        first = self.generate_random_first_name()
        last = self.generate_random_last_name()
        random_full_name = '{} {}'.format(first, last)

        return random_full_name
