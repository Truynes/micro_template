import pika
import os
import time

class Reciever():

	def __init__(self):
		self.url = os.environ['AMQP_URL']
		self.exchange = 'dsenyurt_test'
		self.url = os.environ['AMQP_URL']
		parameters = pika.URLParameters(self.url)
		self.connection = pika.BlockingConnection(parameters)
		self.rabbit_channel = self.connection.channel()
		self.rabbit_channel.queue_declare(queue='testing',durable=True)
		

	def create_connection(self):
		pass

	def recieve_message(self, ch, method, properties, body):
		# print("Recieved a message:" + str(body))
		print(self.url)
		return ("Recieved a message: " + str(body))

	def start_consuming(self):
		self.rabbit_channel.basic_consume(self.recieve_message, queue='testing', no_ack=True)
		self.rabbit_channel.start_consuming()
		# self.rabbit_channel.basic_consume(self.recieve_message,queue='testing',no_ack=True)


if __name__ == "__main__":
	rc = Reciever()
	rc.create_connection()

	while True:
		result = rc.start_consuming()
		print("result test" + str(result))
		time.sleep(5)
		pass
	
	
