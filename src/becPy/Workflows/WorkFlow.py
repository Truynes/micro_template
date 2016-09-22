#!/usr/bin/python
import pika

class WorkFlow(object):

	def __init__(self):
		"""
		url, exchange will be stored in external configuration file
		"""
		self.exchange = 'dsenyurt_test'
		url = "amqp://micro:bench629@green.benchmarkeducation.ny:5672/%2F"
		self.connect_rabbit(url)

	def connect_rabbit(self, url):
		print('Connecting to RabbitMQ')
		parameters = pika.URLParameters(url)
		self.connection = pika.BlockingConnection(parameters)
		self.rabbit_channel = self.connection.channel()
		

	def declare_queue(self, callback_function, queue_name, binding_key):
		self.rabbit_channel.queue_declare(queue=queue_name, durable=True)
		self.rabbit_channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=binding_key)
		self.rabbit_channel.basic_qos(prefetch_count=1)
		self.rabbit_channel.basic_consume(callback_function, queue=queue_name, no_ack=True)
		self.rabbit_channel.start_consuming()

	def send_message(self, payload, routing_key):
		self.rabbit_channel.basic_publish(exchange=self.exchange, 
			routing_key=routing_key, 
			body=payload, 
			properties=pika.BasicProperties(delivery_mode=2))

	def do_work(self):
		pass
		