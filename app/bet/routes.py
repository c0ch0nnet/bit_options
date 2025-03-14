import typing

from app.bet.views import (
    BetAddView,
    index
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    app.router.add_view("/add_bet", BetAddView)
    app.router.add_get("/", index)
