## RigVMFunction_MathRayIntersectPlane Objects

```python
class RigVMFunction_MathRayIntersectPlane(RigVMFunction_MathRayBase)
```

Returns the closest point intersection of a ray with a plane

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathRay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance`` (float):  [Read-Write]
- ``plane_normal`` (Vector):  [Read-Write]
- ``plane_point`` (Vector):  [Read-Write]
- ``ratio`` (float):  [Read-Write]
- ``ray`` (Ray):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.__init__"></a>

#### __init__

```python
def __init__(ray: Ray = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000]],
             plane_point: Vector = [0.000000, 0.000000, 0.000000],
             plane_normal: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000],
             distance: float = 0.000000,
             ratio: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectPlane.ray"></a>

#### ray

```python
@property
def ray() -> Ray
```

(Ray):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.ray"></a>

#### ray

```python
@ray.setter
def ray(value: Ray) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectPlane.plane_point"></a>

#### plane_point

```python
@property
def plane_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.plane_point"></a>

#### plane_point

```python
@plane_point.setter
def plane_point(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectPlane.plane_normal"></a>

#### plane_normal

```python
@property
def plane_normal() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.plane_normal"></a>

#### plane_normal

```python
@plane_normal.setter
def plane_normal(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathRayIntersectPlane.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayIntersectPlane.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathRayGetAt"></a>