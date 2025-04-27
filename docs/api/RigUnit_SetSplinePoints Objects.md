## RigUnit_SetSplinePoints Objects

```python
class RigUnit_SetSplinePoints(RigUnitMutable)
```

* Set the points of a spline, given a spline and an array of positions

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``points`` (Array[Vector]):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_SetSplinePoints.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             points: Array[Vector] = [],
             spline: ControlRigSpline = []) -> None
```

<a id="unreal.RigUnit_SetSplinePoints.points"></a>

#### points

```python
@property
def points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigUnit_SetSplinePoints.points"></a>

#### points

```python
@points.setter
def points(value: Array[Vector]) -> None
```

<a id="unreal.RigUnit_SetSplinePoints.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_SetSplinePoints.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_SetSplineTransforms"></a>