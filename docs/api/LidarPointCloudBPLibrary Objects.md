## LidarPointCloudBPLibrary Objects

```python
class LidarPointCloudBPLibrary(BlueprintFunctionLibrary)
```

Lidar Point Cloud BPLibrary

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: LidarPointCloudBPLibrary.h

<a id="unreal.LidarPointCloudBPLibrary.set_point_cloud_level_colors"></a>

#### set\_point\_cloud\_level\_colors

```python
@classmethod
def set_point_cloud_level_colors(cls,
                                 m_level_colors: Array[LinearColor]) -> None
```

X.set_point_cloud_level_colors(m_level_colors) -> None
Set Point Cloud Level Colors

Args:
    m_level_colors (Array[LinearColor]):

<a id="unreal.LidarPointCloudBPLibrary.reset_point_cloud_level_colors"></a>

#### reset\_point\_cloud\_level\_colors

```python
@classmethod
def reset_point_cloud_level_colors(cls) -> None
```

X.reset_point_cloud_level_colors() -> None
Reset Point Cloud Level Colors

<a id="unreal.LidarPointCloudBPLibrary.reflush_point_cloud_with_data"></a>

#### reflush\_point\_cloud\_with\_data

```python
@classmethod
def reflush_point_cloud_with_data(
        cls, point_cloud_actor: LidarPointCloudActor,
        point_cloud_datas_info: CreatePointCloudInfo) -> None
```

X.reflush_point_cloud_with_data(point_cloud_actor, point_cloud_datas_info) -> None
Reflush Point Cloud with Data

Args:
    point_cloud_actor (LidarPointCloudActor): 
    point_cloud_datas_info (CreatePointCloudInfo):

<a id="unreal.LidarPointCloudBPLibrary.get_point_cloud_data_color_by_value"></a>

#### get\_point\_cloud\_data\_color\_by\_value

```python
@classmethod
def get_point_cloud_data_color_by_value(cls, world_context_object: Object,
                                        min_value: float, max_value: float,
                                        value: float) -> Color
```

X.get_point_cloud_data_color_by_value(world_context_object, min_value, max_value, value) -> Color
Get Point Cloud Data Color by Value

Args:
    world_context_object (Object): 
    min_value (float): 
    max_value (float): 
    value (float): 

Returns:
    Color: 

    color (Color):

<a id="unreal.LidarPointCloudBPLibrary.export_sphere_point_cloud_actor_file"></a>

#### export\_sphere\_point\_cloud\_actor\_file

```python
@classmethod
def export_sphere_point_cloud_actor_file(cls, world_context_object: Object,
                                         filename: str, radius: float,
                                         section: float) -> None
```

X.export_sphere_point_cloud_actor_file(world_context_object, filename, radius, section) -> None
Export Sphere Point Cloud Actor File

Args:
    world_context_object (Object): 
    filename (str): 
    radius (float): 
    section (float):

<a id="unreal.LidarPointCloudBPLibrary.export_point_cloud_actor_file_by_mesh"></a>

#### export\_point\_cloud\_actor\_file\_by\_mesh

```python
@classmethod
def export_point_cloud_actor_file_by_mesh(cls, world_context_object: Object,
                                          static_mesh: StaticMesh,
                                          use_scale: bool,
                                          filename: str) -> None
```

X.export_point_cloud_actor_file_by_mesh(world_context_object, static_mesh, use_scale, filename) -> None
Export Point Cloud Actor File by Mesh

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): 
    use_scale (bool): 
    filename (str):

<a id="unreal.LidarPointCloudBPLibrary.export_cylinder_point_cloud_actor_file"></a>

#### export\_cylinder\_point\_cloud\_actor\_file

```python
@classmethod
def export_cylinder_point_cloud_actor_file(cls, world_context_object: Object,
                                           filename: str, radius: float,
                                           height: float,
                                           section: float) -> None
```

X.export_cylinder_point_cloud_actor_file(world_context_object, filename, radius, height, section) -> None
Export Cylinder Point Cloud Actor File

Args:
    world_context_object (Object): 
    filename (str): 
    radius (float): 
    height (float): 
    section (float):

