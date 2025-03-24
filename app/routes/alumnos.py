from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import get_alumno_by_dni
from app.schemas import AlumnoSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/alumnos/{dni}", response_model=AlumnoSchema)
def read_alumno(dni: str, db: Session = Depends(get_db)):
    alumno = get_alumno_by_dni(db, dni)
    if alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno
