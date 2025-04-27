## ComputeNegativeSpaceOptions Objects

```python
class ComputeNegativeSpaceOptions(StructBase)
```

Options controlling how to sample the negative space of shapes, e.g. to define a region that must be avoided when merging collision shapes

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_voxels_per_dim`` (int32):  [Read-Write] When performing Voxel Search, maximum number of voxels to use along each dimension
- ``min_radius`` (double):  [Read-Write] Spheres smaller than this are not included in the negative space
- ``min_sample_spacing`` (double):  [Read-Write] Minimum desired spacing between sphere centers; if > 0, will attempt not to place sphere centers closer than this
- ``negative_space_tolerance`` (double):  [Read-Write] Amount of space to leave between convex hulls and protected negative space
- ``only_connected_to_hull`` (bool):  [Read-Write] When performing Voxel Search, only look for negative space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. Only applies to Voxel Search.
- ``require_search_sample_coverage`` (bool):  [Read-Write] Whether to require that all candidate locations identified by Voxel Search are covered by negative space samples, up to the specified Min Sample Spacing. Only applies to Voxel Search.
- ``sample_method`` (NegativeSpaceSampleMethod):  [Read-Write] Method to use to find and sample negative space
- ``target_num_samples`` (int32):  [Read-Write] Approximate number of spheres to consider when covering negative space

<a id="unreal.ComputeNegativeSpaceOptions.__init__"></a>

#### __init__

```python
def __init__(
        sample_method: NegativeSpaceSampleMethod = NegativeSpaceSampleMethod.
    UNIFORM,
        require_search_sample_coverage: bool = False,
        only_connected_to_hull: bool = False,
        max_voxels_per_dim: int = 0,
        target_num_samples: int = 0,
        min_sample_spacing: float = 0.000000,
        negative_space_tolerance: float = 0.000000,
        min_radius: float = 0.000000) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.sample_method"></a>

#### sample_method

```python
@property
def sample_method() -> NegativeSpaceSampleMethod
```

(NegativeSpaceSampleMethod):  [Read-Write] Method to use to find and sample negative space

<a id="unreal.ComputeNegativeSpaceOptions.sample_method"></a>

#### sample_method

```python
@sample_method.setter
def sample_method(value: NegativeSpaceSampleMethod) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.require_search_sample_coverage"></a>

#### require_search_sample_coverage

```python
@property
def require_search_sample_coverage() -> bool
```

(bool):  [Read-Write] Whether to require that all candidate locations identified by Voxel Search are covered by negative space samples, up to the specified Min Sample Spacing. Only applies to Voxel Search.

<a id="unreal.ComputeNegativeSpaceOptions.require_search_sample_coverage"></a>

#### require_search_sample_coverage

```python
@require_search_sample_coverage.setter
def require_search_sample_coverage(value: bool) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.only_connected_to_hull"></a>

#### only_connected_to_hull

```python
@property
def only_connected_to_hull() -> bool
```

(bool):  [Read-Write] When performing Voxel Search, only look for negative space that is connected out to the convex hull. This removes inaccessable internal negative space from consideration. Only applies to Voxel Search.

<a id="unreal.ComputeNegativeSpaceOptions.only_connected_to_hull"></a>

#### only_connected_to_hull

```python
@only_connected_to_hull.setter
def only_connected_to_hull(value: bool) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.max_voxels_per_dim"></a>

#### max_voxels_per_dim

```python
@property
def max_voxels_per_dim() -> int
```

(int32):  [Read-Write] When performing Voxel Search, maximum number of voxels to use along each dimension

<a id="unreal.ComputeNegativeSpaceOptions.max_voxels_per_dim"></a>

#### max_voxels_per_dim

```python
@max_voxels_per_dim.setter
def max_voxels_per_dim(value: int) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.target_num_samples"></a>

#### target_num_samples

```python
@property
def target_num_samples() -> int
```

(int32):  [Read-Write] Approximate number of spheres to consider when covering negative space

<a id="unreal.ComputeNegativeSpaceOptions.target_num_samples"></a>

#### target_num_samples

```python
@target_num_samples.setter
def target_num_samples(value: int) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.min_sample_spacing"></a>

#### min_sample_spacing

```python
@property
def min_sample_spacing() -> float
```

(double):  [Read-Write] Minimum desired spacing between sphere centers; if > 0, will attempt not to place sphere centers closer than this

<a id="unreal.ComputeNegativeSpaceOptions.min_sample_spacing"></a>

#### min_sample_spacing

```python
@min_sample_spacing.setter
def min_sample_spacing(value: float) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.negative_space_tolerance"></a>

#### negative_space_tolerance

```python
@property
def negative_space_tolerance() -> float
```

(double):  [Read-Write] Amount of space to leave between convex hulls and protected negative space

<a id="unreal.ComputeNegativeSpaceOptions.negative_space_tolerance"></a>

#### negative_space_tolerance

```python
@negative_space_tolerance.setter
def negative_space_tolerance(value: float) -> None
```

<a id="unreal.ComputeNegativeSpaceOptions.min_radius"></a>

#### min_radius

```python
@property
def min_radius() -> float
```

(double):  [Read-Write] Spheres smaller than this are not included in the negative space

<a id="unreal.ComputeNegativeSpaceOptions.min_radius"></a>

#### min_radius

```python
@min_radius.setter
def min_radius(value: float) -> None
```

<a id="unreal.NavigableConvexDecompositionOptions"></a>