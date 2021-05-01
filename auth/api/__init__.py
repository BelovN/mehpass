# fastapi
from fastapi import APIRouter

# project
from .auth import router as auth_router


router = APIRouter()
router.include_router(auth_router)
