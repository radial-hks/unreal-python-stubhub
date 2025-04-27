## LidarPointCloud Objects

```python
class LidarPointCloud(Object)
```

Represents the Point Cloud asset

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloud.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_accuracy`` (float):  [Read-Write]
  deprecated: Use MaxCollisionError instead.
- ``max_collision_error`` (float):  [Read-Write] Determines the maximum error (in cm) of the collision for this point cloud.
  NOTE: Lower values will require more time to build.
  Rebuild collision for the changes to take effect.
- ``normals_noise_tolerance`` (float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
  Lower values retain more detail, at the expense of time.
  NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.
- ``normals_quality`` (int32):  [Read-Write] Higher values will generally result in more accurate calculations, at the expense of time
- ``optimized_for_dynamic_data`` (bool):  [Read-Write] Disables the LOD pipeline, allowing for much faster data operations (insert/remove/set)
  at a potential expense of runtime performance. The whole asset will be treated as a single,
  large asset with no granular density control, nor occlusion culling.

  Recommended for assets, which have their data updated per-frame (such as live streaming).
- ``original_coordinates`` (Vector):  [Read-Write] Stores the original offset as a double.
- ``source_path`` (FilePath):  [Read-Write] Stores the path to the original source file. Empty if dynamically created.

<a id="unreal.LidarPointCloud.max_collision_error"></a>

#### max_collision_error

```python
@property
def max_collision_error() -> float
```

(float):  [Read-Write] Determines the maximum error (in cm) of the collision for this point cloud.
NOTE: Lower values will require more time to build.
Rebuild collision for the changes to take effect.

<a id="unreal.LidarPointCloud.max_collision_error"></a>

#### max_collision_error

```python
@max_collision_error.setter
def max_collision_error(value: float) -> None
```

<a id="unreal.LidarPointCloud.collision_accuracy"></a>

#### collision_accuracy

```python
@property
def collision_accuracy() -> float
```

(float):  [Read-Write]
deprecated: Use MaxCollisionError instead.

<a id="unreal.LidarPointCloud.collision_accuracy"></a>

#### collision_accuracy

```python
@collision_accuracy.setter
def collision_accuracy(value: float) -> None
```

<a id="unreal.LidarPointCloud.normals_quality"></a>

#### normals_quality

```python
@property
def normals_quality() -> int
```

(int32):  [Read-Write] Higher values will generally result in more accurate calculations, at the expense of time

<a id="unreal.LidarPointCloud.normals_quality"></a>

#### normals_quality

```python
@normals_quality.setter
def normals_quality(value: int) -> None
```

<a id="unreal.LidarPointCloud.normals_noise_tolerance"></a>

#### normals_noise_tolerance

```python
@property
def normals_noise_tolerance() -> float
```

(float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
Lower values retain more detail, at the expense of time.
NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.

<a id="unreal.LidarPointCloud.normals_noise_tolerance"></a>

#### normals_noise_tolerance

```python
@normals_noise_tolerance.setter
def normals_noise_tolerance(value: float) -> None
```

<a id="unreal.LidarPointCloud.original_coordinates"></a>

#### original_coordinates

```python
@property
def original_coordinates() -> Vector
```

(Vector):  [Read-Only] Stores the original offset as a double.

<a id="unreal.LidarPointCloud.unhide_all"></a>

#### unhide_all

```python
def unhide_all() -> None
```

x.unhide_all() -> None
Marks all points visible

<a id="unreal.LidarPointCloud.set_visibility_of_points_in_sphere"></a>

#### set_visibility_of_points_in_sphere

```python
def set_visibility_of_points_in_sphere(new_visibility: bool, center: Vector,
                                       radius: float) -> None
```

x.set_visibility_of_points_in_sphere(new_visibility, center, radius) -> None
Sets visibility of points within the given sphere.

Args:
    new_visibility (bool): 
    center (Vector): 
    radius (float):

<a id="unreal.LidarPointCloud.set_visibility_of_points_in_box"></a>

#### set_visibility_of_points_in_box

```python
def set_visibility_of_points_in_box(new_visibility: bool, center: Vector,
                                    extent: Vector) -> None
```

x.set_visibility_of_points_in_box(new_visibility, center, extent) -> None
Sets visibility of points within the given box.

Args:
    new_visibility (bool): 
    center (Vector): 
    extent (Vector):

<a id="unreal.LidarPointCloud.set_visibility_of_points_by_ray"></a>

#### set_visibility_of_points_by_ray

```python
def set_visibility_of_points_by_ray(new_visibility: bool, origin: Vector,
                                    direction: Vector, radius: float) -> None
```

x.set_visibility_of_points_by_ray(new_visibility, origin, direction, radius) -> None
Sets visibility of points hit by the given ray.

Args:
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloud.set_visibility_of_first_point_by_ray"></a>

#### set_visibility_of_first_point_by_ray

```python
def set_visibility_of_first_point_by_ray(new_visibility: bool, origin: Vector,
                                         direction: Vector,
                                         radius: float) -> None
```

x.set_visibility_of_first_point_by_ray(new_visibility, origin, direction, radius) -> None
Sets visibility of the first point hit by the given ray.

Args:
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloud.set_source_path"></a>

#### set_source_path

```python
def set_source_path(new_source_path: str) -> None
```

x.set_source_path(new_source_path) -> None
Set Source Path

Args:
    new_source_path (str):

<a id="unreal.LidarPointCloud.set_optimized_for_dynamic_data"></a>

#### set_optimized_for_dynamic_data

```python
def set_optimized_for_dynamic_data(
        new_optimized_for_dynamic_data: bool) -> None
```

x.set_optimized_for_dynamic_data(new_optimized_for_dynamic_data) -> None
Set Optimized for Dynamic Data

Args:
    new_optimized_for_dynamic_data (bool):

<a id="unreal.LidarPointCloud.set_optimal_collision_error"></a>

#### set_optimal_collision_error

```python
def set_optimal_collision_error() -> None
```

x.set_optimal_collision_error() -> None
Set Optimal Collision Error

<a id="unreal.LidarPointCloud.set_location_offset"></a>

#### set_location_offset

```python
def set_location_offset(offset: Vector) -> None
```

x.set_location_offset(offset) -> None
Applies given offset to this point cloud.

Args:
    offset (Vector):

<a id="unreal.LidarPointCloud.set_data"></a>

#### set_data

```python
def set_data(points: Array[LidarPointCloudPoint]) -> bool
```

x.set_data(points) -> bool
Reinitializes the cloud with the new set of data.

Args:
    points (Array[LidarPointCloudPoint]): 

Returns:
    bool:

<a id="unreal.LidarPointCloud.restore_original_coordinates"></a>

#### restore_original_coordinates

```python
def restore_original_coordinates() -> None
```

x.restore_original_coordinates() -> None
Restores original coordinates

<a id="unreal.LidarPointCloud.remove_points_in_sphere"></a>

#### remove_points_in_sphere

```python
def remove_points_in_sphere(center: Vector, radius: float,
                            visible_only: bool) -> None
```

x.remove_points_in_sphere(center, radius, visible_only) -> None
Removes all points within the given sphere

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.remove_points_in_box"></a>

#### remove_points_in_box

```python
def remove_points_in_box(center: Vector, extent: Vector,
                         visible_only: bool) -> None
```

x.remove_points_in_box(center, extent, visible_only) -> None
Removes all points within the given box

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.remove_points_by_ray"></a>

#### remove_points_by_ray

```python
def remove_points_by_ray(origin: Vector, direction: Vector, radius: float,
                         visible_only: bool) -> None
```

x.remove_points_by_ray(origin, direction, radius, visible_only) -> None
Removes all points hit by the given ray

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.remove_point"></a>

#### remove_point

```python
def remove_point(point: LidarPointCloudPoint) -> None
```

x.remove_point(point) -> None
Attempts to remove the given point.

Args:
    point (LidarPointCloudPoint):

<a id="unreal.LidarPointCloud.remove_hidden_points"></a>

#### remove_hidden_points

```python
def remove_hidden_points() -> None
```

x.remove_hidden_points() -> None
Removes all hidden points

<a id="unreal.LidarPointCloud.remove_first_point_by_ray"></a>

#### remove_first_point_by_ray

```python
def remove_first_point_by_ray(origin: Vector, direction: Vector, radius: float,
                              visible_only: bool) -> None
```

x.remove_first_point_by_ray(origin, direction, radius, visible_only) -> None
Removes the first point hit by the given ray

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.remove_collision"></a>

#### remove_collision

```python
def remove_collision() -> None
```

x.remove_collision() -> None
Removes collision mesh from the cloud.

<a id="unreal.LidarPointCloud.reimport"></a>

#### reimport

```python
def reimport(
        world_context_object: Object, use_async: bool,
        latent_info: LatentActionInfo
) -> Tuple[LidarPointCloudAsyncMode, float]
```

x.reimport(world_context_object, use_async, latent_info) -> (async_mode=LidarPointCloudAsyncMode, progress=float)
Re-imports the cloud from it's original source file, overwriting any current point information.

Args:
    world_context_object (Object): 
    use_async (bool): 
    latent_info (LatentActionInfo): 

Returns:
    tuple: 

    async_mode (LidarPointCloudAsyncMode): 

    progress (float):

<a id="unreal.LidarPointCloud.refresh_rendering"></a>

#### refresh_rendering

```python
def refresh_rendering() -> None
```

x.refresh_rendering() -> None
Refresh Rendering

<a id="unreal.LidarPointCloud.refresh_bounds"></a>

#### refresh_bounds

```python
def refresh_bounds() -> None
```

x.refresh_bounds() -> None
Recalculates and updates points bounds.

<a id="unreal.LidarPointCloud.merge_single"></a>

#### merge_single

```python
def merge_single(point_cloud_to_merge: LidarPointCloud) -> None
```

x.merge_single(point_cloud_to_merge) -> None
Merges this point cloud with the one provided

Args:
    point_cloud_to_merge (LidarPointCloud):

<a id="unreal.LidarPointCloud.merge"></a>

#### merge

```python
def merge(point_clouds_to_merge: Array[LidarPointCloud]) -> None
```

x.merge(point_clouds_to_merge) -> None
Merges this point cloud with the ones provided

Args:
    point_clouds_to_merge (Array[LidarPointCloud]):

<a id="unreal.LidarPointCloud.mark_point_visibility_dirty"></a>

#### mark_point_visibility_dirty

```python
def mark_point_visibility_dirty() -> None
```

x.mark_point_visibility_dirty() -> None
This should to be called if any manual modification to individual points' visibility has been made.
If not marked dirty, the rendering may work sub-optimally.

<a id="unreal.LidarPointCloud.load_all_nodes"></a>

#### load_all_nodes

```python
def load_all_nodes() -> None
```

x.load_all_nodes() -> None
Persistently loads all nodes.

<a id="unreal.LidarPointCloud.line_trace_single"></a>

#### line_trace_single

```python
def line_trace_single(origin: Vector, direction: Vector, radius: float,
                      visible_only: bool) -> Optional[LidarPointCloudPoint]
```

x.line_trace_single(origin, direction, radius, visible_only) -> LidarPointCloudPoint or None
Performs a raycast test against the point cloud. Returns the pointer if hit or nullptr otherwise.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    LidarPointCloudPoint or None: 

    point_hit (LidarPointCloudPoint):

<a id="unreal.LidarPointCloud.line_trace_multi"></a>

#### line_trace_multi

```python
def line_trace_multi(
        origin: Vector, direction: Vector, radius: float, visible_only: bool,
        return_world_space: bool) -> Optional[Array[LidarPointCloudPoint]]
```

x.line_trace_multi(origin, direction, radius, visible_only, return_world_space) -> Array[LidarPointCloudPoint] or None
Performs a raycast test against the point cloud.
Populates OutHits array with the results.
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.
Returns true it anything has been hit.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint] or None: 

    out_hits (Array[LidarPointCloudPoint]):

<a id="unreal.LidarPointCloud.is_optimized_for_dynamic_data"></a>

#### is_optimized_for_dynamic_data

```python
def is_optimized_for_dynamic_data() -> bool
```

x.is_optimized_for_dynamic_data() -> bool
Is Optimized for Dynamic Data

Returns:
    bool:

<a id="unreal.LidarPointCloud.is_fully_loaded"></a>

#### is_fully_loaded

```python
def is_fully_loaded() -> bool
```

x.is_fully_loaded() -> bool
Returns true, if the cloud is fully and persistently loaded.

Returns:
    bool:

<a id="unreal.LidarPointCloud.is_centered"></a>

#### is_centered

```python
def is_centered() -> bool
```

x.is_centered() -> bool
Returns true, if the cloud has been centered.

Returns:
    bool:

<a id="unreal.LidarPointCloud.insert_points"></a>

#### insert_points

```python
def insert_points(points: Array[LidarPointCloudPoint],
                  duplicate_handling: LidarPointCloudDuplicateHandling,
                  refresh_points_bounds: bool, translation: Vector) -> None
```

x.insert_points(points, duplicate_handling, refresh_points_bounds, translation) -> None
Inserts group of points into the Octree structure, multi-threaded.
If bRefreshPointsBounds is set to false, make sure you call RefreshBounds() manually or cloud centering may not work correctly.

Args:
    points (Array[LidarPointCloudPoint]): 
    duplicate_handling (LidarPointCloudDuplicateHandling): 
    refresh_points_bounds (bool): 
    translation (Vector):

<a id="unreal.LidarPointCloud.insert_point"></a>

#### insert_point

```python
def insert_point(point: LidarPointCloudPoint,
                 duplicate_handling: LidarPointCloudDuplicateHandling,
                 refresh_points_bounds: bool, translation: Vector) -> None
```

x.insert_point(point, duplicate_handling, refresh_points_bounds, translation) -> None
Inserts the given point into the Octree structure.
If bRefreshPointsBounds is set to false, make sure you call RefreshBounds() manually or cloud centering may not work correctly.

Args:
    point (LidarPointCloudPoint): 
    duplicate_handling (LidarPointCloudDuplicateHandling): 
    refresh_points_bounds (bool): 
    translation (Vector):

<a id="unreal.LidarPointCloud.initialize"></a>

#### initialize

```python
def initialize(new_bounds: Box) -> None
```

x.initialize(new_bounds) -> None
Re-initializes the asset with new bounds.
Warning: Will erase all currently held data!

Args:
    new_bounds (Box):

<a id="unreal.LidarPointCloud.hide_all"></a>

#### hide_all

```python
def hide_all() -> None
```

x.hide_all() -> None
Marks all points hidden

<a id="unreal.LidarPointCloud.has_points_in_sphere"></a>

#### has_points_in_sphere

```python
def has_points_in_sphere(center: Vector, radius: float,
                         visible_only: bool) -> bool
```

x.has_points_in_sphere(center, radius, visible_only) -> bool
Returns true if there are any points within the given sphere.

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloud.has_points_in_box"></a>

#### has_points_in_box

```python
def has_points_in_box(center: Vector, extent: Vector,
                      visible_only: bool) -> bool
```

x.has_points_in_box(center, extent, visible_only) -> bool
Returns true if there are any points within the given box.

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloud.has_points_by_ray"></a>

#### has_points_by_ray

```python
def has_points_by_ray(origin: Vector, direction: Vector, radius: float,
                      visible_only: bool) -> bool
```

x.has_points_by_ray(origin, direction, radius, visible_only) -> bool
Returns true if there are any points hit by the given ray.

Args:
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloud.has_collision_data"></a>

#### has_collision_data

```python
def has_collision_data() -> bool
```

x.has_collision_data() -> bool
Returns true, if the Octree has collision built

Returns:
    bool:

<a id="unreal.LidarPointCloud.get_source_path"></a>

#### get_source_path

```python
def get_source_path() -> str
```

x.get_source_path() -> str
Get Source Path

Returns:
    str:

<a id="unreal.LidarPointCloud.get_points_in_sphere_as_copies"></a>

#### get_points_in_sphere_as_copies

```python
def get_points_in_sphere_as_copies(
        center: Vector, radius: float, visible_only: bool,
        return_world_space: bool) -> Array[LidarPointCloudPoint]
```

x.get_points_in_sphere_as_copies(center, radius, visible_only, return_world_space) -> Array[LidarPointCloudPoint]
Returns an array with copies of points within the given sphere
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.

Args:
    center (Vector): 
    radius (float): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint]:

