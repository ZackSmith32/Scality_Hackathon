from pyspark import SparkConf, SparkContext
import collections


def mp():
	conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
	sc = SparkContext(conf = conf)

	lines = sc.textFile("./logs.txt")
	print(lines)
	ratings = lines.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

	sortedResults = ratings.map(lambda x: (x[1], x[0])).sortByKey()
	results = sortedResults.collect()

	for result in results:
	    count = str(result[0])
	    word = result[1].encode('ascii','ignore')
	    if word:
	    	print(word.decode() + ":\t\t" + count)

def main():
	mp()

if __name__ == "__main__":
	main()