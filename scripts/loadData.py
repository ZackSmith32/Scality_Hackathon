import boto3

dummyDir = "/Users/mba/scality_hackathon/test_stuff/"

client = boto3.client(
	's3',
	aws_access_key_id='accessKey1',
	aws_secret_access_key='verySecretKey1',
	endpoint_url='http://localhost:8000'
)

lines = open(dummyDir + 'ml-1m/' + 'movies.dat')

for line in lines:
	a = line.strip().split("::")
	k = a[1]
	v = a[2]
	print(k, v)
	try:
		client.put_object(Key=k, Body=v, Bucket='zackbuk')
	except Exception, e:
		print(e.message)