<a id="unreal.LidarPointCloud.get_points_in_box_as_copies"></a>

#### get_points_in_box_as_copies

```python
def get_points_in_box_as_copies(
        center: Vector, extent: Vector, visible_only: bool,
        return_world_space: bool) -> Array[LidarPointCloudPoint]
```

x.get_points_in_box_as_copies(center, extent, visible_only, return_world_space) -> Array[LidarPointCloudPoint]
Returns an array with copies of points within the given box
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.

Args:
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 
    return_world_space (bool): 

Returns:
    Array[LidarPointCloudPoint]:

<a id="unreal.LidarPointCloud.get_points_as_copies"></a>

#### get_points_as_copies

```python
def get_points_as_copies(return_world_space: bool,
                         start_index: int = 0,
                         count: int = -1) -> Array[LidarPointCloudPoint]
```

x.get_points_as_copies(return_world_space, start_index=0, count=-1) -> Array[LidarPointCloudPoint]
Returns an array with copies of points from the tree
If ReturnWorldSpace is selected, the points' locations will be converted into absolute value, otherwise they will be relative to the center of the cloud.

Args:
    return_world_space (bool): 
    start_index (int32): 
    count (int32): 

Returns:
    Array[LidarPointCloudPoint]:

<a id="unreal.LidarPointCloud.get_num_visible_points"></a>

