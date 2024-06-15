from .domain_error import DomainError


class AppointmentServiceMismatchError(DomainError):
    """
    Raised when the requested service is incompatible with the appointment details.
    """

    def __init__(self, message: str):
        super().__init__(message)
