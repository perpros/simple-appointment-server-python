from app.entities.time_range_entity import TimeRangeEntity


from ..response.report_by_time_response_model import ReportByTimeResponseModel


class IReportProvider():
    def reportByTime(self, time_range: TimeRangeEntity) -> ReportByTimeResponseModel:
        pass

