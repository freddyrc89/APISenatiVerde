from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_acceso
from app.schemas import AccesoCreateSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/accesos/")
def create_acceso_route(acceso: AccesoCreateSchema, db: Session = Depends(get_db)):
    return create_acceso(db, acceso)
