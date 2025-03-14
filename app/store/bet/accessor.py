from app.base.base_accessor import BaseAccessor
from app.bet.models import Bet


class BetAccessor(BaseAccessor):
    async def create_bet(self, in_data) -> Bet:
        data = {'id': self.app.database.next_bet_id}
        data.update(in_data)
        print(data)
        bet = Bet(**data)
        self.app.database.bets.append(bet)
        return bet

    # async def get_theme_by_title(self, title: str) -> Theme | None:
    #     for theme in self.app.database.themes:
    #         if theme.title == title:
    #             return theme