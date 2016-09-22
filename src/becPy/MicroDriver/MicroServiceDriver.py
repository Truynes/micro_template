import abc

class MicroServiceDriver(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self):
		pass
	
	@abc.abstractmethod
	def create_connection(self, options = {}):
		pass

	@abc.abstractmethod
	def send_message(self, options = {}):
		pass

	@abc.abstractmethod
	def recieve_message(self, options = {}):
		pass





