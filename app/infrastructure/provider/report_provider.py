from typing import List
from app.entities.appointment_entity import AppointmentEntity
from app.entities.time_range_entity import TimeRangeEntity
from app.use_cases.provider.i_report_provider import IReportProvider
from app.use_cases.response.report_by_time_response_model import ReportByTimeResponseModel


from ..interfaces.i_data_provider import IDataProvider


class ReportProvider(IReportProvider):
    def __init__(self, db: IDataProvider):
        self.db = db

    db = IDataProvider

    def reportByTime(self, time_range: TimeRangeEntity) -> List[AppointmentEntity]:
        return self.db.reportByTime(time_range=time_range)
