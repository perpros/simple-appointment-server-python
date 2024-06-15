class DomainError:
    """
    Base class for all domain errors in the appointment system.
    """

    def __init__(self, message: str):
        self.message = message
