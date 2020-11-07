"""
This file defines a file that will apply the transformation pipeline

"""

import findspark

findspark.init()

from analysis.transformers.LocationTransformer import LocationParserTransformer
from analysis.transformers.LanguageTransformer import LanguageIdentificationTransformer
from analysis.transformers.SentimentAnalysisTransformer import SentimentTransformer

from pyspark.ml import Pipeline

def apply_transformation(dataframe):
    languageTransformer = LanguageIdentificationTransformer(inputCol='content', outputCol='language')
    locationTransformer = LocationParserTransformer(inputCol='location', outputCol='parsed_location')
    sentimentTransformer = SentimentTransformer(inputCol='content')
    pipeline = Pipeline(stages=[languageTransformer, locationTransformer, sentimentTransformer])
    pipeline_model = pipeline.fit(dataframe)
    return pipeline_model.transform(dataframe)
