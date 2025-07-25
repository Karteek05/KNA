from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class WheelsetMeasurementCreate(BaseModel):
    form_number: str = Field(..., alias="formNumber")
    submitted_by: str = Field(..., alias="submittedBy")
    submitted_date: date = Field(..., alias="submittedDate")

    tread_diameter_new: str = Field(..., alias="treadDiameterNew")
    last_shop_issue_size: str = Field(..., alias="lastShopIssueSize")
    condemning_dia: str = Field(..., alias="condemningDia")
    wheel_gauge: str = Field(..., alias="wheelGauge")
    variation_same_axle: str = Field(..., alias="variationSameAxle")
    variation_same_bogie: str = Field(..., alias="variationSameBogie")
    variation_same_coach: str = Field(..., alias="variationSameCoach")
    wheel_profile: str = Field(..., alias="wheelProfile")
    intermediate_wwp: str = Field(..., alias="intermediateWWP")
    bearing_seat_diameter: str = Field(..., alias="bearingSeatDiameter")
    roller_bearing_outer_dia: str = Field(..., alias="rollerBearingOuterDia")
    roller_bearing_bore_dia: str = Field(..., alias="rollerBearingBoreDia")
    roller_bearing_width: str = Field(..., alias="rollerBearingWidth")
    axle_box_housing_bore_dia: str = Field(..., alias="axleBoxHousingBoreDia")
    wheel_disc_width: str = Field(..., alias="wheelDiscWidth")
    remarks: Optional[str] = None

    class Config:
        populate_by_name = True


class WheelsetMeasurementOut(WheelsetMeasurementCreate):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class WheelsetMeasurementUpdate(BaseModel):
    form_number: Optional[str] = Field(None, alias="formNumber")
    submitted_by: Optional[str] = Field(None, alias="submittedBy")
    submitted_date: Optional[date] = Field(None, alias="submittedDate")

    tread_diameter_new: Optional[str] = Field(None, alias="treadDiameterNew")
    last_shop_issue_size: Optional[str] = Field(None, alias="lastShopIssueSize")
    condemning_dia: Optional[str] = Field(None, alias="condemningDia")
    wheel_gauge: Optional[str] = Field(None, alias="wheelGauge")
    variation_same_axle: Optional[str] = Field(None, alias="variationSameAxle")
    variation_same_bogie: Optional[str] = Field(None, alias="variationSameBogie")
    variation_same_coach: Optional[str] = Field(None, alias="variationSameCoach")
    wheel_profile: Optional[str] = Field(None, alias="wheelProfile")
    intermediate_wwp: Optional[str] = Field(None, alias="intermediateWWP")
    bearing_seat_diameter: Optional[str] = Field(None, alias="bearingSeatDiameter")
    roller_bearing_outer_dia: Optional[str] = Field(None, alias="rollerBearingOuterDia")
    roller_bearing_bore_dia: Optional[str] = Field(None, alias="rollerBearingBoreDia")
    roller_bearing_width: Optional[str] = Field(None, alias="rollerBearingWidth")
    axle_box_housing_bore_dia: Optional[str] = Field(None, alias="axleBoxHousingBoreDia")
    wheel_disc_width: Optional[str] = Field(None, alias="wheelDiscWidth")
    remarks: Optional[str] = None

    class Config:
        populate_by_name = True