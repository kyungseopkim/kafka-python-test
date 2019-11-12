import kafka
import configparser

config = configparser.ConfigParser()

config.read('kafka.ini')
bootstrap = config['kafka']['bootstrap_hosts'].split(',')
print(bootstrap)

consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=bootstrap, security_protocol="SSL")
topics = consumer.topics()
for topic in topics:
    print(topic)
