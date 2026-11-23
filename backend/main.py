from fastapi import FastAPI

app = FastAPI(title="Safar Hazara API")


@app.get("/")
def home():
    return {"message": "Safar Hazara chal raha hai"}