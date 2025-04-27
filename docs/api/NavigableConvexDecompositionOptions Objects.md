## NavigableConvexDecompositionOptions Objects

```python
class NavigableConvexDecompositionOptions(StructBase)
```

Settings to define the important regions for a convex decomposition to preserve for a given input shape.

Note: this is similar to FComputeNegativeSpaceOptions, but with better default behavior and more intuitive parameters.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_navigable_positions`` (Array[Vector]):  [Read-Write] Optional list of locations that we expect to be navigable
- ``ignore_unreachable_internal_space`` (bool):  [Read-Write] Whether to only consider navigable space that is accessible from outside the shape. (Note this parameter is called bOnlyConnectedToHull elsewhere.)
- ``min_radius`` (double):  [Read-Write] Minimum radius of characters/manipulators that should be able to navigate an input shape
- ``tolerance`` (double):  [Read-Write] Tolerance distance: convex decomposition should be no further than this from an input shape, in the navigable regions
- ``unreachable_planes`` (Array[Plane]):  [Read-Write] Optional list of planes defining unreachable space (on their negative side)
  Use this for example to specify a ground plane, if a mesh will always be placed on ground and need not be navigable from below.

<a id="unreal.NavigableConvexDecompositionOptions.__init__"></a>

#### __init__

```python
def __init__(min_radius: float = 0.000000,
             tolerance: float = 0.000000,
             ignore_unreachable_internal_space: bool = False,
             custom_navigable_positions: Array[Vector] = [],
             unreachable_planes: Array[Plane] = []) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions.min_radius"></a>

#### min_radius

```python
@property
def min_radius() -> float
```

(double):  [Read-Write] Minimum radius of characters/manipulators that should be able to navigate an input shape

<a id="unreal.NavigableConvexDecompositionOptions.min_radius"></a>

#### min_radius

```python
@min_radius.setter
def min_radius(value: float) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(double):  [Read-Write] Tolerance distance: convex decomposition should be no further than this from an input shape, in the navigable regions

<a id="unreal.NavigableConvexDecompositionOptions.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions.ignore_unreachable_internal_space"></a>

#### ignore_unreachable_internal_space

```python
@property
def ignore_unreachable_internal_space() -> bool
```

(bool):  [Read-Write] Whether to only consider navigable space that is accessible from outside the shape. (Note this parameter is called bOnlyConnectedToHull elsewhere.)

<a id="unreal.NavigableConvexDecompositionOptions.ignore_unreachable_internal_space"></a>

#### ignore_unreachable_internal_space

```python
@ignore_unreachable_internal_space.setter
def ignore_unreachable_internal_space(value: bool) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions.custom_navigable_positions"></a>

#### custom_navigable_positions

```python
@property
def custom_navigable_positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] Optional list of locations that we expect to be navigable

<a id="unreal.NavigableConvexDecompositionOptions.custom_navigable_positions"></a>

#### custom_navigable_positions

```python
@custom_navigable_positions.setter
def custom_navigable_positions(value: Array[Vector]) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions.unreachable_planes"></a>

#### unreachable_planes

```python
@property
def unreachable_planes() -> Array[Plane]
```

(Array[Plane]):  [Read-Write] Optional list of planes defining unreachable space (on their negative side)
Use this for example to specify a ground plane, if a mesh will always be placed on ground and need not be navigable from below.

<a id="unreal.NavigableConvexDecompositionOptions.unreachable_planes"></a>

#### unreachable_planes

```python
@unreachable_planes.setter
def unreachable_planes(value: Array[Plane]) -> None
```

<a id="unreal.GeometryScriptMergeSimpleCollisionOptions"></a>