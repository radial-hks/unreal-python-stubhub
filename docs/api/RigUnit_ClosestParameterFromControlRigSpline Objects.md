## RigUnit_ClosestParameterFromControlRigSpline Objects

```python
class RigUnit_ClosestParameterFromControlRigSpline(RigUnit_ControlRigSplineBase
                                                   )
```

* Retrieves the closest U value from a given Spline and a position

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position`` (Vector):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [],
             position: Vector = [0.000000, 0.000000, 0.000000],
             u: float = 0.000000) -> None
```

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.RigUnit_ClosestParameterFromControlRigSpline.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_ParameterAtPercentage"></a>