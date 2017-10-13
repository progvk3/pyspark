from pyspark import SparkContext, SparkConf

conf = SparkConf()
sc = SparkContext.getOrCreate(conf)

rdd1 = sc.textFile("file:///home/vasanth/pyspark/docs/testfile1.txt")

rdd2 = rdd1.flatMap(lambda x: x.split(" "))

final = []

for i in rdd2.collect():
	a = sc.accumulator(0)
	for j in rdd2.collect():
		if i == j:
			a +=1
	final.append(i,a.value)

print(final)

