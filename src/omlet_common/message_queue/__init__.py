from typing import Callable, Union

import pika


class RabbitQueue:
    """`RabbitMQ`를 사용하기 위한 클래스"""
    def __init__(self, host: str = '127.0.0.1', port: int = 5672,
                 vhost: str = '/', username: str = 'guest', password: str = 'guest'):
        """
        Args:
            :param str host: 메시지 큐 서버의 주소
            :param int port: 메시지 큐 서버의 포트 번호
            :param str vhost: `Virtual Host`의 이름 (https://www.rabbitmq.com/vhosts.html)
            :param str username: 메시지 큐 서버의 사용자 이름
            :param str password: 메시지 큐 서버의 사용자 비밀번호
        """
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
        """메시지 큐에 메시지를 발송합니다.

        Args:
            :param Union[bytes, str] message: 메시지 큐에 전달할 메시지 내용
            :param str exchange: ... (https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
            :param str routing_key: ... (https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
        """
        if type(message) is str:
            message = message.encode('utf-8')
        self._channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message,
                                    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    def subscribe(self, queue: str,
                  on_message_callback: Callable[[pika.adapters.blocking_connection.BlockingChannel, str, str, bytes], None]):
        """메시지를 수신하기 위한 큐를 생성하고 콜백 함수를 등록합니다.

        Args:
            :param str queue: 수신할 큐 이름
            :paral Callable on_message_callback: 메시지가 도착했을 때 수행할 동작이 정의된 콜백 함수
        """
        self._channel.queue_declare(queue, durable=True, auto_delete=True)
        self._channel.basic_consume(queue, on_message_callback=on_message_callback)
        try:
            self._channel.start_consuming()
        except (KeyboardInterrupt, Exception):
            self._channel.stop_consuming()
        self.close()

    def close(self):
        """`Connection`을 종료합니다."""
        if self._connection.is_open:
            self._connection.close()
