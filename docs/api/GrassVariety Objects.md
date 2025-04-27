## GrassVariety Objects

```python
class GrassVariety(StructBase)
```

Grass Variety

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeGrassType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.
- ``align_to_surface`` (bool):  [Read-Write] Whether the grass instances should be tilted to the normal of the landscape (true), or always vertical (false)
- ``allowed_density_range`` (FloatInterval):  [Read-Write] Specifies the density range where the grass variety is allowed to be spawned ([0,1] represents the entire range).
- ``cast_contact_shadow`` (bool):  [Read-Write] Whether the grass should cast contact shadows. *
- ``cast_dynamic_shadow`` (bool):  [Read-Write] Whether the grass should cast shadows when using non-precomputed shadowing. *
- ``end_cull_distance`` (PerPlatformInt):  [Read-Write] The distance where instances will have completely faded out when using a PerInstanceFadeAmount material node. 0 disables.
  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all.
- ``end_cull_distance_quality`` (PerQualityLevelInt):  [Read-Write]
- ``grass_density`` (PerPlatformFloat):  [Read-Write] Instances per 10 square meters.
- ``grass_density_quality`` (PerQualityLevelFloat):  [Read-Write]
- ``grass_mesh`` (StaticMesh):  [Read-Write]
- ``instance_world_position_offset_disable_distance`` (uint32):  [Read-Write] Distance at which to grass instances should disable WPO for performance reasons
- ``keep_instance_buffer_cpu_copy`` (bool):  [Read-Write] Whether we should keep a cpu copy of the instance buffer. This should be set to true if you plan on using GetOverlappingXXXXCount functions of the component otherwise it won't return any data.*
- ``lighting_channels`` (LightingChannels):  [Read-Write] Lighting channels that the grass will be assigned. Lights with matching channels will affect the grass.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
- ``max_scale_weight_attenuation`` (float):  [Read-Write] Modulate the scale of the instances based on weight (normalized density). The weight range (ScaleWeightAttenuation, 1.0) maps to (scaleMin, scaleMax), weight values less than ScaleWeightAttenuation are set to minScale
- ``min_lod`` (int32):  [Read-Write] Specifies the smallest LOD that will be used for this component.
  If -1 (default), the MinLOD of the static mesh asset will be used instead.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material Overrides.
- ``placement_jitter`` (float):  [Read-Write]
- ``random_rotation`` (bool):  [Read-Write] Whether the grass instances should be placed at random rotation (true) or all at the same rotation (false)
- ``receives_decals`` (bool):  [Read-Write] Whether the grass instances should receive decals.
- ``scale_x`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's X Scale property
- ``scale_y`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Y Scale property
- ``scale_z`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Z Scale property
- ``scaling`` (GrassScaling):  [Read-Write] Specifies grass instance scaling type
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``start_cull_distance`` (PerPlatformInt):  [Read-Write] The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.
- ``start_cull_distance_quality`` (PerQualityLevelInt):  [Read-Write]
- ``use_grid`` (bool):  [Read-Write] If true, use a jittered grid sequence for placement, otherwise use a halton sequence.
- ``use_landscape_lightmap`` (bool):  [Read-Write] Whether to use the landscape's lightmap when rendering the grass.
- ``weight_attenuates_max_scale`` (bool):  [Read-Write] If enabled the the scale of instances is reduced as the weight (density) decreases

<a id="unreal.GrassVariety.__init__"></a>

#### __init__

```python
def __init__(
    grass_mesh: StaticMesh = None,
    override_materials: Array[MaterialInterface] = [],
    grass_density: PerPlatformFloat = [0.000000],
    grass_density_quality: PerQualityLevelFloat = [0.000000],
    use_grid: bool = False,
    placement_jitter: float = 0.000000,
    start_cull_distance: PerPlatformInt = [0],
    start_cull_distance_quality: PerQualityLevelInt = [0],
    end_cull_distance: PerPlatformInt = [0],
    end_cull_distance_quality: PerQualityLevelInt = [0],
    min_lod: int = 0,
    allowed_density_range: FloatInterval = [0.000000, 0.000000],
    scaling: GrassScaling = GrassScaling.UNIFORM,
    scale_x: FloatInterval = [0.000000, 0.000000],
    scale_y: FloatInterval = [0.000000, 0.000000],
    scale_z: FloatInterval = [0.000000, 0.000000],
    weight_attenuates_max_scale: bool = False,
    max_scale_weight_attenuation: float = 0.000000,
    random_rotation: bool = False,
    align_to_surface: bool = False,
    use_landscape_lightmap: bool = False,
    lighting_channels: LightingChannels = [True, False, False],
    receives_decals: bool = False,
    affect_distance_field_lighting: bool = False,
    cast_dynamic_shadow: bool = False,
    cast_contact_shadow: bool = False,
    keep_instance_buffer_cpu_copy: bool = False,
    shadow_cache_invalidation_behavior:
    ShadowCacheInvalidationBehavior = ShadowCacheInvalidationBehavior.AUTO
) -> None
```

<a id="unreal.GrassVariety.grass_mesh"></a>

#### grass_mesh

```python
@property
def grass_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Only]

