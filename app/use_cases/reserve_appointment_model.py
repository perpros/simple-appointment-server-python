from app.entities.appointment_entity import AppointmentEntity


from .repository.i_appointment_repository import IAppointmentRepository


class ReserveAppointmentModel:
    appointment = AppointmentEntity
    repository = IAppointmentRepository

    def reserve_appointment(self):
        return self.repository.reserve_appointment(self.appointment)


