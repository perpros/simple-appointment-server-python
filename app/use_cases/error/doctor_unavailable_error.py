from typing import Optional


from .domain_error import DomainError


class DoctorUnavailableError(DomainError):
    """
    Raised when the requested doctor is unavailable for the appointment.
    """

    def __init__(self, doctor_id: int, reason: Optional[str] = None):
        message = f"Doctor with ID {doctor_id} is unavailable for the requested appointment."
        if reason:
            message += f" ({reason})"
        super().__init__(message)
