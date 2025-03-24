from sqlalchemy.orm import Session
from app.models import Alumno, Acceso
from app.schemas import AccesoCreateSchema

def get_alumno_by_dni(db: Session, dni: str):
    return db.query(Alumno).filter(Alumno.dni == dni).first()

def create_acceso(db: Session, acceso: AccesoCreateSchema):
    db_acceso = Acceso(**acceso.dict())
    db.add(db_acceso)
    db.commit()
    db.refresh(db_acceso)
    return db_acceso
