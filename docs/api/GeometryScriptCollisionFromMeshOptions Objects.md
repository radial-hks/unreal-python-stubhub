## GeometryScriptCollisionFromMeshOptions Objects

```python
class GeometryScriptCollisionFromMeshOptions(StructBase)
```

Geometry Script Collision from Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_detect_boxes`` (bool):  [Read-Write]
- ``auto_detect_capsules`` (bool):  [Read-Write]
- ``auto_detect_spheres`` (bool):  [Read-Write]
- ``convex_decomposition_error_tolerance`` (float):  [Read-Write]
- ``convex_decomposition_min_part_thickness`` (float):  [Read-Write]
- ``convex_decomposition_search_factor`` (float):  [Read-Write]
- ``convex_hull_target_face_count`` (int32):  [Read-Write]
- ``emit_transaction`` (bool):  [Read-Write]
- ``max_convex_hulls_per_mesh`` (int32):  [Read-Write]
- ``max_shape_count`` (int32):  [Read-Write]
- ``method`` (GeometryScriptCollisionGenerationMethod):  [Read-Write]
- ``min_thickness`` (float):  [Read-Write]
- ``remove_fully_contained_shapes`` (bool):  [Read-Write]
- ``simplify_hulls`` (bool):  [Read-Write]
- ``swept_hull_axis`` (GeometryScriptSweptHullAxis):  [Read-Write]
- ``swept_hull_simplify_tolerance`` (float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.__init__"></a>

#### __init__

```python
def __init__(
        emit_transaction: bool = False,
        method:
    GeometryScriptCollisionGenerationMethod = GeometryScriptCollisionGenerationMethod
    .ALIGNED_BOXES,
        auto_detect_spheres: bool = False,
        auto_detect_boxes: bool = False,
        auto_detect_capsules: bool = False,
        min_thickness: float = 0.000000,
        simplify_hulls: bool = False,
        convex_hull_target_face_count: int = 0,
        max_convex_hulls_per_mesh: int = 0,
        convex_decomposition_search_factor: float = 0.000000,
        convex_decomposition_error_tolerance: float = 0.000000,
        convex_decomposition_min_part_thickness: float = 0.000000,
        swept_hull_simplify_tolerance: float = 0.000000,
        swept_hull_axis:
    GeometryScriptSweptHullAxis = GeometryScriptSweptHullAxis.X,
        remove_fully_contained_shapes: bool = False,
        max_shape_count: int = 0) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.emit_transaction"></a>

#### emit_transaction

```python
@property
def emit_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.emit_transaction"></a>

#### emit_transaction

```python
@emit_transaction.setter
def emit_transaction(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.method"></a>

#### method

```python
@property
def method() -> GeometryScriptCollisionGenerationMethod
```

(GeometryScriptCollisionGenerationMethod):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.method"></a>

#### method

```python
@method.setter
def method(value: GeometryScriptCollisionGenerationMethod) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_spheres"></a>

#### auto_detect_spheres

```python
@property
def auto_detect_spheres() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_spheres"></a>

#### auto_detect_spheres

```python
@auto_detect_spheres.setter
def auto_detect_spheres(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_boxes"></a>

#### auto_detect_boxes

```python
@property
def auto_detect_boxes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_boxes"></a>

#### auto_detect_boxes

```python
@auto_detect_boxes.setter
def auto_detect_boxes(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_capsules"></a>

#### auto_detect_capsules

```python
@property
def auto_detect_capsules() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_capsules"></a>

#### auto_detect_capsules

```python
@auto_detect_capsules.setter
def auto_detect_capsules(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.min_thickness"></a>

#### min_thickness

```python
@property
def min_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.min_thickness"></a>

#### min_thickness

```python
@min_thickness.setter
def min_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.simplify_hulls"></a>

#### simplify_hulls

```python
@property
def simplify_hulls() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.simplify_hulls"></a>

#### simplify_hulls

```python
@simplify_hulls.setter
def simplify_hulls(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_hull_target_face_count"></a>

#### convex_hull_target_face_count

```python
@property
def convex_hull_target_face_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_hull_target_face_count"></a>

#### convex_hull_target_face_count

```python
@convex_hull_target_face_count.setter
def convex_hull_target_face_count(value: int) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_convex_hulls_per_mesh"></a>

#### max_convex_hulls_per_mesh

```python
@property
def max_convex_hulls_per_mesh() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_convex_hulls_per_mesh"></a>

#### max_convex_hulls_per_mesh

```python
@max_convex_hulls_per_mesh.setter
def max_convex_hulls_per_mesh(value: int) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_search_factor"></a>

#### convex_decomposition_search_factor

```python
@property
def convex_decomposition_search_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_search_factor"></a>

#### convex_decomposition_search_factor

```python
@convex_decomposition_search_factor.setter
def convex_decomposition_search_factor(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_error_tolerance"></a>

#### convex_decomposition_error_tolerance

```python
@property
def convex_decomposition_error_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_error_tolerance"></a>

#### convex_decomposition_error_tolerance

```python
@convex_decomposition_error_tolerance.setter
def convex_decomposition_error_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_min_part_thickness"></a>

#### convex_decomposition_min_part_thickness

```python
@property
def convex_decomposition_min_part_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_min_part_thickness"></a>

#### convex_decomposition_min_part_thickness

```python
@convex_decomposition_min_part_thickness.setter
def convex_decomposition_min_part_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_simplify_tolerance"></a>

#### swept_hull_simplify_tolerance

```python
@property
def swept_hull_simplify_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_simplify_tolerance"></a>

#### swept_hull_simplify_tolerance

```python
@swept_hull_simplify_tolerance.setter
def swept_hull_simplify_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_axis"></a>

#### swept_hull_axis

```python
@property
def swept_hull_axis() -> GeometryScriptSweptHullAxis
```

(GeometryScriptSweptHullAxis):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_axis"></a>

#### swept_hull_axis

```python
@swept_hull_axis.setter
def swept_hull_axis(value: GeometryScriptSweptHullAxis) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.remove_fully_contained_shapes"></a>

#### remove_fully_contained_shapes

```python
@property
def remove_fully_contained_shapes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.remove_fully_contained_shapes"></a>

#### remove_fully_contained_shapes

```python
@remove_fully_contained_shapes.setter
def remove_fully_contained_shapes(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_shape_count"></a>

#### max_shape_count

```python
@property
def max_shape_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_shape_count"></a>

#### max_shape_count

```python
@max_shape_count.setter
def max_shape_count(value: int) -> None
```

<a id="unreal.GeometryScriptSetSimpleCollisionOptions"></a>