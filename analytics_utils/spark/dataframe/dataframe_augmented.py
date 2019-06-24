from typing import Iterable
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, array, struct, lit, explode


class DataFrameAug(DataFrame):
    """Extends functionality of the pyspark :class:`DataFrame` class"""

    def __init__(self, df: DataFrame):
        super().__init__(df._jdf, df.sql_ctx)

    def melt(
            self: DataFrame,
            id_vars: Iterable[str], value_vars: Iterable[str],
            var_name: str = "variable", value_name: str = "value") -> DataFrame:
        """Converts :class:`DataFrame` from wide to long format."""

        # Create array<struct<variable: str, value: ...>>
        _vars_and_vals = array(*(
            struct(lit(c).alias(var_name), col(c).alias(value_name))
            for c in value_vars))

        # Add to the DataFrame and explode
        _tmp = self.withColumn("_vars_and_vals", explode(_vars_and_vals))

        cols = id_vars + [
            col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
        return _tmp.select(*cols)
