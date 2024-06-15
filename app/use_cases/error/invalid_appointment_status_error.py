from .domain_error import DomainError


class InvalidAppointmentStatusError(DomainError):
    """
    Raised when performing an action on an appointment in an invalid state.
    """

    def __init__(self, message: str):
        super().__init__(message)
