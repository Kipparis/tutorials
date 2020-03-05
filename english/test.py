#!python3

import os
from utils.dtypes import StringBool
from utils.file   import parse_dict

import argparse

parser = argparse.ArgumentParser(description="write a test, store "
        "results in db, than programm will decide what words to give you")
parser.add_argument("db_file_name", help="db filename for store results")
parser.add_argument("-c", "--create", help="create new db",
        action="store_true")
parser.add_argument("-w", "--words_file", type=str, default="words.dict",
        help="words file for sync with db", metavar="file_name")
parser.add_argument("-u", "--update", help="update words in database",
        action="store_true", default=True)
args = parser.parse_args()

if args.create:
    args.create = StringBool(input("Are you sure you want to recreate database "
            "(operation will remove any file/folder/symnlink on "
            "specified path - '{}')\ny,[n]: ".format(args.db_file_name)))
    if args.create:
        if os.path.exists(args.db_file_name):   # check file exists
            os.remove(args.db_file_name)        # if so, remove


import sqlite3 # https://docs.python.org/3/library/sqlite3.html
db_conn = sqlite3.connect(args.db_file_name)
db_cursor = db_conn.cursor()
if args.create:
    # create tables
    db_cursor.execute('''CREATE TABLE categories
            (ID int NOT NULL PRIMARY KEY,
            category_name text
            )''')
    db_cursor.execute('''CREATE TABLE results
            (ID int NOT NULL PRIMARY KEY,
            word text,
            score int,
            date_added date,
            category int DEFAULT -1
                REFERENCES categories(ID)
                ON UPDATE CASCADE
                ON DELETE SET DEFAULT
            )''')
    # iterate over words in .dict file and uppend them
    for entry in parse_dict(args.words_file): # must return iterable
        print(f"GOT THIIS {entry}")
        # becouse I reassign every variable for every entry
        # it gonna to be very nice to memory (but opposite to CPU)
        # for every entry -> store in db


# if args.update:



# TODO: in loop:
#   1. ask user how many words he wants to learn (default = 7)
#   2. ask user which categories does he prefer (default = all)
#   3. run test
#   4. collect how many words from each category does he answered,
#       output statistic
#       on welcom page output this statistic
#       and percantage of overall words knowledge
# Formalities:
#   1. Create simple usage for newcommers


db_conn.close() # close connection
