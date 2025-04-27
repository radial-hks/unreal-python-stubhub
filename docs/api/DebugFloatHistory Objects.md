## DebugFloatHistory Objects

```python
class DebugFloatHistory(StructBase)
```

Structure for recording float values and displaying them as an Histogram through DrawDebugFloatHistory.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_adjust_min_max`` (bool):  [Read-Write] Auto adjust Min/Max as new values are recorded?
- ``max_samples`` (int32):  [Read-Write] Max Samples to record.
- ``max_value`` (float):  [Read-Write] Max value to record.
- ``min_value`` (float):  [Read-Write] Min value to record.

<a id="unreal.DebugFloatHistory.__init__"></a>

#### __init__

```python
def __init__(max_samples: int = 0,
             min_value: float = 0.000000,
             max_value: float = 0.000000,
             auto_adjust_min_max: bool = False) -> None
```

<a id="unreal.DebugFloatHistory.max_samples"></a>

#### max_samples

```python
@property
def max_samples() -> int
```

(int32):  [Read-Write] Max Samples to record.

<a id="unreal.DebugFloatHistory.max_samples"></a>

#### max_samples

```python
@max_samples.setter
def max_samples(value: int) -> None
```

<a id="unreal.DebugFloatHistory.min_value"></a>

#### min_value

```python
@property
def min_value() -> float
```

(float):  [Read-Write] Min value to record.

<a id="unreal.DebugFloatHistory.min_value"></a>

#### min_value

```python
@min_value.setter
def min_value(value: float) -> None
```

<a id="unreal.DebugFloatHistory.max_value"></a>

#### max_value

```python
@property
def max_value() -> float
```

(float):  [Read-Write] Max value to record.

<a id="unreal.DebugFloatHistory.max_value"></a>

#### max_value

```python
@max_value.setter
def max_value(value: float) -> None
```

<a id="unreal.DebugFloatHistory.auto_adjust_min_max"></a>

#### auto_adjust_min_max

```python
@property
def auto_adjust_min_max() -> bool
```

(bool):  [Read-Write] Auto adjust Min/Max as new values are recorded?

<a id="unreal.DebugFloatHistory.auto_adjust_min_max"></a>

#### auto_adjust_min_max

```python
@auto_adjust_min_max.setter
def auto_adjust_min_max(value: bool) -> None
```

<a id="unreal.BaseComponentReference"></a>