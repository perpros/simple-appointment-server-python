from .domain_error import DomainError


class AppointmentReminderError(DomainError):
    """
    Raised when attempting to send a reminder for an invalid appointment.
    """

    def __init__(self, message: str):
        super().__init__(message)
