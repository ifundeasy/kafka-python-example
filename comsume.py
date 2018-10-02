import json
from kafka import KafkaConsumer

topic = 'omedPage'
group_id = 'my-group'
bootstrap_servers = ['localhost:9092', 'localhost:9093', 'localhost:9094']

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
	auto_offset_reset='earliest',
	enable_auto_commit=False,
	# consumer_timeout_ms=1000,
	value_deserializer=lambda m: json.loads(m.decode('ascii')),
	group_id=group_id, 
	bootstrap_servers=bootstrap_servers
)

consumer.subscribe(topic)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print (
      "> consuming message from %s partition=%d with offset=%d and key=%s" % (
      	message.topic, message.partition, message.offset, message.key
      )
    )
    print('', message.value)