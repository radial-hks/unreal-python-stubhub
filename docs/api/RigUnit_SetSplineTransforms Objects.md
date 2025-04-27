## RigUnit_SetSplineTransforms Objects

```python
class RigUnit_SetSplineTransforms(RigUnitMutable)
```

* Set the points of a spline, given a spline and an array of positions

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``transforms`` (Array[Transform]):  [Read-Write]

<a id="unreal.RigUnit_SetSplineTransforms.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             transforms: Array[Transform] = [],
             spline: ControlRigSpline = []) -> None
```

<a id="unreal.RigUnit_SetSplineTransforms.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write]

<a id="unreal.RigUnit_SetSplineTransforms.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.RigUnit_SetSplineTransforms.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_SetSplineTransforms.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_PositionFromControlRigSpline"></a>