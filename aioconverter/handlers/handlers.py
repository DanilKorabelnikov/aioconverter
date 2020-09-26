async def currency(curr: str):

	currency = ("EURRUB", "RUBEUR", "USDRUB", "RUBUSD", "BTCRUB", "RUBBTC", "BTCEUR", "EURBTC", "USDBTC","BTCUSD")

	if curr.lower() not in currency:
		raise TypeError("Unknown currency index!")
	else:
		return curr.lower()