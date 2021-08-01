# thirdparty
from fastapi import APIRouter

# app
from crypto.api.controllers.credentials import router as credentials_router


router = APIRouter()
router.include_router(credentials_router)
