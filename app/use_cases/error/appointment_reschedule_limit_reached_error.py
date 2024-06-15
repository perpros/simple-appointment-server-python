from .domain_error import DomainError


class AppointmentRescheduleLimitReachedError(DomainError):
    """
    Raised when the maximum allowed reschedules for an appointment is reached.
    """

    def __init__(self):
        super().__init__("Appointment cannot be rescheduled any further.")
