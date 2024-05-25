from ..provider.i_report_provider import IReportProvider


class IReportRepository:
    provider = IReportProvider

    def report_by_time(self, time_range):
        return self.provider.report_by_time(time_range)

