from typing import Union

from fastapi import FastAPI

from routers.bookings import router as booking_router

app = FastAPI()


app.include_router(
    router=booking_router,
    prefix='/bookings',
)