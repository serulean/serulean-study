from fastapi import APIRouter

app = APIRouter()


@app.get('/hello')
async def say_hello() -> dict:
    return {
        'message' : 'Hello World'
    }
