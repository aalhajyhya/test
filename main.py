from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def HOME():
    return {"message":"this is home"}