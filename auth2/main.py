from fastapi import FastAPI

from auth2.routers.main_router import router

app = FastAPI()

app.include_router(router)
