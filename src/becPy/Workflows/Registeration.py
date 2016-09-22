#!/usr/bin/python
from WorkFlow import WorkFlow

class Registeration(WorkFlow):
	result = None
	def __init__(self):
		"""
		queue_name, routing_key will be dynamically mapped via class name where values stored in a json workflow file
		"""
		print(self.__class__.__name__)
		queue_name = 'registeration'
		routing_key = 'registeration'
		WorkFlow.__init__(self)
		self.declare_queue(self.do_work, queue_name, routing_key)

	def do_work(self, ch, method, properties, body):
		"""
		Driver function to perform necessary tasks for that workflow
		"""
		print("Registeration Workflow Msg: " + str(body))

		self.result = body


if __name__ == "__main__":
	print("Initializing Registeration")
	rc = Registeration()
	print(rc.result)
