import pika
import uuid
import threading

# Separate connections for thread safety
send_connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
send_channel = send_connection.channel()

receive_connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
receive_channel = receive_connection.channel()


def on_reply_message_received(channel, method, properties, body):
    print(f"Reply Received Message: {body.decode()}")


# Set up reply queue on receive channel
reply_queue = receive_channel.queue_declare(queue="", exclusive=True)
REPLY_QUEUE_NAME = reply_queue.method.queue
receive_channel.basic_consume(
    queue=REPLY_QUEUE_NAME, auto_ack=True, on_message_callback=on_reply_message_received
)

REQUEST_QUEUE_NAME = "request_queue"
send_channel.queue_declare(queue=REQUEST_QUEUE_NAME)


# Start consuming in a separate thread
def start_consuming():
    receive_channel.start_consuming()


consumer_thread = threading.Thread(target=start_consuming, daemon=True)
consumer_thread.start()


def send_message(message):
    send_channel.basic_publish(
        exchange="",
        routing_key=REQUEST_QUEUE_NAME,
        properties=pika.BasicProperties(
            reply_to=REPLY_QUEUE_NAME, correlation_id=str(uuid.uuid4())
        ),
        body=message,
    )
    print(f"Sent: {message}")


if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")

        if message.lower() == "exit":
            break

        send_message(message)

    receive_channel.stop_consuming()
    receive_connection.close()
    send_connection.close()
    print("Connection closed.")
