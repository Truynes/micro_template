import pika
# from src.becPy.Workflows.WorkFlow import WorkFlow
# import socket
# from src.becPy.MicroDriver.RabbitMQDriver import RabbitMQDriver


class Reciever():

	def __init__(self):
		self.rabbit_channel = None
		self.exchange = None
		pass

	def create_connection(self):
		pass

	def recieve_message(self, ch, method, properties, body):
		# print("Recieved a message:" + str(body))
		return ("Recieved a message: " + str(body))

	def start_consuming(self):
		return (self.recieve_message(None,None,None,"test"))
		# self.rabbit_channel.basic_consume(self.recieve_message,queue='testing',no_ack=True)


if __name__ == "__main__":
	rc = Reciever()
	rc.create_connection()
	result = rc.start_consuming()
	print(result)
