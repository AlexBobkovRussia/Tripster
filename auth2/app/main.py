from fastapi import FastAPI

from auth2.routers.main_router import router

app = FastAPI()


@app.get('/')
async def about_app():
    # TODO: return a html page
    return None


app = FastAPI()

app.include_router(router)
