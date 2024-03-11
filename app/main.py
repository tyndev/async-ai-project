
from fastapi import FastAPI #, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()


# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_main():
    return FileResponse('static/index.html')

# TODO setup websocket connection to OpenAI api for streaming responses

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = "Message from WebSocket"
#         await websocket.send_text(data)
#         # Logic to send real-time data