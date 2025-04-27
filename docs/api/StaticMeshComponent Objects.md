## StaticMeshComponent Objects

```python
class StaticMeshComponent(MeshComponent)
```

StaticMeshComponent is used to create an instance of a UStaticMesh.
A static mesh is a piece of geometry that consists of a static set of polygons.
see: https://docs.unrealengine.com/latest/INT/Engine/Content/Types/StaticMeshes/
see: UStaticMesh

**C++ Source:**

- **Module**: Engine
- **File**: StaticMeshComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``apply_impulse_on_damage`` (bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``body_instance`` (BodyInstance):  [Read-Write] Physics scene information for this component, holds a single rigid body with multiple shapes.
- ``bounds_scale`` (float):  [Read-Write] Scales the bounds of the object.
  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.
  Warning: Increasing the bounds of an object will reduce performance and shadow quality!
  Currently only used by StaticMeshComponent and SkeletalMeshComponent.
- ``cached_max_draw_distance`` (float):  [Read-Only] The distance to cull this primitive at.
  A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance.
- ``can_character_step_up_on`` (CanBeCharacterBase):  [Read-Write] Determine whether a Character can step up onto this component.
  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.
  see: FWalkableSlopeOverride
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_cinematic_shadow`` (bool):  [Read-Write] Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.
  This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired.
- ``cast_contact_shadow`` (bool):  [Read-Write] Whether the object should cast contact shadows.
  This flag is only used if CastShadow is true.
- ``cast_distance_field_indirect_shadow`` (bool):  [Read-Write] Whether to use the mesh distance field representation (when present) for shadowing indirect lighting (from lightmaps or skylight) on Movable components.
  This works like capsule shadows on skeletal meshes, except using the mesh distance field so no physics asset is required.
  The StaticMesh must have 'Generate Mesh Distance Field' enabled, or the project must have 'Generate Mesh Distance Fields' enabled for this feature to work.
- ``cast_dynamic_shadow`` (bool):  [Read-Write] Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. *
- ``cast_far_shadow`` (bool):  [Read-Write] When enabled, the component will be rendering into the far shadow cascades (only for directional lights).
- ``cast_hidden_shadow`` (bool):  [Read-Write] If true, the primitive will cast shadows even if bHidden is true.
  Controls whether the primitive should cast shadows when hidden.
  This flag is only used if CastShadow is true.
- ``cast_inset_shadow`` (bool):  [Read-Write] Whether this component should create a per-object shadow that gives higher effective shadow resolution.
  Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled.
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the primitive component should cast a shadow or not.
- ``cast_shadow_as_two_sided`` (bool):  [Read-Write] Whether this primitive should cast dynamic shadows as if it were a two sided material.
- ``cast_static_shadow`` (bool):  [Read-Write] Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true.
- ``cast_volumetric_translucent_shadow`` (bool):  [Read-Write] Whether the object should cast a volumetric translucent shadow.
  Volumetric translucent shadows are useful for primitives with smoothly changing opacity like particles representing a volume,
  But have artifacts when used on highly opaque surfaces.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``disallow_nanite`` (bool):  [Read-Write] Forces this component to use fallback mesh for rendering if Nanite is enabled on the mesh.
- ``distance_field_indirect_shadow_min_visibility`` (float):  [Read-Write] Controls how dark the dynamic indirect shadow can be.
- ``distance_field_self_shadow_bias`` (float):  [Read-Write] Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``enable_texture_color_mesh_painting`` (bool):  [Read-Write] If false, texture color mesh painting is disabled on this component.
- ``enable_vertex_color_mesh_painting`` (bool):  [Read-Write] If false, vertex color mesh painting is disabled on this component.
  This may be set to false by blueprint functions that override vertex colors in construction script.
- ``evaluate_world_position_offset`` (bool):  [Read-Write] Whether to evaluate World Position Offset.
- ``evaluate_world_position_offset_in_ray_tracing`` (bool):  [Read-Write] Whether to evaluate World Position Offset for ray tracing.
  This is only used when running with r.RayTracing.Geometry.StaticMeshes.WPO=1
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``force_nanite_for_masked`` (bool):  [Read-Write] Forces this component to always use Nanite for masked materials, even if FNaniteSettings::bAllowMaskedMaterials=false
- ``forced_lod_model`` (int32):  [Read-Write] If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1).
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``ignore_instance_for_texture_streaming`` (bool):  [Read-Write] Ignore this instance of this static mesh when calculating streaming information.
  This can be useful when doing things like applying character textures to static geometry,
  to avoid them using distance-based streaming.
