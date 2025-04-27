## FoliageType_InstancedStaticMesh Objects

```python
class FoliageType_InstancedStaticMesh(FoliageType)
```

Foliage Type Instanced Static Mesh

**C++ Source:**

- **Module**: Foliage
- **File**: FoliageType_InstancedStaticMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true.
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the foliage should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true.
- ``align_max_angle`` (float):  [Read-Write] The maximum angle in degrees that foliage instances will be adjusted away from the vertical
- ``align_to_normal`` (bool):  [Read-Write] Whether foliage instances should have their angle adjusted away from vertical to match the normal of the surface they're painted on
  If AlignToNormal is enabled and RandomYaw is disabled, the instance will be rotated so that the +X axis points down-slope
- ``average_normal`` (bool):  [Read-Write] Will average normal based on Foliage Type base radius (this as a cost as it will do extra line traces)
- ``average_normal_sample_count`` (int32):  [Read-Write] Line trace count to use around hit location when averaging normal
- ``average_normal_single_component`` (bool):  [Read-Write] Whether to discard normals originating from other hit components or not when averaging normals
- ``average_spread_distance`` (float):  [Read-Write] The average distance between the spreading instance and its seeds. For example, a tree with an AverageSpreadDistance 10 will ensure the average distance between the tree and its seeds is 10cm
- ``body_instance`` (BodyInstance):  [Read-Write] Custom collision for foliage
- ``can_grow_in_shade`` (bool):  [Read-Write] If true, seeds of this type will ignore shade radius during overlap tests with other types.
- ``cast_contact_shadow`` (bool):  [Read-Write] Whether the object should cast contact shadows. This flag is only used if CastShadow is true.
- ``cast_dynamic_shadow`` (bool):  [Read-Write] Controls whether the foliage should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true.
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the foliage should cast a shadow or not.
- ``cast_shadow_as_two_sided`` (bool):  [Read-Write] Whether this foliage should cast dynamic shadows as if it were a two sided material.
- ``cast_static_shadow`` (bool):  [Read-Write] Whether the foliage should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true.
- ``collision_radius`` (float):  [Read-Write] The CollisionRadius determines when two instances overlap. When two instances overlap a winner will be picked based on rules and priority.
- ``collision_scale`` (Vector):  [Read-Write] The foliage instance's collision bounding box will be scaled by the specified amount before performing the overlap check
- ``collision_with_world`` (bool):  [Read-Write] If checked, an overlap test with existing world geometry is performed before each instance is placed
- ``component_class`` (type(Class)):  [Read-Write] The component class to use for foliage instances.
  You can make a Blueprint subclass of FoliageInstancedStaticMeshComponent to implement custom behavior and assign that class here.
- ``cull_distance`` (Int32Interval):  [Read-Write] The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.
  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all.
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_navigable_geometry`` (HasCustomNavigableGeometry):  [Read-Write] Force navmesh
- ``density`` (float):  [Read-Write] Foliage instances will be placed at this density, specified in instances per 1000x1000 unit area
- ``density_adjustment_factor`` (float):  [Read-Write] The factor by which to adjust the density of instances. Values >1 will increase density while values <1 will decrease it.
- ``density_falloff`` (FoliageDensityFalloff):  [Read-Write]
- ``distribution_seed`` (int32):  [Read-Write] The seed that determines placement of initial seeds.
- ``enable_cull_distance_scaling`` (bool):  [Read-Write] * Whether this foliage type should be affected by the Engine's "foliage.CullDistanceScale" setting
- ``enable_density_scaling`` (bool):  [Read-Write] Whether this foliage type should be affected by the Engine Scalability system's Foliage scalability setting.
  Enable for detail meshes that don't really affect the game. Disable for anything important.
  Typically, this will be enabled for small meshes without collision (e.g. grass) and disabled for large meshes with collision (e.g. trees)
