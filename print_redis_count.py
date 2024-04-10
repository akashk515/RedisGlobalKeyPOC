import time

from redis_main import redis_session
from config import load_config

config = load_config()


def main():
    last_sec = 0
    while True:
        value = redis_session().get(config['REDIS_COUNTER_KEY'])
        print('per sec diff-->', value - last_sec)
        last_sec = value
        print(value)
        time.sleep(1)


main()
