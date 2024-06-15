from .domain_error import DomainError


class InvalidPatientCredentialsError(DomainError):
    """
    Raised when a patient provides invalid credentials.
    """

    def __init__(self):
        super().__init__("Invalid patient ID or password.")
