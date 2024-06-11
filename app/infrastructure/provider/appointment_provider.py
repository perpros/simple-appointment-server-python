# import pyodbc

from app.entities.appointment_entity import AppointmentEntity
from app.use_cases.provider.i_appointment_provider import IAppointmentProvider
from ..interfaces.i_data_provider import IDataProvider


class AppointmentProvider(IAppointmentProvider):
    def __init__(self, db: IDataProvider):
        self.db = db

    db = IDataProvider

    def cancelAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        return self.db.cancelAppointment(appointment.id)

    def manageAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        return self.db.manageAppointment(appointment.estimate_time)

    def reserveAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        return self.db.reserveAppointment(appointment.user.id, appointment.service.id, appointment.estimate_time)
