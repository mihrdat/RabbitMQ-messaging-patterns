# RabbitMQ Messaging Patterns

A comprehensive collection of RabbitMQ messaging patterns implemented in Python using the `pika` library. This repository demonstrates various message queuing patterns and exchange types commonly used in distributed systems.

## 🚀 Features

- **Multiple Messaging Patterns**: Work queues, pub/sub, routing, RPC, and more
- **Different Exchange Types**: Direct, fanout, topic, and headers exchanges
- **Real-world Examples**: Practical implementations with proper error handling
- **Easy to Run**: Simple Python scripts with clear documentation

## 📋 Prerequisites

- Python 3.6+
- RabbitMQ server running on localhost

## 📁 Project Structure

### 🏁 Competing Consumers (Work Queues)
**Directory: `competing/`**
- Distributes tasks among multiple workers
- Uses round-robin dispatching with acknowledgments
- Perfect for load balancing time-consuming tasks

### 📢 Publish/Subscribe
**Directory: `pubsub/`**
- Broadcasts messages to multiple consumers
- Uses fanout exchange
- Each consumer receives all messages

### 🎯 Routing (Direct Exchange)
**Directory: `routing/`**
- Routes messages based on routing keys
- Uses direct exchange for selective message delivery
- Includes examples for analytics, payments, and user services

### 🔄 Request/Reply (RPC)
**Directory: `request-reply/`**
- Implements synchronous request-response pattern
- Uses correlation IDs and reply queues
- Client-server communication example

### 🔀 Advanced Exchange Types
**Directory: `other-exchanges/`**

#### Headers Exchange
- Routes messages based on header attributes
- More flexible than routing keys
- Supports complex routing logic

#### Exchange-to-Exchange Binding
- Demonstrates exchange binding capabilities
- Chain multiple exchanges for complex routing

## 📚 Messaging Patterns Explained

| Pattern | Use Case | Exchange Type |
|---------|----------|---------------|
| **Work Queues** | Task distribution, load balancing | Default (direct) |
| **Pub/Sub** | Broadcasting, notifications | Fanout |
| **Routing** | Selective message delivery | Direct |
| **Topics** | Pattern-based routing | Topic |
| **RPC** | Synchronous communication | Direct |
| **Headers** | Attribute-based routing | Headers |

## 🔗 Resources

- [RabbitMQ Official Documentation](https://www.rabbitmq.com/documentation.html)
- [Pika Documentation](https://pika.readthedocs.io/)
- [RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html)

---

⭐ **Star this repository if you find it helpful!**
