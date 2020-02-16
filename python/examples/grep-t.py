import threading
import queue

class Worker(threading.Thread):
    def __init__(self, work_queue, word, number):
        super().__init__()  # must init parent class
        self.work_queue = work_queue
        self.word       = word
        self.number     = number

    def run(self):
        while True: # use becouse of daemon
            try:
                # would be blocked until queue not empty
                filename = self.work_queue.get()
                self.process(filename)
            finally:
                # notify queue, for queue.join correct work
                self.work_queue.task_done()


def main():
    opts, word, args = parse_options() # get options
    filelist = get_files(args, opts.recurse)
    work_queue = queue.Queue()  # create FIFO queue for filelist
    for i in range(opts.count): # create opts.count workers
        number = "{0}: ".format(i+1) if opts.debug else ""
        # pass queue as reference to get file from there
        # pass word to search
        worker = Worker(work_queue, word, number)   # pass number for debug
        # to close program after all workers are created
        worker.daemon = True
        worker.start()  # starts worker
        # he will wait until queue is not empty
    for filename in filelist:
        work_queue.put(filename)
    # blocks untill all items in the queue have been gotten
    # and processed
    work_queue.join() 
        
