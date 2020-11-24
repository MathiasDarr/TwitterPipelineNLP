"""
Experimenting wi/ UDFs

Everything that is passed to a UDF is interpreted as a column/column name.  If you want to pass a literal, you have to options



"""
from analysis.utils.spark_utilities import getSparkInstance
from analysis.utils.dataframe_utilities import create_tweets_dataframe, download_parquet_files, create_dataframe_from_parquet

from pyspark.sql.types import BooleanType
from pyspark.sql.functions import udf
from pyspark.sql import functions as F

from analysis.transformers.LocationTransformer import LocationParserTransformer
from analysis.transformers.LanguageTransformer import LanguageIdentificationTransformer
from analysis.transformers.SentimentAnalysisTransformer import SentimentTransformer
from pyspark.ml import Pipeline

#download_parquet_files('trump')

spark = getSparkInstance()

tweets_dataframe = create_tweets_dataframe(spark, 'trump')
# tweets_dataframe = create_dataframe_from_parquet(spark, "./")
tweets_dataframe = tweets_dataframe.drop('_corrupt_record')


content_contains_subject_filter_udf = udf(lambda content, subject: content and subject in content, BooleanType())

virus_tweets_dataframe = tweets_dataframe.where(content_contains_subject_filter_udf(tweets_dataframe["content"], F.lit('virus')))
trump_tweets_dataframe = tweets_dataframe.where(content_contains_subject_filter_udf(tweets_dataframe["content"], F.lit('trump')))
biden_tweets_dataframe = tweets_dataframe.where(content_contains_subject_filter_udf(tweets_dataframe["content"], F.lit('biden')))


def apply_transformation(dataframe):
    languageTransformer = LanguageIdentificationTransformer(inputCol='content', outputCol='language')
    locationTransformer = LocationParserTransformer(inputCol='location', outputCol='parsed_location')
    sentimentTransformer = SentimentTransformer(inputCol='content')
    pipeline = Pipeline(stages=[languageTransformer, locationTransformer, sentimentTransformer])
    pipeline_model = pipeline.fit(dataframe)
    return pipeline_model.transform(dataframe)


languageTransformer = LanguageIdentificationTransformer(inputCol='content', outputCol='language')
locationTransformer = LocationParserTransformer(inputCol='location', outputCol='parsed_location')
sentimentTransformer = SentimentTransformer(inputCol='content')



tweets = trump_tweets_dataframe.limit(5)
df = biden_tweets_dataframe.limit(5)
transformed_dataframe = apply_transformation(virus_tweets_dataframe)
transformed_dataframe.collect()
