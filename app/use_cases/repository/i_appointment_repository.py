from ..provider.i_appointment_provider import IAppointmentProvider


class IAppointmentRepository:
    provider = IAppointmentProvider

    def reserve_appointment(self, appointment):
        return self.provider.reserve_appointment(appointment)

    def cancel_appointment(self, appointment):
        return self.provider.cancel_appointment(appointment)

    def manage_appointment(self, appointment):
        return self.provider.manage_appointment(appointment)
