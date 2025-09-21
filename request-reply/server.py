import pika
import random, time

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

QUEUE_NAME = "request_queue"
channel.queue_declare(queue=QUEUE_NAME)


def on_request_message_received(channel, method, properties, body):
    print(f"Request Received Message: {body.decode()}")
    print(f"correlation_id: {properties.correlation_id}")

    channel.basic_publish(
        exchange="",
        routing_key=properties.reply_to,
        body=f"This is reply to this message -> {body.decode()}",
    )


channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=on_request_message_received, auto_ack=True
)

if __name__ == "__main__":
    print("Waiting for messages. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()
        print("Connection closed.")
