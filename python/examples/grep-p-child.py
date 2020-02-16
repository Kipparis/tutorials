import os, sys

BLOCK_SIZE = 8000

number = "{0}: ".format(sys.argv[1]) if len(sys.argv) == 2 else ""
stdin = sys.stdin.buffer.read() # read from stdin
# decode task from bytes and parse to lines
# ignore means ignore errors during decoding
lines = stdin.decode("utf8", "ignore").splitlines() 
word = lines[0].rstrip() # get word to search
for filename in lines[1:]:
    filename = filename.rstrip()
    previous = "" # store previous to compare word split on two sections
    try:
        with open(filename, "rb") as fh:
            while True:
                current = fh.read(BLOCK_SIZE)
                if not current: break
                current = current.decode("utf8", "ignore")
                if (word in current or 
                        word in previous[-len(word):] + current[:len(word)]):
                    # found concurrence
                    print("{0}{1}".format(number, filename))
                    break
                if len(current) != BLOCK_SIZE: # last block
                    break
                previous = current
    except EnvironmentError as err:
        print("{0}{1}".format(number, err))

