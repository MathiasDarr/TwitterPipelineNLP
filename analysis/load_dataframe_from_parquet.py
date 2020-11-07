"""This file demonstrates how to load the dataframe from parquet (the create_dataframe_from_supplied_data script must
already have been run. """


from analysis.sparkNLP.utils.construct_spark_dataframe import create_dataframe_from_parquet, download_parquet_files



df = create_dataframe_from_parquet('data/parquet')
