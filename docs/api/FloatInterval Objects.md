## FloatInterval Objects

```python
class FloatInterval(StructBase)
```

An interval of floats, defined by inclusive min and max values
note: This is a mirror of TInterval<float>, defined in Interval.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max`` (float):  [Read-Write] Values must be <= Max
- ``min`` (float):  [Read-Write] Values must be >= Min

<a id="unreal.FloatInterval.__init__"></a>

#### __init__

```python
def __init__(min: float = 0.000000, max: float = 0.000000) -> None
```

<a id="unreal.FloatInterval.min"></a>

#### min

```python
@property
def min() -> float
```

(float):  [Read-Write] Values must be >= Min

<a id="unreal.FloatInterval.min"></a>

#### min

```python
@min.setter
def min(value: float) -> None
```

<a id="unreal.FloatInterval.max"></a>

#### max

```python
@property
def max() -> float
```

(float):  [Read-Write] Values must be <= Max

<a id="unreal.FloatInterval.max"></a>

#### max

```python
@max.setter
def max(value: float) -> None
```

<a id="unreal.FloatRange"></a>