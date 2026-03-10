from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def indext():
    return {"hello":"world"}