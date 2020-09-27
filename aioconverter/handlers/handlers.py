async def pairs(pairs: str):
	"""
	:param language: accepts language identifier (ru, en)
	:return: True if lang in identifiers. False if lang not in identifiers
	"""

	identifiers = ("usdrub", "rubusd")

	if pairs.lower() not in identifiers:
		raise TypeError("Unknown pairs identifier!")
	else:
		return pairs.lower()