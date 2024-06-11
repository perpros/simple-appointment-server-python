from typing import List
from abc import ABC, abstractmethod

from app.entities.appointment_entity import AppointmentEntity
from app.entities.time_range_entity import TimeRangeEntity


class IReportProvider(ABC):
    @abstractmethod
    def reportByTime(self, time_range: TimeRangeEntity) -> List[AppointmentEntity]:
        raise NotImplementedError("Subclasses must implement reportByTime()")

