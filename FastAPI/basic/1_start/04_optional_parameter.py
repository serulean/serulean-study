from typing import Optional

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/items/{item_id}')
def read_item(item_id: str, q: Optional[str]=None):
    if q:
        return {'item_id': item_id, 'q':q}
    return {'item_id': item_id}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    