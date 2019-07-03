from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, array, struct, lit, explode


class DataFrameAug(DataFrame):
    """Extends functionality of the pyspark :class:`DataFrame`"""

    def __init__(self, df: DataFrame):
        super().__init__(df._jdf, df.sql_ctx)

    def melt(
            self: DataFrame,
            id_vars: List[str],
            value_vars: List[str],
            var_name: str = "variable",
            value_name: str = "value") -> DataFrame:
        """Converts `DataFrame` from wide to long format."""

        # Assertions
        assert var_name not in id_vars + value_vars, "var_name cannot equal a value in id_vars or value_vars"
        assert value_name not in id_vars + value_vars, "value_name cannot equal a value in id_vars or value_vars"
        assert var_name != value_name, "var_name cannot hold the same value as value_name"
        assert len(id_vars) > 0, "id_vars must not be an empty list"
        assert len(value_vars) > 0, "value_vars must not be an empty list"
        assert len(set(id_vars) & set(value_vars)) == 0, "there must be no intersection between id_vars and value_vars"

        _d = dict(id_vars=id_vars, value_vars=value_vars)

        for param in _d.keys():

            _invalid_elements = [i for i in _d[param] if i not in self.columns]
            assert \
                len(_invalid_elements) == 0, \
                "elements: `{1}` in param: `{0}` are not column names in `DataFrame`".format(param, ", ".join(_invalid_elements))

        # Create array<struct<variable: str, value: ...>>
        _vars_and_vals = array(*(
            struct(lit(c).alias(var_name), col(c).alias(value_name))
            for c in value_vars))

        # Add to the DataFrame and explode
        _tmp = self.withColumn("_vars_and_vals", explode(_vars_and_vals))

        cols = [
            col(id_var).alias(id_var) for id_var in ["cat", "name"]] + [
            col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
        return _tmp.select(*cols)
