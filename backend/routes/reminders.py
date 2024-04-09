from fastapi import APIRouter, status

reminders = APIRouter(
    prefix='/reminders'
)


@reminders.get("/")
async def read_mys_reminders():
    return [{"username": "Rick"}, {"username": "Morty"}]

@reminders.get("/{id}")
async def read_one_reminder():
    return [{"username": "Rick"}, {"username": "Morty"}]

@reminders.post("/", status_code=status.HTTP_201_CREATED)
async def create_reminders():
    return [{"username": "Rick"}, {"username": "Morty"}]

@reminders.patch("/{id}")
async def remindersreminder():
    return [{"username": "Rick"}, {"username": "Morty"}]
@reminders.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reminder():
    return [{"username": "Rick"}, {"username": "Morty"}]
