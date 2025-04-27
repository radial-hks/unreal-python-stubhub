## GeometryScriptConvexDecompositionOptions Objects

```python
class GeometryScriptConvexDecompositionOptions(StructBase)
```

Geometry Script Convex Decomposition Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ContainmentFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``error_tolerance`` (double):  [Read-Write] Error tolerance to guide convex decomposition (in cm); we stop adding new parts if the volume error is below the threshold.  For volumetric errors, value will be cubed.
- ``min_part_thickness`` (double):  [Read-Write] Minimum part thickness for convex decomposition (in cm); hulls thinner than this will be merged into adjacent hulls, if possible.
- ``num_hulls`` (int32):  [Read-Write] How many convex pieces to target per mesh when creating convex decompositions.  If ErrorTolerance is set, can create fewer pieces.
- ``search_factor`` (double):  [Read-Write] How much additional decomposition decomposition + merging to do, as a fraction of max pieces.  Larger values can help better-cover small features, while smaller values create a cleaner decomposition with less overlap between hulls.
- ``simplify_to_face_count`` (int32):  [Read-Write] Try to simplify each convex hull to this triangle count. If 0, no simplification

<a id="unreal.GeometryScriptConvexDecompositionOptions.__init__"></a>

#### __init__

```python
def __init__(num_hulls: int = 0,
             search_factor: float = 0.000000,
             error_tolerance: float = 0.000000,
             min_part_thickness: float = 0.000000,
             simplify_to_face_count: int = 0) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions.num_hulls"></a>

#### num_hulls

```python
@property
def num_hulls() -> int
```

(int32):  [Read-Write] How many convex pieces to target per mesh when creating convex decompositions.  If ErrorTolerance is set, can create fewer pieces.

<a id="unreal.GeometryScriptConvexDecompositionOptions.num_hulls"></a>

#### num_hulls

```python
@num_hulls.setter
def num_hulls(value: int) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions.search_factor"></a>

#### search_factor

```python
@property
def search_factor() -> float
```

(double):  [Read-Write] How much additional decomposition decomposition + merging to do, as a fraction of max pieces.  Larger values can help better-cover small features, while smaller values create a cleaner decomposition with less overlap between hulls.

<a id="unreal.GeometryScriptConvexDecompositionOptions.search_factor"></a>

#### search_factor

```python
@search_factor.setter
def search_factor(value: float) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions.error_tolerance"></a>

#### error_tolerance

```python
@property
def error_tolerance() -> float
```

(double):  [Read-Write] Error tolerance to guide convex decomposition (in cm); we stop adding new parts if the volume error is below the threshold.  For volumetric errors, value will be cubed.

<a id="unreal.GeometryScriptConvexDecompositionOptions.error_tolerance"></a>

#### error_tolerance

```python
@error_tolerance.setter
def error_tolerance(value: float) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions.min_part_thickness"></a>

#### min_part_thickness

```python
@property
def min_part_thickness() -> float
```

(double):  [Read-Write] Minimum part thickness for convex decomposition (in cm); hulls thinner than this will be merged into adjacent hulls, if possible.

<a id="unreal.GeometryScriptConvexDecompositionOptions.min_part_thickness"></a>

#### min_part_thickness

```python
@min_part_thickness.setter
def min_part_thickness(value: float) -> None
```

<a id="unreal.GeometryScriptConvexDecompositionOptions.simplify_to_face_count"></a>

#### simplify_to_face_count

```python
@property
def simplify_to_face_count() -> int
```

(int32):  [Read-Write] Try to simplify each convex hull to this triangle count. If 0, no simplification

<a id="unreal.GeometryScriptConvexDecompositionOptions.simplify_to_face_count"></a>

#### simplify_to_face_count

```python
@simplify_to_face_count.setter
def simplify_to_face_count(value: int) -> None
```

<a id="unreal.GeometryScriptMeshSelection"></a>