import kafka
import configparser

config = configparser.ConfigParser()

config.read('kafka.ini')
bootstrap = config['kafka']['bootstrap_hosts']
consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=[bootstrap])
topics = consumer.topics()
for topic in topics:
    print(topic)
