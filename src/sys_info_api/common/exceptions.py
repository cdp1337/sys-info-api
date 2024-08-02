class MetricNotAvailable(BaseException):
	"""
	General exception thrown when a metric is not available

	Usually used to encompass various things like FileNotFound or cmd exceptions.
	"""
	pass
