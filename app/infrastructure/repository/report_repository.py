from app.entities.time_range_entity import TimeRangeEntity
from app.use_cases.repository.i_report_repository import IReportRepository
from app.use_cases.response.incomplete_operation_response_model import IncompleteOperationResponseModel
from app.use_cases.response.report_by_time_response_model import ReportByTimeResponseModel


from ..provider.report_provider import ReportProvider


class ReportRepository (IReportRepository):
    provider: ReportProvider

    def reportByTime(self, time_range: TimeRangeEntity) -> ReportByTimeResponseModel:
        try:
            reported_appointments = self.provider.reportByTime(time_range)
            ReportByTimeResponseModel(
                success=True, message="", error_code="", data=reported_appointments)
        except:
            return IncompleteOperationResponseModel(message="", error_code="")
