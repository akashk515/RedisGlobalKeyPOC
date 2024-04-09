import concurrent.futures
import time

from config import load_config
from redis_main import redis_session
from logger import setup_logging

config = load_config()
log = setup_logging()


def incr_count(value):
    start_time = time.perf_counter()
    redis_session().incr(config['REDIS_COUNTER_KEY'], value)
    end_time = time.perf_counter()
    return end_time - start_time


def create_map_list():
    thd_count = config['THREAD_COUNT']
    map_list = []
    count = 0
    while count < thd_count:
        map_list.append(1)
        count += 1
    return map_list


def start():
    while True:
        # flag = redis_session().get('START_INCR')
        # if not flag:
        #     log.info('waiting on master to give the go ahead')
        #     time.sleep(1)
        #     continue
        with concurrent.futures.ThreadPoolExecutor(max_workers=config['THREAD_COUNT']) as executor:
            # Submit the tasks to the executor
            result = executor.map(incr_count, create_map_list())

        for ele in result:
            log.info("latency-->", ele)
        log.info("You can do ctrl+c to exit")
        time.sleep(2)


start()
