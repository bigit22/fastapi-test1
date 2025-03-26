from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('DB is cleared')
    await create_tables()
    print('DB is ready')
    yield
    print('DB is off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
