## ControlRigComponent Objects

```python
class ControlRigComponent(PrimitiveComponent)
```

A component that hosts an animation ControlRig, manages control components and marshals data between the two

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigComponent.h

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
- ``control_rig_class`` (type(Class)):  [Read-Write] The class of control rig to instantiate
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``draw_bones`` (bool):  [Read-Write] When checked the rig's bones are drawn using debug drawing similar to the animation editor viewport
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_lazy_evaluation`` (bool):  [Read-Write] When checked the rig will only run if any of the mapped inputs has changed
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
- ``lazy_evaluation_position_threshold`` (float):  [Read-Write] The delta threshold for a translation / position difference. 0.0 disables position differences.
- ``lazy_evaluation_rotation_threshold`` (float):  [Read-Write] The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences.
- ``lazy_evaluation_scale_threshold`` (float):  [Read-Write] The delta threshold for a scale difference. 0.0 disables scale differences.
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``mapped_elements`` (Array[ControlRigComponentMappedElement]):  [Read-Only]
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
- ``on_post_construction_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig is setup
- ``on_post_forwards_solve_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig's forwards solve
- ``on_post_initialize_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig is initialized
- ``on_pre_construction_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired before this component's ControlRig is setup
- ``on_pre_forwards_solve_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired before this component's ControlRig's forwards solve
- ``on_pre_initialize_delegate`` (ControlRigComponentDelegate):  [Read-Write] Event fired just before this component's ControlRig is initialized
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
- ``reset_initials_before_construction`` (bool):  [Read-Write] When checked the initial transforms on bones, nulls and controls are reset prior to a construction event
- ``reset_transform_before_tick`` (bool):  [Read-Write] When checked the transforms are reset before a tick / update of the rig
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_debug_drawing`` (bool):  [Read-Write] When checked the rig's debug drawing instructions are drawn in the viewport
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
- ``update_in_editor`` (bool):  [Read-Write] When checked the rig is run in the editor viewport without running / simulation the game
- ``update_rig_on_tick`` (bool):  [Read-Write] When checked this ensures to run the rig's update on the component's tick automatically
- ``use_as_occluder`` (bool):  [Read-Write] Whether to render the primitive in the depth only pass.
  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
  todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``user_defined_elements`` (Array[ControlRigComponentMappedElement]):  [Read-Write]
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

<a id="unreal.ControlRigComponent.control_rig_class"></a>

#### control_rig_class

```python
@property
def control_rig_class() -> Class
```

(type(Class)):  [Read-Write] The class of control rig to instantiate

<a id="unreal.ControlRigComponent.control_rig_class"></a>

#### control_rig_class

```python
@control_rig_class.setter
def control_rig_class(value: Class) -> None
```

<a id="unreal.ControlRigComponent.on_pre_initialize_delegate"></a>

#### on_pre_initialize_delegate

```python
@property
def on_pre_initialize_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired just before this component's ControlRig is initialized

<a id="unreal.ControlRigComponent.on_pre_initialize_delegate"></a>

#### on_pre_initialize_delegate

```python
@on_pre_initialize_delegate.setter
def on_pre_initialize_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_post_initialize_delegate"></a>

#### on_post_initialize_delegate

```python
@property
def on_post_initialize_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig is initialized

<a id="unreal.ControlRigComponent.on_post_initialize_delegate"></a>

#### on_post_initialize_delegate

```python
@on_post_initialize_delegate.setter
def on_post_initialize_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_pre_construction_delegate"></a>

#### on_pre_construction_delegate

```python
@property
def on_pre_construction_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired before this component's ControlRig is setup

<a id="unreal.ControlRigComponent.on_pre_construction_delegate"></a>

#### on_pre_construction_delegate

```python
@on_pre_construction_delegate.setter
def on_pre_construction_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_pre_setup_delegate"></a>

#### on_pre_setup_delegate

```python
@property
def on_pre_setup_delegate() -> ControlRigComponentDelegate
```

deprecated: 'on_pre_setup_delegate' was renamed to 'on_pre_construction_delegate'.

<a id="unreal.ControlRigComponent.on_pre_setup_delegate"></a>

#### on_pre_setup_delegate

```python
@on_pre_setup_delegate.setter
def on_pre_setup_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_post_construction_delegate"></a>

#### on_post_construction_delegate

```python
@property
def on_post_construction_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig is setup

