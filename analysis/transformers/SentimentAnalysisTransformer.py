import findspark

findspark.init()

from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType, DoubleType
from pyspark.ml.pipeline import Transformer
from pyspark.ml.param.shared import HasInputCol, HasOutputCol, Param, Params, TypeConverters
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsWritable
from pyspark import keyword_only

from analysis.nlp.sentiment_analysis import SentimentAnalyzer


class SentimentTransformer(Transformer, HasInputCol, HasOutputCol, DefaultParamsReadable, DefaultParamsWritable):
    '''
    This transformer is used in the spark.ml pipeline to assign each topic found in the tweets a sentiment score
    '''

    @keyword_only
    def __init__(self, inputCol=None, outputCol=None, stopwords=None):
        '''

        :param topics: list of topics on which to perform sentiment analysis e.g ['biden', 'trump']
        '''

        super(SentimentTransformer, self).__init__()
        self.stopwords = Param(self, "stopwords", "")
        self._setDefault(stopwords=[])
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

        self.sentimentAnalyzer = SentimentAnalyzer(['biden', 'trump', 'virus'])

    @keyword_only
    def setParams(self, inputCol=None, outputCol=None, stopwords=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)

    # Required in Spark >= 3.0
    def setInputCol(self, value):
        """
        Sets the value of :py:attr:`inputCol`.
        """
        return self._set(inputCol=value)

    # Required in Spark >= 3.0
    def setOutputCol(self, value):
        """
        Sets the value of :py:attr:`outputCol`.
        """
        return self._set(outputCol=value)

    def _transform(self, dataset):
        sentiment_analysis_udf = udf(lambda content: self.sentimentAnalyzer.generate_sentimenet_scores(content),
                                     ArrayType(DoubleType()))
        sentiments = sentiment_analysis_udf(self.getInputCol())

        for i, subject in enumerate(self.sentimentAnalyzer.subjects):
            dataset = dataset.withColumn('{}-sentiment'.format(subject), sentiments[i])

        return dataset
