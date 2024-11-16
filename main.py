import pika
import asyncio


async def main():
    connection_params = pika.ConnectionParameters(
        host='0.0.0.0',
        port=5672,          
        virtual_host='/',   
        credentials=pika.PlainCredentials(
        username='guest',  
        password='guest'   
        )
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    queue_name = 'hello'

    channel.queue_declare(queue=queue_name)

    message = 'Hello, RabbitMQ!'

    for i in range(0, 10):
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    connection.close()


asyncio.run(main())