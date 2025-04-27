## LidarPointCloudBlueprintLibrary Objects

```python
class LidarPointCloudBlueprintLibrary(BlueprintFunctionLibrary)
```

Blueprint library for the Point Cloud assets

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloud.h

<a id="unreal.LidarPointCloudBlueprintLibrary.set_visibility_of_points_in_sphere"></a>

#### set_visibility_of_points_in_sphere

```python
@classmethod
def set_visibility_of_points_in_sphere(cls, world_context_object: Object,
                                       new_visibility: bool, center: Vector,
                                       radius: float) -> None
```

X.set_visibility_of_points_in_sphere(world_context_object, new_visibility, center, radius) -> None
Sets visibility of points within the given sphere.

Args:
    world_context_object (Object): 
    new_visibility (bool): 
    center (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudBlueprintLibrary.set_visibility_of_points_in_box"></a>

#### set_visibility_of_points_in_box

```python
@classmethod
def set_visibility_of_points_in_box(cls, world_context_object: Object,
                                    new_visibility: bool, center: Vector,
                                    extent: Vector) -> None
```

X.set_visibility_of_points_in_box(world_context_object, new_visibility, center, extent) -> None
Sets visibility of points within the given box.

Args:
    world_context_object (Object): 
    new_visibility (bool): 
    center (Vector): 
    extent (Vector):

<a id="unreal.LidarPointCloudBlueprintLibrary.set_visibility_of_points_by_ray"></a>

#### set_visibility_of_points_by_ray

```python
@classmethod
def set_visibility_of_points_by_ray(cls, world_context_object: Object,
                                    new_visibility: bool, origin: Vector,
                                    direction: Vector, radius: float) -> None
```

X.set_visibility_of_points_by_ray(world_context_object, new_visibility, origin, direction, radius) -> None
Sets visibility of points hit by the given ray.

Args:
    world_context_object (Object): 
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudBlueprintLibrary.set_visibility_of_first_point_by_ray"></a>

#### set_visibility_of_first_point_by_ray

```python
@classmethod
def set_visibility_of_first_point_by_ray(cls, world_context_object: Object,
                                         new_visibility: bool, origin: Vector,
                                         direction: Vector,
                                         radius: float) -> None
```

X.set_visibility_of_first_point_by_ray(world_context_object, new_visibility, origin, direction, radius) -> None
Sets visibility of the first point hit by the given ray.

Args:
    world_context_object (Object): 
    new_visibility (bool): 
    origin (Vector): 
    direction (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudBlueprintLibrary.remove_points_in_sphere"></a>

#### remove_points_in_sphere

```python
@classmethod
def remove_points_in_sphere(cls, world_context_object: Object, center: Vector,
                            radius: float, visible_only: bool) -> None
```

X.remove_points_in_sphere(world_context_object, center, radius, visible_only) -> None
Removes all points within the given sphere

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.remove_points_in_box"></a>

#### remove_points_in_box

```python
@classmethod
def remove_points_in_box(cls, world_context_object: Object, center: Vector,
                         extent: Vector, visible_only: bool) -> None
```

X.remove_points_in_box(world_context_object, center, extent, visible_only) -> None
Removes all points within the given box

Args:
    world_context_object (Object): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.remove_points_by_ray"></a>

#### remove_points_by_ray

```python
@classmethod
def remove_points_by_ray(cls, world_context_object: Object, origin: Vector,
                         direction: Vector, radius: float,
                         visible_only: bool) -> None
```

X.remove_points_by_ray(world_context_object, origin, direction, radius, visible_only) -> None
Removes all points hit by the given ray

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.remove_first_point_by_ray"></a>

#### remove_first_point_by_ray

```python
@classmethod
def remove_first_point_by_ray(cls, world_context_object: Object,
                              origin: Vector, direction: Vector, radius: float,
                              visible_only: bool) -> None
```

X.remove_first_point_by_ray(world_context_object, origin, direction, radius, visible_only) -> None
Removes the first point hit by the given ray

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.normal_from_vector"></a>

#### normal_from_vector

```python
@classmethod
def normal_from_vector(cls, normal: LidarPointCloudNormal,
                       vector: Vector) -> LidarPointCloudNormal
```

X.normal_from_vector(normal, vector) -> LidarPointCloudNormal
Sets the given normal using provided vector

Args:
    normal (LidarPointCloudNormal): 
    vector (Vector): 

Returns:
    LidarPointCloudNormal: 

    normal (LidarPointCloudNormal):

<a id="unreal.LidarPointCloudBlueprintLibrary.line_trace_single"></a>

#### line_trace_single

```python
@classmethod
def line_trace_single(cls, world_context_object: Object, origin: Vector,
                      direction: Vector, radius: float,
                      visible_only: bool) -> Optional[LidarPointCloudTraceHit]
```

X.line_trace_single(world_context_object, origin, direction, radius, visible_only) -> LidarPointCloudTraceHit or None
Does a collision trace along the given line and returns the first blocking hit encountered.

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    LidarPointCloudTraceHit or None: 

    hit (LidarPointCloudTraceHit):

<a id="unreal.LidarPointCloudBlueprintLibrary.line_trace_multi"></a>

#### line_trace_multi

```python
@classmethod
def line_trace_multi(
        cls, world_context_object: Object, origin: Vector, direction: Vector,
        radius: float,
        visible_only: bool) -> Optional[Array[LidarPointCloudTraceHit]]
```

X.line_trace_multi(world_context_object, origin, direction, radius, visible_only) -> Array[LidarPointCloudTraceHit] or None
Does a collision trace along the given line and returns all hits encountered up to and including the first blocking hit.

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    Array[LidarPointCloudTraceHit] or None: 

    hits (Array[LidarPointCloudTraceHit]):

<a id="unreal.LidarPointCloudBlueprintLibrary.get_points_in_sphere_as_copies"></a>

#### get_points_in_sphere_as_copies

```python
@classmethod
def get_points_in_sphere_as_copies(
        cls, world_context_object: Object, center: Vector, radius: float,
        visible_only: bool) -> Array[LidarPointCloudPoint]
```

X.get_points_in_sphere_as_copies(world_context_object, center, radius, visible_only) -> Array[LidarPointCloudPoint]
Returns an array with copies of points within the given sphere

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    Array[LidarPointCloudPoint]: 

    selected_points (Array[LidarPointCloudPoint]):

<a id="unreal.LidarPointCloudBlueprintLibrary.get_points_in_box_as_copies"></a>

#### get_points_in_box_as_copies

```python
@classmethod
def get_points_in_box_as_copies(
        cls, world_context_object: Object, center: Vector, extent: Vector,
        visible_only: bool) -> Array[LidarPointCloudPoint]
```

X.get_points_in_box_as_copies(world_context_object, center, extent, visible_only) -> Array[LidarPointCloudPoint]
Returns an array with copies of points within the given box

Args:
    world_context_object (Object): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 

Returns:
    Array[LidarPointCloudPoint]: 

    selected_points (Array[LidarPointCloudPoint]):

<a id="unreal.LidarPointCloudBlueprintLibrary.export_point_cloud_to_file"></a>

#### export_point_cloud_to_file

```python
@classmethod
def export_point_cloud_to_file(cls, point_cloud: LidarPointCloud,
                               filename: str) -> bool
```

X.export_point_cloud_to_file(point_cloud, filename) -> bool
Exports the Point Cloud to the given filename.
Consult supported export formats.
Returns true if successful

Args:
    point_cloud (LidarPointCloud): 
    filename (str): 

Returns:
    bool:

<a id="unreal.LidarPointCloudBlueprintLibrary.create_point_cloud_from_file"></a>

#### create_point_cloud_from_file

```python
@classmethod
def create_point_cloud_from_file(
    cls, world_context_object: Object, filename: str, use_async: bool,
    latent_info: LatentActionInfo
) -> Tuple[LidarPointCloudAsyncMode, float, LidarPointCloud]
```

X.create_point_cloud_from_file(world_context_object, filename, use_async, latent_info) -> (async_mode=LidarPointCloudAsyncMode, progress=float, point_cloud=LidarPointCloud)
Returns new Point Cloud object imported using default settings.
If using Async, the process runs in the background without blocking the game thread.

Args:
    world_context_object (Object): 
    filename (str): 
    use_async (bool): 
    latent_info (LatentActionInfo): 

Returns:
    tuple: 

    async_mode (LidarPointCloudAsyncMode): 

    progress (float): 

    point_cloud (LidarPointCloud):

<a id="unreal.LidarPointCloudBlueprintLibrary.create_point_cloud_from_data"></a>

#### create_point_cloud_from_data

```python
@classmethod
def create_point_cloud_from_data(
    cls, world_context_object: Object, points: Array[LidarPointCloudPoint],
    use_async: bool, latent_info: LatentActionInfo
) -> Tuple[LidarPointCloudAsyncMode, float, LidarPointCloud]
```

X.create_point_cloud_from_data(world_context_object, points, use_async, latent_info) -> (async_mode=LidarPointCloudAsyncMode, progress=float, point_cloud=LidarPointCloud)
* Returns new Point Cloud object created from the data provided.
* Warning: If using Async, make sure the data does not get invalidated during processing!

Args:
    world_context_object (Object): 
    points (Array[LidarPointCloudPoint]): 
    use_async (bool): 
    latent_info (LatentActionInfo): 

Returns:
    tuple: 

    async_mode (LidarPointCloudAsyncMode): 

    progress (float): 

    point_cloud (LidarPointCloud):

<a id="unreal.LidarPointCloudBlueprintLibrary.create_point_cloud_empty"></a>

#### create_point_cloud_empty

```python
@classmethod
def create_point_cloud_empty(cls) -> LidarPointCloud
```

X.create_point_cloud_empty() -> LidarPointCloud
Returns new, empty Point Cloud object.

Returns:
    LidarPointCloud:

<a id="unreal.LidarPointCloudBlueprintLibrary.conv_vector_to_lidar_point_cloud_normal"></a>

#### conv_vector_to_lidar_point_cloud_normal

```python
@classmethod
def conv_vector_to_lidar_point_cloud_normal(
        cls, vector: Vector) -> LidarPointCloudNormal
```

X.conv_vector_to_lidar_point_cloud_normal(vector) -> LidarPointCloudNormal
Converts a Vector to a Lidar Point Cloud Normal

Args:
    vector (Vector): 

Returns:
    LidarPointCloudNormal:

<a id="unreal.LidarPointCloudBlueprintLibrary.conv_lidar_point_cloud_normal_to_vector"></a>

#### conv_lidar_point_cloud_normal_to_vector

```python
@classmethod
def conv_lidar_point_cloud_normal_to_vector(
        cls, normal: LidarPointCloudNormal) -> Vector
```

X.conv_lidar_point_cloud_normal_to_vector(normal) -> Vector
Converts a Lidar Point Cloud Normal to a Vector

Args:
    normal (LidarPointCloudNormal): 

Returns:
    Vector:

<a id="unreal.LidarPointCloudBlueprintLibrary.are_points_in_sphere"></a>

#### are_points_in_sphere

```python
@classmethod
def are_points_in_sphere(cls, world_context_object: Object, center: Vector,
                         radius: float, visible_only: bool) -> bool
```

X.are_points_in_sphere(world_context_object, center, radius, visible_only) -> bool
Returns true if there are any points within the given sphere.

Args:
    world_context_object (Object): 
    center (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudBlueprintLibrary.are_points_in_box"></a>

#### are_points_in_box

```python
@classmethod
def are_points_in_box(cls, world_context_object: Object, center: Vector,
                      extent: Vector, visible_only: bool) -> bool
```

X.are_points_in_box(world_context_object, center, extent, visible_only) -> bool
Returns true if there are any points within the given box.

Args:
    world_context_object (Object): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudBlueprintLibrary.are_points_by_ray"></a>

#### are_points_by_ray

```python
@classmethod
def are_points_by_ray(cls, world_context_object: Object, origin: Vector,
                      direction: Vector, radius: float,
                      visible_only: bool) -> bool
```

X.are_points_by_ray(world_context_object, origin, direction, radius, visible_only) -> bool
Returns true if there are any points hit by the given ray.

Args:
    world_context_object (Object): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool): 

Returns:
    bool:

<a id="unreal.LidarPointCloudBlueprintLibrary.apply_color_to_points_in_sphere"></a>

#### apply_color_to_points_in_sphere

```python
@classmethod
def apply_color_to_points_in_sphere(cls, world_context_object: Object,
                                    new_color: Color, center: Vector,
                                    radius: float, visible_only: bool) -> None
```

X.apply_color_to_points_in_sphere(world_context_object, new_color, center, radius, visible_only) -> None
Applies the given color to all points within the sphere

Args:
    world_context_object (Object): 
    new_color (Color): 
    center (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.apply_color_to_points_in_box"></a>

#### apply_color_to_points_in_box

```python
@classmethod
def apply_color_to_points_in_box(cls, world_context_object: Object,
                                 new_color: Color, center: Vector,
                                 extent: Vector, visible_only: bool) -> None
```

X.apply_color_to_points_in_box(world_context_object, new_color, center, extent, visible_only) -> None
Applies the given color to all points within the box

Args:
    world_context_object (Object): 
    new_color (Color): 
    center (Vector): 
    extent (Vector): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.apply_color_to_points_by_ray"></a>

#### apply_color_to_points_by_ray

```python
@classmethod
def apply_color_to_points_by_ray(cls, world_context_object: Object,
                                 new_color: Color, origin: Vector,
                                 direction: Vector, radius: float,
                                 visible_only: bool) -> None
```

X.apply_color_to_points_by_ray(world_context_object, new_color, origin, direction, radius, visible_only) -> None
Applies the given color to all points hit by the given ray

Args:
    world_context_object (Object): 
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.apply_color_to_first_point_by_ray"></a>

#### apply_color_to_first_point_by_ray

```python
@classmethod
def apply_color_to_first_point_by_ray(cls, world_context_object: Object,
                                      new_color: Color, origin: Vector,
                                      direction: Vector, radius: float,
                                      visible_only: bool) -> None
```

X.apply_color_to_first_point_by_ray(world_context_object, new_color, origin, direction, radius, visible_only) -> None
Applies the given color to the first point hit by the given ray

Args:
    world_context_object (Object): 
    new_color (Color): 
    origin (Vector): 
    direction (Vector): 
    radius (float): 
    visible_only (bool):

<a id="unreal.LidarPointCloudBlueprintLibrary.align_clouds"></a>

#### align_clouds

```python
@classmethod
def align_clouds(cls, point_clouds_to_align: Array[LidarPointCloud]) -> None
```

X.align_clouds(point_clouds_to_align) -> None
Aligns provided clouds based on the relative offset between their Original Coordinates. Retains overall centering of the group.

Args:
    point_clouds_to_align (Array[LidarPointCloud]):

<a id="unreal.LidarClippingVolume"></a>