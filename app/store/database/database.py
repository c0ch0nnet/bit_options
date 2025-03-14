from dataclasses import dataclass, field

from app.bet.models import Bet


@dataclass
class Database:
    # TODO: добавить поля admins и questions
    bets: list[Bet] = field(default_factory=list)

    @property
    def next_bet_id(self) -> int:
        return len(self.bets) + 1
