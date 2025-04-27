## RigVMFunction_MathDistanceToPlane Objects

```python
class RigVMFunction_MathDistanceToPlane(RigVMFunction_MathVectorBase)
```

Find the point on the plane that is closest to the given point and the distance between them.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closest_point_on_plane`` (Vector):  [Read-Write]
- ``plane_normal`` (Vector):  [Read-Write]
- ``plane_point`` (Vector):  [Read-Write]
- ``point`` (Vector):  [Read-Write]
- ``signed_distance`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_MathDistanceToPlane.__init__"></a>

#### __init__

```python
def __init__(point: Vector = [0.000000, 0.000000, 0.000000],
             plane_point: Vector = [0.000000, 0.000000, 0.000000],
             plane_normal: Vector = [0.000000, 0.000000, 0.000000],
             closest_point_on_plane: Vector = [0.000000, 0.000000, 0.000000],
             signed_distance: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathDistanceToPlane.point"></a>

#### point

```python
@property
def point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathDistanceToPlane.point"></a>

#### point

```python
@point.setter
def point(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathDistanceToPlane.plane_point"></a>

#### plane_point

```python
@property
def plane_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathDistanceToPlane.plane_point"></a>

#### plane_point

```python
@plane_point.setter
def plane_point(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathDistanceToPlane.plane_normal"></a>

#### plane_normal

```python
@property
def plane_normal() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathDistanceToPlane.plane_normal"></a>

#### plane_normal

```python
@plane_normal.setter
def plane_normal(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathDistanceToPlane.closest_point_on_plane"></a>

#### closest_point_on_plane

```python
@property
def closest_point_on_plane() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathDistanceToPlane.signed_distance"></a>

#### signed_distance

```python
@property
def signed_distance() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathDistanceToPlane"></a>