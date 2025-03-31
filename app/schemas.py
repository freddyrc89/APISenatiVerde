from pydantic import BaseModel
from datetime import datetime

class AlumnoSchema(BaseModel):
    dni: str
    nombre: str
    programa_estudios: str
    estado: str
    observaciones: str | None = None

    class Config:
        from_attributes = True

class CreacionQRBase(BaseModel):
    dni_alumno: int
    estado_qr: int

class CreacionQRCreate(CreacionQRBase):
    pass

class CreacionQRResponse(CreacionQRBase):
    id: int
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True

