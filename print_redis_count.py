import time

from redis_main import redis_session
from config import load_config

config = load_config()


def main():
    while True:
        value = redis_session().get(config['REDIS_COUNTER_KEY'])
        print(value)
        time.sleep(1)


main()
