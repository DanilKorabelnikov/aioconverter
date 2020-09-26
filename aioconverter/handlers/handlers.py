async def currency(curr: str):

	currency = ("EURRUB", "RUBEUR", "USDRUB", "RUBUSD", "BTCRUB", "RUBBTC", "BTCEUR", "EURBTC", "USDBTC", "BTCUSD")

	for i in currency:
		if i.lower() not in currency:
			raise TypeError("Unknown currency index!")
		else:
			return i.lower()