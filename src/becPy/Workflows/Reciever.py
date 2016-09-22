import pika
import os
import time
from WorkFlow import WorkFlow

class Reciever(WorkFlow):

	def __init__(self):
		self.exchange = 'dsenyurt_test'
		# self.url = os.environ['AMQP_URL']
		# self.url = 'test'
		self.url = "amqp://micro:password@localhost:5672/%2F"
		parameters = pika.URLParameters(self.url)


		# credentials = pika.PlainCredentials('micro', 'password')
		# parameters = pika.ConnectionParameters(credentials=credentials, host='localhost')

		self.connection = pika.BlockingConnection(parameters)
		self.rabbit_channel = self.connection.channel()
		self.rabbit_channel.queue_declare(queue='testing', durable=True)
		self.rabbit_channel.queue_bind(exchange=self.exchange, queue='testing', routing_key='worker1')



		

	def create_connection(self):
		pass

	def recieve_message(self, ch, method, properties, body):
		print("Recieved a message:" + str(body))
		# print(self.url)
		# return ("Recieved a message: " + str(body))

	def start_consuming(self):
		# self.rabbit_channel.basic_consume(self.recieve_message, queue='testing', no_ack=True)
		self.rabbit_channel.basic_qos(prefetch_count=1)
		self.rabbit_channel.basic_consume(self.recieve_message, queue='testing', no_ack=True)
		self.rabbit_channel.start_consuming()
		# self.rabbit_channel.basic_consume(self.recieve_message,queue='testing',no_ack=True)


if __name__ == "__main__":
	rc = Reciever()
	# rc.create_connection()
	print("Before Consuming")
	rc.start_consuming()
	print("After Consuming")

	while True:
		print("result test")
		time.sleep(5)
		
	
	
