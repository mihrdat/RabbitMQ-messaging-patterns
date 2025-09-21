import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()


def on_message_received(channel, method, properties, body):
    print(f"Payment Service Received: {body.decode()}")


channel.exchange_declare(exchange="routing-topic", exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue="", exclusive=True)

QUEUE_NAME = queue.method.queue

channel.queue_bind(exchange="routing-topic", queue=QUEUE_NAME, routing_key="user_only")

channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message_received)

if __name__ == "__main__":
    print("Waiting for messages. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()
        print("Connection closed.")
