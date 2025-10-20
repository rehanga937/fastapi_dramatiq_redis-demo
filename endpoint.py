import time

from fastapi import FastAPI, Response
import dramatiq
from dramatiq.brokers.redis import RedisBroker


redis_broker = RedisBroker(url="redis://localhost:6379")
dramatiq.set_broker(redis_broker)

app = FastAPI()


@app.get("/task1")
def task1():
    long_task_1.send()
    return Response(status_code=202)

@app.get("/task2")
def task2():
    long_task_2.send()
    return Response(status_code=202)


@dramatiq.actor(queue_name="high_priority")
def long_task_1():
    print("Started high priority task")
    time.sleep(10)
    with open("haha1.txt", "at") as f:
        f.write("did high priority task\n")
    print("Ended high priority task")

@dramatiq.actor(queue_name="low_priority")
def long_task_2():
    print("Started low priority task")
    time.sleep(5)
    with open("haha1.txt", "at") as f:
        f.write("did low priority task\n")
    print("Ended low priority task")