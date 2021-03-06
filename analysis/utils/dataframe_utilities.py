"""This file contains utility functions for working with spark dataframes and the parquet file format used to save
the data in s3.

"""


import findspark
findspark.init()
import pyspark as ps
import os
import boto3


def download_parquet_files(index):
    '''
    This function downloads parquet files from the specified topic & specified date range

    index: Select the index/topic from which to download the data.  e.g biden or trump.
    days: List of days in format MMDD so 1028 -> October 28th.

    :return:
    '''
    s3 = boto3.resource('s3')
    bucket = 'datathon-election-tweets'
    tweets_bucket = s3.Bucket(bucket)
    tweet_parquet_files = [file.key for file in list(tweets_bucket.objects.filter(Prefix='{}/'.format(index)).all()) if
                           file.key.split('.')[-1] == 'parquet']
    client = boto3.client('s3')

    folders = {'/'.join(file.split('/')[:2]) for file in tweet_parquet_files}
    for folder in folders:
        full_path = 'tmp/{}'.format(folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    for file in tweet_parquet_files:
        client.download_file(bucket, file, 'tmp/{}.parquet'.format(file))


def create_tweets_dataframe(spark, index):
    '''
    This function constructs a spark dataframe with the locally downloaded parquet files (downloaded from the
    download_parquet_files) and the index from which to construct the dataframe.

    I will want to extend this to allow the creation of a dataframe with multiple idices/topics but will have to be
    cognizant of the fact that there may be duplicates if I join data from multiple indices.
    '''
    parquet_files = []
    directory = 'tmp/{}'.format(index)
    for folder in os.listdir(directory):
        for file in os.listdir('{}/{}/'.format('tmp/{}'.format(index), folder)):
            parquet_files.append('tmp/{}/{}/{}'.format(index, folder, file))

    # for file in os.listdir('tmp/'+folder):
    #         parquet_files.append('tmp/{}/{}'.format(folder,file))
    dataframes = []
    for file in parquet_files:
        df = spark.read.parquet(file)
        dataframes.append(df)
    df = dataframes[0]
    for dataf in dataframes[1:]:
        df = df.union(dataf)
    return df


def create_dataframe_from_parquet(spark, directory):
    """
    This function returns a dataframe from a parquet file in directory.
    """
    parquet_files = [file for file in os.listdir(directory) if file.split('.')[-1] == 'parquet']
    parquet_files = ['{}/{}'.format(directory, file) for file in parquet_files]

    dataframes = [spark.read.parquet(file) for file in parquet_files]
    return dataframes[0]
