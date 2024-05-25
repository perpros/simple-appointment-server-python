from app.entities.appointment_entity import AppointmentEntity


from ..response.manage_appointment_response_model import ManageAppointmentResponseModel
from ..response.cancel_appointment_response_model import CancelAppointmentResponseModel
from ..response.reserve_appointment_response_model import ReserveAppointmentResponseModel


class IAppointmentProvider:
    def reserveAppointment(self, appointment: AppointmentEntity) -> ReserveAppointmentResponseModel:
        pass

    def cancelAppointment(self, appointment: AppointmentEntity) -> CancelAppointmentResponseModel:
        pass

    def manageAppointment(self, appointment: AppointmentEntity) -> ManageAppointmentResponseModel:
        pass

