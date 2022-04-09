from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/home")
def write_home():
    return {"Name": "Thomas", "Age": 24}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        # host=settings.HOST,
        reload=True,
        # port=settings.PORT,
    )
