from fastapi import APIRouter

reminders = APIRouter()


@reminders.get("/reminders/", tags=["reminders"])
async def read_my_reminders():
    return [{"username": "Rick"}, {"username": "Morty"}]