<a id="unreal.ControlRigComponent.on_post_construction_delegate"></a>

#### on_post_construction_delegate

```python
@on_post_construction_delegate.setter
def on_post_construction_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_post_setup_delegate"></a>

#### on_post_setup_delegate

```python
@property
def on_post_setup_delegate() -> ControlRigComponentDelegate
```

deprecated: 'on_post_setup_delegate' was renamed to 'on_post_construction_delegate'.

<a id="unreal.ControlRigComponent.on_post_setup_delegate"></a>

#### on_post_setup_delegate

```python
@on_post_setup_delegate.setter
def on_post_setup_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_pre_forwards_solve_delegate"></a>

#### on_pre_forwards_solve_delegate

```python
@property
def on_pre_forwards_solve_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired before this component's ControlRig's forwards solve

<a id="unreal.ControlRigComponent.on_pre_forwards_solve_delegate"></a>

#### on_pre_forwards_solve_delegate

```python
@on_pre_forwards_solve_delegate.setter
def on_pre_forwards_solve_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_pre_update_delegate"></a>

#### on_pre_update_delegate

```python
@property
def on_pre_update_delegate() -> ControlRigComponentDelegate
```

deprecated: 'on_pre_update_delegate' was renamed to 'on_pre_forwards_solve_delegate'.

<a id="unreal.ControlRigComponent.on_pre_update_delegate"></a>

#### on_pre_update_delegate

