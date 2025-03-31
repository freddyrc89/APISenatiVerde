from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(10), unique=True, index=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    programa_estudios = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False)
    observaciones = Column(String(255), nullable=True)

class CreacionQR(Base):
    __tablename__ = "creacion_qr"
    
    id = Column(Integer, primary_key=True, index=True)
    dni_alumno = Column(Integer, ForeignKey("alumnos.dni"))
    fecha_creacion = Column(DateTime, server_default="CURRENT_TIMESTAMP")
    estado_qr = Column(Integer, default=0)
    
    alumno = relationship("Alumno")