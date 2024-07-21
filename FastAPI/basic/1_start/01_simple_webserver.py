from fastapi import FastAPI
import uvicorn

# FastAPI 객체 생성
app = FastAPI()

# '/'로 접근하면 return을 보여줌
@app.get('/')   # get 방식으로 루트'/'에 접근했을 때 아래 함수를 실행한다
def read_root():
    return {'Hello':'World'}

if __name__ == '__main__':
    # uvicorn.run(app, host='0.0.0.0', port=8000)
    uvicorn.run(app, host='127.0.0.1', port=8000)