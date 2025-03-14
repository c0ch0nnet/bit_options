from dataclasses import dataclass


@dataclass
class Bet:
    id: int | None
    user_id: int
    instrument: str
    time_frame: str
    price: float
    direction: str
    create_data: str
