## GeometryScriptRayHitResult Objects

```python
class GeometryScriptRayHitResult(StructBase)
```

Geometry Script Ray Hit Result

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSpatialFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hit`` (bool):  [Read-Write]
- ``hit_bary_coords`` (Vector):  [Read-Write]
- ``hit_position`` (Vector):  [Read-Write]
- ``hit_triangle_id`` (int32):  [Read-Write]
- ``ray_parameter`` (float):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(hit: bool = False,
             ray_parameter: float = 0.000000,
             hit_triangle_id: int = 0,
             hit_position: Vector = [0.000000, 0.000000, 0.000000],
             hit_bary_coords: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GeometryScriptRayHitResult.hit"></a>

#### hit

```python
@property
def hit() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.hit"></a>

#### hit

```python
@hit.setter
def hit(value: bool) -> None
```

<a id="unreal.GeometryScriptRayHitResult.ray_parameter"></a>

#### ray\_parameter

```python
@property
def ray_parameter() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.ray_parameter"></a>

#### ray\_parameter

```python
@ray_parameter.setter
def ray_parameter(value: float) -> None
```

<a id="unreal.GeometryScriptRayHitResult.hit_triangle_id"></a>

#### hit\_triangle\_id

```python
@property
def hit_triangle_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.hit_triangle_id"></a>

#### hit\_triangle\_id

```python
@hit_triangle_id.setter
def hit_triangle_id(value: int) -> None
```

<a id="unreal.GeometryScriptRayHitResult.hit_position"></a>

#### hit\_position

```python
@property
def hit_position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.hit_position"></a>

#### hit\_position

```python
@hit_position.setter
def hit_position(value: Vector) -> None
```

<a id="unreal.GeometryScriptRayHitResult.hit_bary_coords"></a>

#### hit\_bary\_coords

```python
@property
def hit_bary_coords() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptRayHitResult.hit_bary_coords"></a>

#### hit\_bary\_coords

```python
@hit_bary_coords.setter
def hit_bary_coords(value: Vector) -> None
```

<a id="unreal.GeometryScriptPNTessellateOptions"></a>