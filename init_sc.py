from pyspark import SparkContext
sc = SparkContext(appName = "test")

a = sc.parallelize([1,2,3,4])

print (a.collect())

sc.stop()