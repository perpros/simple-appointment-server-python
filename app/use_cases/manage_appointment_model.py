from app.entities.appointment_entity import AppointmentEntity


from .repository.i_appointment_repository import IAppointmentRepository


class ManageAppointmentModel:
    appointment = AppointmentEntity
    repository = IAppointmentRepository

    def manage_appointment(self):
        return self.repository.manage_appointment(self.appointment)

