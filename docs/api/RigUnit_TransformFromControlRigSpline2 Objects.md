## RigUnit_TransformFromControlRigSpline2 Objects

```python
class RigUnit_TransformFromControlRigSpline2(RigUnit_ControlRigSplineBase)
```

* Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``primary_axis`` (Vector):  [Read-Write]
- ``secondary_axis`` (Vector):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``u`` (float):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline2.__init__"></a>

#### __init__

```python
def __init__(
    spline: ControlRigSpline = [],
    u: float = 0.000000,
    primary_axis: Vector = [0.000000, 0.000000, 0.000000],
    secondary_axis: Vector = [0.000000, 0.000000, 0.000000],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline2.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline2.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline2.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline2.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline2.primary_axis"></a>

#### primary_axis

```python
@property
def primary_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline2.primary_axis"></a>

#### primary_axis

```python
@primary_axis.setter
def primary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline2.secondary_axis"></a>

#### secondary_axis

```python
@property
def secondary_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_TransformFromControlRigSpline2.secondary_axis"></a>

#### secondary_axis

```python
@secondary_axis.setter
def secondary_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_TransformFromControlRigSpline2.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_TangentFromControlRigSpline"></a>