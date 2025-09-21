import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange="routing-direct", exchange_type=ExchangeType.direct)


def send_message(message):
    channel.basic_publish(
        exchange="routing-direct", routing_key="analytic_only", body=message
    )
    print(f"Sent: {message}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        send_message(message)

    connection.close()
    print("Connection closed.")
