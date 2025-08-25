from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def about_app():
    # TODO: return a html page
    return None
