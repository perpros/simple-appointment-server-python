from app.entities.appointment_entity import AppointmentEntity


from .response.manage_appointment_response_model import ManageAppointmentResponseModel
from .repository.i_appointment_repository import IAppointmentRepository


class ManageAppointmentModel:
    def __init__(self, appointment: AppointmentEntity, repository: IAppointmentRepository):
        self.appointment = appointment
        self.repository = repository

    def manage_appointment(self) -> ManageAppointmentResponseModel:
        return self.repository.manage_appointment(self.appointment)
