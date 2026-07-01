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

@app.get("/feat1/{x}/{y}")
def feature1(x,y):
    return {"message":"this is feat1 of "+str(int(x)+int(y))+str(type(x))}

@app.get("/div/{x}/{y}")
def div(x,y):
    x=int(x)
    y=int(y)
    return {"message":"result is "+str(x/y)}