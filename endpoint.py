from fastapi import FastAPI, Response

from jobs import long_task_1


app = FastAPI()


@app.get("/task1")
def task1():
    long_task_1.send("https://thebestmotherfucking.website/")
    return Response(status_code=202)




