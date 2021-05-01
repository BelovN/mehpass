# stdlib
from typing import List

# fastapi
from fastapi import APIRouter, Depends

# project
from auth.services.auth import get_current_user
from auth.tables import User
from crypto import tables
from crypto.models.passwords import Password
from mehpass.database import get_session, Session

router = APIRouter(prefix="/passwords")


@router.get("/", response_model=List[Password])
def get_passwords(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    passwords = session.query(tables.Password).all()
    return passwords
