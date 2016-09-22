#!/usr/bin/python
import pika
import time

class RabbitMQDriver(object):
	
	def __init__(self):
		self.exchange = 'dsenyurt_test'
		# self.url = "amqp://micro:password@localhost:5672/%2F"
		self.url = "amqp://micro:bench629@green.benchmarkeducation.ny:5672/%2F"
		parameters = pika.URLParameters(self.url)
		self.connection = pika.BlockingConnection(parameters)
		self.rabbit_channel = self.connection.channel()

		"""exchange,connection declerations will occur in master micro controller class"""
		# self.rabbit_channel.exchange_declare(exchange=self.exchange, type='topic', durable=True)

		

	def send_message(self, payload, routing_key):
		self.rabbit_channel.basic_publish(exchange=self.exchange, 
			routing_key=routing_key, 
			body=payload, 
			properties=pika.BasicProperties(delivery_mode=2))


if __name__ == "__main__":
	rabbit = RabbitMQDriver()
	cnt = 0
	work_flows = ['reciever','registeration', 'publish', 'ingestion']
	while True:
		print(cnt)
		for workflow in work_flows:
			rabbit.send_message("Testing Workflow: " +workflow+ " Message Count: "+ str(cnt), workflow)
		cnt += 1
		time.sleep(7)
