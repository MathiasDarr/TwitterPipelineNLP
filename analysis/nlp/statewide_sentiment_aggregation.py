"""
This file contains functions for creating a dictionary where the keys are state names and the values are the average sentiment
for each candidate.

"""


def generate_average_sentiment_dictionary(dataframe):
    """
    Generates a dictionary whose keys are a state name or identifying number and which has average sentiment in that state
    as a value.
    :param dataframe:
    :return:
    """
    biden_sentiment_dataframe = dataframe.groupBy('parsed_location').avg('biden-sentiment')
    trump_sentiment_dataframe = dataframe.groupBy('parsed_location').avg('trump-sentiment')
    return biden_sentiment_dataframe.join(trump_sentiment_dataframe, ['parsed_location'], how='full')


