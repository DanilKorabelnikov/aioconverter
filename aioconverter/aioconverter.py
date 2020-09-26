from typing import Optional

from aioconverter.const import const
from aioconverter.http.http import request
from aioconverter.types.models import Model
from aioconverter.handlers.handlers import currency_get


class Currency:
	def __init__(self, token: str):
		"""
		:param token: your api-key https://currate.ru/
		"""
		self._token = token

	async def converter(self, pairs: Optional[str] = 'USDRUB') -> Model:
		response = await request(
				const.currency_api, {
					'key': self._token,
					'get': 'rates',
					'pairs': currency_get(curr=pairs)
				}
		)
		return Model(**response)