<a id="unreal.LidarPointCloudBPLibrary.export_box_point_cloud_actor_file"></a>

#### export\_box\_point\_cloud\_actor\_file

```python
@classmethod
def export_box_point_cloud_actor_file(cls, world_context_object: Object,
                                      filename: str, box_extent: Vector,
                                      section: float) -> None
```

X.export_box_point_cloud_actor_file(world_context_object, filename, box_extent, section) -> None
Export Box Point Cloud Actor File

Args:
    world_context_object (Object): 
    filename (str): 
    box_extent (Vector): 
    section (float):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_sphere_data"></a>

#### create\_point\_cloud\_sphere\_data

```python
@classmethod
def create_point_cloud_sphere_data(
    cls, world_context_object: Object, latent_info: LatentActionInfo,
    datas: Array[Vector4], min_max_value: Vector2D, radius: float,
    m_section: float
) -> Tuple[PointCloudAsyncMode, float, CreatePointCloudInfo]
```

X.create_point_cloud_sphere_data(world_context_object, latent_info, datas, min_max_value, radius, m_section) -> (async_mode=PointCloudAsyncMode, progress=float, point_cloud_datas_info=CreatePointCloudInfo)
Create Point Cloud Sphere Data

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    datas (Array[Vector4]): 
    min_max_value (Vector2D): 
    radius (float): 
    m_section (float): 

Returns:
    tuple: 

    async_mode (PointCloudAsyncMode): 

    progress (float): 

    point_cloud_datas_info (CreatePointCloudInfo):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_sphere_actor"></a>

#### create\_point\_cloud\_sphere\_actor

```python
@classmethod
def create_point_cloud_sphere_actor(
        cls,
        world_context_object: Object,
        point_cloud_transform: Transform,
        radius: float,
        section: float,
        custom_material: MaterialInterface = None) -> PointCloudBpActor
```

X.create_point_cloud_sphere_actor(world_context_object, point_cloud_transform, radius, section, custom_material=None) -> PointCloudBpActor
Create Point Cloud Sphere Actor

Args:
    world_context_object (Object): 
    point_cloud_transform (Transform): 
    radius (float): 
    section (float): 
    custom_material (MaterialInterface): 

Returns:
    PointCloudBpActor: 

    point_cloud_actor (PointCloudBpActor):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_data_point"></a>

#### create\_point\_cloud\_data\_point

```python
@classmethod
def create_point_cloud_data_point(cls, world_context_object: Object,
                                  datas: Array[Vector]) -> None
```

X.create_point_cloud_data_point(world_context_object, datas) -> None
Create Point Cloud Data Point

Args:
    world_context_object (Object): 
    datas (Array[Vector]):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_cylinder_data"></a>

#### create\_point\_cloud\_cylinder\_data

```python
@classmethod
def create_point_cloud_cylinder_data(
    cls, world_context_object: Object, latent_info: LatentActionInfo,
    datas: Array[Vector4], min_max_value: Vector2D, radius: float,
    height: float, m_section: Vector2D
) -> Tuple[PointCloudAsyncMode, float, CreatePointCloudInfo]
```

X.create_point_cloud_cylinder_data(world_context_object, latent_info, datas, min_max_value, radius, height, m_section) -> (async_mode=PointCloudAsyncMode, progress=float, point_cloud_datas_info=CreatePointCloudInfo)
Create Point Cloud Cylinder Data

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    datas (Array[Vector4]): 
    min_max_value (Vector2D): 
    radius (float): 
    height (float): 
    m_section (Vector2D): 

Returns:
    tuple: 

    async_mode (PointCloudAsyncMode): 

    progress (float): 

    point_cloud_datas_info (CreatePointCloudInfo):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_cylinder_actor"></a>

#### create\_point\_cloud\_cylinder\_actor

```python
@classmethod
def create_point_cloud_cylinder_actor(
        cls,
        world_context_object: Object,
        point_cloud_transform: Transform,
        radius: float,
        height: float,
        section: float,
        custom_material: MaterialInterface = None) -> PointCloudBpActor
```

