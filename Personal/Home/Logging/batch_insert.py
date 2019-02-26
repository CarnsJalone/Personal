import os
import sys
import sqlite3

LOGGING_DIR = os.path.dirname(os.path.abspath(__file__))
HOME_DIR = os.path.dirname(LOGGING_DIR)
BASE_DIR = os.path.dirname(HOME_DIR)
TXT_DIR = os.path.join(BASE_DIR, 'static/txt')

LOGGING_FILE = os.path.join(TXT_DIR, 'logger.txt')
DB_PATH = os.path.join(BASE_DIR, 'db.sqlite3')

DELIMITER = "\n\n"

with open(LOGGING_FILE, 'r') as text_file:
    
    read_file = text_file.read()

    data = read_file

    data = data.split(DELIMITER)

    for line in data:

        connection = sqlite3.connect(DB_PATH)

        # Create table if it doesn't exist
        connection.execute('''CREATE TABLE IF NOT EXISTS Logs (
            "Log" varchar(254) NOT NULL 
        )''')

        connection.execute('''
        INSERT INTO Logs (Log) 
        VALUES ("{}")
        '''.format(line))

        connection.commit()

        connection.execute('''
        DELETE 
        FROM Logs
        WHERE Log = ""
        ''')

        connection.commit()

        connection.close()