- ``enable_discard_on_load`` (bool):  [Read-Write] Whether this foliage type should be discarded when CVarFoliageDiscardDataOnLoad is enabled.
- ``evaluate_world_position_offset`` (bool):  [Read-Write]
- ``exclusion_landscape_layers`` (Array[Name]):  [Read-Write] If layer names are specified, painting on landscape will exclude the foliage to areas of landscape without the specified layers painted
- ``ground_slope_angle`` (FloatInterval):  [Read-Write] Foliage instances will only be placed on surfaces sloping in the specified angle range from the horizontal
- ``height`` (FloatInterval):  [Read-Write] The valid altitude range where foliage instances will be placed, specified using minimum and maximum world coordinate Z values
- ``include_in_hlod`` (bool):  [Read-Write]
- ``initial_seed_density`` (float):  [Read-Write] Specifies the number of seeds to populate along 10 meters. The number is implicitly squared to cover a 10m x 10m area
- ``landscape_layers`` (Array[Name]):  [Read-Write] If layer names are specified, painting on landscape will limit the foliage to areas of landscape with the specified layers painted
- ``lighting_channels`` (LightingChannels):  [Read-Write] Lighting channels that placed foliage will be assigned. Lights with matching channels will affect the foliage.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
- ``lightmap_type`` (LightmapType):  [Read-Write] Controls the type of lightmap used for this component.
- ``max_age`` (float):  [Read-Write] Specifies the oldest a seed can be. After reaching this age the instance will still spread seeds, but will not get any older
- ``max_initial_age`` (float):  [Read-Write] Allows a new seed to be older than 0 when created. New seeds will be randomly assigned an age in the range [0,MaxInitialAge]
- ``max_initial_seed_offset`` (float):  [Read-Write] The seed that determines placement of initial seeds.
- ``mesh`` (StaticMesh):  [Read-Write]
- ``minimum_exclusion_layer_weight`` (float):  [Read-Write] Specifies the minimum value above which the landscape exclusion layer weight value must be, in order for foliage instances to be excluded in a specific area
- ``minimum_layer_weight`` (float):  [Read-Write] Specifies the minimum value above which the landscape layer weight value must be, in order for foliage instances to be placed in a specific area
- ``mobility`` (ComponentMobility):  [Read-Write] Mobility property to apply to foliage components
- ``nanite_override_materials`` (Array[MaterialInterface]):  [Read-Write] Nanite material overrides for foliage instances.
- ``num_steps`` (int32):  [Read-Write] The number of times we age the species and spread its seeds.
- ``overlap_priority`` (float):  [Read-Write] When two instances overlap we must determine which instance to remove.
  The instance with a lower OverlapPriority will be removed.
  In the case where OverlapPriority is the same regular simulation rules apply.
- ``overridden_light_map_res`` (int32):  [Read-Write] Overrides the lightmap resolution defined in the static mesh
- ``override_light_map_res`` (bool):  [Read-Write] Whether to override the lightmap resolution defined in the static mesh.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides for foliage instances.
- ``procedural_scale`` (FloatInterval):  [Read-Write] The scale range of this type when being procedurally generated. Configured with the Scale Curve.
- ``radius`` (float):  [Read-Write] The minimum distance between foliage instances
- ``random_pitch_angle`` (float):  [Read-Write] A random pitch adjustment can be applied to each instance, up to the specified angle in degrees, from the original vertical
- ``random_yaw`` (bool):  [Read-Write] If selected, foliage instances will have a random yaw rotation around their vertical axis applied
- ``reapply_align_to_normal`` (bool):  [Read-Write] If checked, foliage instances will have their normal alignment adjusted by the Reapply tool
- ``reapply_collision_with_world`` (bool):  [Read-Write] If checked, foliage instances will have an overlap test with the world reapplied, and overlapping instances will be removed by the Reapply tool
- ``reapply_density`` (bool):  [Read-Write] If checked, the density of foliage instances already placed will be adjusted by the density adjustment factor.
- ``reapply_ground_slope`` (bool):  [Read-Write] If checked, foliage instances not meeting the ground slope condition will be removed by the Reapply too
- ``reapply_height`` (bool):  [Read-Write] If checked, foliage instances not meeting the valid Z height condition will be removed by the Reapply tool
- ``reapply_landscape_layers`` (bool):  [Read-Write] If checked, foliage instances painted on areas that do not have the appropriate landscape layer painted will be removed by the Reapply tool
- ``reapply_radius`` (bool):  [Read-Write] If checked, foliage instances not meeting the new Radius constraint will be removed
- ``reapply_random_pitch_angle`` (bool):  [Read-Write] If checked, foliage instances will have their pitch adjusted by the Reapply tool
- ``reapply_random_yaw`` (bool):  [Read-Write] If checked, foliage instances will have their yaw adjusted by the Reapply tool
- ``reapply_scale_x`` (bool):  [Read-Write] If checked, foliage instances will have their X scale adjusted by the Reapply tool
- ``reapply_scale_y`` (bool):  [Read-Write] If checked, foliage instances will have their Y scale adjusted by the Reapply tool
- ``reapply_scale_z`` (bool):  [Read-Write] If checked, foliage instances will have their Z scale adjusted by the Reapply tool
- ``reapply_scaling`` (bool):  [Read-Write] If checked, foliage instances will have their scale adjusted to fit the specified scaling behavior by the Reapply tool
- ``reapply_vertex_color_mask`` (bool):  [Read-Write] If checked, foliage instances no longer matching the vertex color constraint will be removed by the Reapply too
- ``reapply_z_offset`` (bool):  [Read-Write] If checked, foliage instances will have their Z offset adjusted by the Reapply tool
- ``receives_decals`` (bool):  [Read-Write] Whether the foliage receives decals.
- ``render_custom_depth`` (bool):  [Read-Write] If true, the foliage will be rendered in the CustomDepth pass (usually used for outlines)
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the instances.
  The mesh material also needs to be set up to output to a virtual texture.
