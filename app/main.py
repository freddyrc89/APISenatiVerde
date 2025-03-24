from fastapi import FastAPI
from app.routes import alumnos, accesos
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(alumnos.router, prefix="/api", tags=["Alumnos"])
app.include_router(accesos.router, prefix="/api", tags=["Accesos"])