#!/usr/bin/python
from WorkFlow import WorkFlow

class Ingestion(WorkFlow):

	def __init__(self):
		"""
		queue_name, routing_key will be dynamically mapped via class name where values stored in a json workflow file
		"""
		print(self.__class__.__name__)
		queue_name = 'ingestion'
		routing_key = 'ingestion'
		WorkFlow.__init__(self)
		self.declare_queue(self.do_work, queue_name, routing_key)

	def do_work(self, ch, method, properties, body):
		"""
		Driver function to perform necessary tasks for that workflow
		"""
		print("Ingest Workflow Msg: " + str(body))


if __name__ == "__main__":
	print("Initializing Ingestion")
	rc = Ingestion()
