from random import randint
from time import sleep
import logging


logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Tasks:
    def __init__(self):
        self.process_count = 0 

    def sum(self):
        self.process_count = self.process_count + 1
        logging.info("Initializing process 1...")
        value = randint(1, 20)
        for i in range(5):
            value += 1
            sleep(2)
        logging.info("Process 1 completed.")

    def check(self):
        self.process_count = self.process_count + 1
        logging.info("Initializing process 2...")
        value = randint(1, 20)
        sleep(3 if value % 2 == 0 else 2)
        sleep(5)
        logging.info("Process 2 completed.")

    def walk(self):
        self.process_count = self.process_count + 1
        logging.info("Initializing process 3...")
        value = randint(1, 6)
        v = [1, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while value > 0 and i + 1 < len(v):
            v[i + 1] = v[i]
            value -= 1
            i += 1
        sleep(5)
        logging.info("Process 3 completed.")

    def stay(self):
        self.process_count = self.process_count + 1
        logging.info("Initializing process 4...")
        sleep(6)
        logging.info("Process 4 completed.")
