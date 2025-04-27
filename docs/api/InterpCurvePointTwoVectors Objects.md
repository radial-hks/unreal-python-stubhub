## InterpCurvePointTwoVectors Objects

```python
class InterpCurvePointTwoVectors(StructBase)
```

Describes one specific point on an interpolation curve.
note: This is a mirror of TInterpCurvePoint<FTwoVectors>, defined in InterpCurvePoint.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arrive_tangent`` (TwoVectors):  [Read-Write] Tangent of curve arriving at this point.
- ``interp_mode`` (InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.
- ``leave_tangent`` (TwoVectors):  [Read-Write] Tangent of curve leaving this point.
- ``out_val`` (TwoVectors):  [Read-Write] Two 3D vectors output value of when input is equal to InVal.
- ``val`` (float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointTwoVectors.__init__"></a>

#### __init__

```python
def __init__(
        val: float = 0.000000,
        out_val: TwoVectors = [[0.000000, 0.000000, 0.000000],
                               [0.000000, 0.000000, 0.000000]],
        arrive_tangent: TwoVectors = [[0.000000, 0.000000, 0.000000],
                                      [0.000000, 0.000000, 0.000000]],
        leave_tangent: TwoVectors = [[0.000000, 0.000000, 0.000000],
                                     [0.000000, 0.000000, 0.000000]],
        interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
```

<a id="unreal.InterpCurvePointTwoVectors.val"></a>

#### val

```python
@property
def val() -> float
```

(float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointTwoVectors.val"></a>

#### val

```python
@val.setter
def val(value: float) -> None
```

<a id="unreal.InterpCurvePointTwoVectors.out_val"></a>

#### out_val

```python
@property
def out_val() -> TwoVectors
```

(TwoVectors):  [Read-Write] Two 3D vectors output value of when input is equal to InVal.

<a id="unreal.InterpCurvePointTwoVectors.out_val"></a>

#### out_val

```python
@out_val.setter
def out_val(value: TwoVectors) -> None
```

<a id="unreal.InterpCurvePointTwoVectors.arrive_tangent"></a>

#### arrive_tangent

```python
@property
def arrive_tangent() -> TwoVectors
```

(TwoVectors):  [Read-Write] Tangent of curve arriving at this point.

<a id="unreal.InterpCurvePointTwoVectors.arrive_tangent"></a>

#### arrive_tangent

```python
@arrive_tangent.setter
def arrive_tangent(value: TwoVectors) -> None
```

<a id="unreal.InterpCurvePointTwoVectors.leave_tangent"></a>

#### leave_tangent

```python
@property
def leave_tangent() -> TwoVectors
```

(TwoVectors):  [Read-Write] Tangent of curve leaving this point.

<a id="unreal.InterpCurvePointTwoVectors.leave_tangent"></a>

#### leave_tangent

```python
@leave_tangent.setter
def leave_tangent(value: TwoVectors) -> None
```

<a id="unreal.InterpCurvePointTwoVectors.interp_mode"></a>

#### interp_mode

```python
@property
def interp_mode() -> InterpCurveMode
```

(InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.

<a id="unreal.InterpCurvePointTwoVectors.interp_mode"></a>

#### interp_mode

```python
@interp_mode.setter
def interp_mode(value: InterpCurveMode) -> None
```

<a id="unreal.TwoVectors"></a>