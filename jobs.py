import aiohttp
import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.middleware import AsyncIO


# setup dramatiq
redis_broker = RedisBroker(url="redis://localhost:6379")
redis_broker.add_middleware(AsyncIO())
dramatiq.set_broker(redis_broker)


@dramatiq.actor(queue_name="low_priority")
async def long_task_1(url: str):
    print("Started job")
    time.sleep(10)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
    with open("haha1.txt", "at") as f:
        f.write(data[:100])
        f.write("\n")
    print("Ended job")