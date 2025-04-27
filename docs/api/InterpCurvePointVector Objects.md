## InterpCurvePointVector Objects

```python
class InterpCurvePointVector(StructBase)
```

Describes one specific point on an interpolation curve.
note: This is a mirror of TInterpCurvePoint<FVector>, defined in InterpCurvePoint.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arrive_tangent`` (Vector):  [Read-Write] Tangent of curve arriving at this point.
- ``interp_mode`` (InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.
- ``leave_tangent`` (Vector):  [Read-Write] Tangent of curve leaving this point.
- ``out_val`` (Vector):  [Read-Write] 3D vector output value of when input is equal to InVal.
- ``val`` (float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointVector.__init__"></a>

#### __init__

```python
def __init__(
        val: float = 0.000000,
        out_val: Vector = [0.000000, 0.000000, 0.000000],
        arrive_tangent: Vector = [0.000000, 0.000000, 0.000000],
        leave_tangent: Vector = [0.000000, 0.000000, 0.000000],
        interp_mode: InterpCurveMode = InterpCurveMode.CIM_LINEAR) -> None
```

<a id="unreal.InterpCurvePointVector.val"></a>

#### val

```python
@property
def val() -> float
```

(float):  [Read-Write] Float input value that corresponds to this key (eg. time).

<a id="unreal.InterpCurvePointVector.val"></a>

#### val

```python
@val.setter
def val(value: float) -> None
```

<a id="unreal.InterpCurvePointVector.out_val"></a>

#### out_val

```python
@property
def out_val() -> Vector
```

(Vector):  [Read-Write] 3D vector output value of when input is equal to InVal.

<a id="unreal.InterpCurvePointVector.out_val"></a>

#### out_val

```python
@out_val.setter
def out_val(value: Vector) -> None
```

<a id="unreal.InterpCurvePointVector.arrive_tangent"></a>

#### arrive_tangent

```python
@property
def arrive_tangent() -> Vector
```

(Vector):  [Read-Write] Tangent of curve arriving at this point.

<a id="unreal.InterpCurvePointVector.arrive_tangent"></a>

#### arrive_tangent

```python
@arrive_tangent.setter
def arrive_tangent(value: Vector) -> None
```

<a id="unreal.InterpCurvePointVector.leave_tangent"></a>

#### leave_tangent

```python
@property
def leave_tangent() -> Vector
```

(Vector):  [Read-Write] Tangent of curve leaving this point.

<a id="unreal.InterpCurvePointVector.leave_tangent"></a>

#### leave_tangent

```python
@leave_tangent.setter
def leave_tangent(value: Vector) -> None
```

<a id="unreal.InterpCurvePointVector.interp_mode"></a>

#### interp_mode

```python
@property
def interp_mode() -> InterpCurveMode
```

(InterpCurveMode):  [Read-Write] Interpolation mode between this point and the next one.

<a id="unreal.InterpCurvePointVector.interp_mode"></a>

#### interp_mode

```python
@interp_mode.setter
def interp_mode(value: InterpCurveMode) -> None
```

<a id="unreal.InterpCurvePointVector2D"></a>