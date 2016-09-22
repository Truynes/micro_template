import pika
import os
import time
class RabbitMQDriver():
	
	def __init__(self):
		self.exchange = 'dsenyurt_test'
		# self.url = os.environ['AMQP_URL']

		self.url = "amqp://micro:password@localhost:5672/%2F"
		parameters = pika.URLParameters(self.url)

		# credentials = pika.PlainCredentials('micro', 'password')
		# parameters = pika.ConnectionParameters(credentials=credentials, host='localhost')

		self.connection = pika.BlockingConnection(parameters)
		self.rabbit_channel = self.connection.channel()
		self.rabbit_channel.exchange_declare(exchange=self.exchange, type='topic', durable=True)
		self.rabbit_channel.queue_declare(queue='testing', durable=True)

	# def create_connection(self,options):
	# 	credentials = pika.PlainCredentials('micro','bench629')
	# 	parameters = pika.ConnectionParameters(credentials=credentials, host='green.benchmarkeducation.ny')
	# 	rabbit_connection = pika.TwistedProtocolConnection(parameters)
	# 	self.rabbit_channel = rabbit_connection.channel()
	# 	self.exchange = 'dsenyurt_test' 
		

	def send_message(self, options):
		self.rabbit_channel.basic_publish(exchange=self.exchange, 
			routing_key='worker1', 
			body=options, 
			properties=pika.BasicProperties(delivery_mode=2))
		# pass


if __name__ == "__main__":
	rabbit = RabbitMQDriver()
	cnt = 0
	
	while True:
		rabbit.send_message("testing this queue" + str(cnt))
		cnt += 1
		print(cnt)
		time.sleep(7)
