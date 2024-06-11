from typing import Optional
from app.entities.appointment_entity import AppointmentEntity
from i_response_model import IResponseModel


class ManageAppointmentResponseModel(IResponseModel):
    def __init__(self, success: bool, message: Optional[str] = None, error_code: Optional[str] = None, data: Optional[AppointmentEntity] = None):
        self.success = success
        self.message = message
        self.error_code = error_code
        self.data = data
    
    def to_dict(self) -> dict:
        response_dict = {
            "success": self.success,
            "message": self.message,
            "error_code": self.error_code,
        }

        if self.data:
            response_dict["data"] = self.data.to_dict()

        return response_dict