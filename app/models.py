from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(10), unique=True, index=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    programa_estudios = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False)
    observaciones = Column(String(255), nullable=True)

class Acceso(Base):
    __tablename__ = "accesos"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(10), ForeignKey("alumnos.dni"), nullable=False)
    fecha_hora = Column(DateTime, default=datetime.utcnow)
    estado_acceso = Column(String(20), nullable=False)
    observaciones = Column(String(255), nullable=True)
    qr_creado = Column(Boolean, default=False)
    qr_expira = Column(DateTime, nullable=False)