#### get_num_visible_points

```python
def get_num_visible_points() -> int
```

x.get_num_visible_points() -> int64
Get Num Visible Points

Returns:
    int64:

<a id="unreal.LidarPointCloud.get_num_points"></a>

#### get_num_points

```python
def get_num_points() -> int
```

x.get_num_points() -> int64
Get Num Points

Returns:
    int64:

<a id="unreal.LidarPointCloud.get_num_nodes"></a>

#### get_num_nodes

```python
def get_num_nodes() -> int
```

x.get_num_nodes() -> int32
Get Num Nodes

Returns:
    int32:

<a id="unreal.LidarPointCloud.get_num_lo_ds"></a>

#### get_num_lo_ds

```python
def get_num_lo_ds() -> int
```

x.get_num_lo_ds() -> int32
End UObject Interface.

Returns:
    int32:

<a id="unreal.LidarPointCloud.get_estimated_point_spacing"></a>

#### get_estimated_point_spacing

```python
def get_estimated_point_spacing() -> float
```

x.get_estimated_point_spacing() -> float
Get Estimated Point Spacing

Returns:
    float:

<a id="unreal.LidarPointCloud.get_data_size"></a>

#### get_data_size

```python
def get_data_size() -> int
```

x.get_data_size() -> int32
Returns the amount of memory in MB used to store the point cloud.

