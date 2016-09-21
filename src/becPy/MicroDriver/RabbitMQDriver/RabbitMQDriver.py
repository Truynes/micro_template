import pika
import os
class RabbitMQDriver():
	
	def __init__(self):
		self.rabbit_channel = None
		self.exchange = 'dsenyurt_test'
		self.url = os.environ['AMQP_URL']

		

	def create_connection(self,options):
		credentials = pika.PlainCredentials('micro','bench629')
		parameters = pika.ConnectionParameters(credentials=credentials, host='green.benchmarkeducation.ny')
		rabbit_connection = pika.TwistedProtocolConnection(parameters)
		self.rabbit_channel = rabbit_connection.channel()
		self.exchange = 'dsenyurt_test' 
		exchange_type = 'topic'
		self.rabbit_channel.exchange_declare(exchange = self.exchange, type=exchange_type, durable=True)
		self.rabbit_channel.queue_declare(queue='testing',durable=True)

	def send_message(self,options):
		self.rabbit_channel.basic_publish(self.exchange,'testing',options)
		# pass

	def recieve_message(self,options):
		pass


if __name__	== "__main__":
	rabbit = RabbitMQDriver()
	rabbit.send_message("testing this queue")
