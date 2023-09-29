from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def bookings():
    return [
        {
            "id": 1,
            "name": "first"
        }
    ]


@router.get("/{booking_id}")
def read_booking(booking_id: int):
    return {"booking_id": booking_id, "name": "first"}
