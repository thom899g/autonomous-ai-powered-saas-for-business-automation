import logging
from typing import Dict, Any
import pika

class MessagingHandler:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            self.channel = self.connection.channel()
            self.logger.info("Connected to RabbitMQ messaging broker.")
        except Exception as e:
            self.logger.error(f"Failed to connect to RabbitMQ: {str(e)}")
            raise
    
    def listen(self):
        try:
            self.channel.queue_declare('customer_service_queue')
            self.channel.basic_consume(queue='customer_service_queue', 
                                     on_message_callback=self.process_message)
            self.logger.info("Listening for messages. To exit press CTRL+C")
            self.channel.start_consuming()
        except Exception as e:
            self.logger.error(f"Failed to start message listener: {str(e)}")
            raise
    
    def process_message(self, ch, method, properties, body):
        try:
            # Process the incoming message
            message = body.decode('utf-8')
            response = AI_ENGINE.process_query(message)
            ch.basic_ack(method.delivery_tag)
            self.logger.info(f"Processed message: {message}")
        except Exception as e:
            self.logger.error(f"Failed to process message: {str(e)}")
            raise
    
    def send_message(self, queue_name: str, message_body: Dict[str, Any]):
        try:
            self.channel.queue_declare(queue_name)
            self.channel.basic_publish(exchange='', 
                                      routing_key=queue_name,
                                      body=str(message_body))
            self.logger.info(f"Message sent to {queue_name}")
        except Exception as e:
            self.logger.error(f"Failed to send message: {str(e)}")
            raise