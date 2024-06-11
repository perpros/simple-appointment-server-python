from abc import ABC,abstractmethod

from ..response.report_by_time_response_model import ReportByTimeResponseModel
from ..provider.i_report_provider import IReportProvider


class IReportRepository(ABC):
    def __init__(self, provider: IReportProvider):
        self.provider = provider

    @abstractmethod
    def report_by_time(self, time_range) -> ReportByTimeResponseModel:
        raise NotImplementedError("Subclasses must implement report_by_time()")