```python
@on_pre_update_delegate.setter
def on_pre_update_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_post_forwards_solve_delegate"></a>

#### on_post_forwards_solve_delegate

```python
@property
def on_post_forwards_solve_delegate() -> ControlRigComponentDelegate
```

(ControlRigComponentDelegate):  [Read-Write] Event fired after this component's ControlRig's forwards solve

<a id="unreal.ControlRigComponent.on_post_forwards_solve_delegate"></a>

#### on_post_forwards_solve_delegate

```python
@on_post_forwards_solve_delegate.setter
def on_post_forwards_solve_delegate(
        value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.on_post_update_delegate"></a>

#### on_post_update_delegate

```python
@property
def on_post_update_delegate() -> ControlRigComponentDelegate
```

deprecated: 'on_post_update_delegate' was renamed to 'on_post_forwards_solve_delegate'.

<a id="unreal.ControlRigComponent.on_post_update_delegate"></a>

#### on_post_update_delegate

```python
@on_post_update_delegate.setter
def on_post_update_delegate(value: ControlRigComponentDelegate) -> None
```

<a id="unreal.ControlRigComponent.update"></a>

#### update

```python
def update(delta_time: float = 0.000000) -> None
```

x.update(delta_time=0.000000) -> None
Updates and ticks the rig.

Args:
    delta_time (float):

<a id="unreal.ControlRigComponent.set_object_binding"></a>

#### set_object_binding

```python
def set_object_binding(object_to_bind: Object) -> None
```

x.set_object_binding(object_to_bind) -> None
Set Object Binding

Args:
    object_to_bind (Object):

<a id="unreal.ControlRigComponent.set_mapped_elements"></a>

#### set_mapped_elements

```python
def set_mapped_elements(
        new_mapped_elements: Array[ControlRigComponentMappedElement]) -> None
```

x.set_mapped_elements(new_mapped_elements) -> None
Replaces the mapped elements on the component with the provided array, should not be used before OnPreInitialize Event

Args:
    new_mapped_elements (Array[ControlRigComponentMappedElement]):

<a id="unreal.ControlRigComponent.set_initial_space_transform"></a>

#### set_initial_space_transform

```python
def set_initial_space_transform(
    space_name: Name,
    initial_transform: Transform,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> None
```

x.set_initial_space_transform(space_name, initial_transform, space=ControlRigComponentSpace.RIG_SPACE) -> None
Sets the transform of the space in the requested space

Args:
    space_name (Name): The name of the space to set the transform for
    initial_transform (Transform): 
    space (ControlRigComponentSpace): The space to set the transform in

<a id="unreal.ControlRigComponent.set_initial_bone_transform"></a>

#### set_initial_bone_transform

```python
def set_initial_bone_transform(
        bone_name: Name,
        initial_transform: Transform,
        space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE,
        propagate_to_children: bool = False) -> None
```

x.set_initial_bone_transform(bone_name, initial_transform, space=ControlRigComponentSpace.RIG_SPACE, propagate_to_children=False) -> None
Sets the initial transform of the bone in the requested space

Args:
    bone_name (Name): The name of the bone to set the transform for
    initial_transform (Transform): The initial transform to set for the bone
    space (ControlRigComponentSpace): The space to set the transform in
    propagate_to_children (bool): If true the child bones will be moved together with the affected bone

<a id="unreal.ControlRigComponent.set_control_vector2d"></a>

#### set_control_vector2d

```python
def set_control_vector2d(control_name: Name, value: Vector2D) -> None
```

x.set_control_vector2d(control_name, value) -> None
Sets the value of a vector2D control

Args:
    control_name (Name): The name of the control to set
    value (Vector2D): The new value for the control

<a id="unreal.ControlRigComponent.set_control_transform"></a>

#### set_control_transform

```python
def set_control_transform(
    control_name: Name,
    value: Transform,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> None
```

x.set_control_transform(control_name, value, space=ControlRigComponentSpace.RIG_SPACE) -> None
Sets the value of a transform control

Args:
    control_name (Name): The name of the control to set
    value (Transform): The new value for the control
    space (ControlRigComponentSpace): The space to set the value in

<a id="unreal.ControlRigComponent.set_control_scale"></a>

#### set_control_scale

```python
def set_control_scale(
    control_name: Name,
    value: Vector,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> None
```

x.set_control_scale(control_name, value, space=ControlRigComponentSpace.LOCAL_SPACE) -> None
Sets the value of a scale control

Args:
    control_name (Name): The name of the control to set
    value (Vector): The new value for the control
    space (ControlRigComponentSpace): The space to set the value in

<a id="unreal.ControlRigComponent.set_control_rotator"></a>

#### set_control_rotator

```python
def set_control_rotator(
    control_name: Name,
    value: Rotator,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> None
```

x.set_control_rotator(control_name, value, space=ControlRigComponentSpace.LOCAL_SPACE) -> None
Sets the value of a rotator control

Args:
    control_name (Name): The name of the control to set
    value (Rotator): The new value for the control
    space (ControlRigComponentSpace): The space to set the value in

<a id="unreal.ControlRigComponent.set_control_rig_class"></a>

#### set_control_rig_class

```python
def set_control_rig_class(control_rig_class: Class) -> None
```

x.set_control_rig_class(control_rig_class) -> None
Set Control Rig Class

Args:
    control_rig_class (type(Class)):

<a id="unreal.ControlRigComponent.set_control_position"></a>

#### set_control_position

```python
def set_control_position(
    control_name: Name,
    value: Vector,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> None
```

x.set_control_position(control_name, value, space=ControlRigComponentSpace.LOCAL_SPACE) -> None
Sets the value of a position control

Args:
    control_name (Name): The name of the control to set
    value (Vector): The new value for the control
    space (ControlRigComponentSpace): The space to set the value in

<a id="unreal.ControlRigComponent.set_control_offset"></a>

#### set_control_offset

```python
def set_control_offset(
    control_name: Name,
    offset_transform: Transform,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> None
```

x.set_control_offset(control_name, offset_transform, space=ControlRigComponentSpace.RIG_SPACE) -> None
Sets the offset transform of a control

Args:
    control_name (Name): The name of the control to set
    offset_transform (Transform): The new offset trasnform for the control
    space (ControlRigComponentSpace): The space to set the offset transform in

<a id="unreal.ControlRigComponent.set_control_int"></a>

#### set_control_int

```python
def set_control_int(control_name: Name, value: int) -> None
```

x.set_control_int(control_name, value) -> None
Sets the value of an integer control

Args:
    control_name (Name): The name of the control to set
    value (int32): The new value for the control

<a id="unreal.ControlRigComponent.set_control_float"></a>

#### set_control_float

```python
def set_control_float(control_name: Name, value: float) -> None
```

x.set_control_float(control_name, value) -> None
Sets the value of a float control

Args:
    control_name (Name): The name of the control to set
    value (float): The new value for the control

<a id="unreal.ControlRigComponent.set_control_bool"></a>

#### set_control_bool

```python
def set_control_bool(control_name: Name, value: bool) -> None
```

x.set_control_bool(control_name, value) -> None
Sets the value of a bool control

Args:
    control_name (Name): The name of the control to set
    value (bool): The new value for the control

<a id="unreal.ControlRigComponent.set_bone_transform"></a>

#### set_bone_transform

```python
def set_bone_transform(
        bone_name: Name,
        transform: Transform,
        space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE,
        weight: float = 1.000000,
        propagate_to_children: bool = True) -> None
```

x.set_bone_transform(bone_name, transform, space=ControlRigComponentSpace.RIG_SPACE, weight=1.000000, propagate_to_children=True) -> None
Sets the transform of the bone in the requested space

Args:
    bone_name (Name): The name of the bone to set the transform for
    transform (Transform): 
    space (ControlRigComponentSpace): The space to set the transform in
    weight (float): The weight of how much the change should be applied (0.0 to 1.0)
    propagate_to_children (bool): If true the child bones will be moved together with the affected bone

<a id="unreal.ControlRigComponent.set_bone_initial_transforms_from_skeletal_mesh"></a>

#### set_bone_initial_transforms_from_skeletal_mesh

```python
def set_bone_initial_transforms_from_skeletal_mesh(
        skeletal_mesh: SkeletalMesh) -> None
```

x.set_bone_initial_transforms_from_skeletal_mesh(skeletal_mesh) -> None
Setup the initial transforms / ref pose of the bones based on a skeletal mesh

Args:
    skeletal_mesh (SkeletalMesh):

<a id="unreal.ControlRigComponent.on_pre_initialize"></a>

#### on_pre_initialize

```python
def on_pre_initialize(component: ControlRigComponent) -> None
```

x.on_pre_initialize(component) -> None
On Pre Initialize

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.on_pre_forwards_solve"></a>

#### on_pre_forwards_solve

```python
def on_pre_forwards_solve(component: ControlRigComponent) -> None
```

x.on_pre_forwards_solve(component) -> None
On Pre Forwards Solve

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.on_pre_construction"></a>

#### on_pre_construction

```python
def on_pre_construction(component: ControlRigComponent) -> None
```

x.on_pre_construction(component) -> None
On Pre Construction

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.on_post_initialize"></a>

#### on_post_initialize

```python
def on_post_initialize(component: ControlRigComponent) -> None
```

x.on_post_initialize(component) -> None
On Post Initialize

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.on_post_forwards_solve"></a>

#### on_post_forwards_solve

```python
def on_post_forwards_solve(component: ControlRigComponent) -> None
```

x.on_post_forwards_solve(component) -> None
On Post Forwards Solve

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.on_post_construction"></a>

#### on_post_construction

```python
def on_post_construction(component: ControlRigComponent) -> None
```

x.on_post_construction(component) -> None
On Post Construction

Args:
    component (ControlRigComponent):

<a id="unreal.ControlRigComponent.initialize"></a>

#### initialize

```python
def initialize() -> None
```

x.initialize() -> None
Initializes the rig's memory and calls the construction event

<a id="unreal.ControlRigComponent.get_space_transform"></a>

#### get_space_transform

```python
def get_space_transform(
    space_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_space_transform(space_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the transform of the space in the requested space

Args:
    space_name (Name): The name of the space to retrieve the transform for
    space (ControlRigComponentSpace): The space to retrieve the transform in

Returns:
    Transform: the transform of the space in the requested space

<a id="unreal.ControlRigComponent.get_initial_space_transform"></a>

#### get_initial_space_transform

```python
def get_initial_space_transform(
    space_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_initial_space_transform(space_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the initial transform of the space in the requested space

Args:
    space_name (Name): The name of the space to retrieve the transform for
    space (ControlRigComponentSpace): The space to retrieve the transform in

Returns:
    Transform: the initial transform of the space in the requested space

<a id="unreal.ControlRigComponent.get_initial_bone_transform"></a>

#### get_initial_bone_transform

```python
def get_initial_bone_transform(
    bone_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_initial_bone_transform(bone_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the initial transform of the bone in the requested space

Args:
    bone_name (Name): The name of the bone to retrieve the transform for
    space (ControlRigComponentSpace): The space to retrieve the transform in

Returns:
    Transform: the initial transform of the bone in the requested space

<a id="unreal.ControlRigComponent.get_element_names"></a>

#### get_element_names

```python
def get_element_names(
        element_type: RigElementType = RigElementType.BONE) -> Array[Name]
```

x.get_element_names(element_type=RigElementType.BONE) -> Array[Name]
Returns all of the names for a given element type (Bone, Control, etc)

Args:
    element_type (RigElementType): The type of elements to return the names for

Returns:
    Array[Name]: all of the names for a given element type (Bone, Control, etc)

<a id="unreal.ControlRigComponent.get_control_vector2d"></a>

#### get_control_vector2d

```python
def get_control_vector2d(control_name: Name) -> Vector2D
```

x.get_control_vector2d(control_name) -> Vector2D
Returns the value of a Vector3D control

Args:
    control_name (Name): The name of the control to retrieve the value for

Returns:
    Vector2D: The Vector3D value of the control

<a id="unreal.ControlRigComponent.get_control_transform"></a>

#### get_control_transform

```python
def get_control_transform(
    control_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_control_transform(control_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the value of a transform control

Args:
    control_name (Name): The name of the control to retrieve the value for
    space (ControlRigComponentSpace): The space to retrieve the control's value in

Returns:
    Transform: The transform value of the control

<a id="unreal.ControlRigComponent.get_control_scale"></a>

#### get_control_scale

```python
def get_control_scale(
    control_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> Vector
```

x.get_control_scale(control_name, space=ControlRigComponentSpace.LOCAL_SPACE) -> Vector
Returns the value of a scale control

Args:
    control_name (Name): The name of the control to retrieve the value for
    space (ControlRigComponentSpace): The space to retrieve the control's value in

Returns:
    Vector: The scale value of the control

<a id="unreal.ControlRigComponent.get_control_rotator"></a>

#### get_control_rotator

```python
def get_control_rotator(
    control_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> Rotator
```

x.get_control_rotator(control_name, space=ControlRigComponentSpace.LOCAL_SPACE) -> Rotator
Returns the value of a rotator control

Args:
    control_name (Name): The name of the control to retrieve the value for
    space (ControlRigComponentSpace): The space to retrieve the control's value in

Returns:
    Rotator: The rotator value of the control

<a id="unreal.ControlRigComponent.get_control_rig"></a>

#### get_control_rig

```python
def get_control_rig() -> ControlRig
```

x.get_control_rig() -> ControlRig
Get the ControlRig hosted by this component

Returns:
    ControlRig:

<a id="unreal.ControlRigComponent.get_control_position"></a>

#### get_control_position

```python
def get_control_position(
    control_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.LOCAL_SPACE
) -> Vector
```

x.get_control_position(control_name, space=ControlRigComponentSpace.LOCAL_SPACE) -> Vector
Returns the value of a position control

Args:
    control_name (Name): The name of the control to retrieve the value for
    space (ControlRigComponentSpace): The space to retrieve the control's value in

Returns:
    Vector: The position value of the control

<a id="unreal.ControlRigComponent.get_control_offset"></a>

#### get_control_offset

```python
def get_control_offset(
    control_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_control_offset(control_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the offset transform of a control

Args:
    control_name (Name): The name of the control to retrieve the offset transform for
    space (ControlRigComponentSpace): The space to retrieve the offset transform in

Returns:
    Transform: The offset transform of a control

<a id="unreal.ControlRigComponent.get_control_int"></a>

#### get_control_int

```python
def get_control_int(control_name: Name) -> int
```

x.get_control_int(control_name) -> int32
Returns the value of an integer control

Args:
    control_name (Name): The name of the control to retrieve the value for

Returns:
    int32: The int32 value of the control

<a id="unreal.ControlRigComponent.get_control_float"></a>

#### get_control_float

```python
def get_control_float(control_name: Name) -> float
```

x.get_control_float(control_name) -> float
Returns the value of a float control

Args:
    control_name (Name): The name of the control to retrieve the value for

Returns:
    float: The float value of the control

<a id="unreal.ControlRigComponent.get_control_bool"></a>

#### get_control_bool

```python
def get_control_bool(control_name: Name) -> bool
```

x.get_control_bool(control_name) -> bool
Returns the value of a bool control

Args:
    control_name (Name): The name of the control to retrieve the value for

Returns:
    bool: The bool value of the control

<a id="unreal.ControlRigComponent.get_bone_transform"></a>

#### get_bone_transform

```python
def get_bone_transform(
    bone_name: Name,
    space: ControlRigComponentSpace = ControlRigComponentSpace.RIG_SPACE
) -> Transform
```

x.get_bone_transform(bone_name, space=ControlRigComponentSpace.RIG_SPACE) -> Transform
Returns the transform of the bone in the requested space

Args:
    bone_name (Name): The name of the bone to retrieve the transform for
    space (ControlRigComponentSpace): The space to retrieve the transform in

Returns:
    Transform: the transform of the bone in the requested space

<a id="unreal.ControlRigComponent.get_absolute_time"></a>

#### get_absolute_time

```python
def get_absolute_time() -> float
```

x.get_absolute_time() -> float
Get the ControlRig's local time in seconds since its last initialize

Returns:
    float:

<a id="unreal.ControlRigComponent.does_element_exist"></a>

#### does_element_exist

```python
def does_element_exist(
        name: Name,
        element_type: RigElementType = RigElementType.BONE) -> bool
```

x.does_element_exist(name, element_type=RigElementType.BONE) -> bool
Returns true if an element given a type and name exists in the rig

Args:
    name (Name): The name for the element to look up
    element_type (RigElementType): The type of element to look up

Returns:
    bool: true if the element exists

<a id="unreal.ControlRigComponent.clear_mapped_elements"></a>

#### clear_mapped_elements

```python
def clear_mapped_elements() -> None
```

x.clear_mapped_elements() -> None
Removes all mapped elements from the component

<a id="unreal.ControlRigComponent.can_execute"></a>

#### can_execute

```python
def can_execute() -> bool
```

x.can_execute() -> bool
Returns true if the Component can execute its Control Rig

Returns:
    bool:

<a id="unreal.ControlRigComponent.add_mapped_skeletal_mesh"></a>

#### add_mapped_skeletal_mesh

```python
def add_mapped_skeletal_mesh(
    skeletal_mesh_component: SkeletalMeshComponent,
    bones: Array[ControlRigComponentMappedBone],
    curves: Array[ControlRigComponentMappedCurve],
    direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection
    .OUTPUT
) -> None
```

x.add_mapped_skeletal_mesh(skeletal_mesh_component, bones, curves, direction=ControlRigComponentMapDirection.OUTPUT) -> None
Adds a series of mapped bones to the rig, should not be used before OnPreInitialize Event

Args:
    skeletal_mesh_component (SkeletalMeshComponent): 
    bones (Array[ControlRigComponentMappedBone]): 
    curves (Array[ControlRigComponentMappedCurve]): 
    direction (ControlRigComponentMapDirection):

<a id="unreal.ControlRigComponent.add_mapped_elements"></a>

#### add_mapped_elements

```python
def add_mapped_elements(
        new_mapped_elements: Array[ControlRigComponentMappedElement]) -> None
```

x.add_mapped_elements(new_mapped_elements) -> None
Adds the provided mapped elements to the component, should not be used before OnPreInitialize Event

Args:
    new_mapped_elements (Array[ControlRigComponentMappedElement]):

<a id="unreal.ControlRigComponent.add_mapped_components"></a>

#### add_mapped_components

```python
def add_mapped_components(
        components: Array[ControlRigComponentMappedComponent]) -> None
```

x.add_mapped_components(components) -> None
Adds a series of mapped bones to the rig, should not be used before OnPreInitialize Event

Args:
    components (Array[ControlRigComponentMappedComponent]):

<a id="unreal.ControlRigComponent.add_mapped_complete_skeletal_mesh"></a>

#### add_mapped_complete_skeletal_mesh

```python
def add_mapped_complete_skeletal_mesh(
    skeletal_mesh_component: SkeletalMeshComponent,
    direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection
    .OUTPUT
) -> None
```

x.add_mapped_complete_skeletal_mesh(skeletal_mesh_component, direction=ControlRigComponentMapDirection.OUTPUT) -> None
Adds all matching bones to the rig, should not be used before OnPreInitialize Event

Args:
    skeletal_mesh_component (SkeletalMeshComponent): 
    direction (ControlRigComponentMapDirection):

<a id="unreal.ControlRigControlActor"></a>