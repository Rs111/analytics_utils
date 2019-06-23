Analytics Utils
===================================================

Util functions and tooling.

##Installation
**TBD**

##Usage

- [date](#date)
    - [date_range](#date_range)
    - [validate](#validate)
- [semantic_version](#semantic_version)
    - [semantic_version](#semantic_version)
    
### date 

#### date_range
- Returns a List of sequential dates between the input date_start and date_end
- (date_start: String, date_end: String) => List[String]

```python
from analytics_utils.date import date_range

sequential_dates = date_range('2019-01-01', '2019-01-30')
```

#### validate 
- Returns Boolean indicating whether input String is a valid date of the input format
- (date_string: String, format: String) => Boolean

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

# date_format is set to "%Y-%m-%d"
eg7 = validate("2019-01-01")
```

