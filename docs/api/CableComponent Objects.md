## CableComponent Objects

```python
class CableComponent(MeshComponent)
```

Component that allows you to specify custom triangle mesh geometry

**C++ Source:**

- **Plugin**: CableComponent
- **Module**: CableComponent
- **File**: CableComponent.h

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
- ``attach_end`` (bool):  [Read-Write] Should we fix the end to something (using AttachEndTo and EndLocation), or leave it free.
  If false, AttachEndTo and EndLocation are just used for initial location of end of cable
- ``attach_end_to`` (ComponentReference):  [Read-Write] Actor or Component that the defines the end position of the cable
- ``attach_end_to_socket_name`` (Name):  [Read-Write] Socket name on the AttachEndTo component to attach to
- ``attach_start`` (bool):  [Read-Write] Should we fix the start to something, or leave it free.
  If false, component transform is just used for initial location of start of cable
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``body_instance`` (BodyInstance):  [Read-Write] Physics scene information for this component, holds a single rigid body with multiple shapes.
- ``bounds_scale`` (float):  [Read-Write] Scales the bounds of the object.
  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.
  Warning: Increasing the bounds of an object will reduce performance and shadow quality!
  Currently only used by StaticMeshComponent and SkeletalMeshComponent.
- ``cable_force`` (Vector):  [Read-Write] Force vector (world space) applied to all particles in cable.
- ``cable_gravity_scale`` (float):  [Read-Write] Scaling applied to world gravity affecting this cable.
- ``cable_length`` (float):  [Read-Write] Rest length of the cable
- ``cable_width`` (float):  [Read-Write] How wide the cable geometry is
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
- ``collision_friction`` (float):  [Read-Write] If collision is enabled, control how much sliding friction is applied when cable is in contact.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_collision`` (bool):  [Read-Write] EXPERIMENTAL. Perform sweeps for each cable particle, each substep, to avoid collisions with the world.
  Uses the Collision Preset on the component to determine what is collided with.
  This greatly increases the cost of the cable simulation.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``enable_stiffness`` (bool):  [Read-Write] Add stiffness constraints to cable.
- ``end_location`` (Vector):  [Read-Write] End location of cable, relative to AttachEndTo (or AttachEndToSocketName) if specified, otherwise relative to cable component.
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
- ``num_segments`` (int32):  [Read-Write] How many segments the cable has
- ``num_sides`` (int32):  [Read-Write] Number of sides of the cable geometry
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
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
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
- ``skip_cable_update_when_not_owner_recently_rendered`` (bool):  [Read-Write]
- ``skip_cable_update_when_not_visible`` (bool):  [Read-Write]
- ``solver_iterations`` (int32):  [Read-Write] The number of solver iterations controls how 'stiff' the cable is
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``substep_time`` (float):  [Read-Write] Controls the simulation substep time for the cable
- ``tile_material`` (float):  [Read-Write] How many times to repeat the material along the length of the cable
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
- ``use_substepping`` (bool):  [Read-Write] When false, will still wait for SubstepTime to elapse before updating, but will only run the cable simulation once using all of accumulated simulation time
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

<a id="unreal.CableComponent.attach_start"></a>

#### attach_start

```python
@property
def attach_start() -> bool
```

(bool):  [Read-Write] Should we fix the start to something, or leave it free.
If false, component transform is just used for initial location of start of cable

<a id="unreal.CableComponent.attach_start"></a>

#### attach_start

```python
@attach_start.setter
def attach_start(value: bool) -> None
```

<a id="unreal.CableComponent.attach_end"></a>

#### attach_end

```python
@property
def attach_end() -> bool
```

(bool):  [Read-Write] Should we fix the end to something (using AttachEndTo and EndLocation), or leave it free.
If false, AttachEndTo and EndLocation are just used for initial location of end of cable

<a id="unreal.CableComponent.attach_end"></a>

#### attach_end

```python
@attach_end.setter
def attach_end(value: bool) -> None
```

<a id="unreal.CableComponent.end_location"></a>

#### end_location

```python
@property
def end_location() -> Vector
```

(Vector):  [Read-Write] End location of cable, relative to AttachEndTo (or AttachEndToSocketName) if specified, otherwise relative to cable component.

<a id="unreal.CableComponent.end_location"></a>

#### end_location

```python
@end_location.setter
def end_location(value: Vector) -> None
```

<a id="unreal.CableComponent.cable_length"></a>

#### cable_length

```python
@property
def cable_length() -> float
```

(float):  [Read-Write] Rest length of the cable

<a id="unreal.CableComponent.cable_length"></a>

#### cable_length

```python
@cable_length.setter
def cable_length(value: float) -> None
```

<a id="unreal.CableComponent.num_segments"></a>

#### num_segments

```python
@property
def num_segments() -> int
```

(int32):  [Read-Only] How many segments the cable has

<a id="unreal.CableComponent.substep_time"></a>

#### substep_time

```python
@property
def substep_time() -> float
```

(float):  [Read-Only] Controls the simulation substep time for the cable

<a id="unreal.CableComponent.solver_iterations"></a>

#### solver_iterations

```python
@property
def solver_iterations() -> int
```

(int32):  [Read-Write] The number of solver iterations controls how 'stiff' the cable is

<a id="unreal.CableComponent.solver_iterations"></a>

#### solver_iterations

```python
@solver_iterations.setter
def solver_iterations(value: int) -> None
```

<a id="unreal.CableComponent.enable_stiffness"></a>

#### enable_stiffness

```python
@property
def enable_stiffness() -> bool
```

(bool):  [Read-Write] Add stiffness constraints to cable.

<a id="unreal.CableComponent.enable_stiffness"></a>

#### enable_stiffness

