from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
def welcome():
    return "Welcome to Docker Course"

if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=3000)