Returns:
    int32:

<a id="unreal.LidarPointCloud.get_collider_polys"></a>

#### get_collider_polys

```python
def get_collider_polys() -> int
```

x.get_collider_polys() -> int32
Returns the number of polygons in the collider or 0 if no collider is built

Returns:
    int32:

<a id="unreal.LidarPointCloud.get_bounds"></a>

#### get_bounds

```python
def get_bounds(use_original_coordinates: bool = False) -> Box
```

x.get_bounds(use_original_coordinates=False) -> Box
Get Bounds

Args:
    use_original_coordinates (bool): 

Returns:
    Box:

<a id="unreal.LidarPointCloud.export"></a>

#### export

```python
def export(filename: str) -> bool
```

x.export(filename) -> bool
Exports this Point Cloud to the given filename.
Consult supported export formats.
Returns true if successful

Args:
    filename (str): 

Returns:
    bool:

<a id="unreal.LidarPointCloud.center_points"></a>

#### center_points

```python
def center_points() -> None
```

x.center_points() -> None
Centers this cloud

<a id="unreal.LidarPointCloud.calculate_normals"></a>

#### calculate_normals

```python
def calculate_normals(latent_info: LatentActionInfo) -> None
```

x.calculate_normals(latent_info) -> None
Calculates Normals for this point cloud

