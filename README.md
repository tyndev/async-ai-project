# async-ai-project
Learning Project: A simple Python application that demonstrates concurrent programming and interactions with a large language model (LLM) using OpenAI's API.

## Learnings
This project has helped me solidify concurrent programming and real-time interactions with language models. 
### Exploring Asynchronous Programming
An appreciation for the power and complexity of asynchronous operations has been a key takeaway. Python's `asyncio` library and FastAPI framework facilitated the creation of non-blocking API calls to OpenAI's LLM.
### Understanding Websockets and Real-time Communication
Learning to set up a WebSocket endpoint was crucial for real-time browser-server communication and streaming AI responses. It has shown how to maintain a live interaction with the client side.
### .env for Sensitive Information
Implementing the use of environment variables to securely handle API keys. Using `python-dotenv` to load the keys from a `.env` file ensures that sensitive information is not hard-coded into the application.
### Static Files and FastAPI
Learned how to serve static files using FastAPI's `StaticFiles` for frontend assets.

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```
## Summary: Main Takeaways
Through this project I delved into asynchronous programming in Python and learned to interact with OpenAI's API, manage static content in a web application, and use WebSockets for real-time data streaming.