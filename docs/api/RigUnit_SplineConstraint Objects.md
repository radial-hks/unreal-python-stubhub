## RigUnit_SplineConstraint Objects

```python
class RigUnit_SplineConstraint(RigUnit_HighlevelBaseMutable)
```

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (ControlRigCurveAlignment):  [Read-Only] Specifies how to align the chain on the curve
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (Array[RigElementKey]):  [Read-Write] The items to align
- ``maximum`` (float):  [Read-Write] The maximum U value to use on the curve
- ``minimum`` (float):  [Read-Write] The minimum U value to use on the curve
- ``primary_axis`` (Vector):  [Read-Write]
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``secondary_axis`` (Vector):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write] The curve to align to

<a id="unreal.RigUnit_SplineConstraint.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        items: Array[RigElementKey] = [],
        spline: ControlRigSpline = [],
        alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT,
        minimum: float = 0.000000,
        maximum: float = 0.000000,
        primary_axis: Vector = [0.000000, 0.000000, 0.000000],
        secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
        propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SplineConstraint.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write] The items to align

<a id="unreal.RigUnit_SplineConstraint.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_SplineConstraint.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write] The curve to align to

<a id="unreal.RigUnit_SplineConstraint.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_SplineConstraint.alignment"></a>

#### alignment

```python
@property
def alignment() -> ControlRigCurveAlignment
```

(ControlRigCurveAlignment):  [Read-Only] Specifies how to align the chain on the curve

<a id="unreal.RigUnit_SplineConstraint.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Write] The minimum U value to use on the curve

<a id="unreal.RigUnit_SplineConstraint.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigUnit_SplineConstraint.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Write] The maximum U value to use on the curve

<a id="unreal.RigUnit_SplineConstraint.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigUnit_SplineConstraint.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_SplineConstraint.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_SplineConstraint.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_SplineConstraint.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_SplineConstraint.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_FitSplineCurveToChain"></a>