- ``ignore_radial_force`` (bool):  [Read-Write] Will ignore radial forces applied to this component.
- ``ignore_radial_impulse`` (bool):  [Read-Write] Will ignore radial impulses applied to this component.
- ``indirect_lighting_cache_quality`` (IndirectLightingCacheQuality):  [Read-Write] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``lightmass_settings`` (LightmassPrimitiveSettings):  [Read-Write] The Lightmass settings for this object.
- ``mesh_paint_texture`` (Texture):  [Read-Only] Texture containing texture color mesh painting for this mesh component.
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``min_lod`` (int32):  [Read-Write] Specifies the smallest LOD that will be used for this component.
  This is ignored if ForcedLodModel is enabled.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_body_overlap`` (bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
  influence on single body components.
- ``nanite_pixel_programmable_distance`` (float):  [Read-Write] Used to forcefully disable pixel programmable rasterization of Nanite when the mesh is further than a given distance from the camera.
- ``never_distance_cull`` (bool):  [Read-Write] When enabled this object will not be culled by distance. This is ignored if a child of a HLOD.
- ``on_begin_cursor_over`` (ComponentBeginCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller
- ``on_clicked`` (ComponentOnClickedSignature):  [Read-Write] Event called when the left mouse button is clicked while the mouse is over this component and click events are enabled in the player controller
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_begin_overlap`` (ComponentBeginOverlapSignature):  [Read-Write] Event called when something starts to overlaps this component, for example a player walking into a trigger.
  For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
  note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.
  note: When receiving an overlap from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_component_end_overlap`` (ComponentEndOverlapSignature):  [Read-Write] Event called when something stops overlapping this component
  note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.
- ``on_component_hit`` (ComponentHitSignature):  [Read-Write] Event called when a component hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
  note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled for this component.
  note: When receiving a hit from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
  note: NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.
- ``on_component_physics_state_changed`` (ComponentPhysicsStateChanged):  [Read-Write] Event called when physics state is created or destroyed for this component
- ``on_component_sleep`` (ComponentSleepSignature):  [Read-Write] Event called when the underlying physics objects is put to sleep
- ``on_component_wake`` (ComponentWakeSignature):  [Read-Write] Event called when the underlying physics objects is woken up
- ``on_end_cursor_over`` (ComponentEndCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller
- ``on_input_touch_begin`` (ComponentOnInputTouchBeginSignature):  [Read-Write] Event called when a touch input is received over this component when touch events are enabled in the player controller
- ``on_input_touch_end`` (ComponentOnInputTouchEndSignature):  [Read-Write] Event called when a touch input is released over this component when touch events are enabled in the player controller
- ``on_input_touch_enter`` (ComponentBeginTouchOverSignature):  [Read-Write] Event called when a finger is moved over this component when touch over events are enabled in the player controller
- ``on_input_touch_leave`` (ComponentEndTouchOverSignature):  [Read-Write] Event called when a finger is moved off this component when touch over events are enabled in the player controller
- ``on_released`` (ComponentOnReleasedSignature):  [Read-Write] Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``overlay_material`` (MaterialInterface):  [Read-Write] Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material
- ``overlay_material_max_draw_distance`` (float):  [Read-Write] The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance.
- ``overridden_light_map_res`` (int32):  [Read-Write] Light map resolution to use on this component, used if bOverrideLightMapRes is true and there is a valid StaticMesh.
- ``overridden_mesh_paint_texture_coordinate_index`` (int32):  [Read-Write] The overriden coordinate index to use when texture color painting on this component.
- ``overridden_mesh_paint_texture_resolution`` (int32):  [Read-Write] The overriden resolution of texture color mesh paint textures on this component.
- ``override_distance_field_self_shadow_bias`` (bool):  [Read-Write] Whether to override the DistanceFieldSelfShadowBias setting of the static mesh asset with the DistanceFieldSelfShadowBias of this component.
- ``override_light_map_res`` (bool):  [Read-Write] Whether to override the lightmap resolution defined in the static mesh.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
- ``override_mesh_paint_texture_coordinate_index`` (bool):  [Read-Write] Whether to override the MeshPaintTextureCoordinateIndex set on the static mesh.
- ``override_mesh_paint_texture_resolution`` (bool):  [Read-Write] Whether to override the MeshPaintTextureCoordinateIndex set on the static mesh.
- ``override_min_lod`` (bool):  [Read-Write] Whether to override the MinLOD setting of the static mesh asset with the MinLOD of this component.
- ``override_wireframe_color`` (bool):  [Read-Write] If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``ray_tracing_group_culling_priority`` (RayTracingGroupCullingPriority):  [Read-Write] Defines how quickly it should be culled. For example buildings should have a low priority, but small dressing should have a high priority.
- ``ray_tracing_group_id`` (int32):  [Read-Write] Defines run-time groups of components. For example allows to assemble multiple parts of a building at runtime.
  -1 means that component doesn't belong to any group.
- ``receive_mobile_csm_shadows`` (bool):  [Read-Write] Mobile only:
  If disabled this component will not receive CSM shadows. (Components that do not receive CSM may have reduced shading cost)
- ``receives_decals`` (bool):  [Read-Write] Whether the primitive receives decals.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_custom_depth`` (bool):  [Read-Write] If true, this component will be rendered in the CustomDepth pass (usually used for outlines)
- ``render_in_depth_pass`` (bool):  [Read-Write] If true, this component will be rendered in the depth pass even if it's not rendered in the main pass
- ``render_in_main_pass`` (bool):  [Read-Write] If true, this component will be rendered in the main pass (z prepass, basepass, transparency)
- ``replicate_physics_to_autonomous_proxy`` (bool):  [Read-Write] True if physics should be replicated to autonomous proxies. This should be true for
                server-authoritative simulations, and false for client authoritative simulations.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``reverse_culling`` (bool):  [Read-Write] Controls whether the static mesh component's backface culling should be reversed
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``sort_triangles`` (bool):  [Read-Write] Enable dynamic sort mesh's triangles to remove ordering issue when rendered with a translucent material
- ``static_mesh`` (StaticMesh):  [Read-Write] The static mesh that this component uses to render
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``streaming_distance_multiplier`` (float):  [Read-Write] Allows adjusting the desired resolution of streaming textures that uses UV 0.  1.0 is the default, whereas a higher value increases the streamed-in resolution.
- ``trace_complex_on_move`` (bool):  [Read-Write] If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).
  If false, collision will be resolved against simple collision bounds instead.
  see: MoveComponent()
- ``translucency_sort_distance_offset`` (float):  [Read-Write] Modified sort distance offset for translucent objects in world units.
  A positive number will move the sort distance further and a negative number will move the distance closer.

  Ignored if the object is not translucent.
  Warning: Adjusting this value will prevent the renderer from correctly sorting based on distance.  Only modify this value if you are certain it will not cause visual artifacts.
- ``translucency_sort_priority`` (int32):  [Read-Write] Translucent objects with a lower sort priority draw behind objects with a higher priority.
  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
  This setting is also used to sort objects being drawn into a runtime virtual texture.

  Ignored if the object is not translucent.  The default priority is zero.
  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.
  It is especially problematic on dynamic gameplay effects.
- ``treat_as_background_for_occlusion`` (bool):  [Read-Write] Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc.
- ``use_as_occluder`` (bool):  [Read-Write] Whether to render the primitive in the depth only pass.
  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
  todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_default_collision`` (bool):  [Read-Write] Use the collision profile specified in the StaticMesh asset.
- ``virtual_texture_cull_mips`` (int8):  [Read-Write] Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
  Larger values reduce the effective draw distance in the runtime virtual texture.
  This culling method doesn't take into account primitive size or virtual texture size.
- ``virtual_texture_lod_bias`` (int8):  [Read-Write] Bias to the LOD selected for rendering to runtime virtual textures.
- ``virtual_texture_min_coverage`` (int8):  [Read-Write] Set the minimum pixel coverage before culling from the runtime virtual texture.
  Larger values reduce the effective draw distance in the runtime virtual texture.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``visible_in_ray_tracing`` (bool):  [Read-Write] If true, this component will be visible in ray tracing effects. Turning this off will remove it from ray traced reflections, shadows, etc.
- ``visible_in_real_time_sky_captures`` (bool):  [Read-Write] If true, this component will be visible in real-time sky light reflection captures.
- ``visible_in_reflection_captures`` (bool):  [Read-Write] If true, this component will be visible in reflection captures.
- ``visible_in_scene_capture_only`` (bool):  [Read-Write] When true, will only be visible in Scene Capture
- ``wireframe_color_override`` (Color):  [Read-Write] Wireframe color to use if bOverrideWireframeColor is true
- ``world_position_offset_disable_distance`` (int32):  [Read-Write] Distance at which to disable World Position Offset for an entire instance (0 = Never disable WPO).
- ``world_position_offset_writes_velocity`` (bool):  [Read-Write] Whether world position offset turns on velocity writes.
  If the WPO isn't static then setting false may give incorrect motion vectors.
  But if we know that the WPO is static then setting false may save performance.

<a id="unreal.StaticMeshComponent.forced_lod_model"></a>

#### forced_lod_model

```python
@property
def forced_lod_model() -> int
```

(int32):  [Read-Only] If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1).

<a id="unreal.StaticMeshComponent.min_lod"></a>

#### min_lod

```python
@property
def min_lod() -> int
```

(int32):  [Read-Only] Specifies the smallest LOD that will be used for this component.
This is ignored if ForcedLodModel is enabled.

<a id="unreal.StaticMeshComponent.wireframe_color_override"></a>

#### wireframe_color_override

```python
@property
def wireframe_color_override() -> Color
```

(Color):  [Read-Only] Wireframe color to use if bOverrideWireframeColor is true

<a id="unreal.StaticMeshComponent.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Only] The static mesh that this component uses to render

<a id="unreal.StaticMeshComponent.world_position_offset_disable_distance"></a>

#### world_position_offset_disable_distance

```python
@property
def world_position_offset_disable_distance() -> int
```

(int32):  [Read-Only] Distance at which to disable World Position Offset for an entire instance (0 = Never disable WPO).

<a id="unreal.StaticMeshComponent.force_nanite_for_masked"></a>

#### force_nanite_for_masked

```python
@property
def force_nanite_for_masked() -> bool
```

(bool):  [Read-Write] Forces this component to always use Nanite for masked materials, even if FNaniteSettings::bAllowMaskedMaterials=false

<a id="unreal.StaticMeshComponent.force_nanite_for_masked"></a>

#### force_nanite_for_masked

```python
@force_nanite_for_masked.setter
def force_nanite_for_masked(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.disallow_nanite"></a>

#### disallow_nanite

```python
@property
def disallow_nanite() -> bool
```

(bool):  [Read-Write] Forces this component to use fallback mesh for rendering if Nanite is enabled on the mesh.

<a id="unreal.StaticMeshComponent.disallow_nanite"></a>

#### disallow_nanite

```python
@disallow_nanite.setter
def disallow_nanite(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.evaluate_world_position_offset"></a>

#### evaluate_world_position_offset

```python
@property
def evaluate_world_position_offset() -> bool
```

(bool):  [Read-Write] Whether to evaluate World Position Offset.

<a id="unreal.StaticMeshComponent.evaluate_world_position_offset"></a>

#### evaluate_world_position_offset

```python
@evaluate_world_position_offset.setter
def evaluate_world_position_offset(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.world_position_offset_writes_velocity"></a>

#### world_position_offset_writes_velocity

```python
@property
def world_position_offset_writes_velocity() -> bool
```

(bool):  [Read-Write] Whether world position offset turns on velocity writes.
If the WPO isn't static then setting false may give incorrect motion vectors.
But if we know that the WPO is static then setting false may save performance.

<a id="unreal.StaticMeshComponent.world_position_offset_writes_velocity"></a>

#### world_position_offset_writes_velocity

```python
@world_position_offset_writes_velocity.setter
def world_position_offset_writes_velocity(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.evaluate_world_position_offset_in_ray_tracing"></a>

#### evaluate_world_position_offset_in_ray_tracing

```python
@property
def evaluate_world_position_offset_in_ray_tracing() -> bool
```

(bool):  [Read-Write] Whether to evaluate World Position Offset for ray tracing.
This is only used when running with r.RayTracing.Geometry.StaticMeshes.WPO=1

<a id="unreal.StaticMeshComponent.evaluate_world_position_offset_in_ray_tracing"></a>

#### evaluate_world_position_offset_in_ray_tracing

```python
@evaluate_world_position_offset_in_ray_tracing.setter
def evaluate_world_position_offset_in_ray_tracing(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.override_wireframe_color"></a>

#### override_wireframe_color

```python
@property
def override_wireframe_color() -> bool
```

(bool):  [Read-Only] If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings

<a id="unreal.StaticMeshComponent.override_min_lod"></a>

#### override_min_lod

```python
@property
def override_min_lod() -> bool
```

(bool):  [Read-Only] Whether to override the MinLOD setting of the static mesh asset with the MinLOD of this component.

<a id="unreal.StaticMeshComponent.ignore_instance_for_texture_streaming"></a>

#### ignore_instance_for_texture_streaming

```python
@property
def ignore_instance_for_texture_streaming() -> bool
```

(bool):  [Read-Write] Ignore this instance of this static mesh when calculating streaming information.
This can be useful when doing things like applying character textures to static geometry,
to avoid them using distance-based streaming.

<a id="unreal.StaticMeshComponent.ignore_instance_for_texture_streaming"></a>

#### ignore_instance_for_texture_streaming

```python
@ignore_instance_for_texture_streaming.setter
def ignore_instance_for_texture_streaming(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.override_light_map_res"></a>

#### override_light_map_res

```python
@property
def override_light_map_res() -> bool
```

(bool):  [Read-Only] Whether to override the lightmap resolution defined in the static mesh.

<a id="unreal.StaticMeshComponent.cast_distance_field_indirect_shadow"></a>

#### cast_distance_field_indirect_shadow

```python
@property
def cast_distance_field_indirect_shadow() -> bool
```

(bool):  [Read-Only] Whether to use the mesh distance field representation (when present) for shadowing indirect lighting (from lightmaps or skylight) on Movable components.
This works like capsule shadows on skeletal meshes, except using the mesh distance field so no physics asset is required.
The StaticMesh must have 'Generate Mesh Distance Field' enabled, or the project must have 'Generate Mesh Distance Fields' enabled for this feature to work.

<a id="unreal.StaticMeshComponent.override_distance_field_self_shadow_bias"></a>

#### override_distance_field_self_shadow_bias

```python
@property
def override_distance_field_self_shadow_bias() -> bool
```

(bool):  [Read-Only] Whether to override the DistanceFieldSelfShadowBias setting of the static mesh asset with the DistanceFieldSelfShadowBias of this component.

<a id="unreal.StaticMeshComponent.sort_triangles"></a>

#### sort_triangles

```python
@property
def sort_triangles() -> bool
```

(bool):  [Read-Only] Enable dynamic sort mesh's triangles to remove ordering issue when rendered with a translucent material

<a id="unreal.StaticMeshComponent.reverse_culling"></a>

#### reverse_culling

```python
@property
def reverse_culling() -> bool
```

(bool):  [Read-Only] Controls whether the static mesh component's backface culling should be reversed

<a id="unreal.StaticMeshComponent.enable_vertex_color_mesh_painting"></a>

#### enable_vertex_color_mesh_painting

```python
@property
def enable_vertex_color_mesh_painting() -> bool
```

(bool):  [Read-Write] If false, vertex color mesh painting is disabled on this component.
This may be set to false by blueprint functions that override vertex colors in construction script.

<a id="unreal.StaticMeshComponent.enable_vertex_color_mesh_painting"></a>

#### enable_vertex_color_mesh_painting

```python
@enable_vertex_color_mesh_painting.setter
def enable_vertex_color_mesh_painting(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.enable_texture_color_mesh_painting"></a>

#### enable_texture_color_mesh_painting

```python
@property
def enable_texture_color_mesh_painting() -> bool
```

(bool):  [Read-Write] If false, texture color mesh painting is disabled on this component.

<a id="unreal.StaticMeshComponent.enable_texture_color_mesh_painting"></a>

#### enable_texture_color_mesh_painting

```python
@enable_texture_color_mesh_painting.setter
def enable_texture_color_mesh_painting(value: bool) -> None
```

<a id="unreal.StaticMeshComponent.overridden_light_map_res"></a>

#### overridden_light_map_res

```python
@property
def overridden_light_map_res() -> int
```

(int32):  [Read-Only] Light map resolution to use on this component, used if bOverrideLightMapRes is true and there is a valid StaticMesh.

<a id="unreal.StaticMeshComponent.distance_field_indirect_shadow_min_visibility"></a>

#### distance_field_indirect_shadow_min_visibility

```python
@property
def distance_field_indirect_shadow_min_visibility() -> float
```

(float):  [Read-Only] Controls how dark the dynamic indirect shadow can be.

<a id="unreal.StaticMeshComponent.distance_field_self_shadow_bias"></a>

#### distance_field_self_shadow_bias

```python
@property
def distance_field_self_shadow_bias() -> float
```

(float):  [Read-Only] Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices.

<a id="unreal.StaticMeshComponent.streaming_distance_multiplier"></a>

#### streaming_distance_multiplier

```python
@property
def streaming_distance_multiplier() -> float
```

(float):  [Read-Write] Allows adjusting the desired resolution of streaming textures that uses UV 0.  1.0 is the default, whereas a higher value increases the streamed-in resolution.

<a id="unreal.StaticMeshComponent.streaming_distance_multiplier"></a>

#### streaming_distance_multiplier

```python
@streaming_distance_multiplier.setter
def streaming_distance_multiplier(value: float) -> None
```

<a id="unreal.StaticMeshComponent.nanite_pixel_programmable_distance"></a>

#### nanite_pixel_programmable_distance

```python
@property
def nanite_pixel_programmable_distance() -> float
```

(float):  [Read-Only] Used to forcefully disable pixel programmable rasterization of Nanite when the mesh is further than a given distance from the camera.

<a id="unreal.StaticMeshComponent.update_initial_evaluate_world_position_offset"></a>

#### update_initial_evaluate_world_position_offset

```python
def update_initial_evaluate_world_position_offset() -> None
```

x.update_initial_evaluate_world_position_offset() -> None
This manually updates the initial value of bEvaluateWorldPositionOffset to be the current value.
    This is useful if the default value of bEvaluateWorldPositionOffset is changed after constructing
    the component.

<a id="unreal.StaticMeshComponent.set_world_position_offset_disable_distance"></a>

#### set_world_position_offset_disable_distance

```python
def set_world_position_offset_disable_distance(new_value: int) -> None
```

x.set_world_position_offset_disable_distance(new_value) -> None
Set World Position Offset Disable Distance

Args:
    new_value (int32):

<a id="unreal.StaticMeshComponent.set_static_mesh"></a>

#### set_static_mesh

```python
def set_static_mesh(new_mesh: StaticMesh) -> bool
```

x.set_static_mesh(new_mesh) -> bool
Change the StaticMesh used by this instance.

Args:
    new_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.StaticMeshComponent.set_reverse_culling"></a>

#### set_reverse_culling

```python
def set_reverse_culling(reverse_culling: bool) -> None
```

x.set_reverse_culling(reverse_culling) -> None
Set forced reverse culling

Args:
    reverse_culling (bool):

<a id="unreal.StaticMeshComponent.set_forced_lod_model"></a>

#### set_forced_lod_model

```python
def set_forced_lod_model(new_forced_lod_model: int) -> None
```

x.set_forced_lod_model(new_forced_lod_model) -> None
Set Forced Lod Model

Args:
    new_forced_lod_model (int32):

<a id="unreal.StaticMeshComponent.set_force_disable_nanite"></a>

#### set_force_disable_nanite

```python
def set_force_disable_nanite(force_disable_nanite: bool) -> None
```

x.set_force_disable_nanite(force_disable_nanite) -> None
Force disabling of Nanite rendering. When true, Will swap to the the fallback mesh instead.

Args:
    force_disable_nanite (bool):

<a id="unreal.StaticMeshComponent.set_evaluate_world_position_offset_in_ray_tracing"></a>

#### set_evaluate_world_position_offset_in_ray_tracing

```python
def set_evaluate_world_position_offset_in_ray_tracing(new_value: bool) -> None
```

x.set_evaluate_world_position_offset_in_ray_tracing(new_value) -> None
Set Evaluate World Position Offset in Ray Tracing

Args:
    new_value (bool):

<a id="unreal.StaticMeshComponent.set_evaluate_world_position_offset"></a>

#### set_evaluate_world_position_offset

```python
def set_evaluate_world_position_offset(new_value: bool) -> None
```

x.set_evaluate_world_position_offset(new_value) -> None
Set Evaluate World Position Offset

Args:
    new_value (bool):

<a id="unreal.StaticMeshComponent.set_distance_field_self_shadow_bias"></a>

#### set_distance_field_self_shadow_bias

```python
def set_distance_field_self_shadow_bias(new_value: float) -> None
```

x.set_distance_field_self_shadow_bias(new_value) -> None
Sets the component's DistanceFieldSelfShadowBias.  bOverrideDistanceFieldSelfShadowBias must be enabled for this to have an effect.

Args:
    new_value (float):

<a id="unreal.StaticMeshComponent.get_local_bounds"></a>

#### get_local_bounds

```python
def get_local_bounds() -> Tuple[Vector, Vector]
```

x.get_local_bounds() -> (min=Vector, max=Vector)
Get Local bounds

Returns:
    tuple: 

    min (Vector): 

    max (Vector):

<a id="unreal.StaticMeshComponent.get_initial_evaluate_world_position_offset"></a>

#### get_initial_evaluate_world_position_offset

```python
def get_initial_evaluate_world_position_offset() -> bool
```

x.get_initial_evaluate_world_position_offset() -> bool
Get the initial value of bEvaluateWorldPositionOffset. This is the value when BeginPlay() was last called, or if UpdateInitialEvaluateWorldPositionOffset is called.

Returns:
    bool:

<a id="unreal.StaticMeshReplicatedComponent"></a>