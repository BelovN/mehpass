# thirdparty
from fastapi import APIRouter

# project
from auth.api import router as auth_router
from crypto.api import router as crypto_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(crypto_router)
