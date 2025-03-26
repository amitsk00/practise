from fastapi import FastAPI
import asyncio

app = FastAPI()

# Simulating a time-consuming task (e.g., making an API request)
async def slow_task():
    print("Task started...")
    await asyncio.sleep(5)  # Simulate a 5-second delay
    print("Task completed!")
    return "Task result"

# Async endpoint
@app.get("/async-task")
async def async_task():
    result = await slow_task()  # We await the slow_task coroutine here
    return {"message": result}

