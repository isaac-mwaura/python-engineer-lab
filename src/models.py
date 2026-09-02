from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """
    Represents a user entity in the system.
    """
    id: int
    name: str
    email: str
    age: int
    city: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert User instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "city": self.city,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create a User instance from a dictionary safely."""
        return cls(
            id=int(data.get("id", 0)),
            name=str(data.get("name", "Unknown")),
            email=str(data.get("email", "")),
            age=int(data.get("age", 0)),
            city=str(data.get("city")) if data.get("city") else None,
        )