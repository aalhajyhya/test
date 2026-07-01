from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def HOME():
    return {"message":"this is home"}

@app.get("/nei/{id}")
def NEIGHBOOR(id):
    return {"message":"this is neighboor"+str(id)}

@app.get("/friend/{id}")
def FRIEND(id):
    return {"message":"this is friend "+str(id)}

@app.get("/add/{x}/{y}")
def add(x,y):
    return {"message":"result is"+str(int(x)+int(y))}

@app.get("/div/{x}/{y}")
def div(x,y):
    x=int(x)
    y=int(y)
    return {"message":"result is "+str(x/y)}

@app.get("/sub/{x}/{y}")
def sub(x,y):
    return {"message":"result is "+str(int(x)-int(y))}

@app.get("/hello")
def hello():
    return {"message":"hello world"}

@app.get("/tell-me-a-joke")
def joke():
    return {"message":"a joke"}