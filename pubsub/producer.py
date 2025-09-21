import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)


def send_message(message):
    channel.basic_publish(exchange="pubsub", routing_key="", body=message)
    print(f"Sent: {message}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        send_message(message)

    connection.close()
    print("Connection closed.")
