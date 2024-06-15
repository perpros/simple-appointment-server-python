from .domain_error import DomainError


class InvalidAppointmentTimeError(DomainError):
    """
    Raised when the appointment time is invalid.
    """

    def __init__(self):
        super().__init__("Appointment time is outside allowed hours.")
