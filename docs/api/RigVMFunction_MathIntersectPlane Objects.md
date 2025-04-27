## RigVMFunction_MathIntersectPlane Objects

```python
class RigVMFunction_MathIntersectPlane(RigVMFunction_MathVectorBase)
```

Intersects a plane with a vector given a start and direction

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (Vector):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``plane_normal`` (Vector):  [Read-Write]
- ``plane_point`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``start`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntersectPlane.__init__"></a>

#### __init__

```python
def __init__(start: Vector = [0.000000, 0.000000, 0.000000],
             direction: Vector = [0.000000, 0.000000, 0.000000],
             plane_point: Vector = [0.000000, 0.000000, 0.000000],
             plane_normal: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000],
             distance: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathIntersectPlane.start"></a>

#### start

```python
@property
def start() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntersectPlane.start"></a>

#### start

```python
@start.setter
def start(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathIntersectPlane.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntersectPlane.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathIntersectPlane.plane_point"></a>

#### plane_point

```python
@property
def plane_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntersectPlane.plane_point"></a>

#### plane_point

```python
@plane_point.setter
def plane_point(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathIntersectPlane.plane_normal"></a>

#### plane_normal

```python
@property
def plane_normal() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathIntersectPlane.plane_normal"></a>

#### plane_normal

```python
@plane_normal.setter
def plane_normal(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathIntersectPlane.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathIntersectPlane.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_MathIntersectPlane"></a>