## GeometryScriptMergeSimpleCollisionOptions Objects

```python
class GeometryScriptMergeSimpleCollisionOptions(StructBase)
```

Options controlling how collision shapes can be merged together

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compute_negative_space`` (bool):  [Read-Write] Whether to compute a new sphere covering representing the negative space of the input shapes
- ``compute_negative_space_options`` (ComputeNegativeSpaceOptions):  [Read-Write] Options controlling how the negative space is computed, if ComputeNegativeSpace is true
- ``consider_all_possible_merges`` (bool):  [Read-Write] Whether to consider merges between every shape. If false, will only merge shapes that have overlapping or nearby bounding boxes.
- ``error_tolerance`` (double):  [Read-Write] Error tolerance to use to decide to convex hulls together, in cm.
  If merging two hulls would increase the volume by more than this ErrorTolerance cubed, the merge is not accepted.
- ``max_shape_count`` (int32):  [Read-Write] If > 0, merge down to at most this many simple shapes. (If <= 0, this value is ignored.)
- ``min_thickness_tolerance`` (double):  [Read-Write] Always attempt to merge parts thicker than this, ignoring ErrorTolerance and MaxShapeCount.
  Note: Negative space, if set, will still prevent merges.
- ``precomputed_negative_space`` (GeometryScriptSphereCovering):  [Read-Write] Negative space that must be preserved during merging
- ``shape_to_hull_triangulation`` (GeometryScriptSimpleCollisionTriangulationOptions):  [Read-Write] Controls for how smooth shapes can be triangulated when/if converted to a convex hull for a merge

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.__init__"></a>

#### __init__

```python
def __init__(
    max_shape_count: int = 0,
    error_tolerance: float = 0.000000,
    min_thickness_tolerance: float = 0.000000,
    consider_all_possible_merges: bool = False,
    precomputed_negative_space: GeometryScriptSphereCovering = [],
    compute_negative_space: bool = False,
    compute_negative_space_options: ComputeNegativeSpaceOptions = [
        NegativeSpaceSampleMethod.UNIFORM, False, False, 128, 50, 1.000000,
        2.000000, 10.000000
    ],
    shape_to_hull_triangulation:
    GeometryScriptSimpleCollisionTriangulationOptions = [4, 5, 8, False]
) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.max_shape_count"></a>

#### max_shape_count

```python
@property
def max_shape_count() -> int
```

(int32):  [Read-Write] If > 0, merge down to at most this many simple shapes. (If <= 0, this value is ignored.)

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.max_shape_count"></a>

#### max_shape_count

```python
@max_shape_count.setter
def max_shape_count(value: int) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.error_tolerance"></a>

#### error_tolerance

```python
@property
def error_tolerance() -> float
```

(double):  [Read-Write] Error tolerance to use to decide to convex hulls together, in cm.
If merging two hulls would increase the volume by more than this ErrorTolerance cubed, the merge is not accepted.

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.error_tolerance"></a>

#### error_tolerance

```python
@error_tolerance.setter
def error_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.min_thickness_tolerance"></a>

#### min_thickness_tolerance

```python
@property
def min_thickness_tolerance() -> float
```

(double):  [Read-Write] Always attempt to merge parts thicker than this, ignoring ErrorTolerance and MaxShapeCount.
Note: Negative space, if set, will still prevent merges.

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.min_thickness_tolerance"></a>

#### min_thickness_tolerance

```python
@min_thickness_tolerance.setter
def min_thickness_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.consider_all_possible_merges"></a>

#### consider_all_possible_merges

```python
@property
def consider_all_possible_merges() -> bool
```

(bool):  [Read-Write] Whether to consider merges between every shape. If false, will only merge shapes that have overlapping or nearby bounding boxes.

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.consider_all_possible_merges"></a>

#### consider_all_possible_merges

```python
@consider_all_possible_merges.setter
def consider_all_possible_merges(value: bool) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.precomputed_negative_space"></a>

#### precomputed_negative_space

```python
@property
def precomputed_negative_space() -> GeometryScriptSphereCovering
```

(GeometryScriptSphereCovering):  [Read-Write] Negative space that must be preserved during merging

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.precomputed_negative_space"></a>

#### precomputed_negative_space

```python
@precomputed_negative_space.setter
def precomputed_negative_space(value: GeometryScriptSphereCovering) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space"></a>

#### compute_negative_space

```python
@property
def compute_negative_space() -> bool
```

(bool):  [Read-Write] Whether to compute a new sphere covering representing the negative space of the input shapes

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space"></a>

#### compute_negative_space

```python
@compute_negative_space.setter
def compute_negative_space(value: bool) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space_options"></a>

#### compute_negative_space_options

```python
@property
def compute_negative_space_options() -> ComputeNegativeSpaceOptions
```

(ComputeNegativeSpaceOptions):  [Read-Write] Options controlling how the negative space is computed, if ComputeNegativeSpace is true

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.compute_negative_space_options"></a>

#### compute_negative_space_options

```python
@compute_negative_space_options.setter
def compute_negative_space_options(value: ComputeNegativeSpaceOptions) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.shape_to_hull_triangulation"></a>

#### shape_to_hull_triangulation

```python
@property
def shape_to_hull_triangulation(
) -> GeometryScriptSimpleCollisionTriangulationOptions
```

(GeometryScriptSimpleCollisionTriangulationOptions):  [Read-Write] Controls for how smooth shapes can be triangulated when/if converted to a convex hull for a merge

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions.shape_to_hull_triangulation"></a>

#### shape_to_hull_triangulation

```python
@shape_to_hull_triangulation.setter
def shape_to_hull_triangulation(
        value: GeometryScriptSimpleCollisionTriangulationOptions) -> None
```

<a id="unreal.GeometryScriptConvexHullSimplificationOptions"></a>