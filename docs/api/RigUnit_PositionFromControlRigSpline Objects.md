## RigUnit_PositionFromControlRigSpline Objects

```python
class RigUnit_PositionFromControlRigSpline(RigUnit_ControlRigSplineBase)
```

* Retrieves the position from a given Spline and U value

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position`` (Vector):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_PositionFromControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [],
             u: float = 0.000000,
             position: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_PositionFromControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_PositionFromControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_PositionFromControlRigSpline.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_PositionFromControlRigSpline.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.RigUnit_PositionFromControlRigSpline.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_TransformFromControlRigSpline"></a>