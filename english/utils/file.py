import re
from collections import namedtuple

Word = namedtuple('Word', ['category', 'eng_str','ru_str',
    'description', 'clarification'])

class Dict:
    __slots__ = ("file_name", "word_dict")

    def __init__(self, file_name):
        self.file_name = file_name  # store inited filename
        self.word_dict = {}         # dictionary containing words from file

        d = self.word_dict  # shortcut for faster access


# I don't want to keep dictionary in python memory, so I just return info
# from file
def parse_dict(file_name):
    """Parse categories in dict and return iterable"""
    import os, itertools
    words = []  # structure I'll yield
    with open(file_name, "r") as f:
        line = f.readLine()
        header = ""
        while line:
            # for each line there are two cases:  
            #       header - assign variable header to it
            #       entry  - store into yielding value
            search = re.search(r"\A[.*]", line)
            if not search.group(0):
                # rm comments
                line = re.sub(r'#.*\Z',"",line).strip()
            else: header = search.group(0)

    pass

