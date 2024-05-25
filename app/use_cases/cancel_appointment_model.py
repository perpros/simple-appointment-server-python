from app.entities.appointment_entity import AppointmentEntity


from .repository.i_appointment_repository import IAppointmentRepository
from .response.cancel_appointment_response_model import CancelAppointmentResponseModel


class CancelAppointmentModel:
    appointment = AppointmentEntity
    repository = IAppointmentRepository

    def cancelAppointment(self) -> CancelAppointmentResponseModel:
        return self.repository.cancelAppointment(self.appointment)
