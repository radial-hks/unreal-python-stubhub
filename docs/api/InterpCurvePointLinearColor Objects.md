## InterpCurvePointLinearColor Objects

```python
class InterpCurvePointLinearColor(StructBase)
```

Describes one specific point on an interpolation curve.
note: This is a mirror of TInterpCurvePoint<FLinearColor>, defined in InterpCurvePoint.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arrive_tangent`` (LinearColor):  [Read-Write] Tangent of curve arriving at this point.
- ``interp_mode`` (InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.
- ``leave_tangent`` (LinearColor):  [Read-Write] Tangent of curve leaving this point.
- ``out_val`` (LinearColor):  [Read-Write] Color output value of when input is equal to InVal.
- ``val`` (float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointLinearColor.__init__"></a>

#### __init__

```python
def __init__(
        val: float = 0.000000,
        out_val: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        arrive_tangent: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        leave_tangent: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
```

<a id="unreal.InterpCurvePointLinearColor.val"></a>

#### val

```python
@property
def val() -> float
```

(float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointLinearColor.val"></a>

#### val

```python
@val.setter
def val(value: float) -> None
```

<a id="unreal.InterpCurvePointLinearColor.out_val"></a>

#### out_val

```python
@property
def out_val() -> LinearColor
```

(LinearColor):  [Read-Write] Color output value of when input is equal to InVal.

<a id="unreal.InterpCurvePointLinearColor.out_val"></a>

#### out_val

```python
@out_val.setter
def out_val(value: LinearColor) -> None
```

<a id="unreal.InterpCurvePointLinearColor.arrive_tangent"></a>

#### arrive_tangent

```python
@property
def arrive_tangent() -> LinearColor
```

(LinearColor):  [Read-Write] Tangent of curve arriving at this point.

<a id="unreal.InterpCurvePointLinearColor.arrive_tangent"></a>

#### arrive_tangent

```python
@arrive_tangent.setter
def arrive_tangent(value: LinearColor) -> None
```

<a id="unreal.InterpCurvePointLinearColor.leave_tangent"></a>

#### leave_tangent

```python
@property
def leave_tangent() -> LinearColor
```

(LinearColor):  [Read-Write] Tangent of curve leaving this point.

<a id="unreal.InterpCurvePointLinearColor.leave_tangent"></a>

#### leave_tangent

```python
@leave_tangent.setter
def leave_tangent(value: LinearColor) -> None
```

<a id="unreal.InterpCurvePointLinearColor.interp_mode"></a>

#### interp_mode

```python
@property
def interp_mode() -> InterpCurveMode
```

(InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.

<a id="unreal.InterpCurvePointLinearColor.interp_mode"></a>

#### interp_mode

```python
@interp_mode.setter
def interp_mode(value: InterpCurveMode) -> None
```

<a id="unreal.LinearColor"></a>