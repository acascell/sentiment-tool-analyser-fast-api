from fastapi import FastAPI
from src.app.models import User
from src.app.core.base import database

app = FastAPI(title="Sentiment tool analyser.")


@app.get("/")
async def read_root():
    return await User.objects.all()


# set event handlers on startup and shutdown
@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create dummy entry
    await User.objects.get_or_create(
        username="test", email="test@test.com", hashed_password="dGVzdHB3"  # testpw
    )


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
