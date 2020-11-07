from analysis.utils.spark_utilities import getSparkInstance
from analysis.utils.dataframe_utilities import create_tweets_dataframe, download_parquet_files

#download_parquet_files('trump')
spark = getSparkInstance()

tweets_dataframe = create_tweets_dataframe(spark, 'trump')

tweets_dataframe = tweets_dataframe.drop('_corrupt_record')


