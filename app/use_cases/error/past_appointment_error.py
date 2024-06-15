from .domain_error import DomainError


class PastAppointmentError(DomainError):
    """
    Raised when the requested appointment time is in the past.
    """

    def __init__(self):
        super().__init__("Appointment cannot be scheduled for a time in the past.")
