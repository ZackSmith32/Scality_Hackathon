from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotTest as h
# from pyspark import SparkConf, SparkContext
import messageProcesser as mp

f = open('logs.txt', 'w')
consumer = KafkaConsumer('test3')
keys = {}
elapsed_time = []
try:
	for msg in consumer:
		try:
			m = json.loads(msg.value)
			print(m)
		except ValueError, e:
			print("value error")
			print(e.message)

		try:
			f.write(m['message'] + '\n')
		except Exception, e:
			print(e.message)

		for k in m:
			if k in keys:
				keys[k] += 1
			else:
				keys[k] = 1
			if k == 'elapsed_ms':
				print(m[k])
				elapsed_time.append(m[k])
except:
	print("Keyboard Interupt")
	print("\n\n\n\n")

mp.mp()
print('\n\n')
raw_input()

print (elapsed_time)
print('\n\n')
raw_input()

print (keys)
print('\n\n')
raw_input()
h.hist(elapsed_time)




'''
	{u'clientPort': 52966, 
	u'name': u'S3', 
	u'level': u'info', 
	u'pid': 8349, 
	u'hostname': u'off-the-rip.local', 
	u'httpURL': u'/zackbuk/Steal%20Big%2C%20Steal%20Little%20%281995%29', 
	u'httpMethod': u'PUT', 
	u'req_id': u'3c14f8a9b74aaa03fa96', 
	u'time': 1503041244877, 
	u'clientIP': u'::1', 
	u'message': u'received request'}

	{u'clientPort': 52966, 
	u'name': u'S3', 
	u'level': u'info', 
	u'pid': 8349, 
	u'hostname': u'off-the-rip.local', 
	u'httpURL': u'/zackbuk/Anne%20Frank%20Remembered%20%281995%29', 
	u'httpMethod': u'PUT', 
	u'req_id': u'edbf435b644da863d14b', 
	u'time': 1503041244757, 
	u'clientIP': u'::1', 
	u'message': u'received request'}

	{u'bytesReceived': 5, 
	u'clientPort': 52966, 
	u'hostname': u'off-the-rip.local', 
	u'name': u'S3', 
	u'elapsed_ms': 43.263151, 
	u'message': u'responded to request', 
	u'pid': 8349, 
	u'bodyLength': 5, 
	u'level': u'info', 
	u'httpURL': u'/zackbuk/Young%20Poisoner%27s%20Handbook%2C%20The%20%281995%29', 
	u'httpCode': 200, 
	u'httpMethod': u'PUT', 
	u'objectKey': u"Young Poisoner's Handbook, The (1995)", 
	u'bucketName': u'zackbuk', 
	u'req_id': u'9a6e959dbd48a4a520ed', 
	u'time': 1503041244837, 
	u'clientIP': u'::1', 
	u'contentLength': 5}

	{u'bytesReceived': 5, 
	u'clientPort': 52966, 
	u'hostname': u'off-the-rip.local', 
	u'name': u'S3', 
	u'elapsed_ms': 20.269738, 
	u'message': u'responded to request', 
	u'pid': 8349, 
	u'bodyLength': 5, 
	u'level': 
	u'info', 
	u'httpURL': 
	u'/zackbuk/Race%20the%20Sun%20%281996%29', 
	u'httpCode': 200, 
	u'httpMethod': u'PUT', 
	u'objectKey': u'Race the Sun (1996)', 
	u'bucketName': u'zackbuk', 
	u'req_id': u'c82596af2048b3b55f11', 
	u'time': 1503041244927, 
	u'clientIP': u'::1', 
	u'contentLength': 5}

{u'bytesReceived': 320, 
u'clientPort': 642, 
u'name': 642, 
u'level': 642, 
u'pid': 642, 
u'bodyLength': 320, 
u'hostname': 642, 
u'httpURL': 642, 
u'httpCode': 321, 
u'contentLength': 320, 
u'httpMethod': 642, 
u'elapsed_ms': 321, 
u'objectKey': 320, 
u'bytesSent': 1, 
u'bucketName': 320, 
u'req_id': 642, 
u'time': 642, 
u'clientIP': 642, 
u'message': 642}

'''





















