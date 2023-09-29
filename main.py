from typing import Union

from fastapi import FastAPI

from routers.items import router as item_router

app = FastAPI()


app.include_router(
    router=item_router,
    prefix='/items',
)