from typing import Optional
from .service_entity import ServiceEntity
from .time_range_entity import TimeRangeEntity
from .user_entity import UserEntity


class AppointmentEntity:
    user: UserEntity
    service: ServiceEntity
    estimate_time: Optional[TimeRangeEntity] = None