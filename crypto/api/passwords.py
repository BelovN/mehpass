from typing import List

from fastapi import APIRouter, Depends

from crypto import tables
from crypto.models.passwords import Password

from mehpass.database import get_session, Session

router = APIRouter(prefix="/passwords")


@router.get("/", response_model=List[Password])
def get_passwords(session: Session = Depends(get_session)):
    passwords = session.query(tables.Password).all()
    return passwords
