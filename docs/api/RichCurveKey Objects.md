## RichCurveKey Objects

```python
class RichCurveKey(StructBase)
```

One key in a rich, editable float curve

**C++ Source:**

- **Module**: Engine
- **File**: RichCurve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interp_mode`` (RichCurveInterpMode):  [Read-Write] Interpolation mode between this key and the next
- ``tangent_mode`` (RichCurveTangentMode):  [Read-Write] Mode for tangents at this key
- ``tangent_weight_mode`` (RichCurveTangentWeightMode):  [Read-Write] If either tangent at this key is 'weighted'
- ``time`` (float):  [Read-Write] Time at this key
- ``value`` (float):  [Read-Write] Value at this key

<a id="unreal.RichCurveKey.__init__"></a>

#### __init__

```python
def __init__(
        interp_mode: RichCurveInterpMode = RichCurveInterpMode.RCIM_LINEAR,
        tangent_mode: RichCurveTangentMode = RichCurveTangentMode.RCTM_AUTO,
        tangent_weight_mode:
    RichCurveTangentWeightMode = RichCurveTangentWeightMode.
    RCTWM_WEIGHTED_NONE,
        time: float = 0.000000,
        value: float = 0.000000) -> None
```

<a id="unreal.RichCurveKey.interp_mode"></a>

#### interp_mode

```python
@property
def interp_mode() -> RichCurveInterpMode
```

(RichCurveInterpMode):  [Read-Write] Interpolation mode between this key and the next

<a id="unreal.RichCurveKey.interp_mode"></a>

#### interp_mode

```python
@interp_mode.setter
def interp_mode(value: RichCurveInterpMode) -> None
```

<a id="unreal.RichCurveKey.tangent_mode"></a>

#### tangent_mode

```python
@property
def tangent_mode() -> RichCurveTangentMode
```

(RichCurveTangentMode):  [Read-Write] Mode for tangents at this key

<a id="unreal.RichCurveKey.tangent_mode"></a>

#### tangent_mode

```python
@tangent_mode.setter
def tangent_mode(value: RichCurveTangentMode) -> None
```

<a id="unreal.RichCurveKey.tangent_weight_mode"></a>

#### tangent_weight_mode

```python
@property
def tangent_weight_mode() -> RichCurveTangentWeightMode
```

(RichCurveTangentWeightMode):  [Read-Write] If either tangent at this key is 'weighted'

<a id="unreal.RichCurveKey.tangent_weight_mode"></a>

#### tangent_weight_mode

```python
@tangent_weight_mode.setter
def tangent_weight_mode(value: RichCurveTangentWeightMode) -> None
```

<a id="unreal.RichCurveKey.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Write] Time at this key

<a id="unreal.RichCurveKey.time"></a>

#### time

```python
@time.setter
def time(value: float) -> None
```

<a id="unreal.RichCurveKey.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Value at this key

<a id="unreal.RichCurveKey.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.PositionHistory"></a>