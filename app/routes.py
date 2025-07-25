from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/wheelsets", response_model=schemas.WheelsetMeasurementOut)
def create_wheelset(data: schemas.WheelsetMeasurementCreate, db: Session = Depends(get_db)):
    wheelset = models.WheelsetMeasurement(**data.dict())
    db.add(wheelset)
    db.commit()
    db.refresh(wheelset)
    return wheelset

@router.get("/wheelsets", response_model=list[schemas.WheelsetMeasurementOut])
def get_wheelsets(db: Session = Depends(get_db)):
    return db.query(models.WheelsetMeasurement).all()