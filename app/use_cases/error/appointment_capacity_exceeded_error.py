from typing import Optional


from .domain_error import DomainError


class AppointmentCapacityExceededError(DomainError):
    """
    Raised when the appointment slot is already full.
    """

    def __init__(self, doctor_id: Optional[int] = None, service_id: Optional[str] = None):
        message = "Appointment slot is already full."
        if doctor_id:
            message = f"Doctor with ID {doctor_id} is already booked for this time slot."
        elif service_id:
            message = f"Maximum appointments reached for service with ID {service_id} at this time."
        super().__init__(message)
