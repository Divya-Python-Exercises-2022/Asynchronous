import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()

async def heavy_task():
    await asyncio.sleep(5)

@app.get('/operation')
async def operation():
    await heavy_task()
    return 'something'


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
