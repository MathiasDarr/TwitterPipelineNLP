"""
Experimenting wi/ UDFs

Everything that is passed to a UDF is interpreted as a column/column name.  If you want to pass a literal, you have to options



"""


from analysis.utils.spark_utilities import getSparkInstance
from analysis.utils.dataframe_utilities import create_tweets_dataframe, download_parquet_files, create_dataframe_from_parquet
from pyspark.sql.types import BooleanType
from pyspark.sql.functions import udf
from pyspark.sql import functions as F
#download_parquet_files('trump')

spark = getSparkInstance()

# tweets_dataframe = create_tweets_dataframe(spark, 'trump')
# tweets_dataframe = tweets_dataframe.drop('_corrupt_record')

tweets_dataframe = create_dataframe_from_parquet(spark, "./")




def contains_subject(content, subject):
    # convert each word in lowecase

    if content and subject in content:
        return True
    return False


filterUDF = udf(lambda content, subject: content and subject in content, BooleanType())
virus_tweets = tweets_dataframe.where(filterUDF(tweets_dataframe["content"], F.lit('virus')))
trump_tweets = tweets_dataframe.where(filterUDF(tweets_dataframe["content"], F.lit('trump')))
biden_tweets = tweets_dataframe.where(filterUDF(tweets_dataframe["content"], F.lit('biden')))
biden_tweets.take(10)

tweets_dataframe.


### Apply the transformations

# languageTransformer = LanguageIdentificationTransformer(inputCol='content', outputCol='language')
# locationTransformer = LocationParserTransformer(inputCol='location', outputCol='parsed_location')
#
# pipeline = Pipeline(stages=[languageTransformer, locationTransformer])
#
# pipeline_model = pipeline.fit(tweets_dataframe)
#
# transformed_dataframe = pipeline_model.transform(tweets_dataframe)
