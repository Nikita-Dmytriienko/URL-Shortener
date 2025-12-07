from fastapi import FastAPI, Body


app = FastAPI()



@app.post("/short_url")
async def generate_short_url(
    long_url: str = Body(embeded=True)
):
    return {"data": 1}

@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ... #redirect