from bs4 import BeautifulSoup
from datetime import date

from aioconverter.const import const
from aioconverter.http.http import request
from aioconverter.types.models import Model
from aioconverter.handlers.handlers import pairs


class Currency:
    def __init__(self, langue: str):
        """
        :param token: your api-key https://currate.ru/
        """
        self.langue = langue

    async def course(self, currency: str = 'usdrub') -> Model:
        response = await request(
            const.currency_api, {
            'q': f'курс+{await pairs(pairs=currency)}'
            }
        )
        return response
