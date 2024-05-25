from app.entities.time_range_entity import TimeRangeEntity


from .provider.i_report_provider import IReportProvider


class ReportByTimeModel:
    provider = IReportProvider
    time_range = TimeRangeEntity

    def report_by_time(self, time_range):
        return self.provider.report_by_time(time_range)


