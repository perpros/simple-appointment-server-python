from .domain_error import DomainError


class AppointmentDoubleBookingError(DomainError):
    """
    Raised when an appointment slot is accidentally double-booked.
    """

    def __init__(self, appointment_id: int):
        super().__init__(f"Appointment with ID {appointment_id} is already booked.")
