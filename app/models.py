from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WheelsetMeasurement(Base):
    __tablename__ = "wheelset_measurements"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(Date, nullable=False)

    tread_diameter_new = Column(String, nullable=False)
    last_shop_issue_size = Column(String, nullable=False)
    condemning_dia = Column(String, nullable=False)
    wheel_gauge = Column(String, nullable=False)
    variation_same_axle = Column(String, nullable=False)
    variation_same_bogie = Column(String, nullable=False)
    variation_same_coach = Column(String, nullable=False)
    wheel_profile = Column(String, nullable=False)
    intermediate_wwp = Column(String, nullable=False)
    bearing_seat_diameter = Column(String, nullable=False)
    roller_bearing_outer_dia = Column(String, nullable=False)
    roller_bearing_bore_dia = Column(String, nullable=False)
    roller_bearing_width = Column(String, nullable=False)
    axle_box_housing_bore_dia = Column(String, nullable=False)
    wheel_disc_width = Column(String, nullable=False)

    remarks = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
