from fastapi import FastAPI, Form, Request  # request할 때의 객체를 뜻함. request data 다 가지고 있음
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory='./')


@app.get('/login/')
def get_login_form(request: Request):
    return templates.TemplateResponse('login_form.html', context={'request': request})


@app.post('/login/')
def login(username: str=Form(...), password: str=Form(...)):
    return {'username': username}


if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8000)