```python
@enable_stiffness.setter
def enable_stiffness(value: bool) -> None
```

<a id="unreal.CableComponent.use_substepping"></a>

#### use_substepping

```python
@property
def use_substepping() -> bool
```

(bool):  [Read-Write] When false, will still wait for SubstepTime to elapse before updating, but will only run the cable simulation once using all of accumulated simulation time

<a id="unreal.CableComponent.use_substepping"></a>

#### use_substepping

```python
@use_substepping.setter
def use_substepping(value: bool) -> None
```

<a id="unreal.CableComponent.skip_cable_update_when_not_visible"></a>

#### skip_cable_update_when_not_visible

```python
@property
def skip_cable_update_when_not_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CableComponent.skip_cable_update_when_not_visible"></a>

#### skip_cable_update_when_not_visible

```python
@skip_cable_update_when_not_visible.setter
def skip_cable_update_when_not_visible(value: bool) -> None
```

<a id="unreal.CableComponent.skip_cable_update_when_not_owner_recently_rendered"></a>

#### skip_cable_update_when_not_owner_recently_rendered

```python
@property
def skip_cable_update_when_not_owner_recently_rendered() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CableComponent.skip_cable_update_when_not_owner_recently_rendered"></a>

#### skip_cable_update_when_not_owner_recently_rendered

```python
@skip_cable_update_when_not_owner_recently_rendered.setter
def skip_cable_update_when_not_owner_recently_rendered(value: bool) -> None
```

<a id="unreal.CableComponent.enable_collision"></a>

#### enable_collision

```python
@property
def enable_collision() -> bool
```

(bool):  [Read-Write] EXPERIMENTAL. Perform sweeps for each cable particle, each substep, to avoid collisions with the world.
Uses the Collision Preset on the component to determine what is collided with.
This greatly increases the cost of the cable simulation.

<a id="unreal.CableComponent.enable_collision"></a>

#### enable_collision

```python
@enable_collision.setter
def enable_collision(value: bool) -> None
```

<a id="unreal.CableComponent.collision_friction"></a>

#### collision_friction

```python
@property
def collision_friction() -> float
```

(float):  [Read-Write] If collision is enabled, control how much sliding friction is applied when cable is in contact.

<a id="unreal.CableComponent.collision_friction"></a>

#### collision_friction

```python
@collision_friction.setter
def collision_friction(value: float) -> None
```

<a id="unreal.CableComponent.cable_force"></a>

#### cable_force

```python
@property
def cable_force() -> Vector
```

(Vector):  [Read-Write] Force vector (world space) applied to all particles in cable.

<a id="unreal.CableComponent.cable_force"></a>

#### cable_force

```python
@cable_force.setter
def cable_force(value: Vector) -> None
```

<a id="unreal.CableComponent.cable_gravity_scale"></a>

#### cable_gravity_scale

```python
@property
def cable_gravity_scale() -> float
```

(float):  [Read-Write] Scaling applied to world gravity affecting this cable.

<a id="unreal.CableComponent.cable_gravity_scale"></a>

#### cable_gravity_scale

```python
@cable_gravity_scale.setter
def cable_gravity_scale(value: float) -> None
```

<a id="unreal.CableComponent.cable_width"></a>

#### cable_width

```python
@property
def cable_width() -> float
```

(float):  [Read-Write] How wide the cable geometry is

<a id="unreal.CableComponent.cable_width"></a>

#### cable_width

```python
@cable_width.setter
def cable_width(value: float) -> None
```

<a id="unreal.CableComponent.num_sides"></a>

#### num_sides

```python
@property
def num_sides() -> int
```

(int32):  [Read-Only] Number of sides of the cable geometry

<a id="unreal.CableComponent.tile_material"></a>

#### tile_material

```python
@property
def tile_material() -> float
```

(float):  [Read-Write] How many times to repeat the material along the length of the cable

<a id="unreal.CableComponent.tile_material"></a>

#### tile_material

```python
@tile_material.setter
def tile_material(value: float) -> None
```

<a id="unreal.CableComponent.set_attach_end_to_component"></a>

#### set_attach_end_to_component

```python
def set_attach_end_to_component(component: SceneComponent,
                                socket_name: Name = "None") -> None
```

x.set_attach_end_to_component(component, socket_name="None") -> None
Attaches the end of the cable to a specific Component *

Args:
    component (SceneComponent): 
    socket_name (Name):

<a id="unreal.CableComponent.set_attach_end_to"></a>

#### set_attach_end_to

```python
def set_attach_end_to(actor: Actor,
                      component_property: Name,
                      socket_name: Name = "None") -> None
```

x.set_attach_end_to(actor, component_property, socket_name="None") -> None
Attaches the end of the cable to a specific Component within an Actor *

Args:
    actor (Actor): 
    component_property (Name): 
    socket_name (Name):

<a id="unreal.CableComponent.get_cable_particle_locations"></a>

#### get_cable_particle_locations

```python
def get_cable_particle_locations() -> Array[Vector]
```

x.get_cable_particle_locations() -> Array[Vector]
Get array of locations of particles (in world space) making up the cable simulation.

Returns:
    Array[Vector]: 

    locations (Array[Vector]):

<a id="unreal.CableComponent.get_attached_component"></a>

#### get_attached_component

```python
def get_attached_component() -> SceneComponent
```

x.get_attached_component() -> SceneComponent
Gets the specific USceneComponent that the cable is attached to *

Returns:
    SceneComponent:

<a id="unreal.CableComponent.get_attached_actor"></a>

#### get_attached_actor

```python
def get_attached_actor() -> Actor
```

x.get_attached_actor() -> Actor
Gets the Actor that the cable is attached to *

Returns:
    Actor:

<a id="unreal.CustomMeshComponent"></a>