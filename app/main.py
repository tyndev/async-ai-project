import time, os
from dotenv import load_dotenv

from openai import OpenAI
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




app = FastAPI()

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_main():
    return FileResponse('static/index.html')

# TODO ws1 and ws2 are not concurrent... fix this

@app.websocket("/ws1")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': "Concurrent Asynchronous: this means the program is able to switch to other tasks while waiting for a slow task to finish. Explain in 200 words."}
        ],
        temperature=0.7,
        stream=True 
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            data = chunk.choices[0].delta.content
            await websocket.send_text(data)

@app.websocket("/ws2")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': "Concurrent Parallel: this means the program is able to run multiple tasks/threads at the exact same time. Explain in 200 words."}
        ],
        temperature=0.7,
        stream=True 
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            data = chunk.choices[0].delta.content
            await websocket.send_text(data)