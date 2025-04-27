## SmartReduceParams Objects

```python
class SmartReduceParams(StructBase)
```

Smart Reduce Params

**C++ Source:**

- **Module**: CurveEditor
- **File**: CurveEditorSmartReduceFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sample_rate`` (FrameRate):  [Read-Write] Rate at which the curve should be sampled to compare against value tolerance.
- ``tolerance_percentage`` (float):  [Read-Write] Tolerance threshold, set as a percentage of the value's range

<a id="unreal.SmartReduceParams.__init__"></a>

#### __init__

```python
def __init__(tolerance_percentage: float = 0.000000,
             sample_rate: FrameRate = [60000, 1]) -> None
```

<a id="unreal.SmartReduceParams.tolerance_percentage"></a>

#### tolerance_percentage

```python
@property
def tolerance_percentage() -> float
```

(float):  [Read-Write] Tolerance threshold, set as a percentage of the value's range

<a id="unreal.SmartReduceParams.tolerance_percentage"></a>

#### tolerance_percentage

```python
@tolerance_percentage.setter
def tolerance_percentage(value: float) -> None
```

<a id="unreal.SmartReduceParams.sample_rate"></a>

#### sample_rate

```python
@property
def sample_rate() -> FrameRate
```

(FrameRate):  [Read-Write] Rate at which the curve should be sampled to compare against value tolerance.

<a id="unreal.SmartReduceParams.sample_rate"></a>

#### sample_rate

```python
@sample_rate.setter
def sample_rate(value: FrameRate) -> None
```

<a id="unreal.DataLayerCreationParameters"></a>