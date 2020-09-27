async def pairs(pairs: str):

	identifiers = ("usdrub", "rubusd")

	if pairs.lower() not in identifiers:
		raise TypeError("Unknown pairs identifier!")
	else:
		return pairs.lower()