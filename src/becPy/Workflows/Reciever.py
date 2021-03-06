#!/usr/bin/python
#!/usr/bin/python
from WorkFlow import WorkFlow

class Reciever(WorkFlow):

	def __init__(self):
		"""
		queue_name, routing_key will be dynamically mapped via class name where values stored in a json workflow file
		"""
		queue_name = 'reciever'
		routing_key = 'reciever'
		WorkFlow.__init__(self)
		self.declare_queue(self.do_work, queue_name, routing_key)

	def do_work(self, ch, method, properties, body):
		"""
		Driver function to perform necessary tasks for that workflow
		"""
		print("Recieved a message:" + str(body))


if __name__ == "__main__":
	print("Initializing Reciever")
	rc = Reciever()