Args:
    latent_info (LatentActionInfo):

<a id="unreal.LidarPointCloud.build_collision_with_callback"></a>

#### build_collision_with_callback

```python
def build_collision_with_callback(world_context_object: Object,
                                  latent_info: LatentActionInfo) -> bool
```

x.build_collision_with_callback(world_context_object, latent_info) -> bool
Build Collision with Callback

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    bool: 

    success (bool):

<a id="unreal.LidarPointCloud.build_collision"></a>

#### build_collision

```python
def build_collision() -> None
```

x.build_collision() -> None
Builds collision mesh for the cloud, using current collision settings

<a id="unreal.LidarPointCloud.apply_color_to_points_in_sphere"></a>

#### apply_color_to_points_in_sphere

```python
def apply_color_to_points_in_sphere(new_color: Color, center: Vector,
                                    radius: float, visible_only: bool) -> None
```

x.apply_color_to_points_in_sphere(new_color, center, radius, visible_only) -> None
Applies the given color to all points within the sphere

Args:
    new_color (Color): 
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.apply_color_to_points_in_box"></a>

#### apply_color_to_points_in_box

```python
def apply_color_to_points_in_box(new_color: Color, center: Vector,
                                 extent: Vector, visible_only: bool) -> None
```

x.apply_color_to_points_in_box(new_color, center, extent, visible_only) -> None
Applies the given color to all points within the box

Args:
    new_color (Color): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.apply_color_to_points_by_ray"></a>

#### apply_color_to_points_by_ray

```python
def apply_color_to_points_by_ray(new_color: Color, origin: Vector,
                                 direction: Vector, radius: float,
                                 visible_only: bool) -> None
```

x.apply_color_to_points_by_ray(new_color, origin, direction, radius, visible_only) -> None
Applies the given color to all points hit by the given ray

Args:
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.apply_color_to_first_point_by_ray"></a>

#### apply_color_to_first_point_by_ray

```python
def apply_color_to_first_point_by_ray(new_color: Color, origin: Vector,
                                      direction: Vector, radius: float,
                                      visible_only: bool) -> None
```

x.apply_color_to_first_point_by_ray(new_color, origin, direction, radius, visible_only) -> None
Applies the given color to the first point hit by the given ray

Args:
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloud.apply_color_to_all_points"></a>

#### apply_color_to_all_points

```python
def apply_color_to_all_points(new_color: Color, visible_only: bool) -> None
```

x.apply_color_to_all_points(new_color, visible_only) -> None
Applies the given color to all points

Args:
    new_color (Color): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary"></a>