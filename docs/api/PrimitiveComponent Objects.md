## PrimitiveComponent Objects

```python
class PrimitiveComponent(SceneComponent)
```

PrimitiveComponents are SceneComponents that contain or generate some sort of geometry, generally to be rendered or used as collision data.
There are several subclasses for the various types of geometry, but the most common by far are the ShapeComponents (Capsule, Sphere, Box), StaticMeshComponent, and SkeletalMeshComponent.
ShapeComponents generate geometry that is used for collision detection but are not rendered, while StaticMeshComponents and SkeletalMeshComponents contain pre-built geometry that is rendered, but can also be used for collision detection.

**C++ Source:**

- **Module**: Engine
- **File**: PrimitiveComponent.h

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
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
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
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_body_overlap`` (bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
  influence on single body components.
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
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
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

<a id="unreal.PrimitiveComponent.min_draw_distance"></a>

#### min_draw_distance

```python
@property
def min_draw_distance() -> float
```

(float):  [Read-Only] The minimum distance at which the primitive should be rendered,
measured in world space units from the center of the primitive's bounding sphere to the camera position.

<a id="unreal.PrimitiveComponent.ld_max_draw_distance"></a>

#### ld_max_draw_distance

```python
@property
def ld_max_draw_distance() -> float
```

(float):  [Read-Only] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.

<a id="unreal.PrimitiveComponent.cached_max_draw_distance"></a>

#### cached_max_draw_distance

```python
@property
def cached_max_draw_distance() -> float
```

(float):  [Read-Only] The distance to cull this primitive at.
A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance.

<a id="unreal.PrimitiveComponent.indirect_lighting_cache_quality"></a>

#### indirect_lighting_cache_quality

```python
@property
def indirect_lighting_cache_quality() -> IndirectLightingCacheQuality
```

(IndirectLightingCacheQuality):  [Read-Only] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.

<a id="unreal.PrimitiveComponent.lightmap_type"></a>

#### lightmap_type

```python
@property
def lightmap_type() -> LightmapType
```

(LightmapType):  [Read-Only]

<a id="unreal.PrimitiveComponent.hlod_batching_policy"></a>

#### hlod_batching_policy

```python
@property
def hlod_batching_policy() -> HLODBatchingPolicy
```

(HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.

<a id="unreal.PrimitiveComponent.hlod_batching_policy"></a>

#### hlod_batching_policy

```python
@hlod_batching_policy.setter
def hlod_batching_policy(value: HLODBatchingPolicy) -> None
```

<a id="unreal.PrimitiveComponent.shadow_cache_invalidation_behavior"></a>

#### shadow_cache_invalidation_behavior

```python
@property
def shadow_cache_invalidation_behavior() -> ShadowCacheInvalidationBehavior
```

(ShadowCacheInvalidationBehavior):  [Read-Only] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.

<a id="unreal.PrimitiveComponent.enable_auto_lod_generation"></a>

#### enable_auto_lod_generation

```python
@property
def enable_auto_lod_generation() -> bool
```

(bool):  [Read-Write] Whether to include this component in HLODs or not.

<a id="unreal.PrimitiveComponent.enable_auto_lod_generation"></a>

#### enable_auto_lod_generation

```python
@enable_auto_lod_generation.setter
def enable_auto_lod_generation(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.never_distance_cull"></a>

#### never_distance_cull

```python
@property
def never_distance_cull() -> bool
```

(bool):  [Read-Only] When enabled this object will not be culled by distance. This is ignored if a child of a HLOD.

<a id="unreal.PrimitiveComponent.always_create_physics_state"></a>

#### always_create_physics_state

```python
@property
def always_create_physics_state() -> bool
```

(bool):  [Read-Only] Indicates if we'd like to create physics state all the time (for collision and simulation).
If you set this to false, it still will create physics state if collision or simulation activated.
This can help performance if you'd like to avoid overhead of creating physics state when triggers

<a id="unreal.PrimitiveComponent.generate_overlap_events"></a>

#### generate_overlap_events

```python
@property
def generate_overlap_events() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PrimitiveComponent.generate_overlap_events"></a>

#### generate_overlap_events

```python
@generate_overlap_events.setter
def generate_overlap_events(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.multi_body_overlap"></a>

#### multi_body_overlap

```python
@property
def multi_body_overlap() -> bool
```

(bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
influence on single body components.

<a id="unreal.PrimitiveComponent.multi_body_overlap"></a>

#### multi_body_overlap

```python
@multi_body_overlap.setter
def multi_body_overlap(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.trace_complex_on_move"></a>

#### trace_complex_on_move

```python
@property
def trace_complex_on_move() -> bool
```

(bool):  [Read-Write] If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).
If false, collision will be resolved against simple collision bounds instead.
see: MoveComponent()

<a id="unreal.PrimitiveComponent.trace_complex_on_move"></a>

#### trace_complex_on_move

```python
@trace_complex_on_move.setter
def trace_complex_on_move(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.return_material_on_move"></a>

#### return_material_on_move

```python
@property
def return_material_on_move() -> bool
```

(bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
see: MoveComponent(), FHitResult

<a id="unreal.PrimitiveComponent.return_material_on_move"></a>

#### return_material_on_move

```python
@return_material_on_move.setter
def return_material_on_move(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.allow_cull_distance_volume"></a>

#### allow_cull_distance_volume

```python
@property
def allow_cull_distance_volume() -> bool
```

(bool):  [Read-Only] Whether to accept cull distance volumes to modify cached cull distance.

<a id="unreal.PrimitiveComponent.visible_in_reflection_captures"></a>

#### visible_in_reflection_captures

```python
@property
def visible_in_reflection_captures() -> bool
```

(bool):  [Read-Only] If true, this component will be visible in reflection captures.

<a id="unreal.PrimitiveComponent.visible_in_real_time_sky_captures"></a>

#### visible_in_real_time_sky_captures

```python
@property
def visible_in_real_time_sky_captures() -> bool
```

(bool):  [Read-Only] If true, this component will be visible in real-time sky light reflection captures.

<a id="unreal.PrimitiveComponent.visible_in_ray_tracing"></a>

#### visible_in_ray_tracing

```python
@property
def visible_in_ray_tracing() -> bool
```

(bool):  [Read-Only] If true, this component will be visible in ray tracing effects. Turning this off will remove it from ray traced reflections, shadows, etc.

<a id="unreal.PrimitiveComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@property
def render_in_main_pass() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the main pass (z prepass, basepass, transparency)

<a id="unreal.PrimitiveComponent.render_in_depth_pass"></a>

#### render_in_depth_pass

```python
@property
def render_in_depth_pass() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the depth pass even if it's not rendered in the main pass

<a id="unreal.PrimitiveComponent.receives_decals"></a>

#### receives_decals

```python
@property
def receives_decals() -> bool
```

(bool):  [Read-Only] Whether the primitive receives decals.

<a id="unreal.PrimitiveComponent.holdout"></a>

#### holdout

```python
@property
def holdout() -> bool
```

(bool):  [Read-Only] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.

<a id="unreal.PrimitiveComponent.owner_no_see"></a>

#### owner_no_see

```python
@property
def owner_no_see() -> bool
```

(bool):  [Read-Only] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.

<a id="unreal.PrimitiveComponent.only_owner_see"></a>

#### only_owner_see

```python
@property
def only_owner_see() -> bool
```

(bool):  [Read-Only] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.

<a id="unreal.PrimitiveComponent.treat_as_background_for_occlusion"></a>

#### treat_as_background_for_occlusion

```python
@property
def treat_as_background_for_occlusion() -> bool
```

(bool):  [Read-Only] Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc.

<a id="unreal.PrimitiveComponent.use_as_occluder"></a>

#### use_as_occluder

```python
@property
def use_as_occluder() -> bool
```

(bool):  [Read-Only] Whether to render the primitive in the depth only pass.
This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.

<a id="unreal.PrimitiveComponent.force_mip_streaming"></a>

#### force_mip_streaming

```python
@property
def force_mip_streaming() -> bool
```

(bool):  [Read-Only] If true, forces mips for textures used by this component to be resident when this component's level is loaded.

<a id="unreal.PrimitiveComponent.cast_shadow"></a>

#### cast_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Only] Controls whether the primitive component should cast a shadow or not.

<a id="unreal.PrimitiveComponent.emissive_light_source"></a>

#### emissive_light_source

```python
@property
def emissive_light_source() -> bool
```

(bool):  [Read-Only] Whether the primitive will be used as an emissive light source.

<a id="unreal.PrimitiveComponent.affect_dynamic_indirect_lighting"></a>

#### affect_dynamic_indirect_lighting

```python
@property
def affect_dynamic_indirect_lighting() -> bool
```

(bool):  [Read-Only] Controls whether the primitive should influence indirect lighting.

<a id="unreal.PrimitiveComponent.affect_indirect_lighting_while_hidden"></a>

#### affect_indirect_lighting_while_hidden

```python
@property
def affect_indirect_lighting_while_hidden() -> bool
```

(bool):  [Read-Only] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.

<a id="unreal.PrimitiveComponent.affect_distance_field_lighting"></a>

#### affect_distance_field_lighting

```python
@property
def affect_distance_field_lighting() -> bool
```

(bool):  [Read-Only] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *

<a id="unreal.PrimitiveComponent.cast_dynamic_shadow"></a>

#### cast_dynamic_shadow

```python
@property
def cast_dynamic_shadow() -> bool
```

(bool):  [Read-Only] Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. *

<a id="unreal.PrimitiveComponent.cast_static_shadow"></a>

#### cast_static_shadow

```python
@property
def cast_static_shadow() -> bool
```

(bool):  [Read-Only] Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true.

<a id="unreal.PrimitiveComponent.cast_volumetric_translucent_shadow"></a>

#### cast_volumetric_translucent_shadow

```python
@property
def cast_volumetric_translucent_shadow() -> bool
```

(bool):  [Read-Only] Whether the object should cast a volumetric translucent shadow.
Volumetric translucent shadows are useful for primitives with smoothly changing opacity like particles representing a volume,
But have artifacts when used on highly opaque surfaces.

<a id="unreal.PrimitiveComponent.cast_contact_shadow"></a>

#### cast_contact_shadow

```python
@property
def cast_contact_shadow() -> bool
```

(bool):  [Read-Only] Whether the object should cast contact shadows.
This flag is only used if CastShadow is true.

<a id="unreal.PrimitiveComponent.self_shadow_only"></a>

#### self_shadow_only

```python
@property
def self_shadow_only() -> bool
```

(bool):  [Read-Only] When enabled, the component will only cast a shadow on itself and not other components in the world.
This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.

<a id="unreal.PrimitiveComponent.cast_far_shadow"></a>

#### cast_far_shadow

```python
@property
def cast_far_shadow() -> bool
```

(bool):  [Read-Only] When enabled, the component will be rendering into the far shadow cascades (only for directional lights).

<a id="unreal.PrimitiveComponent.cast_inset_shadow"></a>

#### cast_inset_shadow

```python
@property
def cast_inset_shadow() -> bool
```

(bool):  [Read-Only] Whether this component should create a per-object shadow that gives higher effective shadow resolution.
Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled.

<a id="unreal.PrimitiveComponent.cast_cinematic_shadow"></a>

#### cast_cinematic_shadow

```python
@property
def cast_cinematic_shadow() -> bool
```

(bool):  [Read-Only] Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.
This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired.

<a id="unreal.PrimitiveComponent.cast_hidden_shadow"></a>

#### cast_hidden_shadow

```python
@property
def cast_hidden_shadow() -> bool
```

(bool):  [Read-Only] If true, the primitive will cast shadows even if bHidden is true.
Controls whether the primitive should cast shadows when hidden.
This flag is only used if CastShadow is true.

<a id="unreal.PrimitiveComponent.cast_shadow_as_two_sided"></a>

#### cast_shadow_as_two_sided

```python
@property
def cast_shadow_as_two_sided() -> bool
```

(bool):  [Read-Only] Whether this primitive should cast dynamic shadows as if it were a two sided material.

<a id="unreal.PrimitiveComponent.light_attachments_as_group"></a>

#### light_attachments_as_group

```python
@property
def light_attachments_as_group() -> bool
```

(bool):  [Read-Only] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
This is useful for improving performance when multiple movable components are attached together.

<a id="unreal.PrimitiveComponent.exclude_from_light_attachment_group"></a>

#### exclude_from_light_attachment_group

```python
@property
def exclude_from_light_attachment_group() -> bool
```

(bool):  [Read-Only] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.

<a id="unreal.PrimitiveComponent.receive_mobile_csm_shadows"></a>

#### receive_mobile_csm_shadows

```python
@property
def receive_mobile_csm_shadows() -> bool
```

(bool):  [Read-Only] Mobile only:
If disabled this component will not receive CSM shadows. (Components that do not receive CSM may have reduced shading cost)

<a id="unreal.PrimitiveComponent.single_sample_shadow_from_stationary_lights"></a>

#### single_sample_shadow_from_stationary_lights

```python
@property
def single_sample_shadow_from_stationary_lights() -> bool
```

(bool):  [Read-Only] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
This is currently only used on stationary directional lights.

<a id="unreal.PrimitiveComponent.ignore_radial_impulse"></a>

#### ignore_radial_impulse

```python
@property
def ignore_radial_impulse() -> bool
```

(bool):  [Read-Write] Will ignore radial impulses applied to this component.

<a id="unreal.PrimitiveComponent.ignore_radial_impulse"></a>

#### ignore_radial_impulse

```python
@ignore_radial_impulse.setter
def ignore_radial_impulse(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.ignore_radial_force"></a>

#### ignore_radial_force

```python
@property
def ignore_radial_force() -> bool
```

(bool):  [Read-Write] Will ignore radial forces applied to this component.

<a id="unreal.PrimitiveComponent.ignore_radial_force"></a>

#### ignore_radial_force

```python
@ignore_radial_force.setter
def ignore_radial_force(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.apply_impulse_on_damage"></a>

#### apply_impulse_on_damage

```python
@property
def apply_impulse_on_damage() -> bool
```

(bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.

<a id="unreal.PrimitiveComponent.apply_impulse_on_damage"></a>

#### apply_impulse_on_damage

```python
@apply_impulse_on_damage.setter
def apply_impulse_on_damage(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.replicate_physics_to_autonomous_proxy"></a>

#### replicate_physics_to_autonomous_proxy

```python
@property
def replicate_physics_to_autonomous_proxy() -> bool
```

(bool):  [Read-Write] True if physics should be replicated to autonomous proxies. This should be true for
              server-authoritative simulations, and false for client authoritative simulations.

<a id="unreal.PrimitiveComponent.replicate_physics_to_autonomous_proxy"></a>

#### replicate_physics_to_autonomous_proxy

```python
@replicate_physics_to_autonomous_proxy.setter
def replicate_physics_to_autonomous_proxy(value: bool) -> None
```

<a id="unreal.PrimitiveComponent.render_custom_depth"></a>

#### render_custom_depth

```python
@property
def render_custom_depth() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the CustomDepth pass (usually used for outlines)

<a id="unreal.PrimitiveComponent.visible_in_scene_capture_only"></a>

#### visible_in_scene_capture_only

```python
@property
def visible_in_scene_capture_only() -> bool
```

(bool):  [Read-Only] When true, will only be visible in Scene Capture

<a id="unreal.PrimitiveComponent.hidden_in_scene_capture"></a>

#### hidden_in_scene_capture

```python
@property
def hidden_in_scene_capture() -> bool
```

(bool):  [Read-Only] When true, will not be captured by Scene Capture

<a id="unreal.PrimitiveComponent.first_person_primitive_type"></a>

#### first_person_primitive_type

```python
@property
def first_person_primitive_type() -> FirstPersonPrimitiveType
```

(FirstPersonPrimitiveType):  [Read-Only] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.

<a id="unreal.PrimitiveComponent.static_when_not_moveable"></a>

#### static_when_not_moveable

```python
@property
def static_when_not_moveable() -> bool
```

(bool):  [Read-Only] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable

<a id="unreal.PrimitiveComponent.exclude_for_specific_hlod_levels"></a>

#### exclude_for_specific_hlod_levels

```python
@property
def exclude_for_specific_hlod_levels() -> Array[int]
```

(Array[int32]):  [Read-Write]
deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead

<a id="unreal.PrimitiveComponent.exclude_for_specific_hlod_levels"></a>

#### exclude_for_specific_hlod_levels

```python
@exclude_for_specific_hlod_levels.setter
def exclude_for_specific_hlod_levels(value: Array[int]) -> None
```

<a id="unreal.PrimitiveComponent.can_character_step_up_on"></a>

#### can_character_step_up_on

```python
@property
def can_character_step_up_on() -> CanBeCharacterBase
```

(CanBeCharacterBase):  [Read-Write] Determine whether a Character can step up onto this component.
This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.
see: FWalkableSlopeOverride

<a id="unreal.PrimitiveComponent.can_character_step_up_on"></a>

#### can_character_step_up_on

```python
@can_character_step_up_on.setter
def can_character_step_up_on(value: CanBeCharacterBase) -> None
```

<a id="unreal.PrimitiveComponent.can_be_character_base"></a>

#### can_be_character_base

```python
@property
def can_be_character_base() -> CanBeCharacterBase
```

deprecated: 'can_be_character_base' was renamed to 'can_character_step_up_on'.

<a id="unreal.PrimitiveComponent.can_be_character_base"></a>

#### can_be_character_base

```python
@can_be_character_base.setter
def can_be_character_base(value: CanBeCharacterBase) -> None
```

<a id="unreal.PrimitiveComponent.lighting_channels"></a>

#### lighting_channels

```python
@property
def lighting_channels() -> LightingChannels
```

(LightingChannels):  [Read-Only] Channels that this component should be in.  Lights with matching channels will affect the component.
These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).

<a id="unreal.PrimitiveComponent.ray_tracing_group_culling_priority"></a>

#### ray_tracing_group_culling_priority

```python
@property
def ray_tracing_group_culling_priority() -> RayTracingGroupCullingPriority
```

(RayTracingGroupCullingPriority):  [Read-Only] Defines how quickly it should be culled. For example buildings should have a low priority, but small dressing should have a high priority.

<a id="unreal.PrimitiveComponent.custom_depth_stencil_write_mask"></a>

#### custom_depth_stencil_write_mask

```python
@property
def custom_depth_stencil_write_mask() -> RendererStencilMask
```

(RendererStencilMask):  [Read-Only] Mask used for stencil buffer writes.

<a id="unreal.PrimitiveComponent.ray_tracing_group_id"></a>

#### ray_tracing_group_id

```python
@property
def ray_tracing_group_id() -> int
```

(int32):  [Read-Only] Defines run-time groups of components. For example allows to assemble multiple parts of a building at runtime.
-1 means that component doesn't belong to any group.

<a id="unreal.PrimitiveComponent.custom_depth_stencil_value"></a>

#### custom_depth_stencil_value

```python
@property
def custom_depth_stencil_value() -> int
```

(int32):  [Read-Only] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)

<a id="unreal.PrimitiveComponent.translucency_sort_priority"></a>

#### translucency_sort_priority

```python
@property
def translucency_sort_priority() -> int
```

(int32):  [Read-Only] Translucent objects with a lower sort priority draw behind objects with a higher priority.
Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.
This setting is also used to sort objects being drawn into a runtime virtual texture.

Ignored if the object is not translucent.  The default priority is zero.
Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.
It is especially problematic on dynamic gameplay effects.

<a id="unreal.PrimitiveComponent.translucency_sort_distance_offset"></a>

#### translucency_sort_distance_offset

```python
@property
def translucency_sort_distance_offset() -> float
```

(float):  [Read-Only] Modified sort distance offset for translucent objects in world units.
A positive number will move the sort distance further and a negative number will move the distance closer.

Ignored if the object is not translucent.
Warning: Adjusting this value will prevent the renderer from correctly sorting based on distance.  Only modify this value if you are certain it will not cause visual artifacts.

<a id="unreal.PrimitiveComponent.runtime_virtual_textures"></a>

#### runtime_virtual_textures

```python
@property
def runtime_virtual_textures() -> Array[RuntimeVirtualTexture]
```

(Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
The material also needs to be set up to output to a virtual texture.

<a id="unreal.PrimitiveComponent.runtime_virtual_textures"></a>

#### runtime_virtual_textures

```python
@runtime_virtual_textures.setter
def runtime_virtual_textures(value: Array[RuntimeVirtualTexture]) -> None
```

<a id="unreal.PrimitiveComponent.virtual_texture_render_pass_type"></a>

#### virtual_texture_render_pass_type

```python
@property
def virtual_texture_render_pass_type() -> RuntimeVirtualTextureMainPassType
```

(RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.

<a id="unreal.PrimitiveComponent.virtual_texture_render_pass_type"></a>

#### virtual_texture_render_pass_type

```python
@virtual_texture_render_pass_type.setter
def virtual_texture_render_pass_type(
        value: RuntimeVirtualTextureMainPassType) -> None
```

<a id="unreal.PrimitiveComponent.body_instance"></a>

#### body_instance

```python
@property
def body_instance() -> BodyInstance
```

(BodyInstance):  [Read-Only] Physics scene information for this component, holds a single rigid body with multiple shapes.

<a id="unreal.PrimitiveComponent.on_component_hit"></a>

#### on_component_hit

```python
@property
def on_component_hit() -> ComponentHitSignature
```

(ComponentHitSignature):  [Read-Write] Event called when a component hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled for this component.
note: When receiving a hit from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.
note: NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.

<a id="unreal.PrimitiveComponent.on_component_hit"></a>

#### on_component_hit

```python
@on_component_hit.setter
def on_component_hit(value: ComponentHitSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_component_begin_overlap"></a>

#### on_component_begin_overlap

```python
@property
def on_component_begin_overlap() -> ComponentBeginOverlapSignature
```

(ComponentBeginOverlapSignature):  [Read-Write] Event called when something starts to overlaps this component, for example a player walking into a trigger.
For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.
note: When receiving an overlap from another object's movement, the directions of 'Hit.Normal' and 'Hit.ImpactNormal' will be adjusted to indicate force from the other object against this object.

<a id="unreal.PrimitiveComponent.on_component_begin_overlap"></a>

#### on_component_begin_overlap

```python
@on_component_begin_overlap.setter
def on_component_begin_overlap(value: ComponentBeginOverlapSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_component_end_overlap"></a>

#### on_component_end_overlap

```python
@property
def on_component_end_overlap() -> ComponentEndOverlapSignature
```

(ComponentEndOverlapSignature):  [Read-Write] Event called when something stops overlapping this component
note: Both this component and the other one must have GetGenerateOverlapEvents() set to true to generate overlap events.

<a id="unreal.PrimitiveComponent.on_component_end_overlap"></a>

#### on_component_end_overlap

```python
@on_component_end_overlap.setter
def on_component_end_overlap(value: ComponentEndOverlapSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_component_wake"></a>

#### on_component_wake

```python
@property
def on_component_wake() -> ComponentWakeSignature
```

(ComponentWakeSignature):  [Read-Write] Event called when the underlying physics objects is woken up

<a id="unreal.PrimitiveComponent.on_component_wake"></a>

#### on_component_wake

```python
@on_component_wake.setter
def on_component_wake(value: ComponentWakeSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_component_sleep"></a>

#### on_component_sleep

```python
@property
def on_component_sleep() -> ComponentSleepSignature
```

(ComponentSleepSignature):  [Read-Write] Event called when the underlying physics objects is put to sleep

<a id="unreal.PrimitiveComponent.on_component_sleep"></a>

#### on_component_sleep

```python
@on_component_sleep.setter
def on_component_sleep(value: ComponentSleepSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_component_physics_state_changed"></a>

#### on_component_physics_state_changed

```python
@property
def on_component_physics_state_changed() -> ComponentPhysicsStateChanged
```

(ComponentPhysicsStateChanged):  [Read-Write] Event called when physics state is created or destroyed for this component

<a id="unreal.PrimitiveComponent.on_component_physics_state_changed"></a>

#### on_component_physics_state_changed

```python
@on_component_physics_state_changed.setter
def on_component_physics_state_changed(
        value: ComponentPhysicsStateChanged) -> None
```

<a id="unreal.PrimitiveComponent.on_begin_cursor_over"></a>

#### on_begin_cursor_over

```python
@property
def on_begin_cursor_over() -> ComponentBeginCursorOverSignature
```

(ComponentBeginCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_begin_cursor_over"></a>

#### on_begin_cursor_over

```python
@on_begin_cursor_over.setter
def on_begin_cursor_over(value: ComponentBeginCursorOverSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_end_cursor_over"></a>

#### on_end_cursor_over

```python
@property
def on_end_cursor_over() -> ComponentEndCursorOverSignature
```

(ComponentEndCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_end_cursor_over"></a>

#### on_end_cursor_over

```python
@on_end_cursor_over.setter
def on_end_cursor_over(value: ComponentEndCursorOverSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_clicked"></a>

#### on_clicked

```python
@property
def on_clicked() -> ComponentOnClickedSignature
```

(ComponentOnClickedSignature):  [Read-Write] Event called when the left mouse button is clicked while the mouse is over this component and click events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_clicked"></a>

#### on_clicked

```python
@on_clicked.setter
def on_clicked(value: ComponentOnClickedSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_released"></a>

#### on_released

```python
@property
def on_released() -> ComponentOnReleasedSignature
```

(ComponentOnReleasedSignature):  [Read-Write] Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_released"></a>

#### on_released

```python
@on_released.setter
def on_released(value: ComponentOnReleasedSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_input_touch_begin"></a>

#### on_input_touch_begin

```python
@property
def on_input_touch_begin() -> ComponentOnInputTouchBeginSignature
```

(ComponentOnInputTouchBeginSignature):  [Read-Write] Event called when a touch input is received over this component when touch events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_input_touch_begin"></a>

#### on_input_touch_begin

```python
@on_input_touch_begin.setter
def on_input_touch_begin(value: ComponentOnInputTouchBeginSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_input_touch_end"></a>

#### on_input_touch_end

```python
@property
def on_input_touch_end() -> ComponentOnInputTouchEndSignature
```

(ComponentOnInputTouchEndSignature):  [Read-Write] Event called when a touch input is released over this component when touch events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_input_touch_end"></a>

#### on_input_touch_end

```python
@on_input_touch_end.setter
def on_input_touch_end(value: ComponentOnInputTouchEndSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_input_touch_enter"></a>

#### on_input_touch_enter

```python
@property
def on_input_touch_enter() -> ComponentBeginTouchOverSignature
```

(ComponentBeginTouchOverSignature):  [Read-Write] Event called when a finger is moved over this component when touch over events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_input_touch_enter"></a>

#### on_input_touch_enter

```python
@on_input_touch_enter.setter
def on_input_touch_enter(value: ComponentBeginTouchOverSignature) -> None
```

<a id="unreal.PrimitiveComponent.on_input_touch_leave"></a>

#### on_input_touch_leave

```python
@property
def on_input_touch_leave() -> ComponentEndTouchOverSignature
```

(ComponentEndTouchOverSignature):  [Read-Write] Event called when a finger is moved off this component when touch over events are enabled in the player controller

<a id="unreal.PrimitiveComponent.on_input_touch_leave"></a>

#### on_input_touch_leave

```python
@on_input_touch_leave.setter
def on_input_touch_leave(value: ComponentEndTouchOverSignature) -> None
```

<a id="unreal.PrimitiveComponent.was_recently_rendered"></a>

#### was_recently_rendered

```python
def was_recently_rendered(tolerance: float = 0.200000) -> bool
```

x.was_recently_rendered(tolerance=0.200000) -> bool
Returns true if this component has been rendered "recently", with a tolerance in seconds to define what "recent" means.
e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

Args:
    tolerance (float): How many seconds ago the actor last render time can be and still count as having been "recently" rendered.

Returns:
    bool: Whether this actor was recently rendered.

<a id="unreal.PrimitiveComponent.wake_rigid_body"></a>

#### wake_rigid_body

```python
def wake_rigid_body(bone_name: Name = "None") -> None
```

x.wake_rigid_body(bone_name="None") -> None
'Wake' physics simulation for a single body.

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to wake. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.wake_all_rigid_bodies"></a>

#### wake_all_rigid_bodies

```python
def wake_all_rigid_bodies() -> None
```

x.wake_all_rigid_bodies() -> None
Ensure simulation is running for all bodies in this component.

<a id="unreal.PrimitiveComponent.set_walkable_slope_override"></a>

#### set_walkable_slope_override

```python
def set_walkable_slope_override(new_override: WalkableSlopeOverride) -> None
```

x.set_walkable_slope_override(new_override) -> None
Sets a new slope override for this component instance.

Args:
    new_override (WalkableSlopeOverride):

<a id="unreal.PrimitiveComponent.set_visible_in_scene_capture_only"></a>

#### set_visible_in_scene_capture_only

```python
def set_visible_in_scene_capture_only(value: bool) -> None
```

x.set_visible_in_scene_capture_only(value) -> None
Sets bVisibleInSceneCaptureOnly property and marks the render state dirty.

Args:
    value (bool):

<a id="unreal.PrimitiveComponent.set_visible_in_ray_tracing"></a>

#### set_visible_in_ray_tracing

```python
def set_visible_in_ray_tracing(new_visible_in_ray_tracing: bool) -> None
```

x.set_visible_in_ray_tracing(new_visible_in_ray_tracing) -> None
Changes the value of bIsVisibleInRayTracing.

Args:
    new_visible_in_ray_tracing (bool):

<a id="unreal.PrimitiveComponent.set_vector_parameter_for_default_custom_primitive_data"></a>

#### set_vector_parameter_for_default_custom_primitive_data

```python
def set_vector_parameter_for_default_custom_primitive_data(
        parameter_name: Name, value: Vector4) -> None
```

x.set_vector_parameter_for_default_custom_primitive_data(parameter_name, value) -> None
Set a vector parameter for default custom primitive data. This will be serialized and is useful in construction scripts.

Args:
    parameter_name (Name): The parameter name of the custom primitive
    value (Vector4): The new value of the custom primitive

<a id="unreal.PrimitiveComponent.set_vector_parameter_for_custom_primitive_data"></a>

#### set_vector_parameter_for_custom_primitive_data

```python
def set_vector_parameter_for_custom_primitive_data(parameter_name: Name,
                                                   value: Vector4) -> None
```

x.set_vector_parameter_for_custom_primitive_data(parameter_name, value) -> None
Set a vector parameter for custom primitive data. This sets the run-time data only, so it doesn't serialize.

Args:
    parameter_name (Name): The parameter name of the custom primitive
    value (Vector4): The new value of the custom primitive

<a id="unreal.PrimitiveComponent.set_use_macd"></a>

#### set_use_macd

```python
def set_use_macd(use_macd: bool, bone_name: Name = "None") -> None
```

x.set_use_macd(use_macd, bone_name="None") -> None
[EXPERIMENTAL] Set whether this component should use Motion-Aware Collision Detection

Args:
    use_macd (bool): 
    bone_name (Name):

<a id="unreal.PrimitiveComponent.set_use_ccd"></a>

#### set_use_ccd

```python
def set_use_ccd(use_ccd: bool, bone_name: Name = "None") -> None
```

x.set_use_ccd(use_ccd, bone_name="None") -> None
Set whether this component should use Continuous Collision Detection

Args:
    use_ccd (bool): 
    bone_name (Name):

<a id="unreal.PrimitiveComponent.set_update_kinematic_from_simulation"></a>

#### set_update_kinematic_from_simulation

```python
def set_update_kinematic_from_simulation(
        update_kinematic_from_simulation: bool) -> None
```

x.set_update_kinematic_from_simulation(update_kinematic_from_simulation) -> None
Enables/disables whether this component should be updated by simulation when it is kinematic. This is needed if (for example) its velocity needs to be accessed.

Args:
    update_kinematic_from_simulation (bool):

<a id="unreal.PrimitiveComponent.set_translucent_sort_priority"></a>

#### set_translucent_sort_priority

```python
def set_translucent_sort_priority(new_translucent_sort_priority: int) -> None
```

x.set_translucent_sort_priority(new_translucent_sort_priority) -> None
Changes the value of TranslucentSortPriority.

Args:
    new_translucent_sort_priority (int32):

<a id="unreal.PrimitiveComponent.set_translucency_sort_distance_offset"></a>

#### set_translucency_sort_distance_offset

```python
def set_translucency_sort_distance_offset(
        new_translucency_sort_distance_offset: float) -> None
```

x.set_translucency_sort_distance_offset(new_translucency_sort_distance_offset) -> None
Changes the value of TranslucencySortDistanceOffset.

Args:
    new_translucency_sort_distance_offset (float):

<a id="unreal.PrimitiveComponent.set_static_when_not_moveable"></a>

#### set_static_when_not_moveable

```python
def set_static_when_not_moveable(static_when_not_moveable: bool) -> None
```

x.set_static_when_not_moveable(static_when_not_moveable) -> None
Set Static when Not Moveable

Args:
    static_when_not_moveable (bool):

<a id="unreal.PrimitiveComponent.set_single_sample_shadow_from_stationary_lights"></a>

#### set_single_sample_shadow_from_stationary_lights

```python
def set_single_sample_shadow_from_stationary_lights(
        new_single_sample_shadow_from_stationary_lights: bool) -> None
```

x.set_single_sample_shadow_from_stationary_lights(new_single_sample_shadow_from_stationary_lights) -> None
Changes the value of bSingleSampleShadowFromStationaryLights.

Args:
    new_single_sample_shadow_from_stationary_lights (bool):

<a id="unreal.PrimitiveComponent.set_simulate_physics"></a>

#### set_simulate_physics

```python
def set_simulate_physics(simulate: bool) -> None
```

x.set_simulate_physics(simulate) -> None
When this component is a simple/single body, this will enable or disable simulation on that body. In addition,
if this component is currently attached to something, beginning simulation will detach it. Note that stopping
simulation will not reattach the component - that would need to be done explicitly.

For more complex components (e.g. skeletal meshes), simulation will apply to the bodies contained by the
component (e.g. using a physics asset). Since these bodies will be free to move independently of the component,
the component will not be automatically detached. If detachment is required, then that can be done by
calling DetachFromComponent.

Args:
    simulate (bool): New simulation state for the single body or multiple bodies

<a id="unreal.PrimitiveComponent.set_scalar_parameter_for_default_custom_primitive_data"></a>

#### set_scalar_parameter_for_default_custom_primitive_data

```python
def set_scalar_parameter_for_default_custom_primitive_data(
        parameter_name: Name, value: float) -> None
```

x.set_scalar_parameter_for_default_custom_primitive_data(parameter_name, value) -> None
Set a scalar parameter for default custom primitive data. This will be serialized and is useful in construction scripts.

Args:
    parameter_name (Name): The parameter name of the custom primitive
    value (float): The new value of the custom primitive

<a id="unreal.PrimitiveComponent.set_scalar_parameter_for_custom_primitive_data"></a>

#### set_scalar_parameter_for_custom_primitive_data

```python
def set_scalar_parameter_for_custom_primitive_data(parameter_name: Name,
                                                   value: float) -> None
```

x.set_scalar_parameter_for_custom_primitive_data(parameter_name, value) -> None
Set a scalar parameter for custom primitive data. This sets the run-time data only, so it doesn't serialize.

Args:
    parameter_name (Name): The parameter name of the custom primitive
    value (float): The new value of the custom primitive

<a id="unreal.PrimitiveComponent.set_render_in_main_pass"></a>

#### set_render_in_main_pass

```python
def set_render_in_main_pass(value: bool) -> None
```

x.set_render_in_main_pass(value) -> None
Sets bRenderInMainPass property and marks the render state dirty.

Args:
    value (bool):

<a id="unreal.PrimitiveComponent.set_render_in_depth_pass"></a>

#### set_render_in_depth_pass

```python
def set_render_in_depth_pass(value: bool) -> None
```

x.set_render_in_depth_pass(value) -> None
Sets bRenderInDepthPass property and marks the render state dirty.

Args:
    value (bool):

<a id="unreal.PrimitiveComponent.set_render_custom_depth"></a>

#### set_render_custom_depth

```python
def set_render_custom_depth(value: bool) -> None
```

x.set_render_custom_depth(value) -> None
Sets the bRenderCustomDepth property and marks the render state dirty.

Args:
    value (bool):

<a id="unreal.PrimitiveComponent.set_receives_decals"></a>

#### set_receives_decals

```python
def set_receives_decals(new_receives_decals: bool) -> None
```

x.set_receives_decals(new_receives_decals) -> None
Changes the value of bReceivesDecals.

Args:
    new_receives_decals (bool):

<a id="unreal.PrimitiveComponent.set_phys_material_override"></a>

#### set_phys_material_override

```python
def set_phys_material_override(new_phys_material: PhysicalMaterial) -> None
```

x.set_phys_material_override(new_phys_material) -> None
Changes the current PhysMaterialOverride for this component.
Note that if physics is already running on this component, this will _not_ alter its mass/inertia etc,
it will only change its surface properties like friction.

Args:
    new_phys_material (PhysicalMaterial):

<a id="unreal.PrimitiveComponent.set_physics_max_angular_velocity_in_radians"></a>

#### set_physics_max_angular_velocity_in_radians

```python
def set_physics_max_angular_velocity_in_radians(
        new_max_ang_vel: float,
        add_to_current: bool = False,
        bone_name: Name = "None") -> None
```

x.set_physics_max_angular_velocity_in_radians(new_max_ang_vel, add_to_current=False, bone_name="None") -> None
Set the maximum angular velocity of a single body.

Args:
    new_max_ang_vel (float): New maximum angular velocity to apply to body, in radians per second.
    add_to_current (bool): If true, NewMaxAngVel is added to the existing maximum angular velocity of the body.
    bone_name (Name): If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_physics_max_angular_velocity_in_degrees"></a>

#### set_physics_max_angular_velocity_in_degrees

```python
def set_physics_max_angular_velocity_in_degrees(
        new_max_ang_vel: float,
        add_to_current: bool = False,
        bone_name: Name = "None") -> None
```

x.set_physics_max_angular_velocity_in_degrees(new_max_ang_vel, add_to_current=False, bone_name="None") -> None
Set the maximum angular velocity of a single body.

Args:
    new_max_ang_vel (float): New maximum angular velocity to apply to body, in degrees per second.
    add_to_current (bool): If true, NewMaxAngVel is added to the existing maximum angular velocity of the body.
    bone_name (Name): If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_physics_linear_velocity"></a>

#### set_physics_linear_velocity

```python
def set_physics_linear_velocity(new_vel: Vector,
                                add_to_current: bool = False,
                                bone_name: Name = "None") -> None
```

x.set_physics_linear_velocity(new_vel, add_to_current=False, bone_name="None") -> None
Set the linear velocity of a single body.
This should be used cautiously - it may be better to use AddForce or AddImpulse.

Args:
    new_vel (Vector): New linear velocity to apply to physics.
    add_to_current (bool): If true, NewVel is added to the existing velocity of the body.
    bone_name (Name): If a SkeletalMeshComponent, name of body to modify velocity of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_rb_linear_velocity"></a>

#### set_rb_linear_velocity

```python
def set_rb_linear_velocity(new_vel: Vector,
                           add_to_current: bool = False,
                           bone_name: Name = "None") -> None
```

deprecated: 'set_rb_linear_velocity' was renamed to 'set_physics_linear_velocity'.

<a id="unreal.PrimitiveComponent.set_physics_angular_velocity_in_radians"></a>

#### set_physics_angular_velocity_in_radians

```python
def set_physics_angular_velocity_in_radians(new_ang_vel: Vector,
                                            add_to_current: bool = False,
                                            bone_name: Name = "None") -> None
```

x.set_physics_angular_velocity_in_radians(new_ang_vel, add_to_current=False, bone_name="None") -> None
Set the angular velocity of a single body.
This should be used cautiously - it may be better to use AddTorque or AddImpulse.

Args:
    new_ang_vel (Vector): New angular velocity to apply to body, in radians per second.
    add_to_current (bool): If true, NewAngVel is added to the existing angular velocity of the body.
    bone_name (Name): If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_physics_angular_velocity_in_degrees"></a>

#### set_physics_angular_velocity_in_degrees

```python
def set_physics_angular_velocity_in_degrees(new_ang_vel: Vector,
                                            add_to_current: bool = False,
                                            bone_name: Name = "None") -> None
```

x.set_physics_angular_velocity_in_degrees(new_ang_vel, add_to_current=False, bone_name="None") -> None
Set the angular velocity of a single body.
This should be used cautiously - it may be better to use AddTorque or AddImpulse.

Args:
    new_ang_vel (Vector): New angular velocity to apply to body, in degrees per second.
    add_to_current (bool): If true, NewAngVel is added to the existing angular velocity of the body.
    bone_name (Name): If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_owner_no_see"></a>

#### set_owner_no_see

```python
def set_owner_no_see(new_owner_no_see: bool) -> None
```

x.set_owner_no_see(new_owner_no_see) -> None
Changes the value of bOwnerNoSee.

Args:
    new_owner_no_see (bool):

<a id="unreal.PrimitiveComponent.set_only_owner_see"></a>

#### set_only_owner_see

```python
def set_only_owner_see(new_only_owner_see: bool) -> None
```

x.set_only_owner_see(new_only_owner_see) -> None
Changes the value of bOnlyOwnerSee.

Args:
    new_only_owner_see (bool):

<a id="unreal.PrimitiveComponent.set_notify_rigid_body_collision"></a>

#### set_notify_rigid_body_collision

```python
def set_notify_rigid_body_collision(
        new_notify_rigid_body_collision: bool) -> None
```

x.set_notify_rigid_body_collision(new_notify_rigid_body_collision) -> None
Changes the value of bNotifyRigidBodyCollision

Args:
    new_notify_rigid_body_collision (bool):

<a id="unreal.PrimitiveComponent.set_max_depenetration_velocity"></a>

#### set_max_depenetration_velocity

```python
def set_max_depenetration_velocity(
        bone_name: Name = "None",
        max_depenetration_velocity: float = -1.000000) -> None
```

x.set_max_depenetration_velocity(bone_name="None", max_depenetration_velocity=-1.000000) -> None
The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
A negative value means that the config setting CollisionInitialOverlapDepenetrationVelocity will be used.

Args:
    bone_name (Name): 
    max_depenetration_velocity (float):

<a id="unreal.PrimitiveComponent.set_material_by_name"></a>

#### set_material_by_name

```python
def set_material_by_name(material_slot_name: Name,
                         material: MaterialInterface) -> None
```

x.set_material_by_name(material_slot_name, material) -> None
Changes the material applied to an element of the mesh.

Args:
    material_slot_name (Name): The slot name to access the material of.
    material (MaterialInterface):

<a id="unreal.PrimitiveComponent.set_material"></a>

#### set_material

```python
def set_material(element_index: int, material: MaterialInterface) -> None
```

x.set_material(element_index, material) -> None
Changes the material applied to an element of the mesh.

Args:
    element_index (int32): The element to access the material of.
    material (MaterialInterface):

<a id="unreal.PrimitiveComponent.set_mass_scale"></a>

#### set_mass_scale

```python
def set_mass_scale(bone_name: Name = "None",
                   mass_scale: float = 1.000000) -> None
```

x.set_mass_scale(bone_name="None", mass_scale=1.000000) -> None
Change the mass scale used to calculate the mass of a single physics body

Args:
    bone_name (Name): 
    mass_scale (float):

<a id="unreal.PrimitiveComponent.set_mass_override_in_kg"></a>

#### set_mass_override_in_kg

```python
def set_mass_override_in_kg(bone_name: Name = "None",
                            mass_in_kg: float = 1.000000,
                            override_mass: bool = True) -> None
```

x.set_mass_override_in_kg(bone_name="None", mass_in_kg=1.000000, override_mass=True) -> None
Override the mass (in Kg) of a single physics body.
Note that in the case where multiple bodies are attached together, the override mass will be set for the entire group.
Set the Override Mass to false if you want to reset the body's mass to the auto-calculated physx mass.

Args:
    bone_name (Name): 
    mass_in_kg (float): 
    override_mass (bool):

<a id="unreal.PrimitiveComponent.set_linear_damping"></a>

#### set_linear_damping

```python
def set_linear_damping(damping: float) -> None
```

x.set_linear_damping(damping) -> None
Sets the linear damping of this component.

Args:
    damping (float):

<a id="unreal.PrimitiveComponent.set_lighting_channels"></a>

#### set_lighting_channels

```python
def set_lighting_channels(channel0: bool, channel1: bool,
                          channel2: bool) -> None
```

x.set_lighting_channels(channel0, channel1, channel2) -> None
Set Lighting Channels

Args:
    channel0 (bool): 
    channel1 (bool): 
    channel2 (bool):

<a id="unreal.PrimitiveComponent.set_light_attachments_as_group"></a>

#### set_light_attachments_as_group

```python
def set_light_attachments_as_group(light_attachments_as_group: bool) -> None
```

x.set_light_attachments_as_group(light_attachments_as_group) -> None
Changes the value of LightAttachmentsAsGroup.

Args:
    light_attachments_as_group (bool):

<a id="unreal.PrimitiveComponent.set_ignore_bounds_for_editor_focus"></a>

#### set_ignore_bounds_for_editor_focus

```python
def set_ignore_bounds_for_editor_focus(ignore: bool) -> None
```

x.set_ignore_bounds_for_editor_focus(ignore) -> None
Set if we should ignore bounds when focusing the editor camera.

Args:
    ignore (bool):

<a id="unreal.PrimitiveComponent.set_holdout"></a>

#### set_holdout

```python
def set_holdout(new_holdout: bool) -> None
```

x.set_holdout(new_holdout) -> None
Changes the value of bHoldout

Args:
    new_holdout (bool):

<a id="unreal.PrimitiveComponent.set_hidden_in_scene_capture"></a>

#### set_hidden_in_scene_capture

```python
def set_hidden_in_scene_capture(value: bool) -> None
```

x.set_hidden_in_scene_capture(value) -> None
Sets bHideInSceneCapture property and marks the render state dirty.

Args:
    value (bool):

<a id="unreal.PrimitiveComponent.set_first_person_primitive_type"></a>

#### set_first_person_primitive_type

```python
def set_first_person_primitive_type(value: FirstPersonPrimitiveType) -> None
```

x.set_first_person_primitive_type(value) -> None
Sets FirstPersonPrimitiveType property and marks the render state dirty.

Args:
    value (FirstPersonPrimitiveType):

<a id="unreal.PrimitiveComponent.set_exclude_from_light_attachment_group"></a>

#### set_exclude_from_light_attachment_group

```python
def set_exclude_from_light_attachment_group(
        exclude_from_light_attachment_group: bool) -> None
```

x.set_exclude_from_light_attachment_group(exclude_from_light_attachment_group) -> None
Changes the value of ExcludeFromLightAttachmentGroup.

Args:
    exclude_from_light_attachment_group (bool):

<a id="unreal.PrimitiveComponent.set_excluded_from_hlod_level"></a>

#### set_excluded_from_hlod_level

```python
def set_excluded_from_hlod_level(hlod_level: HLODLevelExclusion,
                                 excluded: bool) -> None
```

x.set_excluded_from_hlod_level(hlod_level, excluded) -> None
Exclude this primitive from the specified HLOD level

Args:
    hlod_level (HLODLevelExclusion): 
    excluded (bool):

<a id="unreal.PrimitiveComponent.set_enable_gravity"></a>

#### set_enable_gravity

```python
def set_enable_gravity(gravity_enabled: bool) -> None
```

x.set_enable_gravity(gravity_enabled) -> None
Enables/disables whether this component is affected by gravity. This applies only to components with bSimulatePhysics set to true.

Args:
    gravity_enabled (bool):

<a id="unreal.PrimitiveComponent.set_emissive_light_source"></a>

#### set_emissive_light_source

```python
def set_emissive_light_source(new_emissive_light_source: bool) -> None
```

x.set_emissive_light_source(new_emissive_light_source) -> None
Changes the value of EmissiveLightSource.

Args:
    new_emissive_light_source (bool):

<a id="unreal.PrimitiveComponent.set_default_custom_primitive_data_vector4"></a>

#### set_default_custom_primitive_data_vector4

```python
def set_default_custom_primitive_data_vector4(data_index: int,
                                              value: Vector4) -> None
```

x.set_default_custom_primitive_data_vector4(data_index, value) -> None
Set default custom primitive data, four floats at once, from index DataIndex to index DataIndex + 3, and marks the render state dirty

Args:
    data_index (int32): 
    value (Vector4):

<a id="unreal.PrimitiveComponent.set_default_custom_primitive_data_vector3"></a>

#### set_default_custom_primitive_data_vector3

```python
def set_default_custom_primitive_data_vector3(data_index: int,
                                              value: Vector) -> None
```

x.set_default_custom_primitive_data_vector3(data_index, value) -> None
Set default custom primitive data, three floats at once, from index DataIndex to index DataIndex + 2, and marks the render state dirty

Args:
    data_index (int32): 
    value (Vector):

<a id="unreal.PrimitiveComponent.set_default_custom_primitive_data_vector2"></a>

#### set_default_custom_primitive_data_vector2

```python
def set_default_custom_primitive_data_vector2(data_index: int,
                                              value: Vector2D) -> None
```

x.set_default_custom_primitive_data_vector2(data_index, value) -> None
Set default custom primitive data, two floats at once, from index DataIndex to index DataIndex + 1, and marks the render state dirty

Args:
    data_index (int32): 
    value (Vector2D):

<a id="unreal.PrimitiveComponent.set_default_custom_primitive_data_float"></a>

#### set_default_custom_primitive_data_float

```python
def set_default_custom_primitive_data_float(data_index: int,
                                            value: float) -> None
```

x.set_default_custom_primitive_data_float(data_index, value) -> None
Set default custom primitive data at index DataIndex, and marks the render state dirty

Args:
    data_index (int32): 
    value (float):

<a id="unreal.PrimitiveComponent.set_custom_primitive_data_vector4"></a>

#### set_custom_primitive_data_vector4

```python
def set_custom_primitive_data_vector4(data_index: int, value: Vector4) -> None
```

x.set_custom_primitive_data_vector4(data_index, value) -> None
Set custom primitive data, four floats at once, from index DataIndex to index DataIndex + 3. This sets the run-time data only, so it doesn't serialize.

Args:
    data_index (int32): 
    value (Vector4):

<a id="unreal.PrimitiveComponent.set_custom_primitive_data_vector3"></a>

#### set_custom_primitive_data_vector3

```python
def set_custom_primitive_data_vector3(data_index: int, value: Vector) -> None
```

x.set_custom_primitive_data_vector3(data_index, value) -> None
Set custom primitive data, three floats at once, from index DataIndex to index DataIndex + 2. This sets the run-time data only, so it doesn't serialize.

Args:
    data_index (int32): 
    value (Vector):

<a id="unreal.PrimitiveComponent.set_custom_primitive_data_vector2"></a>

#### set_custom_primitive_data_vector2

```python
def set_custom_primitive_data_vector2(data_index: int,
                                      value: Vector2D) -> None
```

x.set_custom_primitive_data_vector2(data_index, value) -> None
Set custom primitive data, two floats at once, from index DataIndex to index DataIndex + 1. This sets the run-time data only, so it doesn't serialize.

Args:
    data_index (int32): 
    value (Vector2D):

<a id="unreal.PrimitiveComponent.set_custom_primitive_data_float"></a>

#### set_custom_primitive_data_float

```python
def set_custom_primitive_data_float(data_index: int, value: float) -> None
```

x.set_custom_primitive_data_float(data_index, value) -> None
Set custom primitive data at index DataIndex. This sets the run-time data only, so it doesn't serialize.

Args:
    data_index (int32): 
    value (float):

<a id="unreal.PrimitiveComponent.set_custom_depth_stencil_write_mask"></a>

#### set_custom_depth_stencil_write_mask

```python
def set_custom_depth_stencil_write_mask(
        write_mask_bit: RendererStencilMask) -> None
```

x.set_custom_depth_stencil_write_mask(write_mask_bit) -> None
Sets the CustomDepth stencil write mask and marks the render state dirty.

Args:
    write_mask_bit (RendererStencilMask):

<a id="unreal.PrimitiveComponent.set_custom_depth_stencil_value"></a>

#### set_custom_depth_stencil_value

```python
def set_custom_depth_stencil_value(value: int) -> None
```

x.set_custom_depth_stencil_value(value) -> None
Sets the CustomDepth stencil value (0 - 255) and marks the render state dirty.

Args:
    value (int32):

<a id="unreal.PrimitiveComponent.set_cull_distance"></a>

#### set_cull_distance

```python
def set_cull_distance(new_cull_distance: float) -> None
```

x.set_cull_distance(new_cull_distance) -> None
Changes the value of CullDistance.

Args:
    new_cull_distance (float): The value to assign to CullDistance.

<a id="unreal.PrimitiveComponent.set_constraint_mode"></a>

#### set_constraint_mode

```python
def set_constraint_mode(constraint_mode: DOFMode) -> None
```

x.set_constraint_mode(constraint_mode) -> None
Sets the constraint mode of the component.

Args:
    constraint_mode (DOFMode): The type of constraint to use.

<a id="unreal.PrimitiveComponent.set_collision_response_to_channel"></a>

#### set_collision_response_to_channel

```python
def set_collision_response_to_channel(
        channel: CollisionChannel,
        new_response: CollisionResponseType) -> None
```

x.set_collision_response_to_channel(channel, new_response) -> None
Changes a member of the ResponseToChannels container for this PrimitiveComponent.

Args:
    channel (CollisionChannel): The channel to change the response of
    new_response (CollisionResponseType): What the new response should be to the supplied Channel

<a id="unreal.PrimitiveComponent.set_collision_response_to_all_channels"></a>

#### set_collision_response_to_all_channels

```python
def set_collision_response_to_all_channels(
        new_response: CollisionResponseType) -> None
```

x.set_collision_response_to_all_channels(new_response) -> None
Changes all ResponseToChannels container for this PrimitiveComponent. to be NewResponse

Args:
    new_response (CollisionResponseType): What the new response should be to the supplied Channel

<a id="unreal.PrimitiveComponent.set_collision_profile_name"></a>

#### set_collision_profile_name

```python
def set_collision_profile_name(collision_profile_name: Name,
                               update_overlaps: bool = True) -> None
```

x.set_collision_profile_name(collision_profile_name, update_overlaps=True) -> None
Set Collision Profile Name
This function is called by constructors when they set ProfileName
This will change current CollisionProfileName to be this, and overwrite Collision Setting

Args:
    collision_profile_name (Name): : New Profile Name
    update_overlaps (bool):

<a id="unreal.PrimitiveComponent.set_collision_object_type"></a>

#### set_collision_object_type

```python
def set_collision_object_type(channel: CollisionChannel) -> None
```

x.set_collision_object_type(channel) -> None
Changes the collision channel that this object uses when it moves

Args:
    channel (CollisionChannel): The new channel for this component to use

<a id="unreal.PrimitiveComponent.set_movement_channel"></a>

#### set_movement_channel

```python
def set_movement_channel(channel: CollisionChannel) -> None
```

deprecated: 'set_movement_channel' was renamed to 'set_collision_object_type'.

<a id="unreal.PrimitiveComponent.set_collision_enabled"></a>

#### set_collision_enabled

```python
def set_collision_enabled(new_type: CollisionEnabled) -> None
```

x.set_collision_enabled(new_type) -> None
Controls what kind of collision is enabled for this body

Args:
    new_type (CollisionEnabled):

<a id="unreal.PrimitiveComponent.set_center_of_mass"></a>

#### set_center_of_mass

```python
def set_center_of_mass(center_of_mass_offset: Vector,
                       bone_name: Name = "None") -> None
```

x.set_center_of_mass(center_of_mass_offset, bone_name="None") -> None
Set the center of mass of a single body. This will offset the physx-calculated center of mass.
Note that in the case where multiple bodies are attached together, the center of mass will be set for the entire group.

Args:
    center_of_mass_offset (Vector): User specified offset for the center of mass of this object, from the calculated location.
    bone_name (Name): If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.set_cast_shadow"></a>

#### set_cast_shadow

```python
def set_cast_shadow(new_cast_shadow: bool) -> None
```

x.set_cast_shadow(new_cast_shadow) -> None
Changes the value of CastShadow.

Args:
    new_cast_shadow (bool):

<a id="unreal.PrimitiveComponent.set_cast_inset_shadow"></a>

#### set_cast_inset_shadow

```python
def set_cast_inset_shadow(cast_inset_shadow: bool) -> None
```

x.set_cast_inset_shadow(cast_inset_shadow) -> None
Changes the value of CastInsetShadow.

Args:
    cast_inset_shadow (bool):

<a id="unreal.PrimitiveComponent.set_cast_hidden_shadow"></a>

#### set_cast_hidden_shadow

```python
def set_cast_hidden_shadow(new_cast_hidden_shadow: bool) -> None
```

x.set_cast_hidden_shadow(new_cast_hidden_shadow) -> None
Changes the value of CastHiddenShadow.

Args:
    new_cast_hidden_shadow (bool):

<a id="unreal.PrimitiveComponent.set_cast_contact_shadow"></a>

#### set_cast_contact_shadow

```python
def set_cast_contact_shadow(cast_contact_shadow: bool) -> None
```

x.set_cast_contact_shadow(cast_contact_shadow) -> None
Changes the value of bCastContactShadow.

Args:
    cast_contact_shadow (bool):

<a id="unreal.PrimitiveComponent.set_bounds_scale"></a>

#### set_bounds_scale

```python
def set_bounds_scale(new_bounds_scale: float = 1.000000) -> None
```

x.set_bounds_scale(new_bounds_scale=1.000000) -> None
Scale the bounds of this object, used for frustum culling. Useful for features like WorldPositionOffset.

Args:
    new_bounds_scale (float):

<a id="unreal.PrimitiveComponent.set_angular_damping"></a>

#### set_angular_damping

```python
def set_angular_damping(damping: float) -> None
```

x.set_angular_damping(damping) -> None
Sets the angular damping of this component.

Args:
    damping (float):

<a id="unreal.PrimitiveComponent.set_all_use_macd"></a>

#### set_all_use_macd

```python
def set_all_use_macd(use_macd: bool) -> None
```

x.set_all_use_macd(use_macd) -> None
[EXPERIMENTAL] Set whether all bodies in this component should use Motion-Aware Collision Detection

Args:
    use_macd (bool):

<a id="unreal.PrimitiveComponent.set_all_use_ccd"></a>

#### set_all_use_ccd

```python
def set_all_use_ccd(use_ccd: bool) -> None
```

x.set_all_use_ccd(use_ccd) -> None
Set whether all bodies in this component should use Continuous Collision Detection

Args:
    use_ccd (bool):

<a id="unreal.PrimitiveComponent.set_all_physics_linear_velocity"></a>

#### set_all_physics_linear_velocity

```python
def set_all_physics_linear_velocity(new_vel: Vector,
                                    add_to_current: bool = False) -> None
```

x.set_all_physics_linear_velocity(new_vel, add_to_current=False) -> None
Set the linear velocity of all bodies in this component.

Args:
    new_vel (Vector): New linear velocity to apply to physics.
    add_to_current (bool): If true, NewVel is added to the existing velocity of the body.

<a id="unreal.PrimitiveComponent.set_all_rb_linear_velocity"></a>

#### set_all_rb_linear_velocity

```python
def set_all_rb_linear_velocity(new_vel: Vector,
                               add_to_current: bool = False) -> None
```

deprecated: 'set_all_rb_linear_velocity' was renamed to 'set_all_physics_linear_velocity'.

<a id="unreal.PrimitiveComponent.set_all_physics_angular_velocity_in_radians"></a>

#### set_all_physics_angular_velocity_in_radians

```python
def set_all_physics_angular_velocity_in_radians(new_ang_vel: Vector,
                                                add_to_current: bool = False
                                                ) -> None
```

x.set_all_physics_angular_velocity_in_radians(new_ang_vel, add_to_current=False) -> None
Set the angular velocity of all bodies in this component.

Args:
    new_ang_vel (Vector): New angular velocity to apply to physics, in radians per second.
    add_to_current (bool): If true, NewAngVel is added to the existing angular velocity of all bodies.

<a id="unreal.PrimitiveComponent.set_all_physics_angular_velocity_in_degrees"></a>

#### set_all_physics_angular_velocity_in_degrees

```python
def set_all_physics_angular_velocity_in_degrees(new_ang_vel: Vector,
                                                add_to_current: bool = False
                                                ) -> None
```

x.set_all_physics_angular_velocity_in_degrees(new_ang_vel, add_to_current=False) -> None
Set the angular velocity of all bodies in this component.

Args:
    new_ang_vel (Vector): New angular velocity to apply to physics, in degrees per second.
    add_to_current (bool): If true, NewAngVel is added to the existing angular velocity of all bodies.

<a id="unreal.PrimitiveComponent.set_all_mass_scale"></a>

#### set_all_mass_scale

```python
def set_all_mass_scale(mass_scale: float = 1.000000) -> None
```

x.set_all_mass_scale(mass_scale=1.000000) -> None
Change the mass scale used fo all bodies in this component

Args:
    mass_scale (float):

<a id="unreal.PrimitiveComponent.set_affect_indirect_lighting_while_hidden"></a>

#### set_affect_indirect_lighting_while_hidden

```python
def set_affect_indirect_lighting_while_hidden(
        new_affect_indirect_lighting_while_hidden: bool) -> None
```

x.set_affect_indirect_lighting_while_hidden(new_affect_indirect_lighting_while_hidden) -> None
Changes the value of bAffectIndirectLightingWhileHidden

Args:
    new_affect_indirect_lighting_while_hidden (bool):

<a id="unreal.PrimitiveComponent.set_affect_dynamic_indirect_lighting"></a>

#### set_affect_dynamic_indirect_lighting

```python
def set_affect_dynamic_indirect_lighting(
        new_affect_dynamic_indirect_lighting: bool) -> None
```

x.set_affect_dynamic_indirect_lighting(new_affect_dynamic_indirect_lighting) -> None
Changes the value of bAffectDynamicIndirectLighting

Args:
    new_affect_dynamic_indirect_lighting (bool):

<a id="unreal.PrimitiveComponent.set_affect_distance_field_lighting"></a>

#### set_affect_distance_field_lighting

```python
def set_affect_distance_field_lighting(
        new_affect_distance_field_lighting: bool) -> None
```

x.set_affect_distance_field_lighting(new_affect_distance_field_lighting) -> None
Changes the value of Affect Distance Field Lighting

Args:
    new_affect_distance_field_lighting (bool):

<a id="unreal.PrimitiveComponent.scale_by_moment_of_inertia"></a>

#### scale_by_moment_of_inertia

```python
def scale_by_moment_of_inertia(input_vector: Vector,
                               bone_name: Name = "None") -> Vector
```

x.scale_by_moment_of_inertia(input_vector, bone_name="None") -> Vector
Scales the given vector by the world space moment of inertia. Useful for computing the torque needed to rotate an object.

Args:
    input_vector (Vector): 
    bone_name (Name): 

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.put_rigid_body_to_sleep"></a>

#### put_rigid_body_to_sleep

```python
def put_rigid_body_to_sleep(bone_name: Name = "None") -> None
```

x.put_rigid_body_to_sleep(bone_name="None") -> None
Force a single body back to sleep.

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to put to sleep. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.sphere_trace_component"></a>

#### sphere_trace_component

```python
def sphere_trace_component(
    trace_start: Vector,
    trace_end: Vector,
    sphere_radius: float,
    trace_complex: bool = True,
    show_trace: bool = ...,
    persistent_show_trace: bool = False
) -> Optional[Tuple[Vector, Vector, Name, HitResult]]
```

x.sphere_trace_component(trace_start, trace_end, sphere_radius, trace_complex=True, show_trace, persistent_show_trace=False) -> (hit_location=Vector, hit_normal=Vector, bone_name=Name, out_hit=HitResult) or None
Perform a sphere trace against a single component

Args:
    trace_start (Vector): The start of the trace in world-space
    trace_end (Vector): The end of the trace in world-space
    sphere_radius (float): Radius of the sphere to trace against the component
    trace_complex (bool): Whether or not to trace the complex physics representation or just the simple representation
    show_trace (bool): Whether or not to draw the trace in the world (for debugging)
    persistent_show_trace (bool): Whether or not to make the debugging draw stay in the world permanently

Returns:
    tuple or None: 

    hit_location (Vector): 

    hit_normal (Vector): 

    bone_name (Name): 

    out_hit (HitResult):

<a id="unreal.PrimitiveComponent.sphere_overlap_component"></a>

#### sphere_overlap_component

```python
def sphere_overlap_component(
    sphere_centre: Vector,
    sphere_radius: float,
    trace_complex: bool = True,
    show_trace: bool = ...,
    persistent_show_trace: bool = False
) -> Optional[Tuple[Vector, Vector, Name, HitResult]]
```

x.sphere_overlap_component(sphere_centre, sphere_radius, trace_complex=True, show_trace, persistent_show_trace=False) -> (hit_location=Vector, hit_normal=Vector, bone_name=Name, out_hit=HitResult) or None
Perform a sphere overlap against a single component

Args:
    sphere_centre (Vector): The centre of the sphere to overlap with the component
    sphere_radius (float): The Radius of the sphere to overlap with the component
    trace_complex (bool): Whether or not to trace the complex physics representation or just the simple representation
    show_trace (bool): Whether or not to draw the trace in the world (for debugging)
    persistent_show_trace (bool): Whether or not to make the debugging draw stay in the world permanently

Returns:
    tuple or None: 

    hit_location (Vector): 

    hit_normal (Vector): 

    bone_name (Name): 

    out_hit (HitResult):

<a id="unreal.PrimitiveComponent.line_trace_component"></a>

#### line_trace_component

```python
def line_trace_component(
    trace_start: Vector,
    trace_end: Vector,
    trace_complex: bool = True,
    show_trace: bool = ...,
    persistent_show_trace: bool = False
) -> Optional[Tuple[Vector, Vector, Name, HitResult]]
```

x.line_trace_component(trace_start, trace_end, trace_complex=True, show_trace, persistent_show_trace=False) -> (hit_location=Vector, hit_normal=Vector, bone_name=Name, out_hit=HitResult) or None
Perform a line trace against a single component

Args:
    trace_start (Vector): The start of the trace in world-space
    trace_end (Vector): The end of the trace in world-space
    trace_complex (bool): Whether or not to trace the complex physics representation or just the simple representation
    show_trace (bool): Whether or not to draw the trace in the world (for debugging)
    persistent_show_trace (bool): Whether or not to make the debugging draw stay in the world permanently

Returns:
    tuple or None: 

    hit_location (Vector): 

    hit_normal (Vector): 

    bone_name (Name): 

    out_hit (HitResult):

<a id="unreal.PrimitiveComponent.is_query_collision_enabled"></a>

#### is_query_collision_enabled

```python
def is_query_collision_enabled() -> bool
```

x.is_query_collision_enabled() -> bool
Utility to see if there is any query collision enabled on this component.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.is_physics_collision_enabled"></a>

#### is_physics_collision_enabled

```python
def is_physics_collision_enabled() -> bool
```

x.is_physics_collision_enabled() -> bool
Utility to see if there is any physics collision enabled on this component.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.is_collision_enabled"></a>

#### is_collision_enabled

```python
def is_collision_enabled() -> bool
```

x.is_collision_enabled() -> bool
Utility to see if there is any form of collision (query or physics) enabled on this component.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.box_overlap_component"></a>

#### box_overlap_component

```python
def box_overlap_component(
    box_centre: Vector,
    box: Box,
    trace_complex: bool = True,
    show_trace: bool = ...,
    persistent_show_trace: bool = False
) -> Optional[Tuple[Vector, Vector, Name, HitResult]]
```

x.box_overlap_component(box_centre, box, trace_complex=True, show_trace, persistent_show_trace=False) -> (hit_location=Vector, hit_normal=Vector, bone_name=Name, out_hit=HitResult) or None
Perform a box overlap against a single component as an AABB (No rotation)

Args:
    box_centre (Vector): The centre of the box to overlap with the component
    box (Box): Description of the box to use in the overlap
    trace_complex (bool): Whether or not to trace the complex physics representation or just the simple representation
    show_trace (bool): Whether or not to draw the trace in the world (for debugging)
    persistent_show_trace (bool): Whether or not to make the debugging draw stay in the world permanently

Returns:
    tuple or None: 

    hit_location (Vector): 

    hit_normal (Vector): 

    bone_name (Name): 

    out_hit (HitResult):

<a id="unreal.PrimitiveComponent.is_overlapping_component"></a>

#### is_overlapping_component

```python
def is_overlapping_component(other_comp: PrimitiveComponent) -> bool
```

x.is_overlapping_component(other_comp) -> bool
Check whether this component is overlapping another component.

Args:
    other_comp (PrimitiveComponent): Component to test this component against.

Returns:
    bool: Whether this component is overlapping another component.

<a id="unreal.PrimitiveComponent.is_overlapping_actor"></a>

#### is_overlapping_actor

```python
def is_overlapping_actor(other: Actor) -> bool
```

x.is_overlapping_actor(other) -> bool
Check whether this component is overlapping any component of the given Actor.

Args:
    other (Actor): Actor to test this component against.

Returns:
    bool: Whether this component is overlapping any component of the given Actor.

<a id="unreal.PrimitiveComponent.is_material_slot_name_valid"></a>

#### is_material_slot_name_valid

```python
def is_material_slot_name_valid(material_slot_name: Name) -> bool
```

x.is_material_slot_name_valid(material_slot_name) -> bool
Is Material Slot Name Valid

Args:
    material_slot_name (Name): 

Returns:
    bool:

<a id="unreal.PrimitiveComponent.is_gravity_enabled"></a>

#### is_gravity_enabled

```python
def is_gravity_enabled() -> bool
```

x.is_gravity_enabled() -> bool
Returns whether this component is affected by gravity. Returns always false if the component is not simulated.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.is_excluded_from_hlod_level"></a>

#### is_excluded_from_hlod_level

```python
def is_excluded_from_hlod_level(hlod_level: HLODLevelExclusion) -> bool
```

x.is_excluded_from_hlod_level(hlod_level) -> bool
Whether this primitive is excluded from the specified HLOD level

Args:
    hlod_level (HLODLevelExclusion): 

Returns:
    bool:

<a id="unreal.PrimitiveComponent.is_any_rigid_body_awake"></a>

#### is_any_rigid_body_awake

```python
def is_any_rigid_body_awake() -> bool
```

x.is_any_rigid_body_awake() -> bool
Returns if any body in this component is currently awake and simulating.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.invalidate_lumen_surface_cache"></a>

#### invalidate_lumen_surface_cache

```python
def invalidate_lumen_surface_cache() -> None
```

x.invalidate_lumen_surface_cache() -> None
Invalidates Lumen surface cache and forces it to be refreshed. Useful to make material updates more responsive.

<a id="unreal.PrimitiveComponent.ignore_component_when_moving"></a>

#### ignore_component_when_moving

```python
def ignore_component_when_moving(component: PrimitiveComponent,
                                 should_ignore: bool) -> None
```

x.ignore_component_when_moving(component, should_ignore) -> None
Tells this component whether to ignore collision with another component when this component is moved.
The other components may also need to be told to do the same when they move.
Does not affect movement of this component when simulating physics.

Args:
    component (PrimitiveComponent): 
    should_ignore (bool):

<a id="unreal.PrimitiveComponent.ignore_actor_when_moving"></a>

#### ignore_actor_when_moving

```python
def ignore_actor_when_moving(actor: Actor, should_ignore: bool) -> None
```

x.ignore_actor_when_moving(actor, should_ignore) -> None
Tells this component whether to ignore collision with all components of a specific Actor when this component is moved.
Components on the other Actor may also need to be told to do the same when they move.
Does not affect movement of this component when simulating physics.

Args:
    actor (Actor): 
    should_ignore (bool):

<a id="unreal.PrimitiveComponent.get_walkable_slope_override"></a>

#### get_walkable_slope_override

```python
def get_walkable_slope_override() -> WalkableSlopeOverride
```

x.get_walkable_slope_override() -> WalkableSlopeOverride
Returns the slope override struct for this component.

Returns:
    WalkableSlopeOverride:

<a id="unreal.PrimitiveComponent.get_update_kinematic_from_simulation"></a>

#### get_update_kinematic_from_simulation

```python
def get_update_kinematic_from_simulation() -> bool
```

x.get_update_kinematic_from_simulation() -> bool
Returns whether this component should be updated by simulation when it is kinematic.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.get_static_when_not_moveable"></a>

#### get_static_when_not_moveable

```python
def get_static_when_not_moveable() -> bool
```

x.get_static_when_not_moveable() -> bool
Get Static when Not Moveable

Returns:
    bool:

<a id="unreal.PrimitiveComponent.get_physics_linear_velocity_at_point"></a>

#### get_physics_linear_velocity_at_point

```python
def get_physics_linear_velocity_at_point(point: Vector,
                                         bone_name: Name = "None") -> Vector
```

x.get_physics_linear_velocity_at_point(point, bone_name="None") -> Vector
Get the linear velocity of a point on a single body.

Args:
    point (Vector): Point is specified in world space.
    bone_name (Name): If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_physics_linear_velocity"></a>

#### get_physics_linear_velocity

```python
def get_physics_linear_velocity(bone_name: Name = "None") -> Vector
```

x.get_physics_linear_velocity(bone_name="None") -> Vector
Get the linear velocity of a single body.

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_rb_linear_velocity"></a>

#### get_rb_linear_velocity

```python
def get_rb_linear_velocity(bone_name: Name = "None") -> Vector
```

deprecated: 'get_rb_linear_velocity' was renamed to 'get_physics_linear_velocity'.

<a id="unreal.PrimitiveComponent.get_physics_angular_velocity_in_radians"></a>

#### get_physics_angular_velocity_in_radians

```python
def get_physics_angular_velocity_in_radians(
        bone_name: Name = "None") -> Vector
```

x.get_physics_angular_velocity_in_radians(bone_name="None") -> Vector
Get the angular velocity of a single body, in radians per second.

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_physics_angular_velocity_in_degrees"></a>

#### get_physics_angular_velocity_in_degrees

```python
def get_physics_angular_velocity_in_degrees(
        bone_name: Name = "None") -> Vector
```

x.get_physics_angular_velocity_in_degrees(bone_name="None") -> Vector
Get the angular velocity of a single body, in degrees per second.

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_overlapping_components"></a>

#### get_overlapping_components

```python
def get_overlapping_components() -> Array[PrimitiveComponent]
```

x.get_overlapping_components() -> Array[PrimitiveComponent]
Returns unique list of components this component is overlapping.

Returns:
    Array[PrimitiveComponent]: 

    out_overlapping_components (Array[PrimitiveComponent]):

<a id="unreal.PrimitiveComponent.get_touching_components"></a>

#### get_touching_components

```python
def get_touching_components() -> Array[PrimitiveComponent]
```

deprecated: 'get_touching_components' was renamed to 'get_overlapping_components'.

<a id="unreal.PrimitiveComponent.get_overlapping_actors"></a>

#### get_overlapping_actors

```python
def get_overlapping_actors(class_filter: Class = None) -> Array[Actor]
```

x.get_overlapping_actors(class_filter=None) -> Array[Actor]
Returns a list of actors that this component is overlapping.

Args:
    class_filter (type(Class)): [optional] If set, only returns actors of this class or subclasses

Returns:
    Array[Actor]: 

    overlapping_actors (Array[Actor]): [out] Returned list of overlapping actors

<a id="unreal.PrimitiveComponent.get_touching_actors"></a>

#### get_touching_actors

```python
def get_touching_actors(class_filter: Class = None) -> Array[Actor]
```

deprecated: 'get_touching_actors' was renamed to 'get_overlapping_actors'.

<a id="unreal.PrimitiveComponent.get_num_materials"></a>

#### get_num_materials

```python
def get_num_materials() -> int
```

x.get_num_materials() -> int32
Return number of material elements in this primitive

Returns:
    int32:

<a id="unreal.PrimitiveComponent.get_max_depenetration_velocity"></a>

#### get_max_depenetration_velocity

```python
def get_max_depenetration_velocity(bone_name: Name = "None") -> float
```

x.get_max_depenetration_velocity(bone_name="None") -> float
The maximum velocity used to depenetrate this object from others when spawned or teleported with initial overlaps (does not affect overlaps as a result of normal movement).
A value of zero will allow objects that are spawned overlapping to go to sleep without moving rather than pop out of each other. E.g., use zero if you spawn dynamic rocks
partially embedded in the ground and want them to be interactive but not pop out of the ground when touched.
A negative value means that the config setting CollisionInitialOverlapDepenetrationVelocity will be used.

Args:
    bone_name (Name): 

Returns:
    float:

<a id="unreal.PrimitiveComponent.get_material_slot_names"></a>

#### get_material_slot_names

```python
def get_material_slot_names() -> Array[Name]
```

x.get_material_slot_names() -> Array[Name]
Get Material Slot Names

Returns:
    Array[Name]:

<a id="unreal.PrimitiveComponent.get_material_index"></a>

#### get_material_index

```python
def get_material_index(material_slot_name: Name) -> int
```

x.get_material_index(material_slot_name) -> int32
Get Material Index

Args:
    material_slot_name (Name): 

Returns:
    int32:

<a id="unreal.PrimitiveComponent.get_material_from_collision_face_index"></a>

#### get_material_from_collision_face_index

```python
def get_material_from_collision_face_index(
        face_index: int) -> Tuple[MaterialInterface, int]
```

x.get_material_from_collision_face_index(face_index) -> (MaterialInterface, section_index=int32)
Try and retrieve the material applied to a particular collision face of mesh. Used with face index returned from collision trace.

Args:
    face_index (int32): Face index from hit result that was hit by a trace

Returns:
    int32: Material applied to section that the hit face belongs to

    section_index (int32): Section of the mesh that the face belongs to

<a id="unreal.PrimitiveComponent.get_material_by_name"></a>

#### get_material_by_name

```python
def get_material_by_name(material_slot_name: Name) -> MaterialInterface
```

x.get_material_by_name(material_slot_name) -> MaterialInterface
Returns the material used by the element in the slot with the specified name.

Args:
    material_slot_name (Name): The slot name to access the material of.

Returns:
    MaterialInterface: the material used in the slot specified, or null if none exists or the slot name is not found.

<a id="unreal.PrimitiveComponent.get_material"></a>

#### get_material

```python
def get_material(element_index: int) -> MaterialInterface
```

x.get_material(element_index) -> MaterialInterface
Returns the material used by the element at the specified index

Args:
    element_index (int32): The element to access the material of.

Returns:
    MaterialInterface: the material used by the indexed element of this mesh.

<a id="unreal.PrimitiveComponent.get_mass_scale"></a>

#### get_mass_scale

```python
def get_mass_scale(bone_name: Name = "None") -> float
```

x.get_mass_scale(bone_name="None") -> float
Returns the mass scale used to calculate the mass of a single physics body

Args:
    bone_name (Name): 

Returns:
    float:

<a id="unreal.PrimitiveComponent.get_mass"></a>

#### get_mass

```python
def get_mass() -> float
```

x.get_mass() -> float
Returns the mass of this component in kg.

Returns:
    float:

<a id="unreal.PrimitiveComponent.get_linear_damping"></a>

#### get_linear_damping

```python
def get_linear_damping() -> float
```

x.get_linear_damping() -> float
Returns the linear damping of this component.

Returns:
    float:

<a id="unreal.PrimitiveComponent.get_inertia_tensor"></a>

#### get_inertia_tensor

```python
def get_inertia_tensor(bone_name: Name = "None") -> Vector
```

x.get_inertia_tensor(bone_name="None") -> Vector
Returns the inertia tensor of this component in kg cm^2. The inertia tensor is in local component space.

Args:
    bone_name (Name): 

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_ignore_bounds_for_editor_focus"></a>

#### get_ignore_bounds_for_editor_focus

```python
def get_ignore_bounds_for_editor_focus() -> bool
```

x.get_ignore_bounds_for_editor_focus() -> bool
Whether or not the bounds of this component should be considered when focusing the editor camera to an actor with this component in it.
Useful for debug components which need a bounds for rendering but don't contribute to the visible part of the mesh in a meaningful way

Returns:
    bool:

<a id="unreal.PrimitiveComponent.get_editor_material"></a>

#### get_editor_material

```python
def get_editor_material(element_index: int) -> MaterialInterface
```

x.get_editor_material(element_index) -> MaterialInterface
Returns the material to show in the editor details panel as being used. Skips Nanite Override materials.

Args:
    element_index (int32): 

Returns:
    MaterialInterface:

<a id="unreal.PrimitiveComponent.get_custom_primitive_data_index_for_vector_parameter"></a>

#### get_custom_primitive_data_index_for_vector_parameter

```python
def get_custom_primitive_data_index_for_vector_parameter(
        parameter_name: Name) -> int
```

x.get_custom_primitive_data_index_for_vector_parameter(parameter_name) -> int32
Gets the index of the vector parameter for the custom primitive data array

Args:
    parameter_name (Name): The parameter name of the custom primitive

Returns:
    int32: The index of the custom primitive, INDEX_NONE (-1) if not found

<a id="unreal.PrimitiveComponent.get_custom_primitive_data_index_for_scalar_parameter"></a>

#### get_custom_primitive_data_index_for_scalar_parameter

```python
def get_custom_primitive_data_index_for_scalar_parameter(
        parameter_name: Name) -> int
```

x.get_custom_primitive_data_index_for_scalar_parameter(parameter_name) -> int32
Gets the index of the scalar parameter for the custom primitive data array

Args:
    parameter_name (Name): The parameter name of the custom primitive

Returns:
    int32: The index of the custom primitive, INDEX_NONE (-1) if not found

<a id="unreal.PrimitiveComponent.get_collision_response_to_channel"></a>

#### get_collision_response_to_channel

```python
def get_collision_response_to_channel(
        channel: CollisionChannel) -> CollisionResponseType
```

x.get_collision_response_to_channel(channel) -> CollisionResponseType
Gets the response type given a specific channel

Args:
    channel (CollisionChannel): 

Returns:
    CollisionResponseType:

<a id="unreal.PrimitiveComponent.get_collision_profile_name"></a>

#### get_collision_profile_name

```python
def get_collision_profile_name() -> Name
```

x.get_collision_profile_name() -> Name
Get the collision profile name

Returns:
    Name:

<a id="unreal.PrimitiveComponent.get_collision_object_type"></a>

#### get_collision_object_type

```python
def get_collision_object_type() -> CollisionChannel
```

x.get_collision_object_type() -> CollisionChannel
Gets the collision object type

Returns:
    CollisionChannel:

<a id="unreal.PrimitiveComponent.get_collision_enabled"></a>

#### get_collision_enabled

```python
def get_collision_enabled() -> CollisionEnabled
```

x.get_collision_enabled() -> CollisionEnabled
Returns the form of collision for this component

Returns:
    CollisionEnabled:

<a id="unreal.PrimitiveComponent.get_closest_point_on_collision"></a>

#### get_closest_point_on_collision

```python
def get_closest_point_on_collision(point: Vector,
                                   bone_name: Name = "None"
                                   ) -> Tuple[float, Vector]
```

x.get_closest_point_on_collision(point, bone_name="None") -> (float, out_point_on_body=Vector)
Returns the distance and closest point to the collision surface.
Component must have simple collision to be queried for closest point.

Args:
    point (Vector): World 3D vector
    bone_name (Name): If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body.

Returns:
    Vector: Success if returns > 0.f, if returns 0.f, it is either not convex or inside of the point If returns < 0.f, this primitive does not have collsion

    out_point_on_body (Vector): Point on the surface of collision closest to Point

<a id="unreal.PrimitiveComponent.get_center_of_mass"></a>

#### get_center_of_mass

```python
def get_center_of_mass(bone_name: Name = "None") -> Vector
```

x.get_center_of_mass(bone_name="None") -> Vector
Get the center of mass of a single body. In the case of a welded body this will return the center of mass of the entire welded body (including its parent and children)
Objects that are not simulated return (0,0,0) as they do not have COM

Args:
    bone_name (Name): If a SkeletalMeshComponent, name of body to get center of mass of. 'None' indicates root body.

Returns:
    Vector:

<a id="unreal.PrimitiveComponent.get_body_instance_async_physics_tick_handle"></a>

#### get_body_instance_async_physics_tick_handle

```python
def get_body_instance_async_physics_tick_handle(
        bone_name: Name = "None",
        get_welded: bool = True,
        index: int = -1) -> BodyInstanceAsyncPhysicsTickHandle
```

x.get_body_instance_async_physics_tick_handle(bone_name="None", get_welded=True, index=-1) -> BodyInstanceAsyncPhysicsTickHandle
Returns BodyInstanceAsyncPhysicsTickHandle of the component. For use in the Async Physics Tick event

Args:
    bone_name (Name): Used to get body associated with specific bone. NAME_None automatically gets the root most body
    get_welded (bool): If the component has been welded to another component and bGetWelded is true we return the single welded BodyInstance that is used in the simulation
    index (int32): Index used in Components with multiple body instances

Returns:
    BodyInstanceAsyncPhysicsTickHandle: Returns the BodyInstanceAsyncPhysicsTickHandle based on various states (does component have multiple bodies? Is the body welded to another body?)

<a id="unreal.PrimitiveComponent.get_angular_damping"></a>

#### get_angular_damping

```python
def get_angular_damping() -> float
```

x.get_angular_damping() -> float
Returns the angular damping of this component.

Returns:
    float:

<a id="unreal.PrimitiveComponent.create_dynamic_material_instance"></a>

#### create_dynamic_material_instance

```python
def create_dynamic_material_instance(
        element_index: int,
        source_material: MaterialInterface = None,
        optional_name: Name = "None") -> MaterialInstanceDynamic
```

x.create_dynamic_material_instance(element_index, source_material=None, optional_name="None") -> MaterialInstanceDynamic
Creates a Dynamic Material Instance for the specified element index, optionally from the supplied material.

Args:
    element_index (int32): The index of the skin to replace the material for.  If invalid, the material is unchanged and NULL is returned.
    source_material (MaterialInterface): 
    optional_name (Name): 

Returns:
    MaterialInstanceDynamic:

<a id="unreal.PrimitiveComponent.create_and_set_material_instance_dynamic_from_material"></a>

#### create_and_set_material_instance_dynamic_from_material

```python
def create_and_set_material_instance_dynamic_from_material(
        element_index: int,
        parent: MaterialInterface) -> MaterialInstanceDynamic
```

x.create_and_set_material_instance_dynamic_from_material(element_index, parent) -> MaterialInstanceDynamic
Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.
deprecated: Use CreateDynamicMaterialInstance instead.

Args:
    element_index (int32): The index of the skin to replace the material for.  If invalid, the material is unchanged and NULL is returned.
    parent (MaterialInterface): 

Returns:
    MaterialInstanceDynamic:

<a id="unreal.PrimitiveComponent.create_and_set_material_instance_dynamic"></a>

#### create_and_set_material_instance_dynamic

```python
def create_and_set_material_instance_dynamic(
        element_index: int) -> MaterialInstanceDynamic
```

x.create_and_set_material_instance_dynamic(element_index) -> MaterialInstanceDynamic
Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.
deprecated: Use CreateDynamicMaterialInstance instead.

Args:
    element_index (int32): The index of the skin to replace the material for.  If invalid, the material is unchanged and NULL is returned.

Returns:
    MaterialInstanceDynamic:

<a id="unreal.PrimitiveComponent.copy_array_of_move_ignore_components"></a>

#### copy_array_of_move_ignore_components

```python
def copy_array_of_move_ignore_components() -> Array[PrimitiveComponent]
```

x.copy_array_of_move_ignore_components() -> Array[PrimitiveComponent]
Returns the list of actors we currently ignore when moving.

Returns:
    Array[PrimitiveComponent]:

<a id="unreal.PrimitiveComponent.copy_array_of_move_ignore_actors"></a>

#### copy_array_of_move_ignore_actors

```python
def copy_array_of_move_ignore_actors() -> Array[Actor]
```

x.copy_array_of_move_ignore_actors() -> Array[Actor]
Returns the list of actors we currently ignore when moving.

Returns:
    Array[Actor]:

<a id="unreal.PrimitiveComponent.get_move_ignore_actors"></a>

#### get_move_ignore_actors

```python
def get_move_ignore_actors() -> Array[Actor]
```

deprecated: 'get_move_ignore_actors' was renamed to 'copy_array_of_move_ignore_actors'.

<a id="unreal.PrimitiveComponent.clear_move_ignore_components"></a>

#### clear_move_ignore_components

```python
def clear_move_ignore_components() -> None
```

x.clear_move_ignore_components() -> None
Clear the list of components we ignore when moving.

<a id="unreal.PrimitiveComponent.clear_move_ignore_actors"></a>

#### clear_move_ignore_actors

```python
def clear_move_ignore_actors() -> None
```

x.clear_move_ignore_actors() -> None
Clear the list of actors we ignore when moving.

<a id="unreal.PrimitiveComponent.can_character_step_up"></a>

#### can_character_step_up

```python
def can_character_step_up(pawn: Pawn) -> bool
```

x.can_character_step_up(pawn) -> bool
Return true if the given Pawn can step up onto this component.
This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.
see: CanCharacterStepUpOn

Args:
    pawn (Pawn): the Pawn that wants to step onto this component.

Returns:
    bool:

<a id="unreal.PrimitiveComponent.add_velocity_change_impulse_at_location"></a>

#### add_velocity_change_impulse_at_location

```python
def add_velocity_change_impulse_at_location(impulse: Vector,
                                            location: Vector,
                                            bone_name: Name = "None") -> None
```

x.add_velocity_change_impulse_at_location(impulse, location, bone_name="None") -> None
Add an impulse to a single rigid body at a specific location. The Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

Args:
    impulse (Vector): Magnitude and direction of impulse to apply.
    location (Vector): Point in world space to apply impulse at.
    bone_name (Name): If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.add_torque_in_radians"></a>

#### add_torque_in_radians

```python
def add_torque_in_radians(torque: Vector,
                          bone_name: Name = "None",
                          accel_change: bool = False) -> None
```

x.add_torque_in_radians(torque, bone_name="None", accel_change=False) -> None
Add a torque to a single rigid body.

Args:
    torque (Vector): Torque to apply. Direction is axis of rotation and magnitude is strength of torque.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body.
    accel_change (bool): If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_torque_in_degrees"></a>

#### add_torque_in_degrees

```python
def add_torque_in_degrees(torque: Vector,
                          bone_name: Name = "None",
                          accel_change: bool = False) -> None
```

x.add_torque_in_degrees(torque, bone_name="None", accel_change=False) -> None
Add a torque to a single rigid body.

Args:
    torque (Vector): Torque to apply. Direction is axis of rotation and magnitude is strength of torque.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body.
    accel_change (bool): If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_radial_impulse"></a>

#### add_radial_impulse

```python
def add_radial_impulse(origin: Vector,
                       radius: float,
                       strength: float,
                       falloff: RadialImpulseFalloff,
                       vel_change: bool = False) -> None
```

x.add_radial_impulse(origin, radius, strength, falloff, vel_change=False) -> None
Add an impulse to all rigid bodies in this component, radiating out from the specified position.

Args:
    origin (Vector): Point of origin for the radial impulse blast, in world space
    radius (float): Size of radial impulse. Beyond this distance from Origin, there will be no affect.
    strength (float): Maximum strength of impulse applied to body.
    falloff (RadialImpulseFalloff): Allows you to control the strength of the impulse as a function of distance from Origin.
    vel_change (bool): If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_radial_force"></a>

#### add_radial_force

```python
def add_radial_force(origin: Vector,
                     radius: float,
                     strength: float,
                     falloff: RadialImpulseFalloff,
                     accel_change: bool = False) -> None
```

x.add_radial_force(origin, radius, strength, falloff, accel_change=False) -> None
Add a force to all bodies in this component, originating from the supplied world-space location.

Args:
    origin (Vector): Origin of force in world space.
    radius (float): Radius within which to apply the force.
    strength (float): Strength of force to apply.
    falloff (RadialImpulseFalloff): Allows you to control the strength of the force as a function of distance from Origin.
    accel_change (bool): If true, Strength is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_impulse_at_location"></a>

#### add_impulse_at_location

```python
def add_impulse_at_location(impulse: Vector,
                            location: Vector,
                            bone_name: Name = "None") -> None
```

x.add_impulse_at_location(impulse, location, bone_name="None") -> None
Add an impulse to a single rigid body at a specific location.

Args:
    impulse (Vector): Magnitude and direction of impulse to apply.
    location (Vector): Point in world space to apply impulse at.
    bone_name (Name): If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.add_impulse_at_position"></a>

#### add_impulse_at_position

```python
def add_impulse_at_position(impulse: Vector,
                            location: Vector,
                            bone_name: Name = "None") -> None
```

deprecated: 'add_impulse_at_position' was renamed to 'add_impulse_at_location'.

<a id="unreal.PrimitiveComponent.add_impulse"></a>

#### add_impulse

```python
def add_impulse(impulse: Vector,
                bone_name: Name = "None",
                vel_change: bool = False) -> None
```

x.add_impulse(impulse, bone_name="None", vel_change=False) -> None
Add an impulse to a single rigid body. Good for one time instant burst.

Args:
    impulse (Vector): Magnitude and direction of impulse to apply.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body.
    vel_change (bool): If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_force_at_location_local"></a>

#### add_force_at_location_local

```python
def add_force_at_location_local(force: Vector,
                                location: Vector,
                                bone_name: Name = "None") -> None
```

x.add_force_at_location_local(force, location, bone_name="None") -> None
Add a force to a single rigid body at a particular location. Both Force and Location should be in body space.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Args:
    force (Vector): Force vector to apply. Magnitude indicates strength of force.
    location (Vector): Location to apply force, in component space.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.add_force_at_location"></a>

#### add_force_at_location

```python
def add_force_at_location(force: Vector,
                          location: Vector,
                          bone_name: Name = "None") -> None
```

x.add_force_at_location(force, location, bone_name="None") -> None
Add a force to a single rigid body at a particular location in world space.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Args:
    force (Vector): Force vector to apply. Magnitude indicates strength of force.
    location (Vector): Location to apply force, in world space.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.

<a id="unreal.PrimitiveComponent.add_force_at_position"></a>

#### add_force_at_position

```python
def add_force_at_position(force: Vector,
                          location: Vector,
                          bone_name: Name = "None") -> None
```

deprecated: 'add_force_at_position' was renamed to 'add_force_at_location'.

<a id="unreal.PrimitiveComponent.add_force"></a>

#### add_force

```python
def add_force(force: Vector,
              bone_name: Name = "None",
              accel_change: bool = False) -> None
```

x.add_force(force, bone_name="None", accel_change=False) -> None
Add a force to a single rigid body.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Args:
    force (Vector): Force vector to apply. Magnitude indicates strength of force.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.
    accel_change (bool): If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_angular_impulse_in_radians"></a>

#### add_angular_impulse_in_radians

```python
def add_angular_impulse_in_radians(impulse: Vector,
                                   bone_name: Name = "None",
                                   vel_change: bool = False) -> None
```

x.add_angular_impulse_in_radians(impulse, bone_name="None", vel_change=False) -> None
Add an angular impulse to a single rigid body. Good for one time instant burst.

Args:
    impulse (Vector): 
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body.
    vel_change (bool): If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

<a id="unreal.PrimitiveComponent.add_angular_impulse_in_degrees"></a>

#### add_angular_impulse_in_degrees

```python
def add_angular_impulse_in_degrees(impulse: Vector,
                                   bone_name: Name = "None",
                                   vel_change: bool = False) -> None
```

x.add_angular_impulse_in_degrees(impulse, bone_name="None", vel_change=False) -> None
Add an angular impulse to a single rigid body. Good for one time instant burst.

Args:
    impulse (Vector): 
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body.
    vel_change (bool): If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect).

<a id="unreal.MeshComponent"></a>