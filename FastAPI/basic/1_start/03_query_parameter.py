from fastapi import FastAPI
import uvicorn


app = FastAPI()

fake_item_db = [{'item_name':'Foo'}, {'item_name':'Bar'}, {'item_name':'Baz'}]


@app.get('/items/')     # path param과 다르게 url에는 아무것도 입력이 안되어있음
def read_item(skip: int=0, limit: int=10):
    return fake_item_db[skip:skip+limit]


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
