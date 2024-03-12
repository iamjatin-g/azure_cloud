from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return "<<<This is a Home Page>>>"

@app.get("/about")
def about():
    return "<<<This is an About Page>>>"