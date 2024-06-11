from datetime import date
from typing import Optional


class TimeRangeEntity:
    def __init__(self, start_date: date, end_date: Optional[date] = None):
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> dict:
        return {
            "start_date": self.start_date.to_dict(),
            "end_date": self.end_date.to_dict(),
        }