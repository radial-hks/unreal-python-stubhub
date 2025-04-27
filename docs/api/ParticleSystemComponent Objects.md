## ParticleSystemComponent Objects

```python
class ParticleSystemComponent(FXSystemComponent)
```

A particle emitter.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleSystemComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``allow_recycling`` (bool):  [Read-Write] If true, this Particle System will be available for recycling after it has completed. Auto-destroyed systems cannot be recycled.
  Some systems (currently particle trail effects) can recycle components to avoid respawning them to play new effects.
  This is only an optimization and does not change particle system behavior, aside from not triggering normal component initialization events more than once.
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``apply_impulse_on_damage`` (bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_attach_location_rule`` (AttachmentRule):  [Read-Write] Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
  see: bAutoManageAttachment, EAttachmentRule
- ``auto_attach_parent`` (SceneComponent):  [Read-Only] Component we automatically attach to when activated, if bAutoManageAttachment is true.
  If null during registration, we assign the existing AttachParent and defer attachment until we activate.
  see: bAutoManageAttachment
- ``auto_attach_rotation_rule`` (AttachmentRule):  [Read-Write] Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
  see: bAutoManageAttachment, EAttachmentRule
- ``auto_attach_scale_rule`` (AttachmentRule):  [Read-Write] Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
  see: bAutoManageAttachment, EAttachmentRule
- ``auto_attach_socket_name`` (Name):  [Read-Write] Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.
  If no auto attach socket name is set during registration, the current attach socket will be
  assigned to AutoAttachSocketName and used when activated.
  see: bAutoManageAttachment
- ``auto_attach_weld_simulated_bodies`` (bool):  [Read-Write] Option for how we handle bWeldSimulatedBodies when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
  see: bAutoManageAttachment
- ``auto_manage_attachment`` (bool):  [Read-Write] True if we should automatically attach to AutoAttachParent when activated, and detach from our parent when completed.
  This overrides any current attachment that may be present at the time of activation (deferring initial attachment until activation, if AutoAttachParent is null).
  When enabled, detachment occurs regardless of whether AutoAttachParent is assigned, and the relative transform from the time of activation is restored.
  This also disables attachment on dedicated servers, where we don't actually activate even if bAutoActivate is true.
  see: AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType
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
- ``custom_time_dilation`` (float):  [Read-Write] Scales DeltaTime in UParticleSystemComponent::Tick(...)
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
- ``instance_parameters`` (Array[ParticleSysParam]):  [Read-Write] Array holding name instance parameters for this ParticleSystemComponent.
  Parameters can be used in Cascade using DistributionFloat/VectorParticleParameters.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``lod_method`` (ParticleSystemLODMethod):  [Read-Write] The method of LOD level determination to utilize for this particle system
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
- ``on_particle_burst`` (ParticleBurstSignature):  [Read-Write]
- ``on_particle_collide`` (ParticleCollisionSignature):  [Read-Write]
- ``on_particle_death`` (ParticleDeathSignature):  [Read-Write]
- ``on_particle_spawn`` (ParticleSpawnSignature):  [Read-Write]
- ``on_released`` (ComponentOnReleasedSignature):  [Read-Write] Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller
- ``on_system_finished`` (OnSystemFinished):  [Read-Write] Called when the particle system is done
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``override_lod_method`` (bool):  [Read-Write] indicates that the component's LODMethod overrides the Template's
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
- ``reset_on_detach`` (bool):  [Read-Write]
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``seconds_before_inactive`` (float):  [Read-Write] Number of seconds of emitter not being rendered that need to pass before it
  no longer gets ticked/ becomes inactive.
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``template`` (ParticleSystem):  [Read-Write]
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

<a id="unreal.ParticleSystemComponent.template"></a>

#### template

```python
@property
def template() -> ParticleSystem
```

(ParticleSystem):  [Read-Only]

<a id="unreal.ParticleSystemComponent.reset_on_detach"></a>

#### reset_on_detach

```python
@property
def reset_on_detach() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ParticleSystemComponent.reset_on_detach"></a>

#### reset_on_detach

```python
@reset_on_detach.setter
def reset_on_detach(value: bool) -> None
```

<a id="unreal.ParticleSystemComponent.allow_recycling"></a>

#### allow_recycling

```python
@property
def allow_recycling() -> bool
```

(bool):  [Read-Write] If true, this Particle System will be available for recycling after it has completed. Auto-destroyed systems cannot be recycled.
Some systems (currently particle trail effects) can recycle components to avoid respawning them to play new effects.
This is only an optimization and does not change particle system behavior, aside from not triggering normal component initialization events more than once.

<a id="unreal.ParticleSystemComponent.allow_recycling"></a>

#### allow_recycling

```python
@allow_recycling.setter
def allow_recycling(value: bool) -> None
```

<a id="unreal.ParticleSystemComponent.auto_manage_attachment"></a>

#### auto_manage_attachment

```python
@property
def auto_manage_attachment() -> bool
```

(bool):  [Read-Only] True if we should automatically attach to AutoAttachParent when activated, and detach from our parent when completed.
This overrides any current attachment that may be present at the time of activation (deferring initial attachment until activation, if AutoAttachParent is null).
When enabled, detachment occurs regardless of whether AutoAttachParent is assigned, and the relative transform from the time of activation is restored.
This also disables attachment on dedicated servers, where we don't actually activate even if bAutoActivate is true.
see: AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType

<a id="unreal.ParticleSystemComponent.auto_attach_weld_simulated_bodies"></a>

#### auto_attach_weld_simulated_bodies

```python
@property
def auto_attach_weld_simulated_bodies() -> bool
```

(bool):  [Read-Write] Option for how we handle bWeldSimulatedBodies when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment

<a id="unreal.ParticleSystemComponent.auto_attach_weld_simulated_bodies"></a>

#### auto_attach_weld_simulated_bodies

```python
@auto_attach_weld_simulated_bodies.setter
def auto_attach_weld_simulated_bodies(value: bool) -> None
```

<a id="unreal.ParticleSystemComponent.override_lod_method"></a>

#### override_lod_method

```python
@property
def override_lod_method() -> bool
```

(bool):  [Read-Write] indicates that the component's LODMethod overrides the Template's

<a id="unreal.ParticleSystemComponent.override_lod_method"></a>

#### override_lod_method

```python
@override_lod_method.setter
def override_lod_method(value: bool) -> None
```

<a id="unreal.ParticleSystemComponent.lod_method"></a>

#### lod_method

```python
@property
def lod_method() -> ParticleSystemLODMethod
```

(ParticleSystemLODMethod):  [Read-Write] The method of LOD level determination to utilize for this particle system

<a id="unreal.ParticleSystemComponent.lod_method"></a>

#### lod_method

```python
@lod_method.setter
def lod_method(value: ParticleSystemLODMethod) -> None
```

<a id="unreal.ParticleSystemComponent.instance_parameters"></a>

#### instance_parameters

```python
@property
def instance_parameters() -> Array[ParticleSysParam]
```

(Array[ParticleSysParam]):  [Read-Write] Array holding name instance parameters for this ParticleSystemComponent.
Parameters can be used in Cascade using DistributionFloat/VectorParticleParameters.

<a id="unreal.ParticleSystemComponent.instance_parameters"></a>

#### instance_parameters

```python
@instance_parameters.setter
def instance_parameters(value: Array[ParticleSysParam]) -> None
```

<a id="unreal.ParticleSystemComponent.on_particle_spawn"></a>

#### on_particle_spawn

```python
@property
def on_particle_spawn() -> ParticleSpawnSignature
```

(ParticleSpawnSignature):  [Read-Write]

<a id="unreal.ParticleSystemComponent.on_particle_spawn"></a>

#### on_particle_spawn

```python
@on_particle_spawn.setter
def on_particle_spawn(value: ParticleSpawnSignature) -> None
```

<a id="unreal.ParticleSystemComponent.on_particle_burst"></a>

#### on_particle_burst

```python
@property
def on_particle_burst() -> ParticleBurstSignature
```

(ParticleBurstSignature):  [Read-Write]

<a id="unreal.ParticleSystemComponent.on_particle_burst"></a>

#### on_particle_burst

```python
@on_particle_burst.setter
def on_particle_burst(value: ParticleBurstSignature) -> None
```

<a id="unreal.ParticleSystemComponent.on_particle_death"></a>

#### on_particle_death

```python
@property
def on_particle_death() -> ParticleDeathSignature
```

(ParticleDeathSignature):  [Read-Write]

<a id="unreal.ParticleSystemComponent.on_particle_death"></a>

#### on_particle_death

```python
@on_particle_death.setter
def on_particle_death(value: ParticleDeathSignature) -> None
```

<a id="unreal.ParticleSystemComponent.on_particle_collide"></a>

#### on_particle_collide

```python
@property
def on_particle_collide() -> ParticleCollisionSignature
```

(ParticleCollisionSignature):  [Read-Write]

<a id="unreal.ParticleSystemComponent.on_particle_collide"></a>

#### on_particle_collide

```python
@on_particle_collide.setter
def on_particle_collide(value: ParticleCollisionSignature) -> None
```

<a id="unreal.ParticleSystemComponent.seconds_before_inactive"></a>

#### seconds_before_inactive

```python
@property
def seconds_before_inactive() -> float
```

(float):  [Read-Write] Number of seconds of emitter not being rendered that need to pass before it
no longer gets ticked/ becomes inactive.

<a id="unreal.ParticleSystemComponent.seconds_before_inactive"></a>

#### seconds_before_inactive

```python
@seconds_before_inactive.setter
def seconds_before_inactive(value: float) -> None
```

<a id="unreal.ParticleSystemComponent.custom_time_dilation"></a>

#### custom_time_dilation

```python
@property
def custom_time_dilation() -> float
```

(float):  [Read-Write] Scales DeltaTime in UParticleSystemComponent::Tick(...)

<a id="unreal.ParticleSystemComponent.custom_time_dilation"></a>

#### custom_time_dilation

```python
@custom_time_dilation.setter
def custom_time_dilation(value: float) -> None
```

<a id="unreal.ParticleSystemComponent.auto_attach_parent"></a>

#### auto_attach_parent

```python
@property
def auto_attach_parent() -> SceneComponent
```

(SceneComponent):  [Read-Only] Component we automatically attach to when activated, if bAutoManageAttachment is true.
If null during registration, we assign the existing AttachParent and defer attachment until we activate.
see: bAutoManageAttachment

<a id="unreal.ParticleSystemComponent.auto_attach_socket_name"></a>

#### auto_attach_socket_name

```python
@property
def auto_attach_socket_name() -> Name
```

(Name):  [Read-Write] Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.
If no auto attach socket name is set during registration, the current attach socket will be
assigned to AutoAttachSocketName and used when activated.
see: bAutoManageAttachment

<a id="unreal.ParticleSystemComponent.auto_attach_socket_name"></a>

#### auto_attach_socket_name

```python
@auto_attach_socket_name.setter
def auto_attach_socket_name(value: Name) -> None
```

<a id="unreal.ParticleSystemComponent.auto_attach_location_rule"></a>

#### auto_attach_location_rule

```python
@property
def auto_attach_location_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.ParticleSystemComponent.auto_attach_location_rule"></a>

#### auto_attach_location_rule

```python
@auto_attach_location_rule.setter
def auto_attach_location_rule(value: AttachmentRule) -> None
```

<a id="unreal.ParticleSystemComponent.auto_attach_rotation_rule"></a>

#### auto_attach_rotation_rule

```python
@property
def auto_attach_rotation_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.ParticleSystemComponent.auto_attach_rotation_rule"></a>

#### auto_attach_rotation_rule

```python
@auto_attach_rotation_rule.setter
def auto_attach_rotation_rule(value: AttachmentRule) -> None
```

<a id="unreal.ParticleSystemComponent.auto_attach_scale_rule"></a>

#### auto_attach_scale_rule

```python
@property
def auto_attach_scale_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.ParticleSystemComponent.auto_attach_scale_rule"></a>

#### auto_attach_scale_rule

```python
@auto_attach_scale_rule.setter
def auto_attach_scale_rule(value: AttachmentRule) -> None
```

<a id="unreal.ParticleSystemComponent.on_system_finished"></a>

#### on_system_finished

```python
@property
def on_system_finished() -> OnSystemFinished
```

(OnSystemFinished):  [Read-Write] Called when the particle system is done

<a id="unreal.ParticleSystemComponent.on_system_finished"></a>

#### on_system_finished

```python
@on_system_finished.setter
def on_system_finished(value: OnSystemFinished) -> None
```

<a id="unreal.ParticleSystemComponent.set_trail_source_data"></a>

#### set_trail_source_data

```python
def set_trail_source_data(first_socket_name: Name, second_socket_name: Name,
                          width_mode: TrailWidthMode, width: float) -> None
```

x.set_trail_source_data(first_socket_name, second_socket_name, width_mode, width) -> None
Sets the defining data for all trails in this component.

Args:
    first_socket_name (Name): The name of the first socket for the trail.
    second_socket_name (Name): The name of the second socket for the trail.
    width_mode (TrailWidthMode): How the width value is applied to the trail.
    width (float): The width of the trail.

<a id="unreal.ParticleSystemComponent.set_template"></a>

#### set_template

```python
def set_template(new_template: ParticleSystem) -> None
```

x.set_template(new_template) -> None
Change the ParticleSystem used by this ParticleSystemComponent

Args:
    new_template (ParticleSystem):

<a id="unreal.ParticleSystemComponent.set_material_parameter"></a>

#### set_material_parameter

```python
def set_material_parameter(parameter_name: Name,
                           param: MaterialInterface) -> None
```

x.set_material_parameter(parameter_name, param) -> None
Set a named material instance parameter on this ParticleSystemComponent.
Updates the parameter if it already exists, or creates a new entry if not.

Args:
    parameter_name (Name): 
    param (MaterialInterface):

<a id="unreal.ParticleSystemComponent.set_beam_target_tangent"></a>

#### set_beam_target_tangent

```python
def set_beam_target_tangent(emitter_index: int, new_tangent_point: Vector,
                            target_index: int) -> None
```

x.set_beam_target_tangent(emitter_index, new_tangent_point, target_index) -> None
Set the beam target tangent

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_tangent_point (Vector): The value to set it to
    target_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_target_strength"></a>

#### set_beam_target_strength

```python
def set_beam_target_strength(emitter_index: int, new_target_strength: float,
                             target_index: int) -> None
```

x.set_beam_target_strength(emitter_index, new_target_strength, target_index) -> None
Set the beam target strength

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_target_strength (float): The value to set it to
    target_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_target_point"></a>

#### set_beam_target_point

```python
def set_beam_target_point(emitter_index: int, new_target_point: Vector,
                          target_index: int) -> None
```

x.set_beam_target_point(emitter_index, new_target_point, target_index) -> None
Set the beam target point

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_target_point (Vector): The value to set it to
    target_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_source_tangent"></a>

#### set_beam_source_tangent

```python
def set_beam_source_tangent(emitter_index: int, new_tangent_point: Vector,
                            source_index: int) -> None
```

x.set_beam_source_tangent(emitter_index, new_tangent_point, source_index) -> None
Set the beam source tangent

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_tangent_point (Vector): The value to set it to
    source_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_source_strength"></a>

#### set_beam_source_strength

```python
def set_beam_source_strength(emitter_index: int, new_source_strength: float,
                             source_index: int) -> None
```

x.set_beam_source_strength(emitter_index, new_source_strength, source_index) -> None
Set the beam source strength

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_source_strength (float): The value to set it to
    source_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_source_point"></a>

#### set_beam_source_point

```python
def set_beam_source_point(emitter_index: int, new_source_point: Vector,
                          source_index: int) -> None
```

x.set_beam_source_point(emitter_index, new_source_point, source_index) -> None
Set the beam source point

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_source_point (Vector): The value to set it to
    source_index (int32): Which beam within the emitter to set it on

<a id="unreal.ParticleSystemComponent.set_beam_end_point"></a>

#### set_beam_end_point

```python
def set_beam_end_point(emitter_index: int, new_end_point: Vector) -> None
```

x.set_beam_end_point(emitter_index, new_end_point) -> None
Set the beam end point

Args:
    emitter_index (int32): The index of the emitter to set it on
    new_end_point (Vector): The value to set it to

<a id="unreal.ParticleSystemComponent.set_auto_attach_params"></a>

#### set_auto_attach_params

```python
def set_auto_attach_params(
    parent: SceneComponent,
    socket_name: Name = "None",
    location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET
) -> None
```

x.set_auto_attach_params(parent, socket_name="None", location_type=AttachLocation.KEEP_RELATIVE_OFFSET) -> None
DEPRECATED: Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.
deprecated: Please use Set Auto Attachment Parameters
see: bAutoManageAttachment, AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType

Args:
    parent (SceneComponent): Component to attach to.
    socket_name (Name): Socket on Parent to attach to.
    location_type (AttachLocation): Option for how we handle our location when we attach to Parent.

<a id="unreal.ParticleSystemComponent.get_num_active_particles"></a>

#### get_num_active_particles

```python
def get_num_active_particles() -> int
```

x.get_num_active_particles() -> int32
Get the current number of active particles in this system

Returns:
    int32:

<a id="unreal.ParticleSystemComponent.get_named_material"></a>

#### get_named_material

```python
def get_named_material(name: Name) -> MaterialInterface
```

x.get_named_material(name) -> MaterialInterface
Returns a named material. If this named material is not found, returns NULL.

Args:
    name (Name): 

Returns:
    MaterialInterface:

<a id="unreal.ParticleSystemComponent.get_beam_target_tangent"></a>

#### get_beam_target_tangent

```python
def get_beam_target_tangent(emitter_index: int,
                            target_index: int) -> Optional[Vector]
```

x.get_beam_target_tangent(emitter_index, target_index) -> Vector or None
Get the beam target tangent

Args:
    emitter_index (int32): The index of the emitter to get
    target_index (int32): Which beam within the emitter to get

Returns:
    Vector or None: true            EmitterIndex and TargetIndex are valid - OutTangentPoint is valid false           EmitterIndex or TargetIndex is invalid - OutTangentPoint is invalid

    out_tangent_point (Vector): Value of target tangent

<a id="unreal.ParticleSystemComponent.get_beam_target_strength"></a>

#### get_beam_target_strength

```python
def get_beam_target_strength(emitter_index: int,
                             target_index: int) -> Optional[float]
```

x.get_beam_target_strength(emitter_index, target_index) -> float or None
Get the beam target strength

Args:
    emitter_index (int32): The index of the emitter to get
    target_index (int32): Which beam within the emitter to get

Returns:
    float or None: true            EmitterIndex and TargetIndex are valid - OutTargetStrength is valid false           EmitterIndex or TargetIndex is invalid - OutTargetStrength is invalid

    out_target_strength (float): Value of target tangent

<a id="unreal.ParticleSystemComponent.get_beam_target_point"></a>

#### get_beam_target_point

```python
def get_beam_target_point(emitter_index: int,
                          target_index: int) -> Optional[Vector]
```

x.get_beam_target_point(emitter_index, target_index) -> Vector or None
Get the beam target point

Args:
    emitter_index (int32): The index of the emitter to get
    target_index (int32): Which beam within the emitter to get

Returns:
    Vector or None: true            EmitterIndex and TargetIndex are valid - OutTargetPoint is valid false           EmitterIndex or TargetIndex is invalid - OutTargetPoint is invalid

    out_target_point (Vector): Value of target point

<a id="unreal.ParticleSystemComponent.get_beam_source_tangent"></a>

#### get_beam_source_tangent

```python
def get_beam_source_tangent(emitter_index: int,
                            source_index: int) -> Optional[Vector]
```

x.get_beam_source_tangent(emitter_index, source_index) -> Vector or None
Get the beam source tangent

Args:
    emitter_index (int32): The index of the emitter to get
    source_index (int32): Which beam within the emitter to get

Returns:
    Vector or None: true            EmitterIndex and SourceIndex are valid - OutTangentPoint is valid false           EmitterIndex or SourceIndex is invalid - OutTangentPoint is invalid

    out_tangent_point (Vector): Value of source tangent

<a id="unreal.ParticleSystemComponent.get_beam_source_strength"></a>

#### get_beam_source_strength

```python
def get_beam_source_strength(emitter_index: int,
                             source_index: int) -> Optional[float]
```

x.get_beam_source_strength(emitter_index, source_index) -> float or None
Get the beam source strength

Args:
    emitter_index (int32): The index of the emitter to get
    source_index (int32): Which beam within the emitter to get

Returns:
    float or None: true            EmitterIndex and SourceIndex are valid - OutSourceStrength is valid false           EmitterIndex or SourceIndex is invalid - OutSourceStrength is invalid

    out_source_strength (float): Value of source tangent

<a id="unreal.ParticleSystemComponent.get_beam_source_point"></a>

#### get_beam_source_point

```python
def get_beam_source_point(emitter_index: int,
                          source_index: int) -> Optional[Vector]
```

x.get_beam_source_point(emitter_index, source_index) -> Vector or None
Get the beam source point

Args:
    emitter_index (int32): The index of the emitter to get
    source_index (int32): Which beam within the emitter to get

Returns:
    Vector or None: true            EmitterIndex and SourceIndex are valid - OutSourcePoint is valid false           EmitterIndex or SourceIndex is invalid - OutSourcePoint is invalid

    out_source_point (Vector): Value of source point

<a id="unreal.ParticleSystemComponent.get_beam_end_point"></a>

#### get_beam_end_point

```python
def get_beam_end_point(emitter_index: int) -> Optional[Vector]
```

x.get_beam_end_point(emitter_index) -> Vector or None
Get the beam end point

Args:
    emitter_index (int32): The index of the emitter to get the value of

Returns:
    Vector or None: true            EmitterIndex is valid and End point is set - OutEndPoint is valid false           EmitterIndex invalid or End point is not set - OutEndPoint is invalid

    out_end_point (Vector):

<a id="unreal.ParticleSystemComponent.generate_particle_event"></a>

#### generate_particle_event

```python
def generate_particle_event(event_name: Name, emitter_time: float,
                            location: Vector, direction: Vector,
                            velocity: Vector) -> None
```

x.generate_particle_event(event_name, emitter_time, location, direction, velocity) -> None
Record a kismet event.

Args:
    event_name (Name): The name of the event that fired.
    emitter_time (float): The emitter time when the event fired.
    location (Vector): The location of the particle when the event fired.
    direction (Vector): 
    velocity (Vector): The velocity of the particle when the event fired.

<a id="unreal.ParticleSystemComponent.end_trails"></a>

#### end_trails

```python
def end_trails() -> None
```

x.end_trails() -> None
Ends all trail emitters in this component.

<a id="unreal.ParticleSystemComponent.create_named_dynamic_material_instance"></a>

#### create_named_dynamic_material_instance

```python
def create_named_dynamic_material_instance(
        name: Name,
        source_material: MaterialInterface = None) -> MaterialInstanceDynamic
```

x.create_named_dynamic_material_instance(name, source_material=None) -> MaterialInstanceDynamic
Creates a Dynamic Material Instance for the specified named material override, optionally from the supplied material.

Args:
    name (Name): 
    source_material (MaterialInterface): 

Returns:
    MaterialInstanceDynamic:

<a id="unreal.ParticleSystemComponent.begin_trails"></a>

#### begin_trails

```python
def begin_trails(first_socket_name: Name, second_socket_name: Name,
                 width_mode: TrailWidthMode, width: float) -> None
```

x.begin_trails(first_socket_name, second_socket_name, width_mode, width) -> None
Begins all trail emitters in this component.

Args:
    first_socket_name (Name): The name of the first socket for the trail.
    second_socket_name (Name): The name of the second socket for the trail.
    width_mode (TrailWidthMode): How the width value is applied to the trail.
    width (float): The width of the trail.

<a id="unreal.PhysicsObjectBlueprintLibrary"></a>