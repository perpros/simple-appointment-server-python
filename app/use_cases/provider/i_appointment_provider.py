from abc import ABC, abstractmethod

from app.entities.appointment_entity import AppointmentEntity


class IAppointmentProvider(ABC):
    @abstractmethod
    def reserveAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        raise NotImplementedError("Subclasses must implement reserveAppointment()")

    @abstractmethod
    def cancelAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        raise NotImplementedError("Subclasses must implement cancelAppointment()")
    
    @abstractmethod
    def manageAppointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        raise NotImplementedError("Subclasses must implement manageAppointment()")

