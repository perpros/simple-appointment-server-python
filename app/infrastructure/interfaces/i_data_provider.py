from abc import ABC, abstractmethod
from typing import List


from app.entities.appointment_entity import AppointmentEntity
from app.entities.time_range_entity import TimeRangeEntity


class IDataProvider(ABC):
    @abstractmethod
    def cancelAppointment(self, appointment_id: str) -> AppointmentEntity:
        raise NotImplementedError(
            "Subclasses must implement cancelAppointment()")

    @abstractmethod
    def manageAppointment(self, estimate_time: TimeRangeEntity) -> AppointmentEntity:
        raise NotImplementedError(
            "Subclasses must implement manageAppointment()")

    @abstractmethod
    def reserveAppointment(self, appointment_id: str, service_id: str, estimate_time: TimeRangeEntity) -> AppointmentEntity:
        raise NotImplementedError(
            "Subclasses must implement reserveAppointment()")

    @abstractmethod
    def reportByTime(self, time_range: TimeRangeEntity) -> List[AppointmentEntity]:
        raise NotImplementedError("Subclasses must implement reportByTime()")
