from pyspark import SparkConf
from pyspark import SparkContext
from pyspark import SQLContext


class SparkConnector(object):

    def __init__(self, app_name="Spark App", spark_conf=None):
        self._app_name = app_name
        if isinstance(spark_conf, SparkConf):
            self._conf = spark_conf
        else:
            self._conf = SparkConf().setAppName(self._app_name)

        self._sc = SparkContext.getOrCreate(conf=self._conf)

        self._sqlContext = SQLContext(self._sc) \
            if self._sc.version < 1.6 \
            else SQLContext.getOrCreate(self._sc)

    @property
    def app_name(self):
        return self._app_name

    @property
    def sc(self):
        return self._sc

    def sql_context(self):
        return self._sqlContext

    def conf(self):
        return self._conf






