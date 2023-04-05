from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    phone_number: str
    address: str
