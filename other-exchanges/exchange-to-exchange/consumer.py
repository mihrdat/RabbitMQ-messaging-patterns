import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

QUEUE_NAME = "letterbox"
SECOND_EXCHANGE = "second-exchange"

channel.exchange_declare(SECOND_EXCHANGE, exchange_type=ExchangeType.fanout)

channel.queue_declare(queue=QUEUE_NAME)
channel.queue_bind(QUEUE_NAME, SECOND_EXCHANGE)


def on_message_received(channel, method, properties, body):
    print(f"Received: {body.decode()}")


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
