import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

FIRST_EXCHANGE = "first-exchange"
SECOND_EXCHANGE = "second-exchange"

channel.exchange_declare(FIRST_EXCHANGE, exchange_type=ExchangeType.direct)
channel.exchange_declare(SECOND_EXCHANGE, exchange_type=ExchangeType.fanout)
channel.exchange_bind(destination=SECOND_EXCHANGE, source=FIRST_EXCHANGE)


def send_message(message):
    channel.basic_publish(exchange=FIRST_EXCHANGE, routing_key="", body=message)
    print(f"Sent: {message}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        send_message(message)

    connection.close()
    print("Connection closed.")
