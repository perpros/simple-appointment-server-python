from app.entities.appointment_entity import AppointmentEntity


from .repository.i_appointment_repository import IAppointmentRepository
from .response.cancel_appointment_response_model import CancelAppointmentResponseModel


class CancelAppointmentModel:
    def __init__(self, appointment: AppointmentEntity, repository: IAppointmentRepository):
        self.appointment = appointment
        self.repository = repository

    def cancelAppointment(self) -> CancelAppointmentResponseModel:
        return self.repository.cancelAppointment(self.appointment)
