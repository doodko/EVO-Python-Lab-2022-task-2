from fastapi import FastAPI, Form
from fastapi.responses import Response
import uvicorn
import db


app = FastAPI()


@app.get("/")
def index_page():
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        home_page = f.read()
    return Response(home_page, media_type="text/html")
    

@app.post('/hello')
def say_hello(username : str = Form(...)):
    answer = db.check_if_met_before(username)
    return Response(answer, media_type='text/html')


@app.get("/friends")
def friends_page():
    friens_list = 'Тут були: ' + ', '.join(db.find_all_friends()) + '...'
    return Response(friens_list, media_type="text/html")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
