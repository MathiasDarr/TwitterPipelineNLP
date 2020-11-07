from analysis.utils.spark_utilities import getSparkInstance
import pyspark.sql.functions  as F



spark = getSparkInstance()


def working_fun(mapping_broadcasted):
    def f(x):
        return mapping_broadcasted.value.get(x)
    return F.udf(f)


df = spark.createDataFrame([
    ['Alabama', ],
    ['Texas', ],
    ['Antioquia', ]
]).toDF('state')
mapping = {'Alabama': 'AL', 'Texas': 'TX'}
b = spark.sparkContext.broadcast(mapping)
df.withColumn('state_abbreviation', working_fun(b)(F.col('state'))).show()