X.create_point_cloud_cylinder_actor(world_context_object, point_cloud_transform, radius, height, section, custom_material=None) -> PointCloudBpActor
Create Point Cloud Cylinder Actor

Args:
    world_context_object (Object): 
    point_cloud_transform (Transform): 
    radius (float): 
    height (float): 
    section (float): 
    custom_material (MaterialInterface): 

Returns:
    PointCloudBpActor: 

    point_cloud_actor (PointCloudBpActor):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_box_data"></a>

#### create\_point\_cloud\_box\_data

```python
@classmethod
def create_point_cloud_box_data(
    cls, world_context_object: Object, latent_info: LatentActionInfo,
    datas: Array[Vector4], min_max_value: Vector2D, m_box_extent: Vector,
    m_section: Vector
) -> Tuple[PointCloudAsyncMode, float, CreatePointCloudInfo]
```

X.create_point_cloud_box_data(world_context_object, latent_info, datas, min_max_value, m_box_extent, m_section) -> (async_mode=PointCloudAsyncMode, progress=float, point_cloud_datas_info=CreatePointCloudInfo)
UFUNCTION(BlueprintCallable, meta = (WorldContext = "WorldContextObject", DisplayName = "CreatePointCloud", Keywords = "CreatePointCloud"), Category = "PointCloud")
static ALidarPointCloudActor* CreatePointCloud(const UObject* WorldContextObject, FString FilePath,FTransform PointCloudTransform, bool &Result, UMaterialInterface* CustomMaterial = NULL);

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 
    datas (Array[Vector4]): 
    min_max_value (Vector2D): 
    m_box_extent (Vector): 
    m_section (Vector): 

Returns:
    tuple: 

    async_mode (PointCloudAsyncMode): 

    progress (float): 

    point_cloud_datas_info (CreatePointCloudInfo):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_box_actor"></a>

#### create\_point\_cloud\_box\_actor

```python
@classmethod
def create_point_cloud_box_actor(
        cls,
        world_context_object: Object,
        point_cloud_transform: Transform,
        box: Vector,
        section: float,
        custom_material: MaterialInterface = None) -> PointCloudBpActor
```

X.create_point_cloud_box_actor(world_context_object, point_cloud_transform, box, section, custom_material=None) -> PointCloudBpActor
Create Point Cloud Box Actor

Args:
    world_context_object (Object): 
    point_cloud_transform (Transform): 
    box (Vector): 
    section (float): 
    custom_material (MaterialInterface): 

Returns:
    PointCloudBpActor: 

    point_cloud_actor (PointCloudBpActor):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud_actor"></a>

#### create\_point\_cloud\_actor

```python
@classmethod
def create_point_cloud_actor(
        cls,
        world_context_object: Object,
        static_mesh: StaticMesh,
        use_scale: bool,
        use_offset: float,
        point_cloud_transform: Transform,
        custom_material: MaterialInterface = None) -> PointCloudBpActor
```

X.create_point_cloud_actor(world_context_object, static_mesh, use_scale, use_offset, point_cloud_transform, custom_material=None) -> PointCloudBpActor
Create Point Cloud Actor

Args:
    world_context_object (Object): 
    static_mesh (StaticMesh): 
    use_scale (bool): 
    use_offset (float): 
    point_cloud_transform (Transform): 
    custom_material (MaterialInterface): 

Returns:
    PointCloudBpActor: 

    point_cloud_actor (PointCloudBpActor):

<a id="unreal.LidarPointCloudBPLibrary.create_point_cloud"></a>

#### create\_point\_cloud

```python
@classmethod
def create_point_cloud(
        cls, world_context_object: Object,
        point_cloud_datas_info: CreatePointCloudInfo,
        point_cloud_transform: Transform,
        custom_material: MaterialInterface) -> LidarPointCloudActor
```

X.create_point_cloud(world_context_object, point_cloud_datas_info, point_cloud_transform, custom_material) -> LidarPointCloudActor
Create Point Cloud

