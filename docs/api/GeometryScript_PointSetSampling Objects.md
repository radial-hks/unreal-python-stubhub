## GeometryScript_PointSetSampling Objects

```python
class GeometryScript_PointSetSampling(BlueprintFunctionLibrary)
```

Geometry Script Library Point Set Sampling Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PointSetFunctions.h

<a id="unreal.GeometryScript_PointSetSampling.unflatten_points"></a>

#### unflatten_points

```python
@classmethod
def unflatten_points(cls,
                     points_in2d: Array[Vector2D],
                     options: GeometryScriptPointFlatteningOptions,
                     height: float = 0.000000) -> Array[Vector]
```

X.unflatten_points(points_in2d, options, height=0.000000) -> Array[Vector]
Convert an array of points from 2D to 3D, by transforming out of the given ReferenceFrame, with the given Height for the non-flat axis (default Z).

Args:
    points_in2d (Array[Vector2D]): 
    options (GeometryScriptPointFlatteningOptions): 
    height (double): 

Returns:
    Array[Vector]: 

    points_in3d (Array[Vector]):

<a id="unreal.GeometryScript_PointSetSampling.transforms_to_points"></a>

#### transforms_to_points

```python
@classmethod
def transforms_to_points(cls, transforms: Array[Transform]) -> Array[Vector]
```

X.transforms_to_points(transforms) -> Array[Vector]
Create an array of the positions of the input Transforms

Args:
    transforms (Array[Transform]): 

Returns:
    Array[Vector]: 

    points (Array[Vector]):

<a id="unreal.GeometryScript_PointSetSampling.offset_transforms"></a>

#### offset_transforms

```python
@classmethod
def offset_transforms(
    cls,
    transforms: Array[Transform],
    offset: float,
    direction: Vector = [0.000000, 0.000000, 1.000000],
    space: GeometryScriptCoordinateSpace = GeometryScriptCoordinateSpace.LOCAL
) -> Array[Transform]
```

X.offset_transforms(transforms, offset, direction=[0.000000, 0.000000, 1.000000], space=GeometryScriptCoordinateSpace.LOCAL) -> Array[Transform]
Offset the location of all Transforms by Offset in the given Direction, either locally in the space of the transform or in world space.
For example, this can offset mesh surface samples along the surface normal direction.

Args:
    transforms (Array[Transform]): 
    offset (double): 
    direction (Vector): 
    space (GeometryScriptCoordinateSpace): 

Returns:
    Array[Transform]: 

    transforms (Array[Transform]):

<a id="unreal.GeometryScript_PointSetSampling.make_bounding_box_from_points"></a>

#### make_bounding_box_from_points

```python
@classmethod
def make_bounding_box_from_points(cls,
                                  points: Array[Vector],
                                  expand_by: float = 0.000000) -> Box
```

X.make_bounding_box_from_points(points, expand_by=0.000000) -> Box
Make a Axis Aligned Bounding Box that bounds the given Points, optionally expanded by some additional amount on each side

Args:
    points (Array[Vector]): 
    expand_by (double): 

Returns:
    Box:

<a id="unreal.GeometryScript_PointSetSampling.k_means_cluster_to_i_ds"></a>

#### k_means_cluster_to_i_ds

```python
@classmethod
def k_means_cluster_to_i_ds(
        cls, points: Array[Vector],
        options: GeometryScriptPointClusteringOptions) -> Array[int]
```

X.k_means_cluster_to_i_ds(points, options) -> Array[int32]
Use K-Means clustering to cluster the given points into a target number of clusters,
and return an array with a cluster index per point.

Args:
    points (Array[Vector]): 
    options (GeometryScriptPointClusteringOptions): 

Returns:
    Array[int32]: 

    point_cluster_indices (Array[int32]):

<a id="unreal.GeometryScript_PointSetSampling.k_means_cluster_to_arrays"></a>

#### k_means_cluster_to_arrays

```python
@classmethod
def k_means_cluster_to_arrays(
    cls, points: Array[Vector], options: GeometryScriptPointClusteringOptions
) -> Array[GeometryScriptIndexList]
```

X.k_means_cluster_to_arrays(points, options) -> Array[GeometryScriptIndexList]
Use K-Means clustering to cluster the given points into a target number of clusters,
and return the clusters as an array of lists of point indices.

Args:
    points (Array[Vector]): 
    options (GeometryScriptPointClusteringOptions): 

Returns:
    Array[GeometryScriptIndexList]: 

    cluster_id_to_lists (Array[GeometryScriptIndexList]):

<a id="unreal.GeometryScript_PointSetSampling.get_points_from_index_list"></a>

#### get_points_from_index_list

```python
@classmethod
def get_points_from_index_list(
        cls, all_points: Array[Vector],
        indices: GeometryScriptIndexList) -> Array[Vector]
```

X.get_points_from_index_list(all_points, indices) -> Array[Vector]
Create an array of the subset of AllPoints indicated by the Indices list

Args:
    all_points (Array[Vector]): 
    indices (GeometryScriptIndexList): 

Returns:
    Array[Vector]: 

    selected_points (Array[Vector]):

<a id="unreal.GeometryScript_PointSetSampling.flatten_points"></a>

#### flatten_points

```python
@classmethod
def flatten_points(
        cls, points_in3d: Array[Vector],
        options: GeometryScriptPointFlatteningOptions) -> Array[Vector2D]
```

X.flatten_points(points_in3d, options) -> Array[Vector2D]
Convert an array of points from 3D to 2D, by transforming into the given ReferenceFrame and taking the X,Y coordinates
Note that to transform into the ReferenceFrame, we apply the inverse of the ReferenceFrame's transform.

Args:
    points_in3d (Array[Vector]): 
    options (GeometryScriptPointFlatteningOptions): 

Returns:
    Array[Vector2D]: 

    points_in2d (Array[Vector2D]):

<a id="unreal.GeometryScript_PointSetSampling.downsample_points"></a>

#### downsample_points

```python
@classmethod
def downsample_points(
        cls,
        points: Array[Vector],
        options: GeometryScriptPointPriorityOptions,
        keep_num_points: int = 100,
        debug: GeometryScriptDebug = None) -> GeometryScriptIndexList
```

X.downsample_points(points, options, keep_num_points=100, debug=None) -> GeometryScriptIndexList
Find a subset of the given Points of a specified size.
Can optionally specify a priorty weighting and/or request uniform spacing for the downsampled points.
Note: Ordering of the result will balance:
(1) if weights are provided, higher weight points come earlier and
(2) if uniform spacing is requested, points will be ordered to have an octree-style coverage --
    so the first 8 points will cover the 8 octants (where samples are available) and the subsequent points will progressively fill in the space

Args:
    points (Array[Vector]): 
    options (GeometryScriptPointPriorityOptions): 
    keep_num_points (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    downsampled_indices (GeometryScriptIndexList):

<a id="unreal.GeometryScript_SimplePolygon"></a>