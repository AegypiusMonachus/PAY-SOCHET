class Config:
	SECRET_KEY = '1E7AB4FFF67A59726E6681C2E87F68F0'

	@staticmethod
	def init_app(app):
		pass


class DebuggingConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True


class ProductionConfig(Config):
	DEBUG = False
	TESTING = False


config = {
	'DEBUGGING': DebuggingConfig,
	'TESTING': TestingConfig,
	'PRODUCTION': ProductionConfig,
}
