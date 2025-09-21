import pika
import random, time
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()


def on_message_received(channel, method, properties, body):
    print(f"First Consumer Received: {body.decode()}")

    # Simulate processing time
    processing_time = random.uniform(1.0, 6.0)
    time.sleep(processing_time)
    channel.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Processed message in {processing_time:.2f} seconds")


PREFETCH_COUNT = 1

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)
queue = channel.queue_declare(queue="", exclusive=True)

QUEUE_NAME = queue.method.queue

channel.queue_bind(exchange="pubsub", queue=QUEUE_NAME)

channel.basic_qos(prefetch_count=PREFETCH_COUNT)
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
