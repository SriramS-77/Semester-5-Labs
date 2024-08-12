from pyspark import SparkContext

sc = SparkContext("local", "testing")

lst = list(map(int, input("Enter space separated list of integers: ").split()))

print(sc.parallelize(lst).map(lambda x: x**2).collect())
