## WdpEnvironmentFunctionLibrary Objects

```python
class WdpEnvironmentFunctionLibrary(BlueprintFunctionLibrary)
```

Wdp Environment Function Library

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WdpEnvironmentFunctionLibrary.h

<a id="unreal.WdpEnvironmentFunctionLibrary.convert_time_string_to_date_time"></a>

#### convert\_time\_string\_to\_date\_time

```python
@classmethod
def convert_time_string_to_date_time(cls, string: str) -> DateTime
```

X.convert_time_string_to_date_time(string) -> DateTime
将String格式时间转换为标准DateTime，String格式支持：hh:mm:ss或者hh mm ss或者hh-mm-ss或者hh.mm.ss

Args:
    string (str): 

Returns:
    DateTime:

<a id="unreal.WdpEnvironmentFunctionLibrary.convert_timestamp_to_date_time"></a>

#### convert\_timestamp\_to\_date\_time

```python
@classmethod
def convert_timestamp_to_date_time(cls,
                                   timestamp: int,
                                   is_utc_time: bool = False) -> DateTime
```

X.convert_timestamp_to_date_time(timestamp, is_utc_time=False) -> DateTime
将TimeStamp转换为DateTime

Args:
    timestamp (int64): 
    is_utc_time (bool): 

Returns:
    DateTime:

<a id="unreal.WdpEnvironmentFunctionLibrary.convert_float_to_date_time"></a>

#### convert\_float\_to\_date\_time

```python
@classmethod
def convert_float_to_date_time(cls, float_time: float) -> DateTime
```

X.convert_float_to_date_time(float_time) -> DateTime
将float（24h以0 - 2400表示）转换为DateTime

Args:
    float_time (float): 

Returns:
    DateTime:

<a id="unreal.WdpEnvironmentFunctionLibrary.convert_date_time_to_timestamp"></a>

#### convert\_date\_time\_to\_timestamp

```python
@classmethod
def convert_date_time_to_timestamp(cls,
                                   date_time: DateTime,
                                   is_utc_time: bool = False) -> int
```

X.convert_date_time_to_timestamp(date_time, is_utc_time=False) -> int64
将DateTime转换为TimeStamp

Args:
    date_time (DateTime): 
    is_utc_time (bool): 

Returns:
    int64:

<a id="unreal.WdpEnvironmentFunctionLibrary.convert_date_time_to_float"></a>

#### convert\_date\_time\_to\_float

```python
@classmethod
def convert_date_time_to_float(cls, datetime: DateTime) -> float
```

X.convert_date_time_to_float(datetime) -> float
将DateTime转换为float（24h以0-2400表示）

Args:
    datetime (DateTime): 

Returns:
    float:

<a id="unreal.WdpEnvironmentSubsystem"></a>