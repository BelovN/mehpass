# thirdparty
from fastapi import FastAPI

# project
from .router import router as main_router


app = FastAPI()
app.include_router(main_router)