<a id="unreal.GrassVariety.override_materials"></a>

#### override_materials

```python
@property
def override_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Only] Material Overrides.

<a id="unreal.GrassVariety.grass_density"></a>

#### grass_density

```python
@property
def grass_density() -> PerPlatformFloat
```

(PerPlatformFloat):  [Read-Only] Instances per 10 square meters.

<a id="unreal.GrassVariety.grass_density_quality"></a>

#### grass_density_quality

```python
@property
def grass_density_quality() -> PerQualityLevelFloat
```

(PerQualityLevelFloat):  [Read-Only]

<a id="unreal.GrassVariety.use_grid"></a>

#### use_grid

```python
@property
def use_grid() -> bool
```

(bool):  [Read-Only] If true, use a jittered grid sequence for placement, otherwise use a halton sequence.

<a id="unreal.GrassVariety.placement_jitter"></a>

#### placement_jitter

```python
@property
def placement_jitter() -> float
```

(float):  [Read-Only]

<a id="unreal.GrassVariety.start_cull_distance"></a>

#### start_cull_distance

```python
@property
def start_cull_distance() -> PerPlatformInt
```

(PerPlatformInt):  [Read-Only] The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.

<a id="unreal.GrassVariety.start_cull_distance_quality"></a>

#### start_cull_distance_quality

```python
@property
def start_cull_distance_quality() -> PerQualityLevelInt
```

(PerQualityLevelInt):  [Read-Only]

<a id="unreal.GrassVariety.end_cull_distance"></a>

#### end_cull_distance

```python
@property
def end_cull_distance() -> PerPlatformInt
```

(PerPlatformInt):  [Read-Only] The distance where instances will have completely faded out when using a PerInstanceFadeAmount material node. 0 disables.
When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all.

<a id="unreal.GrassVariety.end_cull_distance_quality"></a>

#### end_cull_distance_quality

```python
@property
def end_cull_distance_quality() -> PerQualityLevelInt
```

(PerQualityLevelInt):  [Read-Only]

<a id="unreal.GrassVariety.min_lod"></a>

#### min_lod

```python
@property
def min_lod() -> int
```

(int32):  [Read-Only] Specifies the smallest LOD that will be used for this component.
If -1 (default), the MinLOD of the static mesh asset will be used instead.

<a id="unreal.GrassVariety.allowed_density_range"></a>

#### allowed_density_range

```python
@property
def allowed_density_range() -> FloatInterval
```

(FloatInterval):  [Read-Only] Specifies the density range where the grass variety is allowed to be spawned ([0,1] represents the entire range).

<a id="unreal.GrassVariety.scaling"></a>

#### scaling

```python
@property
def scaling() -> GrassScaling
```

(GrassScaling):  [Read-Only] Specifies grass instance scaling type

<a id="unreal.GrassVariety.scale_x"></a>

#### scale_x

```python
@property
def scale_x() -> FloatInterval
```

(FloatInterval):  [Read-Only] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's X Scale property

<a id="unreal.GrassVariety.scale_y"></a>

#### scale_y

```python
@property
def scale_y() -> FloatInterval
```

(FloatInterval):  [Read-Only] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Y Scale property

<a id="unreal.GrassVariety.scale_z"></a>

#### scale_z

```python
@property
def scale_z() -> FloatInterval
```

(FloatInterval):  [Read-Only] Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Z Scale property

<a id="unreal.GrassVariety.weight_attenuates_max_scale"></a>

#### weight_attenuates_max_scale

```python
@property
def weight_attenuates_max_scale() -> bool
```

(bool):  [Read-Only] If enabled the the scale of instances is reduced as the weight (density) decreases

<a id="unreal.GrassVariety.max_scale_weight_attenuation"></a>

#### max_scale_weight_attenuation

```python
@property
def max_scale_weight_attenuation() -> float
```

(float):  [Read-Only] Modulate the scale of the instances based on weight (normalized density). The weight range (ScaleWeightAttenuation, 1.0) maps to (scaleMin, scaleMax), weight values less than ScaleWeightAttenuation are set to minScale

<a id="unreal.GrassVariety.random_rotation"></a>

#### random_rotation

```python
@property
def random_rotation() -> bool
```

(bool):  [Read-Only] Whether the grass instances should be placed at random rotation (true) or all at the same rotation (false)

<a id="unreal.GrassVariety.align_to_surface"></a>

#### align_to_surface

```python
@property
def align_to_surface() -> bool
```

(bool):  [Read-Only] Whether the grass instances should be tilted to the normal of the landscape (true), or always vertical (false)

<a id="unreal.GrassVariety.use_landscape_lightmap"></a>

#### use_landscape_lightmap

```python
@property
def use_landscape_lightmap() -> bool
```

(bool):  [Read-Only] Whether to use the landscape's lightmap when rendering the grass.

<a id="unreal.GrassVariety.lighting_channels"></a>

#### lighting_channels

```python
@property
def lighting_channels() -> LightingChannels
```

(LightingChannels):  [Read-Only] Lighting channels that the grass will be assigned. Lights with matching channels will affect the grass.
These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.

<a id="unreal.GrassVariety.receives_decals"></a>

#### receives_decals

```python
@property
def receives_decals() -> bool
```

(bool):  [Read-Only] Whether the grass instances should receive decals.

<a id="unreal.GrassVariety.affect_distance_field_lighting"></a>

#### affect_distance_field_lighting

```python
@property
def affect_distance_field_lighting() -> bool
```

(bool):  [Read-Only] Controls whether the primitive should affect dynamic distance field lighting methods.

<a id="unreal.GrassVariety.cast_dynamic_shadow"></a>

#### cast_dynamic_shadow

```python
@property
def cast_dynamic_shadow() -> bool
```

(bool):  [Read-Only] Whether the grass should cast shadows when using non-precomputed shadowing. *

<a id="unreal.GrassVariety.cast_contact_shadow"></a>

#### cast_contact_shadow

```python
@property
def cast_contact_shadow() -> bool
```

(bool):  [Read-Only] Whether the grass should cast contact shadows. *

<a id="unreal.GrassVariety.keep_instance_buffer_cpu_copy"></a>

#### keep_instance_buffer_cpu_copy

```python
@property
def keep_instance_buffer_cpu_copy() -> bool
```

(bool):  [Read-Only] Whether we should keep a cpu copy of the instance buffer. This should be set to true if you plan on using GetOverlappingXXXXCount functions of the component otherwise it won't return any data.*

<a id="unreal.GrassVariety.shadow_cache_invalidation_behavior"></a>

#### shadow_cache_invalidation_behavior

```python
@property
def shadow_cache_invalidation_behavior() -> ShadowCacheInvalidationBehavior
```

(ShadowCacheInvalidationBehavior):  [Read-Only] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.

<a id="unreal.PerQualityLevelInt"></a>