import os, sys
import string

import random


num_entries = 1000000

with open("count_dig.tst", "w") as f:
    str_qty = random.randint(0, 20)
    str_len = random.randint(0, 20)
        
    inp = "\n".join(" ".join("".join(random.choice(string.ascii_letters +
        string.digits) for j in range(random.randint(0,20))) for i in
        range(random.randint(0, 20))) for _ in range(num_entries))


    f.write(str(inp))
