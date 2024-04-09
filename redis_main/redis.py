import redis
from redlock import Redlock
from logger import setup_logging
from config import load_config

log = setup_logging()
config = load_config()

redis_host = config['REDIS_MAIN']['HOST']
redis_port = config['REDIS_MAIN']['PORT']
db_number = config['REDIS_MAIN']['DB']

log.log('connection to redis syncer stats db', redis_host, redis_port, db_number)

POOL = redis.ConnectionPool(host=redis_host, port=redis_port, db=db_number, decode_responses=True)
reds = redis.Redis(connection_pool=POOL)
redlock = Redlock([{"host": redis_host, "port": redis_port, "db": db_number}, ])
