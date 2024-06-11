from app.entities.appointment_entity import AppointmentEntity


from .response.reserve_appointment_response_model import ReserveAppointmentResponseModel
from .repository.i_appointment_repository import IAppointmentRepository


class ReserveAppointmentModel:
    def __init__(self, appointment: AppointmentEntity, repository: IAppointmentRepository):
        self.appointment = appointment
        self.repository = repository

    def reserve_appointment(self) -> ReserveAppointmentResponseModel:
        return self.repository.reserve_appointment(self.appointment)
