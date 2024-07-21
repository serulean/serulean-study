from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/users/{user_id}')    # get 방식. users의 user_id에 인자를 주면 path parameter가 됨
def get_user(user_id):
    return {'user_id':user_id}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    