from app.entities.appointment_entity import AppointmentEntity
from app.use_cases.repository.i_appointment_repository import IAppointmentRepository
from app.use_cases.response.cancel_appointment_response_model import CancelAppointmentResponseModel
from app.use_cases.response.incomplete_operation_response_model import IncompleteOperationResponseModel
from app.use_cases.response.manage_appointment_response_model import ManageAppointmentResponseModel
from app.use_cases.response.reserve_appointment_response_model import ReserveAppointmentResponseModel
from ..provider.appointment_provider import AppointmentProvider


class AppointmentRepository (IAppointmentRepository):
    provider: AppointmentProvider

    async def cancelAppointment(self, appointment: AppointmentEntity) -> CancelAppointmentResponseModel:
        try:
            canceled_appointment: AppointmentEntity = await self.provider.cancelAppointment(appointment)
            return CancelAppointmentResponseModel(success=True, message="", error_code="", appointment=canceled_appointment)
        except:
            return IncompleteOperationResponseModel(message="", error_code="")

    async def manageAppointment(self, appointment: AppointmentEntity) -> ManageAppointmentResponseModel:
        try:
            managed_appointment: AppointmentEntity = await self.provider.manageAppointment(appointment)
            return ManageAppointmentResponseModel(success=True, message="", error_code="", appointment=managed_appointment)
        except:
            return IncompleteOperationResponseModel(message="", error_code="")

    def reserveAppointment(self, appointment: AppointmentEntity) -> ReserveAppointmentResponseModel:
        try:
            reserved_appointment: AppointmentEntity = self.provider.reserveAppointment(
                appointment)
            return ReserveAppointmentResponseModel(success=True, message="", error_code="", appointment=reserved_appointment)
        except:
            return IncompleteOperationResponseModel(message="", error_code="")
