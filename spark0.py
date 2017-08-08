#pyspark tutorial 1.0
#Faiz ul haque zeya
#Data scientist and CEO Transys
from pyspark import SparkContext, SparkConf
sc = SparkContext.getOrCreate()
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
lp=distData.reduce(lambda a, b: a + b)
print(lp)
