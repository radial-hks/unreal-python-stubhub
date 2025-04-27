## GeometryScriptConvexHullApproximationOptions Objects

```python
class GeometryScriptConvexHullApproximationOptions(StructBase)
```

Geometry Script Convex Hull Approximation Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_threshold`` (float):  [Read-Write] Approximating shape should be at least this close to the original shape
- ``fit_boxes`` (bool):  [Read-Write] Whether to attempt to replace convex hulls with boxes
- ``fit_spheres`` (bool):  [Read-Write] Whether to attempt to replace convex hulls with spheres
- ``volume_diff_threshold_fraction`` (float):  [Read-Write] Acceptable difference between approximating shape volume and convex hull volume, as a fraction of convex hull volume

<a id="unreal.GeometryScriptConvexHullApproximationOptions.__init__"></a>

#### __init__

```python
def __init__(fit_spheres: bool = False,
             fit_boxes: bool = False,
             distance_threshold: float = 0.000000,
             volume_diff_threshold_fraction: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptConvexHullApproximationOptions.fit_spheres"></a>

#### fit_spheres

```python
@property
def fit_spheres() -> bool
```

(bool):  [Read-Write] Whether to attempt to replace convex hulls with spheres

<a id="unreal.GeometryScriptConvexHullApproximationOptions.fit_spheres"></a>

#### fit_spheres

```python
@fit_spheres.setter
def fit_spheres(value: bool) -> None
```

<a id="unreal.GeometryScriptConvexHullApproximationOptions.fit_boxes"></a>

#### fit_boxes

```python
@property
def fit_boxes() -> bool
```

(bool):  [Read-Write] Whether to attempt to replace convex hulls with boxes

<a id="unreal.GeometryScriptConvexHullApproximationOptions.fit_boxes"></a>

#### fit_boxes

```python
@fit_boxes.setter
def fit_boxes(value: bool) -> None
```

<a id="unreal.GeometryScriptConvexHullApproximationOptions.distance_threshold"></a>

#### distance_threshold

```python
@property
def distance_threshold() -> float
```

(float):  [Read-Write] Approximating shape should be at least this close to the original shape

<a id="unreal.GeometryScriptConvexHullApproximationOptions.distance_threshold"></a>

#### distance_threshold

```python
@distance_threshold.setter
def distance_threshold(value: float) -> None
```

<a id="unreal.GeometryScriptConvexHullApproximationOptions.volume_diff_threshold_fraction"></a>

#### volume_diff_threshold_fraction

```python
@property
def volume_diff_threshold_fraction() -> float
```

(float):  [Read-Write] Acceptable difference between approximating shape volume and convex hull volume, as a fraction of convex hull volume

<a id="unreal.GeometryScriptConvexHullApproximationOptions.volume_diff_threshold_fraction"></a>

#### volume_diff_threshold_fraction

```python
@volume_diff_threshold_fraction.setter
def volume_diff_threshold_fraction(value: float) -> None
```

<a id="unreal.GeometryScriptTransformCollisionOptions"></a>