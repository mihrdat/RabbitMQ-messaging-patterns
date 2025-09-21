import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare("headers-exchange", exchange_type=ExchangeType.headers)


def send_message(message, headers):
    channel.basic_publish(
        exchange="headers-exchange",
        routing_key="",
        body=message,
        properties=pika.BasicProperties(headers=headers),
    )
    print(f"Sent: {message} with headers: {headers}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        # Get header values from user input
        gender = input("Enter gender value: ")
        role = input("Enter role value: ")

        headers = {
            "gender": gender,
            "role": role,
        }

        send_message(message, headers)

    connection.close()
    print("Connection closed.")
