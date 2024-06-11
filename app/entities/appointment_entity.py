from typing import Optional
from .service_entity import ServiceEntity
from .time_range_entity import TimeRangeEntity
from .user_entity import UserEntity


class AppointmentEntity:
    def __init__(self, id: int, user: UserEntity, service: ServiceEntity, estimate_time: Optional[TimeRangeEntity] = None):
        self.id = id
        self.user = user
        self.service = service
        self.estimate_time = estimate_time

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user": self.success.to_dict(),
            "service": self.message.to_dict(),
            "estimate_time": self.error_code.to_dict(),
        }