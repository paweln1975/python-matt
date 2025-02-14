def run():
    while True:
        cmd = work_queue.get()
        try:
            result = subprocess.run(
                cmd,
                timeout=TIMEOUT,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            stdout = result.stdout.decode().strip()
            stderr = result.stderr.decode().strip()
            logging.info(f'\nCommand: {cmd}\nStdout: {stdout}\nStderr: {stderr}\n')
        except subprocess.TimeoutExpired:
            logging.info('Timeout threading_timer_c.py')
            break
        work_queue.task_done()


work_queue = Queue()
t = Timer(DELAY, run)
t.start()

for cmd in COMMANDS:
    work_queue.put(cmd)

t.join(timeout=TIMEOUT)