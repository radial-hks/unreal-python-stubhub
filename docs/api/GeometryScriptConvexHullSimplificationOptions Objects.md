## GeometryScriptConvexHullSimplificationOptions Objects

```python
class GeometryScriptConvexHullSimplificationOptions(StructBase)
```

Geometry Script Convex Hull Simplification Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``min_target_face_count`` (int32):  [Read-Write] The minimum number of faces to use for the convex hull.
  Note that for the MeshQSlim method all faces are triangles, while the AngleTolerance method can consider more general polygons.
- ``simplification_angle_threshold`` (float):  [Read-Write] Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method.
- ``simplification_distance_threshold`` (float):  [Read-Write] Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method.
- ``simplification_method`` (GeometryScriptConvexHullSimplifyMethod):  [Read-Write] Method to use to simplify convex hulls

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.__init__"></a>

#### __init__

```python
def __init__(
        simplification_method:
    GeometryScriptConvexHullSimplifyMethod = GeometryScriptConvexHullSimplifyMethod
    .MESH_Q_SLIM,
        simplification_distance_threshold: float = 0.000000,
        simplification_angle_threshold: float = 0.000000,
        min_target_face_count: int = 0) -> None
```

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_method"></a>

#### simplification_method

```python
@property
def simplification_method() -> GeometryScriptConvexHullSimplifyMethod
```

(GeometryScriptConvexHullSimplifyMethod):  [Read-Write] Method to use to simplify convex hulls

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_method"></a>

#### simplification_method

```python
@simplification_method.setter
def simplification_method(
        value: GeometryScriptConvexHullSimplifyMethod) -> None
```

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_distance_threshold"></a>

#### simplification_distance_threshold

```python
@property
def simplification_distance_threshold() -> float
```

(float):  [Read-Write] Simplified hull should stay within this distance of the initial convex hull. Used by the MeshQSlim simplification method.

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_distance_threshold"></a>

#### simplification_distance_threshold

```python
@simplification_distance_threshold.setter
def simplification_distance_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_angle_threshold"></a>

#### simplification_angle_threshold

```python
@property
def simplification_angle_threshold() -> float
```

(float):  [Read-Write] Simplified hull should preserve angles larger than this (in degrees). Used by the AngleTolerance simplification method.

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.simplification_angle_threshold"></a>

#### simplification_angle_threshold

```python
@simplification_angle_threshold.setter
def simplification_angle_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.min_target_face_count"></a>

#### min_target_face_count

```python
@property
def min_target_face_count() -> int
```

(int32):  [Read-Write] The minimum number of faces to use for the convex hull.
Note that for the MeshQSlim method all faces are triangles, while the AngleTolerance method can consider more general polygons.

<a id="unreal.GeometryScriptConvexHullSimplificationOptions.min_target_face_count"></a>

#### min_target_face_count

```python
@min_target_face_count.setter
def min_target_face_count(value: int) -> None
```

<a id="unreal.GeometryScriptConvexHullApproximationOptions"></a>