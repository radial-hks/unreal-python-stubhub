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

#### \_\_init\_\_

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

#### emit\_transaction

```python
@property
def emit_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.emit_transaction"></a>

#### emit\_transaction

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

#### auto\_detect\_spheres

```python
@property
def auto_detect_spheres() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_spheres"></a>

#### auto\_detect\_spheres

```python
@auto_detect_spheres.setter
def auto_detect_spheres(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_boxes"></a>

#### auto\_detect\_boxes

```python
@property
def auto_detect_boxes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_boxes"></a>

#### auto\_detect\_boxes

```python
@auto_detect_boxes.setter
def auto_detect_boxes(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_capsules"></a>

#### auto\_detect\_capsules

```python
@property
def auto_detect_capsules() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.auto_detect_capsules"></a>

#### auto\_detect\_capsules

```python
@auto_detect_capsules.setter
def auto_detect_capsules(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.min_thickness"></a>

#### min\_thickness

```python
@property
def min_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.min_thickness"></a>

#### min\_thickness

```python
@min_thickness.setter
def min_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.simplify_hulls"></a>

#### simplify\_hulls

```python
@property
def simplify_hulls() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.simplify_hulls"></a>

#### simplify\_hulls

```python
@simplify_hulls.setter
def simplify_hulls(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_hull_target_face_count"></a>

#### convex\_hull\_target\_face\_count

```python
@property
def convex_hull_target_face_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_hull_target_face_count"></a>

#### convex\_hull\_target\_face\_count

```python
@convex_hull_target_face_count.setter
def convex_hull_target_face_count(value: int) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_convex_hulls_per_mesh"></a>

#### max\_convex\_hulls\_per\_mesh

```python
@property
def max_convex_hulls_per_mesh() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_convex_hulls_per_mesh"></a>

#### max\_convex\_hulls\_per\_mesh

```python
@max_convex_hulls_per_mesh.setter
def max_convex_hulls_per_mesh(value: int) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_search_factor"></a>

#### convex\_decomposition\_search\_factor

```python
@property
def convex_decomposition_search_factor() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_search_factor"></a>

#### convex\_decomposition\_search\_factor

```python
@convex_decomposition_search_factor.setter
def convex_decomposition_search_factor(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_error_tolerance"></a>

#### convex\_decomposition\_error\_tolerance

```python
@property
def convex_decomposition_error_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_error_tolerance"></a>

#### convex\_decomposition\_error\_tolerance

```python
@convex_decomposition_error_tolerance.setter
def convex_decomposition_error_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_min_part_thickness"></a>

#### convex\_decomposition\_min\_part\_thickness

```python
@property
def convex_decomposition_min_part_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.convex_decomposition_min_part_thickness"></a>

#### convex\_decomposition\_min\_part\_thickness

```python
@convex_decomposition_min_part_thickness.setter
def convex_decomposition_min_part_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_simplify_tolerance"></a>

#### swept\_hull\_simplify\_tolerance

```python
@property
def swept_hull_simplify_tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_simplify_tolerance"></a>

#### swept\_hull\_simplify\_tolerance

```python
@swept_hull_simplify_tolerance.setter
def swept_hull_simplify_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_axis"></a>

#### swept\_hull\_axis

```python
@property
def swept_hull_axis() -> GeometryScriptSweptHullAxis
```

(GeometryScriptSweptHullAxis):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.swept_hull_axis"></a>

#### swept\_hull\_axis

```python
@swept_hull_axis.setter
def swept_hull_axis(value: GeometryScriptSweptHullAxis) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.remove_fully_contained_shapes"></a>

#### remove\_fully\_contained\_shapes

```python
@property
def remove_fully_contained_shapes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.remove_fully_contained_shapes"></a>

#### remove\_fully\_contained\_shapes

```python
@remove_fully_contained_shapes.setter
def remove_fully_contained_shapes(value: bool) -> None
```

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_shape_count"></a>

#### max\_shape\_count

```python
@property
def max_shape_count() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptCollisionFromMeshOptions.max_shape_count"></a>

#### max\_shape\_count

```python
@max_shape_count.setter
def max_shape_count(value: int) -> None
```

<a id="unreal.GeometryScriptSetSimpleCollisionOptions"></a>