import pika
import random, time

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

QUEUE_NAME = "letterbox"
PREFETCH_COUNT = 1

channel.queue_declare(queue=QUEUE_NAME)
channel.basic_qos(prefetch_count=PREFETCH_COUNT)


def on_message_received(channel, method, properties, body):
    print(f"Received: {body.decode()}")

    # Simulate processing time
    processing_time = random.uniform(1.0, 6.0) * int(body.decode())
    time.sleep(processing_time)
    channel.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Processed message in {processing_time:.2f} seconds")


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
