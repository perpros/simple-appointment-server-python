from typing import Optional
from .location_entity import LocationEntity
from .time_range_entity import TimeRangeEntity


class ServiceEntity:
    def __init__(self, id: int, name: str, location: Optional[LocationEntity] = None, estimate_time: Optional[TimeRangeEntity] = None):
        self.id = id
        self.name = name
        self.location = location
        self.estimate_time = estimate_time

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location.to_dict(),
            "estimate_time": self.estimate_time.to_dict(),
        }