Args:
    world_context_object (Object): 
    point_cloud_datas_info (CreatePointCloudInfo): 
    point_cloud_transform (Transform): 
    custom_material (MaterialInterface): 

Returns:
    LidarPointCloudActor:

<a id="unreal.LidarPointCloudBPLibrary.change_lerp_color_point_cloud_actor_sphere"></a>

#### change\_lerp\_color\_point\_cloud\_actor\_sphere

```python
@classmethod
def change_lerp_color_point_cloud_actor_sphere(
        cls,
        world_context_object: Object,
        point_actor: LidarPointCloudActor,
        colors: Array[LinearColor],
        center: Vector,
        radius: float,
        force_strength: float = 1.000000) -> None
```

X.change_lerp_color_point_cloud_actor_sphere(world_context_object, point_actor, colors, center, radius, force_strength=1.000000) -> None
Change Lerp Color Point Cloud Actor Sphere

Args:
    world_context_object (Object): 
    point_actor (LidarPointCloudActor): 
    colors (Array[LinearColor]): 
    center (Vector): 
    radius (float): 
    force_strength (float):

<a id="unreal.LidarPointCloudBPLibrary.change_lerp_color_point_cloud_actor_by_datas_sphere"></a>

#### change\_lerp\_color\_point\_cloud\_actor\_by\_datas\_sphere

```python
@classmethod
def change_lerp_color_point_cloud_actor_by_datas_sphere(
        cls,
        world_context_object: Object,
        point_actor: LidarPointCloudActor,
        colors: Array[LinearColor],
        datas: Array[Vector4],
        force_strength: float = 1.000000) -> None
```

X.change_lerp_color_point_cloud_actor_by_datas_sphere(world_context_object, point_actor, colors, datas, force_strength=1.000000) -> None
Change Lerp Color Point Cloud Actor by Datas Sphere

Args:
    world_context_object (Object): 
    point_actor (LidarPointCloudActor): 
    colors (Array[LinearColor]): 
    datas (Array[Vector4]): 
    force_strength (float):

<a id="unreal.LidarPointCloudBPLibrary.change_lerp_color_point_cloud_actor_box"></a>

#### change\_lerp\_color\_point\_cloud\_actor\_box

```python
@classmethod
def change_lerp_color_point_cloud_actor_box(
        cls,
        world_context_object: Object,
        point_actor: LidarPointCloudActor,
        colors: Array[LinearColor],
        center: Vector,
        extent: Vector,
        force_strength: float = 1.000000) -> None
```

X.change_lerp_color_point_cloud_actor_box(world_context_object, point_actor, colors, center, extent, force_strength=1.000000) -> None
Change Lerp Color Point Cloud Actor Box

Args:
    world_context_object (Object): 
    point_actor (LidarPointCloudActor): 
    colors (Array[LinearColor]): 
    center (Vector): 
    extent (Vector): 
    force_strength (float):

<a id="unreal.LidarPointCloudBPLibrary.change_color_point_cloud_actor"></a>

#### change\_color\_point\_cloud\_actor

```python
@classmethod
def change_color_point_cloud_actor(cls, world_context_object: Object,
                                   point_actor: LidarPointCloudActor,
                                   new_color: Color, center: Vector,
                                   radius: float) -> None
```

X.change_color_point_cloud_actor(world_context_object, point_actor, new_color, center, radius) -> None
Change Color Point Cloud Actor

Args:
    world_context_object (Object): 
    point_actor (LidarPointCloudActor): 
    new_color (Color): 
    center (Vector): 
    radius (float):

<a id="unreal.LidarPointCloudBPLibrary.change_color_all_point_cloud_actor"></a>

#### change\_color\_all\_point\_cloud\_actor

```python
@classmethod
def change_color_all_point_cloud_actor(cls, world_context_object: Object,
                                       point_actor: LidarPointCloudActor,
                                       new_color: Color) -> None
```

X.change_color_all_point_cloud_actor(world_context_object, point_actor, new_color) -> None
Change Color All Point Cloud Actor

Args:
    world_context_object (Object): 
    point_actor (LidarPointCloudActor): 
    new_color (Color):

<a id="unreal.LightEntity"></a>