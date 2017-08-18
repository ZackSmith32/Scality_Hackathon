from kafka import KafkaProducer
import random
import time

random.seed(None)

producer = KafkaProducer()

# for i in range(10):
# 	num = str(random.randint(0, 1000))
# 	producer.send('test3', "rand " + num)
# 	print(num)
# 	time.sleep(.001)

count = 0
while True:
	i = raw_input().split("\n")
	# if len(i) > 1:
	# 	print("input = {0}".format(len(i)))
	# else:
	# 	print("len = 1")
	for item in i:
		count += 1
		print(item)
		# print ("count = " + str(count))
		producer.send('test3', item)
		time.sleep(.001)



# if i == "quit":
# 	break