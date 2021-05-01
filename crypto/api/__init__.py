# thirdparty
from fastapi import APIRouter

# app
from .passwords import router as passwords_router


router = APIRouter()
router.include_router(passwords_router)
