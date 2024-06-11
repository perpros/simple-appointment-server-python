from app.entities.time_range_entity import TimeRangeEntity


from .response.report_by_time_response_model import ReportByTimeResponseModel
from .provider.i_report_provider import IReportProvider


class ReportByTimeModel:
    def __init__(self, provider: IReportProvider, time_range: TimeRangeEntity):
        self.provider = provider
        self.time_range = time_range

    def report_by_time(self, time_range) -> ReportByTimeResponseModel:
        return self.provider.report_by_time(time_range)
