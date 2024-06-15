from .domain_error import DomainError


class AppointmentCancellationDeadlineError(DomainError):
    """
    Raised when attempting to cancel an appointment after the deadline.
    """

    def __init__(self):
        super().__init__("Appointment cannot be cancelled after the deadline.")
