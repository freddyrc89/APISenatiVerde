from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, crud

router = APIRouter(
    prefix="/creacion_qr",
    tags=["CreacionQR"]
)

@router.post("/", response_model=schemas.CreacionQRResponse)
def create_qr(qr_data: schemas.CreacionQRCreate, db: Session = Depends(get_db)):
    return crud.create_creacion_qr(db, qr_data)
