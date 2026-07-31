from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="RealmRelay Agent",
    version="0.0.3"
)

app.include_router(router)