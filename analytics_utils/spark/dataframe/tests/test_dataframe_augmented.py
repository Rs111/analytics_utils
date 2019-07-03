import unittest
from analytics_utils.spark import spark
from analytics_utils.spark.dataframe import DataFrameAug
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("cat", StringType()),
    StructField("name", StringType()),
    StructField("id", IntegerType()),
    StructField("num", IntegerType())
])

l = [
    ("A", 'Alice', 1, 5),
    ("A", 'Alice', 1, 5),
    ('B', 'Bob', 3, 9),
    ('B', 'Tim', 70, 17),
    ('B', 'Boris', 1, 2),
    ('B', 'Sheldon', 3, 60),
    ('C', 'Bobby', 14, 60),
    ('C', 'Radu', 182832, 121821),
]

df = DataFrameAug(spark.createDataFrame(l, schema))


class TestMelt(unittest.TestCase):

    # should return expected when melt is done with one id_var and one value_var
    def test_melt_one_id_one_value(self):

        expected = [
            Row(cat='A', name='Alice', variable='num', value=5),
            Row(cat='A', name='Alice', variable='id', value=1),
            Row(cat='A', name='Alice', variable='num', value=5),
            Row(cat='A', name='Alice', variable='id', value=1),
            Row(cat='B', name='Bob', variable='num', value=9),
            Row(cat='B', name='Bob', variable='id', value=3),
            Row(cat='B', name='Tim', variable='num', value=17),
            Row(cat='B', name='Tim', variable='id', value=70),
            Row(cat='B', name='Boris', variable='num', value=2),
            Row(cat='B', name='Boris', variable='id', value=1),
            Row(cat='B', name='Sheldon', variable='num', value=60),
            Row(cat='B', name='Sheldon', variable='id', value=3),
            Row(cat='C', name='Bobby', variable='num', value=60),
            Row(cat='C', name='Bobby', variable='id', value=14),
            Row(cat='C', name='Radu', variable='num', value=121821),
            Row(cat='C', name='Radu', variable='id', value=182832)]

        self.assertEqual(df.melt(id_vars=["cat"], value_vars=["num"]).collect(), expected)
