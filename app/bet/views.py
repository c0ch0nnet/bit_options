from aiohttp.web_exceptions import HTTPConflict, HTTPUnauthorized, HTTPBadRequest, HTTPNotFound
from aiohttp_apispec import request_schema, response_schema, querystring_schema
from aiohttp_session import get_session
#
from app.bet.schemes import (BetSchema,
                             BetRequestSchema,
                             BetResponceSchema,
                              # QuestionSchema,
                              # QuestionResponceSchema,
                              # ThemeResponceSchema,
                              # QuestionIdSchema
                             )
from app.web.app import View
# from app.web.app import View
from app.web.utils import json_response


async def index(request):
   return json_response()


class BetAddView(View):
    @request_schema(BetRequestSchema)
    @response_schema(BetResponceSchema)
    async def post(self):
        # session = await get_session(self.request)
        # if not session:
        #     raise HTTPUnauthorized

        data = await self.request.json()
        # theme_exists = await self.store.quizzes.get_theme_by_title(title=title)
        # if theme_exists:
        #     raise HTTPConflict
        bet = await self.store.bets.create_bet(data)
        return json_response(data=BetSchema().dump(bet))


# # TODO: добавить проверку авторизации для этого View
# class ThemeAddView(View):
#     @request_schema(ThemeIdSchema)
#     @response_schema(ThemeResponceSchema)
#     # TODO: добавить валидацию с помощью aiohttp-apispec и marshmallow-схем
#     async def post(self):
#         session = await get_session(self.request)
#         if not session:
#             raise HTTPUnauthorized
#         # title = (await self.request.json())[
#         #     "title"
#         # ]  # TODO: заменить на self.data["title"] после внедрения валидации
#         title = self.data["title"]
#         # TODO: проверять, что не существует темы с таким же именем, отдавать 409 если существует
#         theme_exists = await self.store.quizzes.get_theme_by_title(title=title)
#         if theme_exists:
#             raise HTTPConflict
#         theme = await self.store.quizzes.create_theme(title=title)
#         return json_response(data=ThemeSchema().dump(theme))
