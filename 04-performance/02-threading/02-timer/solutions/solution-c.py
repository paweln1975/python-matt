
import subprocess
from queue import Queue
from threading import Timer


work_queue = Queue()


def run():
    while True:
        cmd = work_queue.get()

        try:
            subprocess.run(cmd, timeout=TIMEOUT, shell=True)
        except subprocess.TimeoutExpired:
            logging.error('Timeout')
            break

        work_queue.task_done()


t = Timer(DELAY, run)
t.start()

# Assign tasks
for todo in
    work_queue.put(todo)

# Wait to complete all tasks
t.join(timeout=TIMEOUT)
