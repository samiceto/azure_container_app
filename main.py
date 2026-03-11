from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def indext():
    return {"hello":"world"}

@app.get("/about")
def indext():
    return {"name":"azure:app"}