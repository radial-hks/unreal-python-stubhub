## TimeSectionDefine Objects

```python
class TimeSectionDefine(StructBase)
```

时间段对应起止时间定义

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherControlDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actual_used_time`` (DateTime):  [Read-Write] 时间段代表时间，切换至某个时间段时用的实际时间
- ``end_time`` (DateTime):  [Read-Write] 时间段结束时间
- ``start_time`` (DateTime):  [Read-Write] 时间段起始时间

<a id="unreal.TimeSectionDefine.__init__"></a>

#### \_\_init\_\_

```python
def __init__(start_time: DateTime = [],
             end_time: DateTime = [],
             actual_used_time: DateTime = []) -> None
```

<a id="unreal.TimeSectionDefine.start_time"></a>

#### start\_time

```python
@property
def start_time() -> DateTime
```

(DateTime):  [Read-Write] 时间段起始时间

<a id="unreal.TimeSectionDefine.start_time"></a>

#### start\_time

```python
@start_time.setter
def start_time(value: DateTime) -> None
```

<a id="unreal.TimeSectionDefine.end_time"></a>

#### end\_time

```python
@property
def end_time() -> DateTime
```

(DateTime):  [Read-Write] 时间段结束时间

<a id="unreal.TimeSectionDefine.end_time"></a>

#### end\_time

```python
@end_time.setter
def end_time(value: DateTime) -> None
```

<a id="unreal.TimeSectionDefine.actual_used_time"></a>

#### actual\_used\_time

```python
@property
def actual_used_time() -> DateTime
```

(DateTime):  [Read-Write] 时间段代表时间，切换至某个时间段时用的实际时间

<a id="unreal.TimeSectionDefine.actual_used_time"></a>

#### actual\_used\_time

```python
@actual_used_time.setter
def actual_used_time(value: DateTime) -> None
```

<a id="unreal.BoneReferencePair"></a>