from typing import Optional
from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float]=None

class ItemOut(BaseModel):
    name: str
    price: float
    tax: Optional[float]=None


app = FastAPI()


@app.post('/items/', response_model=ItemOut)    # respose
def create_item(item: ItemIn):  # request
    return item


if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)