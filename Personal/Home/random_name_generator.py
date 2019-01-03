# Python Imports
import os

# Django Import
from django.conf import settings

class Generation:

    text_file_dir = os.path.dirname(__file__)
    first_name_txt_path = os.path.join(text_file_dir, './txt/First_Names.txt')

    print(text_file_dir)

    first_names_file = '../Personal/static/txt/First_Names.txt'

    # Personal/static

    def read_in_first_name(self):
        with open(self.first_name_txt_path, 'rb') as first_name:
            for line in first_name:
                print(line)

        # print(self.first_name_txt_path)

G1 = Generation()

# G1.read_in_first_name()

print(os.getcwd())