- ``scale_curve`` (RuntimeFloatCurve):  [Read-Write] Instance scale factor as a function of normalized age (i.e. Current Age / Max Age).
  X = 0 corresponds to Age = 0, X = 1 corresponds to Age = Max Age.
  Y = 0 corresponds to Min Scale, Y = 1 corresponds to Max Scale.
- ``scale_x`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's X Scale property
- ``scale_y`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Y Scale property
- ``scale_z`` (FloatInterval):  [Read-Write] Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Z Scale property
- ``scaling`` (FoliageScaling):  [Read-Write] Specifies foliage instance scaling behavior when painting.
- ``seeds_per_step`` (int32):  [Read-Write] The number of seeds an instance will spread in a single step of the simulation.
- ``shade_radius`` (float):  [Read-Write] The ShadeRadius determines when two instances overlap. If an instance can grow in the shade this radius is ignored.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``single_instance_mode_override_radius`` (bool):  [Read-Write] Option to override radius used to detect collision with other instances when painting in single instance mode
- ``single_instance_mode_radius`` (float):  [Read-Write] The radius used in single instance mode to detect collision with other instances
- ``spawns_in_shade`` (bool):  [Read-Write] Whether new seeds are spawned exclusively in shade. Occurs in a second pass after all types that do not spawn in shade have been simulated.
  Only valid when CanGrowInShade is true.
- ``spread_variance`` (float):  [Read-Write] Specifies how much seed distance varies from the average. For example, a tree with an AverageSpreadDistance 10 and a SpreadVariance 1 will produce seeds with an average distance of 10cm plus or minus 1cm
- ``translucency_sort_priority`` (int32):  [Read-Write] Translucent objects with a lower sort priority draw behind objects with a higher priority.
  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
  This setting is also used to sort objects being drawn into a runtime virtual texture.

  Ignored if the object is not translucent.  The default priority is zero.
  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.
  It is especially problematic on dynamic gameplay effects.
- ``use_as_occluder`` (bool):  [Read-Write] If enabled, foliage will render a pre-pass which allows it to occlude other primitives, and also allows
  it to correctly receive DBuffer decals. Enabling this setting may have a negative performance impact.
- ``vertex_color_mask_by_channel`` (FoliageVertexColorChannelMask):  [Read-Write]
- ``virtual_texture_cull_mips`` (int32):  [Read-Write] Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
  Larger values reduce the effective draw distance in the runtime virtual texture.
  This culling method doesn't take into account primitive size or virtual texture size.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``visible_in_ray_tracing`` (bool):  [Read-Write]
- ``world_position_offset_disable_distance`` (int32):  [Read-Write]
- ``z_offset`` (FloatInterval):  [Read-Write] Specifies a range from minimum to maximum of the offset to apply to a foliage instance's Z location

<a id="unreal.FoliageType_InstancedStaticMesh.mesh"></a>

#### mesh

```python
@property
def mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.FoliageType_InstancedStaticMesh.mesh"></a>

#### mesh

```python
@mesh.setter
def mesh(value: StaticMesh) -> None
```

<a id="unreal.FoliageType_InstancedStaticMesh.override_materials"></a>

#### override_materials

```python
@property
def override_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write] Material overrides for foliage instances.

<a id="unreal.FoliageType_InstancedStaticMesh.override_materials"></a>

#### override_materials

```python
@override_materials.setter
def override_materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.FoliageType_InstancedStaticMesh.nanite_override_materials"></a>

#### nanite_override_materials

```python
@property
def nanite_override_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write] Nanite material overrides for foliage instances.

<a id="unreal.FoliageType_InstancedStaticMesh.nanite_override_materials"></a>

#### nanite_override_materials

```python
@nanite_override_materials.setter
def nanite_override_materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.InstancedFoliageSettings"></a>