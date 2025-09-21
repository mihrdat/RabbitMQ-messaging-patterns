import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

QUEUE_NAME = "letterbox"

channel.exchange_declare("headers-exchange", exchange_type=ExchangeType.headers)

channel.queue_declare(queue=QUEUE_NAME)
bind_args = {
    "x-match": "any",
    "gender": "female",
    "role": "backend",
}
channel.queue_bind(QUEUE_NAME, "headers-exchange", arguments=bind_args)


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
