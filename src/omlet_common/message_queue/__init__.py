from typing import Callable, Union

import pika


class RabbitQueue:
    def __init__(self, host: str = '127.0.0.1', port: int = 5672,
                 vhost: str = '/', username: str = 'guest', password: str = 'guest'):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, virtual_host=vhost,
                                      credentials=pika.PlainCredentials(username, password))
        )
        channel = self._connection.channel()
        # channel.exchange_declare(exchange='test_exchange', exchange_type='direct', passive=False, durable=True, auto_delete=False)
        # channel.queue_declare(queue='standard', auto_delete=True)
        # channel.queue_bind(queue='standard', exchange='test_exchange', routing_key='standard_key')
        channel.basic_qos(prefetch_count=1)
        self._channel = channel

    def publish(self, message: Union[bytes, str], exchange: str = '', routing_key: str = ''):
        if type(message) is str:
            message = message.encode('utf-8')
        self._channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message,
                                    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    def subscribe(self, queue: str,
                  on_message_callback: Callable[[pika.adapters.blocking_connection.BlockingChannel, str, str, bytes], None]):
        self._channel.queue_declare(queue, durable=True, auto_delete=True)
        self._channel.basic_consume(queue, on_message_callback=on_message_callback)
        try:
            self._channel.start_consuming()
        except (KeyboardInterrupt, Exception):
            self._channel.stop_consuming()
        self.close()

    def close(self):
        if self._connection.is_open:
            self._connection.close()
