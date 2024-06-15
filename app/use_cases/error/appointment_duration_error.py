from .domain_error import DomainError


class AppointmentDurationError(DomainError):
    """
    Raised when the requested appointment duration is invalid.
    """

    def __init__(self, message: str):
        super().__init__(message)
