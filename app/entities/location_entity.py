from typing import Optional


from .time_range_entity import TimeRangeEntity


class LocationEntity:
    def __init__(self, name: str, address: str, time_range: Optional[TimeRangeEntity] = None):
        self.name = name
        self.address = address
        self.time_range = time_range

    def to_dict(self) -> dict:
        return {
            "user": self.user.to_dict(),
            "service": self.service.to_dict(),
            "estimate_time": self.estimate_time.to_dict(),
        }