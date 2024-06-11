from typing import Optional


class UserEntity:
    def __init__(self, id: int, user_name: str, name: str, email: Optional[str], phone: Optional[str]):
        self.id = id
        self.user_name = user_name
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }