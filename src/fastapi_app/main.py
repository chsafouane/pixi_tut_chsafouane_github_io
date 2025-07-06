from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/")
def welcome():
    """
    A simple endpoint that returns a welcome message.
    """
    return {"Hello": "Pixi"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """
    An endpoint that takes a path parameter and an optional query parameter.
    """
    return {"item_id": item_id, "q": q}