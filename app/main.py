from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Optional: CORS setup for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wheelsets", response_model=list[schemas.WheelsetMeasurementOut])
def get_wheelsets(db: Session = Depends(get_db)):
    return crud.get_all_wheelsets(db)

@app.post("/wheelsets")
def create_wheelset(data: schemas.WheelsetMeasurementCreate, db: Session = Depends(get_db)):
    result = crud.create_wheelset(db, data)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": result
    }

@app.put("/wheelsets/{wheelset_id}", response_model=schemas.WheelsetMeasurementOut)
def update_wheelset(wheelset_id: int, update_data: schemas.WheelsetMeasurementUpdate, db: Session = Depends(get_db)):
    updated = crud.update_wheelset(db, wheelset_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Wheelset not found")
    return updated