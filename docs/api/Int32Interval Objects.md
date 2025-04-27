## Int32Interval Objects

```python
class Int32Interval(StructBase)
```

An interval of integers, defined by inclusive min and max values
note: This is a mirror of TInterval<int32>, defined in Interval.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max`` (int32):  [Read-Write] Values must be <= Max
- ``min`` (int32):  [Read-Write] Values must be >= Min

<a id="unreal.Int32Interval.__init__"></a>

#### __init__

```python
def __init__(min: int = 0, max: int = 0) -> None
```

<a id="unreal.Int32Interval.min"></a>

#### min

```python
@property
def min() -> int
```

(int32):  [Read-Write] Values must be >= Min

<a id="unreal.Int32Interval.min"></a>

#### min

```python
@min.setter
def min(value: int) -> None
```

<a id="unreal.Int32Interval.max"></a>

#### max

```python
@property
def max() -> int
```

(int32):  [Read-Write] Values must be <= Max

<a id="unreal.Int32Interval.max"></a>

#### max

```python
@max.setter
def max(value: int) -> None
```

<a id="unreal.Int32Range"></a>