## MeshProxySettings Objects

```python
class MeshProxySettings(StructBase)
```

Mesh Proxy Settings

**C++ Source:**

- **Module**: Engine
- **File**: MeshProxySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_distance_field`` (bool):  [Read-Write] Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance.
- ``allow_vertex_colors`` (bool):  [Read-Write] Whether to allow vertex colors saved in the merged mesh
- ``calculate_correct_lod_model`` (bool):  [Read-Write] Determines whether or not the correct LOD models should be calculated given the source meshes and transition size
- ``compute_light_map_resolution`` (bool):  [Read-Write] If ticked will compute the lightmap resolution by summing the dimensions for each mesh included for merging
- ``create_collision`` (bool):  [Read-Write] Whether to generate collision for the merged mesh
- ``generate_lightmap_u_vs`` (bool):  [Read-Write] Whether to generate lightmap uvs for the merged mesh
- ``group_identical_meshes_for_baking`` (bool):  [Read-Write] Bake identical meshes (or mesh instances) only once. Can lead to discrepancies with the source mesh visual, especially for materials that are using world position or per instance data. However, this will result in better quality baked textures & greatly reduce baking time.
- ``hard_angle_threshold`` (float):  [Read-Write] Angle at which a hard edge is introduced between faces
- ``landscape_culling_precision`` (LandscapeCullingPrecision):  [Read-Write] Level of detail of the landscape that should be used for the culling
- ``light_map_resolution`` (int32):  [Read-Write] Lightmap resolution
- ``material_settings`` (MaterialProxySettings):  [Read-Write] Material simplification
- ``max_ray_cast_dist`` (float):  [Read-Write] Override search distance used when discovering texture values for simplified geometry. Useful when non-zero Merge Distance setting generates new geometry in concave corners.
- ``merge_distance`` (float):  [Read-Write] Distance at which meshes should be merged together, this can close gaps like doors and windows in distant geometry
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.
- ``normal_calculation_method`` (ProxyNormalComputationMethod):  [Read-Write] Controls the method used to calculate the normal for the simplified geometry
- ``override_transfer_distance`` (bool):  [Read-Write] Enable an override for material transfer distance
- ``override_voxel_size`` (bool):  [Read-Write] If true, Spatial Sampling Distance will not be automatically computed based on geometry and you must set it directly
- ``recalculate_normals`` (bool):  [Read-Write] Whether Simplygon should recalculate normals, otherwise the normals channel will be sampled from the original mesh
- ``reuse_mesh_lightmap_u_vs`` (bool):  [Read-Write] Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set.
- ``screen_size`` (int32):  [Read-Write] Screen size of the resulting proxy mesh in pixels
- ``support_ray_tracing`` (bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.
- ``unresolved_geometry_color`` (Color):  [Read-Write] Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance
- ``use_hard_angle_threshold`` (bool):  [Read-Write] Enable the use of hard angle based vertex splitting
- ``use_landscape_culling`` (bool):  [Read-Write] Whether or not to use available landscape geometry to cull away invisible triangles
- ``voxel_size`` (float):  [Read-Write] Override when converting multiple meshes for proxy LOD merging. Warning, large geometry with small sampling has very high memory costs

<a id="unreal.MeshProxySettings.__init__"></a>

#### __init__

```python
def __init__(
    screen_size: int = 0,
    voxel_size: float = 0.000000,
    material_settings: MaterialProxySettings = [
        TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
        5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000,
        0.000000, 0.500000, 1.000000, 1.000000, 1.000000,
        BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False,
        False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024],
        [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024],
        [1024, 1024], [1024, 1024], [1024, 1024]
    ],
    merge_distance: float = 0.000000,
    unresolved_geometry_color: Color = [0, 0, 0, 0],
    max_ray_cast_dist: float = 0.000000,
    hard_angle_threshold: float = 0.000000,
    light_map_resolution: int = 0,
    normal_calculation_method:
    ProxyNormalComputationMethod = ProxyNormalComputationMethod.ANGLE_WEIGHTED,
    landscape_culling_precision:
    LandscapeCullingPrecision = LandscapeCullingPrecision.HIGH,
    calculate_correct_lod_model: bool = False,
    override_voxel_size: bool = False,
    override_transfer_distance: bool = False,
    use_hard_angle_threshold: bool = False,
    compute_light_map_resolution: bool = False,
    recalculate_normals: bool = False,
    use_landscape_culling: bool = False,
    support_ray_tracing: bool = False,
    allow_distance_field: bool = False,
    reuse_mesh_lightmap_u_vs: bool = False,
    group_identical_meshes_for_baking: bool = False,
    create_collision: bool = False,
    allow_vertex_colors: bool = False,
    generate_lightmap_u_vs: bool = False,
    nanite_settings: MeshNaniteSettings = [
        False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000,
        NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0
    ]
) -> None
```

<a id="unreal.MeshProxySettings.screen_size"></a>

#### screen_size

```python
@property
def screen_size() -> int
```

(int32):  [Read-Write] Screen size of the resulting proxy mesh in pixels

<a id="unreal.MeshProxySettings.screen_size"></a>

#### screen_size

```python
@screen_size.setter
def screen_size(value: int) -> None
```

<a id="unreal.MeshProxySettings.voxel_size"></a>

#### voxel_size

```python
@property
def voxel_size() -> float
```

(float):  [Read-Write] Override when converting multiple meshes for proxy LOD merging. Warning, large geometry with small sampling has very high memory costs

<a id="unreal.MeshProxySettings.voxel_size"></a>

#### voxel_size

```python
@voxel_size.setter
def voxel_size(value: float) -> None
```

<a id="unreal.MeshProxySettings.material_settings"></a>

#### material_settings

```python
@property
def material_settings() -> MaterialProxySettings
```

(MaterialProxySettings):  [Read-Write] Material simplification

<a id="unreal.MeshProxySettings.material_settings"></a>

#### material_settings

```python
@material_settings.setter
def material_settings(value: MaterialProxySettings) -> None
```

<a id="unreal.MeshProxySettings.merge_distance"></a>

#### merge_distance

```python
@property
def merge_distance() -> float
```

(float):  [Read-Write] Distance at which meshes should be merged together, this can close gaps like doors and windows in distant geometry

<a id="unreal.MeshProxySettings.merge_distance"></a>

#### merge_distance

```python
@merge_distance.setter
def merge_distance(value: float) -> None
```

<a id="unreal.MeshProxySettings.unresolved_geometry_color"></a>

#### unresolved_geometry_color

```python
@property
def unresolved_geometry_color() -> Color
```

(Color):  [Read-Write] Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance

<a id="unreal.MeshProxySettings.unresolved_geometry_color"></a>

#### unresolved_geometry_color

```python
@unresolved_geometry_color.setter
def unresolved_geometry_color(value: Color) -> None
```

<a id="unreal.MeshProxySettings.max_ray_cast_dist"></a>

#### max_ray_cast_dist

```python
@property
def max_ray_cast_dist() -> float
```

(float):  [Read-Write] Override search distance used when discovering texture values for simplified geometry. Useful when non-zero Merge Distance setting generates new geometry in concave corners.

<a id="unreal.MeshProxySettings.max_ray_cast_dist"></a>

#### max_ray_cast_dist

```python
@max_ray_cast_dist.setter
def max_ray_cast_dist(value: float) -> None
```

<a id="unreal.MeshProxySettings.hard_angle_threshold"></a>

#### hard_angle_threshold

```python
@property
def hard_angle_threshold() -> float
```

(float):  [Read-Write] Angle at which a hard edge is introduced between faces

<a id="unreal.MeshProxySettings.hard_angle_threshold"></a>

#### hard_angle_threshold

```python
@hard_angle_threshold.setter
def hard_angle_threshold(value: float) -> None
```

<a id="unreal.MeshProxySettings.light_map_resolution"></a>

#### light_map_resolution

```python
@property
def light_map_resolution() -> int
```

(int32):  [Read-Write] Lightmap resolution

<a id="unreal.MeshProxySettings.light_map_resolution"></a>

#### light_map_resolution

```python
@light_map_resolution.setter
def light_map_resolution(value: int) -> None
```

<a id="unreal.MeshProxySettings.normal_calculation_method"></a>

#### normal_calculation_method

```python
@property
def normal_calculation_method() -> ProxyNormalComputationMethod
```

(ProxyNormalComputationMethod):  [Read-Write] Controls the method used to calculate the normal for the simplified geometry

<a id="unreal.MeshProxySettings.normal_calculation_method"></a>

#### normal_calculation_method

```python
@normal_calculation_method.setter
def normal_calculation_method(value: ProxyNormalComputationMethod) -> None
```

<a id="unreal.MeshProxySettings.landscape_culling_precision"></a>

#### landscape_culling_precision

```python
@property
def landscape_culling_precision() -> LandscapeCullingPrecision
```

(LandscapeCullingPrecision):  [Read-Write] Level of detail of the landscape that should be used for the culling

<a id="unreal.MeshProxySettings.landscape_culling_precision"></a>

#### landscape_culling_precision

```python
@landscape_culling_precision.setter
def landscape_culling_precision(value: LandscapeCullingPrecision) -> None
```

<a id="unreal.MeshProxySettings.calculate_correct_lod_model"></a>

#### calculate_correct_lod_model

```python
@property
def calculate_correct_lod_model() -> bool
```

(bool):  [Read-Write] Determines whether or not the correct LOD models should be calculated given the source meshes and transition size

<a id="unreal.MeshProxySettings.calculate_correct_lod_model"></a>

#### calculate_correct_lod_model

```python
@calculate_correct_lod_model.setter
def calculate_correct_lod_model(value: bool) -> None
```

<a id="unreal.MeshProxySettings.override_voxel_size"></a>

#### override_voxel_size

```python
@property
def override_voxel_size() -> bool
```

(bool):  [Read-Write] If true, Spatial Sampling Distance will not be automatically computed based on geometry and you must set it directly

<a id="unreal.MeshProxySettings.override_voxel_size"></a>

#### override_voxel_size

```python
@override_voxel_size.setter
def override_voxel_size(value: bool) -> None
```

<a id="unreal.MeshProxySettings.override_transfer_distance"></a>

#### override_transfer_distance

```python
@property
def override_transfer_distance() -> bool
```

(bool):  [Read-Write] Enable an override for material transfer distance

<a id="unreal.MeshProxySettings.override_transfer_distance"></a>

#### override_transfer_distance

```python
@override_transfer_distance.setter
def override_transfer_distance(value: bool) -> None
```

<a id="unreal.MeshProxySettings.use_hard_angle_threshold"></a>

#### use_hard_angle_threshold

```python
@property
def use_hard_angle_threshold() -> bool
```

(bool):  [Read-Write] Enable the use of hard angle based vertex splitting

<a id="unreal.MeshProxySettings.use_hard_angle_threshold"></a>

#### use_hard_angle_threshold

```python
@use_hard_angle_threshold.setter
def use_hard_angle_threshold(value: bool) -> None
```

<a id="unreal.MeshProxySettings.compute_light_map_resolution"></a>

#### compute_light_map_resolution

```python
@property
def compute_light_map_resolution() -> bool
```

(bool):  [Read-Write] If ticked will compute the lightmap resolution by summing the dimensions for each mesh included for merging

<a id="unreal.MeshProxySettings.compute_light_map_resolution"></a>

#### compute_light_map_resolution

```python
@compute_light_map_resolution.setter
def compute_light_map_resolution(value: bool) -> None
```

<a id="unreal.MeshProxySettings.recalculate_normals"></a>

#### recalculate_normals

```python
@property
def recalculate_normals() -> bool
```

(bool):  [Read-Write] Whether Simplygon should recalculate normals, otherwise the normals channel will be sampled from the original mesh

<a id="unreal.MeshProxySettings.recalculate_normals"></a>

#### recalculate_normals

```python
@recalculate_normals.setter
def recalculate_normals(value: bool) -> None
```

<a id="unreal.MeshProxySettings.use_landscape_culling"></a>

#### use_landscape_culling

```python
@property
def use_landscape_culling() -> bool
```

(bool):  [Read-Write] Whether or not to use available landscape geometry to cull away invisible triangles

<a id="unreal.MeshProxySettings.use_landscape_culling"></a>

#### use_landscape_culling

```python
@use_landscape_culling.setter
def use_landscape_culling(value: bool) -> None
```

<a id="unreal.MeshProxySettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@property
def support_ray_tracing() -> bool
```

(bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.

<a id="unreal.MeshProxySettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@support_ray_tracing.setter
def support_ray_tracing(value: bool) -> None
```

<a id="unreal.MeshProxySettings.allow_distance_field"></a>

#### allow_distance_field

```python
@property
def allow_distance_field() -> bool
```

(bool):  [Read-Write] Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance.

<a id="unreal.MeshProxySettings.allow_distance_field"></a>

#### allow_distance_field

```python
@allow_distance_field.setter
def allow_distance_field(value: bool) -> None
```

<a id="unreal.MeshProxySettings.reuse_mesh_lightmap_u_vs"></a>

#### reuse_mesh_lightmap_u_vs

```python
@property
def reuse_mesh_lightmap_u_vs() -> bool
```

(bool):  [Read-Write] Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set.

<a id="unreal.MeshProxySettings.reuse_mesh_lightmap_u_vs"></a>

#### reuse_mesh_lightmap_u_vs

```python
@reuse_mesh_lightmap_u_vs.setter
def reuse_mesh_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.MeshProxySettings.group_identical_meshes_for_baking"></a>

#### group_identical_meshes_for_baking

```python
@property
def group_identical_meshes_for_baking() -> bool
```

(bool):  [Read-Write] Bake identical meshes (or mesh instances) only once. Can lead to discrepancies with the source mesh visual, especially for materials that are using world position or per instance data. However, this will result in better quality baked textures & greatly reduce baking time.

<a id="unreal.MeshProxySettings.group_identical_meshes_for_baking"></a>

#### group_identical_meshes_for_baking

```python
@group_identical_meshes_for_baking.setter
def group_identical_meshes_for_baking(value: bool) -> None
```

<a id="unreal.MeshProxySettings.create_collision"></a>

#### create_collision

```python
@property
def create_collision() -> bool
```

(bool):  [Read-Write] Whether to generate collision for the merged mesh

<a id="unreal.MeshProxySettings.create_collision"></a>

#### create_collision

```python
@create_collision.setter
def create_collision(value: bool) -> None
```

<a id="unreal.MeshProxySettings.allow_vertex_colors"></a>

#### allow_vertex_colors

```python
@property
def allow_vertex_colors() -> bool
```

(bool):  [Read-Write] Whether to allow vertex colors saved in the merged mesh

<a id="unreal.MeshProxySettings.allow_vertex_colors"></a>

#### allow_vertex_colors

```python
@allow_vertex_colors.setter
def allow_vertex_colors(value: bool) -> None
```

<a id="unreal.MeshProxySettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write] Whether to generate lightmap uvs for the merged mesh

<a id="unreal.MeshProxySettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.MeshProxySettings.nanite_settings"></a>

#### nanite_settings

```python
@property
def nanite_settings() -> MeshNaniteSettings
```

(MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.

<a id="unreal.MeshProxySettings.nanite_settings"></a>

#### nanite_settings

```python
@nanite_settings.setter
def nanite_settings(value: MeshNaniteSettings) -> None
```

<a id="unreal.BoneAnimationTrack"></a>