from abc import ABC, abstractmethod

from ..response.cancel_appointment_response_model import CancelAppointmentResponseModel
from ..response.manage_appointment_response_model import ManageAppointmentResponseModel
from ..response.reserve_appointment_response_model import ReserveAppointmentResponseModel
from ..provider.i_appointment_provider import IAppointmentProvider


class IAppointmentRepository(ABC):
    def __init__(self, provider):
        self.provider = provider

    @abstractmethod
    def reserve_appointment(self, appointment) -> ReserveAppointmentResponseModel:
        raise NotImplementedError("Subclasses must implement reserve_appointment()")

    @abstractmethod
    def cancel_appointment(self, appointment) -> CancelAppointmentResponseModel:
        raise NotImplementedError("Subclasses must implement cancel_appointment()")

    @abstractmethod
    def manage_appointment(self, appointment) -> ManageAppointmentResponseModel:
        raise NotImplementedError("Subclasses must implement manage_appointment()")