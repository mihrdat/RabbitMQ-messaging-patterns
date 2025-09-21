import pika

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

QUEUE_NAME = "letterbox"
channel.queue_declare(queue=QUEUE_NAME)


def send_message(message):
    channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=message)
    print(f"Sent: {message}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        send_message(message)

    connection.close()
    print("Connection closed.")
