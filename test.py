import pika

# rabbitmq:
# host: 118.178.109.15
# port: 5672
# username: admin
# password: admin
# credentials = pika.PlainCredentials('admin', 'admin')
#
# params = pika.ConnectionParameters(host='172.16.157.242',
#                                    port=5672,
#                                     virtual_host='/',
#                                    credentials=credentials)

credentials = pika.PlainCredentials('admin', 'admin')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.16.157.242', port=5672, virtual_host='/', credentials=credentials))

#params = pika.URLParameters('amqp://admin:admin@172.16.157.242:5672/%2F')




channel = connection.channel()
result = channel.queue_declare(queue='python-test33')

channel.basic_publish(exchange='', routing_key='python-test33', body='hello word')

print(' [x] sent "hello world"')
connection.close()
