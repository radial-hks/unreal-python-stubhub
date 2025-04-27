## GeometryScriptSimpleCollisionTriangulationOptions Objects

```python
class GeometryScriptSimpleCollisionTriangulationOptions(StructBase)
```

Settings to control the triangulation of simple collision primitives -- used for conversion to mesh or convex hull geometry

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``approximate_level_sets_with_cubes`` (bool):  [Read-Write] Whether to cheaply approximate level sets with cubes. Otherwise, will use marching cubes.
- ``capsule_circle_steps`` (int32):  [Read-Write] When triangulating a capsule, number of vertices to use for the circular cross-sections
- ``capsule_hemisphere_steps`` (int32):  [Read-Write] When triangulating a capsule's spherical endcaps, number of vertices to use on the arcs across the endcaps.
- ``sphere_steps_per_side`` (int32):  [Read-Write] When triangulating a sphere by deforming a cube to the sphere, number of vertices to use along each edge of the cube

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.__init__"></a>

#### __init__

```python
def __init__(sphere_steps_per_side: int = 0,
             capsule_hemisphere_steps: int = 0,
             capsule_circle_steps: int = 0,
             approximate_level_sets_with_cubes: bool = False) -> None
```

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.sphere_steps_per_side"></a>

#### sphere_steps_per_side

```python
@property
def sphere_steps_per_side() -> int
```

(int32):  [Read-Write] When triangulating a sphere by deforming a cube to the sphere, number of vertices to use along each edge of the cube

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.sphere_steps_per_side"></a>

#### sphere_steps_per_side

```python
@sphere_steps_per_side.setter
def sphere_steps_per_side(value: int) -> None
```

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_hemisphere_steps"></a>

#### capsule_hemisphere_steps

```python
@property
def capsule_hemisphere_steps() -> int
```

(int32):  [Read-Write] When triangulating a capsule's spherical endcaps, number of vertices to use on the arcs across the endcaps.

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_hemisphere_steps"></a>

#### capsule_hemisphere_steps

```python
@capsule_hemisphere_steps.setter
def capsule_hemisphere_steps(value: int) -> None
```

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_circle_steps"></a>

#### capsule_circle_steps

```python
@property
def capsule_circle_steps() -> int
```

(int32):  [Read-Write] When triangulating a capsule, number of vertices to use for the circular cross-sections

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.capsule_circle_steps"></a>

#### capsule_circle_steps

```python
@capsule_circle_steps.setter
def capsule_circle_steps(value: int) -> None
```

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.approximate_level_sets_with_cubes"></a>

#### approximate_level_sets_with_cubes

```python
@property
def approximate_level_sets_with_cubes() -> bool
```

(bool):  [Read-Write] Whether to cheaply approximate level sets with cubes. Otherwise, will use marching cubes.

<a id="unreal.GeometryScriptSimpleCollisionTriangulationOptions.approximate_level_sets_with_cubes"></a>

#### approximate_level_sets_with_cubes

```python
@approximate_level_sets_with_cubes.setter
def approximate_level_sets_with_cubes(value: bool) -> None
```

<a id="unreal.GeometryScriptTriangle"></a>