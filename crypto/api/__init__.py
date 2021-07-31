# thirdparty
from fastapi import APIRouter

# app
from crypto.controllers.credentials import router as passwords_router


router = APIRouter()
router.include_router(passwords_router)
