from typing import Optional
from .i_response_model import IResponseModel


class IncompleteOperationResponseModel(IResponseModel):
    def __init__(self, message: Optional[str] = None, error_code: Optional[str] = None):
        self.success = False
        self.message = message
        self.error_code = error_code
    
    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "message": self.message,
            "error_code": self.error_code,
        }