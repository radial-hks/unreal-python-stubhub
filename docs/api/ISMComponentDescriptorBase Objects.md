## ISMComponentDescriptorBase Objects

```python
class ISMComponentDescriptorBase(StructBase)
```

Struct that holds the relevant properties that can help decide if instances of different
      StaticMeshComponents/InstancedStaticMeshComponents/HISM can be merged into a single component.

**C++ Source:**

- **Module**: Engine
- **File**: ISMComponentDescriptor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_distance_field_lighting`` (bool):  [Read-Write]
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write]
- ``affect_dynamic_indirect_lighting_while_hidden`` (bool):  [Read-Write]
- ``body_instance`` (BodyInstance):  [Read-Write]
- ``cast_contact_shadow`` (bool):  [Read-Write]
- ``cast_dynamic_shadow`` (bool):  [Read-Write]
- ``cast_hidden_shadow`` (bool):  [Read-Write]
- ``cast_shadow`` (bool):  [Read-Write]
- ``cast_shadow_as_two_sided`` (bool):  [Read-Write]
- ``cast_static_shadow`` (bool):  [Read-Write]
- ``component_class`` (type(Class)):  [Read-Write]
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write]
- ``custom_depth_stencil_value`` (int32):  [Read-Write]
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write]
- ``detail_mode`` (DetailMode):  [Read-Write]
- ``emissive_light_source`` (bool):  [Read-Write]
- ``enable_density_scaling`` (bool):  [Read-Write]
- ``enable_discard_on_load`` (bool):  [Read-Write]
- ``evaluate_world_position_offset`` (bool):  [Read-Write]
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write]
- ``force_navigation_obstacle`` (bool):  [Read-Write]
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``has_custom_navigable_geometry`` (HasCustomNavigableGeometry):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write]
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write]
- ``include_in_hlod`` (bool):  [Read-Write]
- ``instance_end_cull_distance`` (int32):  [Read-Write]
- ``instance_lod_distance_scale`` (float):  [Read-Write]
- ``instance_start_cull_distance`` (int32):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write]
- ``lighting_channels`` (LightingChannels):  [Read-Write]
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``mobility`` (ComponentMobility):  [Read-Write]
- ``overridden_light_map_res`` (int32):  [Read-Write]
- ``override_light_map_res`` (bool):  [Read-Write]
- ``override_navigation_export`` (bool):  [Read-Write]
- ``ray_tracing_group_culling_priority`` (RayTracingGroupCullingPriority):  [Read-Write]
- ``ray_tracing_group_id`` (int32):  [Read-Write]
- ``receives_decals`` (bool):  [Read-Write]
- ``render_custom_depth`` (bool):  [Read-Write]
- ``reverse_culling`` (bool):  [Read-Write]
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write]
- ``translucency_sort_priority`` (int32):  [Read-Write]
- ``use_as_occluder`` (bool):  [Read-Write]
- ``use_default_collision`` (bool):  [Read-Write]
- ``use_gpu_lod_selection`` (bool):  [Read-Write]
- ``virtual_texture_cull_mips`` (int32):  [Read-Write]
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write]
- ``visible`` (bool):  [Read-Write]
- ``visible_in_ray_tracing`` (bool):  [Read-Write]
- ``world_position_offset_disable_distance`` (int32):  [Read-Write]

<a id="unreal.ISMComponentDescriptorBase.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SoftISMComponentDescriptor"></a>