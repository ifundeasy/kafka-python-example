import json
from kafka import KafkaProducer

topic = 'omedPage'
group_id = 'my-group'
bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094']
text = open('message.json', 'r').read()
message = json.loads(text)

def success(rec): 
  print('> message delivered to %s with partition %d and offset %d' % (rec.topic, rec.partition, rec.offset))

def error(exception):
  # handle exception
  print('> message unsent with exception:', exception)


producer = KafkaProducer(
  acks=1, 
  # acks='all',
  retries=5,
  compression_type='lz4',
  request_timeout_ms=60000,
  bootstrap_servers=bootstrap_servers,
  value_serializer=lambda m: json.dumps(m).encode('ascii')
)

partitions = list(producer.partitions_for(topic))
sendingCount = len(partitions) * 1000

for i in range(sendingCount):
  partition = i % len(partitions)
  message['partition'] = partition
  
  print('> send message to %s with partition %d. %s' % (topic, partition, message['data']['url']))
  
  # produce asynchronously with callbacks
  producer.send(
    topic=topic, 
    value=message,
    partition=partition,
    key=str.encode(message['id'])
  ).add_callback(success).add_errback(error)

# block until all async messages are sent
producer.flush() 