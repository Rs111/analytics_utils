Analytics Utils
===================================================

Utility functions and tooling for Analytics.

## Installation
**Clone Repo and Use**

## Usage

- [date](#date)
    - [date_range](#date_range)
    - [date_range_with_weeks](#date_range_with_weeks)
    - [days](#days)
    - [validate](#validate)
    - [random_date](#random_date)
- [semantic_version](#semantic_version)
    - [SemanticVersion](#SemanticVersion)
- [DataFrameAug](#DataFrameAug)
    - [melt](#melt)
    - [with_df_transformed](#with_df_transformed)
    
### date 
- All date functions have a `date_format` parameter that is set to `'%Y-%m-%d'` by default

#### date_range
- Returns a List of sequential dates between the input date_start and date_end
- (date_start: String, date_end: String, date_format: String) => List[String]

```python
from analytics_utils.date import date_range


sequential_dates = date_range("2019-01-01", "2019-01-30")

```

#### date_range_with_weeks
- Returns a List of Tuples with:
    - The first element being sequential dates between the input date_start and date_end
    - The second and third elements being the week start and end dates relative to the first element
- (date_start: String, date_end: String, date_format: String) => List[Tuple[String, String, String]]

```python
from analytics_utils.date import date_range


sequential_dates = date_range("2019-01-01", "2019-01-30")

```

#### days
- Functions which add/subtract `days` or `weeks` to `date`
- (date: String, )

```python
from analytics_utils.date.days import add_days, minus_days, add_weeks, minus_weeks


dt_plus_7_days = add_days("2019-01-01", 7)
dt_minus_7_days = minus_days("2019-01-01", 7)
dt_plus_1_week = add_weeks("2019-01-01", 1)
dt_minus_1_week = minus_weeks("2019-01-01", 1)

```

#### random_date
- Returns a random date between the input start and end dates (inclusive)
- (date_start: String, date_end: String, date_format: String) => String

```python
from analytics_utils.date import random_date


rand_date = random_date("2019-07-08", "2019-07-30")

```

#### validate 
- Returns Boolean indicating whether input String is a valid date of the input format
- (date_string: String, date_format: String) => Boolean

```python
from analytics_utils.date import validate


# return true
eg1 = validate(date="2019-01-01", date_format="%Y-%m-%d")

# return false
eg2 = validate("2019-01-01", "%Y-%m-%d")
eg3 = validate("2019-01-01a", "%Y-%m-%d")
eg4 = validate("2019 -01-01", "%Y-%m-%d")
eg5 = validate("2019-13-01", "%Y-%m-%d")
eg6 = validate("2019-3-01", "%Y-%m-%d")

# default date_format is "%Y-%m-%d"
eg7 = validate("2019-01-01")

```


### semantic_version

#### SemanticVersion
- Class holding methods to clean and parse semantic versions
- Semantic versions are those in the form 'major.minor.patch'
- Treatment before parsing:
    - If semantic version is invalid, all methods return None
    - If semantic version is valid but incomplete, methods will set missing semantic components to 0
    - If semantic version is valid and complete, leave as is

```python
from analytics_utils.semantic_version import SemanticVersion


# case one: input is valid and complete 
eg1 = SemanticVersion("6.3.12")
eg1_cleaned = eg1.clean()            # returns 6.3.12
eg1_parsed = eg1.parse()             # returns [6,3,12]
eg1_major_parsed = eg1.parse_major() # returns 6
eg1_minor_parsed = eg1.parse_minor() # returns 3
eg1_major_patch = eg1.parse_patch()  # returns 12

# case two: input is valid but incomplete
eg2 = SemanticVersion("6.3")
eg2_cleaned = eg2.clean()            # returns 6.3.0
eg2_parsed = eg2.parse()             # returns [6,3,0]
eg2_major_parsed = eg2.parse_major() # returns 6
eg2_minor_parsed = eg2.parse_minor() # returns 3
eg2_major_patch = eg2.parse_patch()  # returns 0

# case three: input is invalid
eg3 = SemanticVersion("6.3$")
eg3_cleaned = eg3.clean()            # returns None
eg3_parsed = eg3.parse()             # returns None
eg3_major_parsed = eg3.parse_major() # returns None
eg3_minor_parsed = eg3.parse_minor() # returns None
eg3_major_patch = eg3.parse_patch()  # returns None

```


### DataFrameAug
- Extends functionality of the pyspark `DataFrame`
- Implemented as a subclass which calls the pyspark and adds methods (e.g. df.melt) 

#### melt
- Anti-pivots a dataset from wide-format to long-format
- Same behaviour as the Pandas melt function: https://www.geeksforgeeks.org/python-pandas-melt/

```python
from analytics_utils.spark.dataframe import DataFrameAug
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

df.melt(id_vars=["cat"], value_vars=["name"])

```

#### with_df_transformed
- Apply a `DataFrame => Any` function to a pyspark `DataFrame` instance

```python
from analytics_utils.spark.dataframe import DataFrameAug


condition = True
f = lambda df: df.withColumn("conditional_col", lit(1)) if condition else df

df.with_df_transformed(f)

```