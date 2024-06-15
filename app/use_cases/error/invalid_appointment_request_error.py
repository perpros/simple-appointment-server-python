from typing import List
from .domain_error import DomainError


class InvalidAppointmentRequestError(DomainError):
    """
    Raised when the appointment request data is invalid.
    """

    def __init__(self, errors: List[str]):
        super().__init__("Invalid appointment request: " + ", ".join(errors))
