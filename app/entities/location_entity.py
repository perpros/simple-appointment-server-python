from typing import Optional


from .time_range_entity import TimeRangeEntity


class LocationEntity:
    name = str
    address = str
    time_range = Optional[TimeRangeEntity] = None