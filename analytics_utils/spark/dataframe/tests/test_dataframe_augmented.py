import unittest
from analytics_utils.spark import spark
from analytics_utils.spark.dataframe import DataFrameAug
from pyspark.sql import Row
from pyspark.sql.functions import col
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
    # def test_melt_one_id_one_value(self):
    #
    #     expected = [
    #         Row(cat='A', name='Alice', value=5, variable='num'),
    #         Row(cat='A', name='Alice', value=5, variable='num'),
    #         Row(cat='B', name='Bob', value=9, variable='num'),
    #         Row(cat='B', name='Tim', value=17, variable='num'),
    #         Row(cat='B', name='Boris', value=2, variable='num'),
    #         Row(cat='B', name='Sheldon', value=60, variable='num'),
    #         Row(cat='C', name='Bobby', value=60, variable='num'),
    #         Row(cat='C', name='Radu', value=121821, variable='num')]
    #
    #     self.assertEqual(df.melt(id_vars=["cat"], value_vars=["num"]).collect(), expected)

    # should raise an assert when var_name is equal to an element in id_vars
    def test_melt_assertion_raise_one(self):
        with self.assertRaises(AssertionError):
            df.melt(id_vars=["cat"], value_vars=["num"], var_name="num")

    # should raise an assert when var_name is equal to an element in value_vars
    def test_melt_assertion_raise_two(self):
        with self.assertRaises(AssertionError):
            df.melt(id_vars=["cat"], value_vars=["num"], var_name="cat")
