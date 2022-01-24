from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn


app = FastAPI()


@app.get("/")
def index_page():
    return Response("Let's test this shit", media_type="text/html")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
