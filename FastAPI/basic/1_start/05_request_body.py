from typing import Optional
from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float]=None


app = FastAPI()


@app.post('/items/')
def create_item(item: Item):    # 새로운 값을 받을 때 Item이 정한 클래스에 맞는지 validation
    return item


if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)