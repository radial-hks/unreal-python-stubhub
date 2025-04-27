## RigUnit_TransformFromControlRigSpline Objects

```python
class RigUnit_TransformFromControlRigSpline(RigUnit_ControlRigSplineBase)
```

* Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``roll`` (float):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``u`` (float):  [Read-Write]
- ``up_vector`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(
    spline: ControlRigSpline = [],
    up_vector: Vector = [0.000000, 0.000000, 0.000000],
    roll: float = 0.000000,
    u: float = 0.000000,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline.up_vector"></a>

#### up_vector

```python
@property
def up_vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline.up_vector"></a>

#### up_vector

```python
@up_vector.setter
def up_vector(value: Vector) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline.roll"></a>

#### roll

```python
@property
def roll() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline.roll"></a>

#### roll

```python
@roll.setter
def roll(value: float) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_TransformFromControlRigSpline2"></a>