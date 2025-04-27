## MeshMergingSettings Objects

```python
class MeshMergingSettings(StructBase)
```

Mesh merging settings

**C++ Source:**

- **Module**: Engine
- **File**: MeshMergingSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_distance_field`` (bool):  [Read-Write] Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance.
- ``bake_vertex_data_to_mesh`` (bool):  [Read-Write] Whether or not vertex data such as vertex colours should be baked into the resulting mesh
- ``computed_light_map_resolution`` (bool):  [Read-Write] Whether or not the lightmap resolution should be computed by summing the lightmap resolutions for the input Mesh Components
- ``generate_light_map_uv`` (bool):  [Read-Write] Whether to generate lightmap UVs for a merged mesh
- ``gutter_size`` (int32):  [Read-Write] The gutter (in texels) to add to each sub-chart for our baked-out material for the top mip level
- ``include_imposters`` (bool):  [Read-Write] Whether or not to include any imposter LODs that are part of the source static meshes
- ``lod_selection_type`` (MeshLODSelectionType):  [Read-Write] Which selection mode should be used when generating the merged static mesh
- ``material_settings`` (MaterialProxySettings):  [Read-Write] Material simplification
- ``merge_equivalent_materials`` (bool):  [Read-Write] Whether to attempt to merge materials that are deemed equivalent. This can cause artifacts in the merged mesh if world position/actor position etc. is used to determine output color.
- ``merge_materials`` (bool):  [Read-Write] Whether to merge source materials into one flat material, ONLY available when LOD Selection Type is set to LowestDetailLOD
- ``merge_mesh_sockets`` (bool):  [Read-Write] Whether to merge sockets
- ``merge_physics_data`` (bool):  [Read-Write] Whether to merge physics data (collision primitives)
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.
- ``output_u_vs`` (UVOutput):  [Read-Write] Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel)
- ``pivot_point_at_zero`` (bool):  [Read-Write] Whether merged mesh should have pivot at world origin, or at first merged component otherwise
- ``reuse_mesh_lightmap_u_vs`` (bool):  [Read-Write] Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set.
- ``specific_lod`` (int32):  [Read-Write] A given LOD level to export from the source meshes, used if LOD Selection Type is set to SpecificLOD
- ``support_ray_tracing`` (bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.
- ``target_light_map_resolution`` (int32):  [Read-Write] The lightmap resolution used both for generating lightmap UV coordinates, and also set on the generated static mesh
- ``use_landscape_culling`` (bool):  [Read-Write] Whether or not to use available landscape geometry to cull away invisible triangles
- ``use_texture_binning`` (bool):  [Read-Write] Whether or not to calculate varying output texture sizes according to their importance in the final atlas texture
- ``use_vertex_data_for_baking_material`` (bool):  [Read-Write] Whether or not vertex data such as vertex colours should be used when baking out materials

<a id="unreal.MeshMergingSettings.__init__"></a>

#### __init__

```python
def __init__(
    target_light_map_resolution: int = 0,
    material_settings: MaterialProxySettings = [
        TextureSizingType.TEXTURE_SIZING_TYPE_USE_SINGLE_TEXTURE_SIZE,
        5.000000, 0.500000, 10000.000000, 4.000000, 0.000000, 0.500000,
        0.000000, 0.500000, 1.000000, 1.000000, 1.000000,
        BlendMode.BLEND_OPAQUE, True, True, False, False, False, False, False,
        False, False, False, False, [1024, 1024], [1024, 1024], [1024, 1024],
        [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024], [1024, 1024],
        [1024, 1024], [1024, 1024], [1024, 1024]
    ],
    lod_selection_type: MeshLODSelectionType = MeshLODSelectionType.ALL_LO_DS,
    specific_lod: int = 0,
    generate_light_map_uv: bool = False,
    computed_light_map_resolution: bool = False,
    pivot_point_at_zero: bool = False,
    merge_physics_data: bool = False,
    merge_mesh_sockets: bool = False,
    merge_materials: bool = False,
    bake_vertex_data_to_mesh: bool = False,
    use_vertex_data_for_baking_material: bool = False,
    use_texture_binning: bool = False,
    use_landscape_culling: bool = False,
    include_imposters: bool = False,
    support_ray_tracing: bool = False,
    nanite_settings: MeshNaniteSettings = [
        False, False, False, True, -2147483648, -1, -1, 1.000000, 0.000000,
        NaniteFallbackTarget.AUTO, 1.000000, 1.000000, 0.000000, 0
    ]
) -> None
```

<a id="unreal.MeshMergingSettings.target_light_map_resolution"></a>

#### target_light_map_resolution

```python
@property
def target_light_map_resolution() -> int
```

(int32):  [Read-Write] The lightmap resolution used both for generating lightmap UV coordinates, and also set on the generated static mesh

<a id="unreal.MeshMergingSettings.target_light_map_resolution"></a>

#### target_light_map_resolution

```python
@target_light_map_resolution.setter
def target_light_map_resolution(value: int) -> None
```

<a id="unreal.MeshMergingSettings.material_settings"></a>

#### material_settings

```python
@property
def material_settings() -> MaterialProxySettings
```

(MaterialProxySettings):  [Read-Write] Material simplification

<a id="unreal.MeshMergingSettings.material_settings"></a>

#### material_settings

```python
@material_settings.setter
def material_settings(value: MaterialProxySettings) -> None
```

<a id="unreal.MeshMergingSettings.lod_selection_type"></a>

#### lod_selection_type

```python
@property
def lod_selection_type() -> MeshLODSelectionType
```

(MeshLODSelectionType):  [Read-Write] Which selection mode should be used when generating the merged static mesh

<a id="unreal.MeshMergingSettings.lod_selection_type"></a>

#### lod_selection_type

```python
@lod_selection_type.setter
def lod_selection_type(value: MeshLODSelectionType) -> None
```

<a id="unreal.MeshMergingSettings.specific_lod"></a>

#### specific_lod

```python
@property
def specific_lod() -> int
```

(int32):  [Read-Write] A given LOD level to export from the source meshes, used if LOD Selection Type is set to SpecificLOD

<a id="unreal.MeshMergingSettings.specific_lod"></a>

#### specific_lod

```python
@specific_lod.setter
def specific_lod(value: int) -> None
```

<a id="unreal.MeshMergingSettings.generate_light_map_uv"></a>

#### generate_light_map_uv

```python
@property
def generate_light_map_uv() -> bool
```

(bool):  [Read-Write] Whether to generate lightmap UVs for a merged mesh

<a id="unreal.MeshMergingSettings.generate_light_map_uv"></a>

#### generate_light_map_uv

```python
@generate_light_map_uv.setter
def generate_light_map_uv(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.computed_light_map_resolution"></a>

#### computed_light_map_resolution

```python
@property
def computed_light_map_resolution() -> bool
```

(bool):  [Read-Write] Whether or not the lightmap resolution should be computed by summing the lightmap resolutions for the input Mesh Components

<a id="unreal.MeshMergingSettings.computed_light_map_resolution"></a>

#### computed_light_map_resolution

```python
@computed_light_map_resolution.setter
def computed_light_map_resolution(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.pivot_point_at_zero"></a>

#### pivot_point_at_zero

```python
@property
def pivot_point_at_zero() -> bool
```

(bool):  [Read-Write] Whether merged mesh should have pivot at world origin, or at first merged component otherwise

<a id="unreal.MeshMergingSettings.pivot_point_at_zero"></a>

#### pivot_point_at_zero

```python
@pivot_point_at_zero.setter
def pivot_point_at_zero(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.merge_physics_data"></a>

#### merge_physics_data

```python
@property
def merge_physics_data() -> bool
```

(bool):  [Read-Write] Whether to merge physics data (collision primitives)

<a id="unreal.MeshMergingSettings.merge_physics_data"></a>

#### merge_physics_data

```python
@merge_physics_data.setter
def merge_physics_data(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.merge_mesh_sockets"></a>

#### merge_mesh_sockets

```python
@property
def merge_mesh_sockets() -> bool
```

(bool):  [Read-Write] Whether to merge sockets

<a id="unreal.MeshMergingSettings.merge_mesh_sockets"></a>

#### merge_mesh_sockets

```python
@merge_mesh_sockets.setter
def merge_mesh_sockets(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.merge_materials"></a>

#### merge_materials

```python
@property
def merge_materials() -> bool
```

(bool):  [Read-Write] Whether to merge source materials into one flat material, ONLY available when LOD Selection Type is set to LowestDetailLOD

<a id="unreal.MeshMergingSettings.merge_materials"></a>

#### merge_materials

```python
@merge_materials.setter
def merge_materials(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.bake_vertex_data_to_mesh"></a>

#### bake_vertex_data_to_mesh

```python
@property
def bake_vertex_data_to_mesh() -> bool
```

(bool):  [Read-Write] Whether or not vertex data such as vertex colours should be baked into the resulting mesh

<a id="unreal.MeshMergingSettings.bake_vertex_data_to_mesh"></a>

#### bake_vertex_data_to_mesh

```python
@bake_vertex_data_to_mesh.setter
def bake_vertex_data_to_mesh(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.use_vertex_data_for_baking_material"></a>

#### use_vertex_data_for_baking_material

```python
@property
def use_vertex_data_for_baking_material() -> bool
```

(bool):  [Read-Write] Whether or not vertex data such as vertex colours should be used when baking out materials

<a id="unreal.MeshMergingSettings.use_vertex_data_for_baking_material"></a>

#### use_vertex_data_for_baking_material

```python
@use_vertex_data_for_baking_material.setter
def use_vertex_data_for_baking_material(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.use_texture_binning"></a>

#### use_texture_binning

```python
@property
def use_texture_binning() -> bool
```

(bool):  [Read-Write] Whether or not to calculate varying output texture sizes according to their importance in the final atlas texture

<a id="unreal.MeshMergingSettings.use_texture_binning"></a>

#### use_texture_binning

```python
@use_texture_binning.setter
def use_texture_binning(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.use_landscape_culling"></a>

#### use_landscape_culling

```python
@property
def use_landscape_culling() -> bool
```

(bool):  [Read-Write] Whether or not to use available landscape geometry to cull away invisible triangles

<a id="unreal.MeshMergingSettings.use_landscape_culling"></a>

#### use_landscape_culling

```python
@use_landscape_culling.setter
def use_landscape_culling(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.include_imposters"></a>

#### include_imposters

```python
@property
def include_imposters() -> bool
```

(bool):  [Read-Write] Whether or not to include any imposter LODs that are part of the source static meshes

<a id="unreal.MeshMergingSettings.include_imposters"></a>

#### include_imposters

```python
@include_imposters.setter
def include_imposters(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@property
def support_ray_tracing() -> bool
```

(bool):  [Read-Write] Whether ray tracing will be supported on this mesh. Disable this to save memory if the generated mesh will only be rendered in the distance.

<a id="unreal.MeshMergingSettings.support_ray_tracing"></a>

#### support_ray_tracing

```python
@support_ray_tracing.setter
def support_ray_tracing(value: bool) -> None
```

<a id="unreal.MeshMergingSettings.nanite_settings"></a>

#### nanite_settings

```python
@property
def nanite_settings() -> MeshNaniteSettings
```

(MeshNaniteSettings):  [Read-Write] Settings related to building Nanite data.

<a id="unreal.MeshMergingSettings.nanite_settings"></a>

#### nanite_settings

```python
@nanite_settings.setter
def nanite_settings(value: MeshNaniteSettings) -> None
```

<a id="unreal.MeshProxySettings"></a>