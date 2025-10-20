# Intro
This is a demo showing how `dramatiq` and `redis` can be used to perform CPU intensive tasks that should be run in the background in a `FastAPI` server.

# Setup
## 1. Install packages
From either requirements_frozen.txt or requirements.txt.
## 2. Run these commands in 3 terminals
1. Make sure a redis server is running.

    For windows just use a docker image:
    ```bash
    docker run -d --name redis -p 6379:6379 redis:latest
    ```
2. Run the FastAPI server.
    ```bash
    fastapi dev endpoint.py
    ```

3. Run the Dramatiq worker.
    ```bash
    dramatiq endpoint --queues high_priority low_priority --processes 1 --threads 1
    ```
    Here by setting processes and threads both to 1, we can ensure that only one task will be run at a time (for demonstration purposes)

# Demo
Call the 2 endpoints provided. One will run a low priority task, the other will run a high priority task.

In the dramatiq worker command, notice that 'high_priority' is typed before 'low_priority'. This ensures that the dramtiq worker prioritizes the first queue. The names do not matter, only the order does.

The dramatiq worker will prioritze the high_priority queue. U can see this by spamming the 2 endpoints.

# How it works
U can run the demo without the dramatiq worker. What will happen is, when the endpoints are called, messages are sent to the redis message queues. The dramatiq worker needs to be running to execute the jobs in the queues.
    

