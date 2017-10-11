from pyspark import SparkContext, SparkConf

conf = SparkConf()
sc = SparkContext.getOrCreate(conf)

a = sc.parallelize([1,2,3,4])

print (a.collect())

sc.stop()