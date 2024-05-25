from typing import Optional
from .location_entity import LocationEntity
from .time_range_entity import TimeRangeEntity


class ServiceEntity:
    name = str
    location = Optional[LocationEntity]
    estimate_time = Optional[TimeRangeEntity]