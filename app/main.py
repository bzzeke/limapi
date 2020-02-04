import api
import os
import time
import sys
import threading
from threading import Thread


def import_env():
    filepath = os.path.dirname(os.path.realpath(__file__)) + '/../.env'
    if not os.path.isfile(filepath):
        return

    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            parts = line.split('=', 1)
            if len(parts) == 2:
                os.environ[parts[0].strip()] = parts[1].strip()


if __name__ == "__main__":

    import_env()

    s = Thread(target = api.main)
    s.daemon = True
    s.start()
    total_threads = threading.active_count()

    while True:
        time.sleep(1)
        if threading.active_count() < total_threads:
            print("Some thread is dead")
            sys.exit(1)