from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/user")
def get_user(id):
    # ❌ no typing, no response_model, no validation
    return {"id": id, "name": "Alice"}


@app.post("/login")
def login(request: Request):
    data = request.json()  # ❌ no schema, unsafe parsing
    if data["password"] == "secret":
        return {"status": "ok"}
    return {"status": "fail"}
