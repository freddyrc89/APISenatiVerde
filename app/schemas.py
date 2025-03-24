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

class AccesoCreateSchema(BaseModel):
    dni: str
    estado_acceso: str
    observaciones: str | None = None
    qr_expira: datetime

    class Config:
        from_attributes = True
