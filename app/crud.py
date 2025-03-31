from sqlalchemy.orm import Session
from app.models import Alumno
from app import models, schemas


def get_alumno_by_dni(db: Session, dni: str):
    return db.query(Alumno).filter(Alumno.dni == dni).first()


def create_creacion_qr(db: Session, qr_data: schemas.CreacionQRCreate):
    db_qr = models.CreacionQR(**qr_data.dict())
    db.add(db_qr)
    db.commit()
    db.refresh(db_qr)
    return db_qr
