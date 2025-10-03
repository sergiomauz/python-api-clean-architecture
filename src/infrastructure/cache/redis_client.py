
import os
import redis


REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
_redis_instance = None


def get_redis_client():
    global _redis_instance
    if _redis_instance is None:
        _redis_instance = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            max_connections=100
        )
    return _redis_instance
