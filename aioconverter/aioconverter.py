from aioconverter.const import const
from aioconverter.http.http import request
import datetime
from aioconverter.types.models import Model


class Currency:
	def __init__(self, token: str):
		"""
		:param token: your api-key https://currate.ru/
		"""
		self._token = token

	async def converter(self, pairs: str = 'USDRUB') -> Model:
		response = await request(
				const.currency_api, {
					'key': self._token,
					'get': 'rates',
					'pairs': pairs,
					'date': datetime.datetime.strftime('%Y-%m-%d')
				}
		)
		return Model(**response)