class AppointmentConflictError:
    """
    Raised when there's a conflict with the requested appointment time.
    """

    def __init__(self, patient_id):
        super.__init__(
            f"Patient with ID {patient_id} already has an appointment at the requested time.")
