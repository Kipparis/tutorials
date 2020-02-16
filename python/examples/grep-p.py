#!python3

# -*- coding: utf-8 -*-

import os, sys

def main():
    child = os.path.join(os.path.dirname(__file__), "grep-p-child.py")
    # opts = namedtuple and show does we search recursively
    # word is the word we searching
    # args is additional data
    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    files_per_process = len(filelist) // opts.count
    # becouse of situation were files not delimeted by processes,
    # we give first process more files to handle
    start, end = 0, files_per_process + (len(filelist) % opts.count)
    number = 1
    pipes = [] # store all pipes to wait them at the end
    while start < len(filelist):
        # sys.executable stores save version of python
        comand = [sys.executable, child]
        if opts.debug:
            # pass number to track which process is outputting
            command.append(str(number)) 
        pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
        pipes.append(pipe)
        # write word and files for search in
        pipe.stdin.write(word.encode("utf8") + b"\n")
        for filename in filelist[start:end]:
            pipe.stdin.write(filename.encode("utf8") + b"\n")
        # when done close the pipe
        pipe.stdin.close()
        number += 1
        start, end = end, end + files_per_process

    # do not exit from main program until we're done with subprocesses
    # and exit as all subprocesses gone
    while pipes:
        pipe = pipes.pop()
        pipe.wait()

