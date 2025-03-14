from aiohttp.web_app import Application


def setup_routes(app: Application):
    pass
    from app.bet.routes import setup_routes as bet_setup_routes
    # from app.admin.routes import setup_routes as admin_setup_routes
    # from app.bet.routes import setup_routes as quiz_setup_routes

    bet_setup_routes(app)
    # admin_setup_routes(app)
    # quiz_setup_routes(app)
