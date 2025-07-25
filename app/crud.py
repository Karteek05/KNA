from sqlalchemy.orm import Session
from app import models, schemas

def create_wheelset(db: Session, data: schemas.WheelsetMeasurementCreate):
    new_entry = models.WheelsetMeasurement(**data.model_dump())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_all_wheelsets(db: Session):
    return db.query(models.WheelsetMeasurement).all()

def update_wheelset(db: Session, wheelset_id: int, update_data: schemas.WheelsetMeasurementUpdate):
    db_obj = db.query(models.WheelsetMeasurement).filter(models.WheelsetMeasurement.id == wheelset_id).first()
    if not db_obj:
        return None
    update_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj