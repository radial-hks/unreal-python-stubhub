## RigUnit_TangentFromControlRigSpline Objects

```python
class RigUnit_TangentFromControlRigSpline(RigUnit_ControlRigSplineBase)
```

* Retrieves the tangent from a given Spline and U value

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``spline`` (ControlRigSpline):  [Read-Write]
- ``tangent`` (Vector):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_TangentFromControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [],
             u: float = 0.000000,
             tangent: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_TangentFromControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_TangentFromControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_TangentFromControlRigSpline.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_TangentFromControlRigSpline.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.RigUnit_TangentFromControlRigSpline.tangent"></a>

#### tangent

```python
@property
def tangent() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_DrawControlRigSpline"></a>