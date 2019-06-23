Analytics Utils
===================================================

Util functions and tooling.

## Installation
**TBD**

## Usage

- [date](#date)
    - [date_range](#date_range)
    - [validate](#validate)
- [semantic_version](#semantic_version)
    - [SemanticVersion](#SemanticVersion)
    
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