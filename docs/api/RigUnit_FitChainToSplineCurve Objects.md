## RigUnit_FitChainToSplineCurve Objects

```python
class RigUnit_FitChainToSplineCurve(RigUnit_HighlevelBaseMutable)
```

Fits a given chain to a spline curve.
Additionally provides rotational control matching the features of the Distribute Rotation node.

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment`` (ControlRigCurveAlignment):  [Read-Only] Specifies how to align the chain on the curve
- ``debug_settings`` (RigUnit_FitChainToCurve_DebugSettings):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (RigElementKeyCollection):  [Read-Write] The items to align
- ``maximum`` (float):  [Read-Only] The maximum U value to use on the curve
- ``minimum`` (float):  [Read-Only] The minimum U value to use on the curve
- ``pole_vector_position`` (Vector):  [Read-Write] The the position of the pole vector used for aligning the secondary axis.
  Only has an effect if the secondary axis is set.
- ``primary_axis`` (Vector):  [Read-Write] The major axis being aligned - along the bone
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``rotation_ease_type`` (RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.
- ``rotations`` (Array[RigUnit_FitChainToCurve_Rotation]):  [Read-Write] The list of rotations to be applied along the curve
- ``sampling_precision`` (int32):  [Read-Only] The number of samples to use on the curve. Clamped at 64.
- ``secondary_axis`` (Vector):  [Read-Write] The minor axis being aligned - towards the pole vector.
  You can use (0.0, 0.0, 0.0) to disable it.
- ``spline`` (ControlRigSpline):  [Read-Write] The curve to align to
- ``weight`` (float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_FitChainToSplineCurve.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    items: RigElementKeyCollection = [[]],
    spline: ControlRigSpline = [],
    alignment: ControlRigCurveAlignment = ControlRigCurveAlignment.FRONT,
    minimum: float = 0.000000,
    maximum: float = 0.000000,
    sampling_precision: int = 0,
    primary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
    pole_vector_position: Vector = [0.000000, 0.000000, 0.000000],
    rotations: Array[RigUnit_FitChainToCurve_Rotation] = [],
    rotation_ease_type: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
    weight: float = 0.000000,
    propagate_to_children: bool = False,
    debug_settings: RigUnit_FitChainToCurve_DebugSettings = [
        False, 1.000000, [1.000000, 1.000000, 0.000000, 1.000000],
        [1.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ]
) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The items to align

<a id="unreal.RigUnit_FitChainToSplineCurve.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write] The curve to align to

<a id="unreal.RigUnit_FitChainToSplineCurve.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.alignment"></a>

#### alignment

```python
@property
def alignment() -> ControlRigCurveAlignment
```

(ControlRigCurveAlignment):  [Read-Only] Specifies how to align the chain on the curve

<a id="unreal.RigUnit_FitChainToSplineCurve.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Only] The minimum U value to use on the curve

<a id="unreal.RigUnit_FitChainToSplineCurve.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Only] The maximum U value to use on the curve

<a id="unreal.RigUnit_FitChainToSplineCurve.sampling_precision"></a>

#### sampling_precision

```python
@property
def sampling_precision() -> int
```

(int32):  [Read-Only] The number of samples to use on the curve. Clamped at 64.

<a id="unreal.RigUnit_FitChainToSplineCurve.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write] The major axis being aligned - along the bone

<a id="unreal.RigUnit_FitChainToSplineCurve.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write] The minor axis being aligned - towards the pole vector.
You can use (0.0, 0.0, 0.0) to disable it.

<a id="unreal.RigUnit_FitChainToSplineCurve.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.pole_vector_position"></a>

#### pole_vector_position

```python
@property
def pole_vector_position() -> Vector
```

(Vector):  [Read-Write] The the position of the pole vector used for aligning the secondary axis.
Only has an effect if the secondary axis is set.

<a id="unreal.RigUnit_FitChainToSplineCurve.pole_vector_position"></a>

#### pole_vector_position

```python
@pole_vector_position.setter
def pole_vector_position(value: Vector) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.rotations"></a>

#### rotations

```python
@property
def rotations() -> Array[RigUnit_FitChainToCurve_Rotation]
```

(Array[RigUnit_FitChainToCurve_Rotation]):  [Read-Write] The list of rotations to be applied along the curve

<a id="unreal.RigUnit_FitChainToSplineCurve.rotations"></a>

#### rotations

```python
@rotations.setter
def rotations(value: Array[RigUnit_FitChainToCurve_Rotation]) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.rotation_ease_type"></a>

#### rotation_ease_type

```python
@property
def rotation_ease_type() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Only] The easing to use between to rotations.

<a id="unreal.RigUnit_FitChainToSplineCurve.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the solver - how much the rotation should be applied

<a id="unreal.RigUnit_FitChainToSplineCurve.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurve.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_FitChainToSplineCurve.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_FitChainToCurve_DebugSettings
```

(RigUnit_FitChainToCurve_DebugSettings):  [Read-Write]

<a id="unreal.RigUnit_FitChainToSplineCurve.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_FitChainToCurve_DebugSettings) -> None
```

<a id="unreal.RigUnit_FitChainToSplineCurveItemArray"></a>