## NiagaraComponent Objects

```python
class NiagaraComponent(FXSystemComponent)
```

UNiagaraComponent is the primitive component for a Niagara System.
see: ANiagaraActor
see: UNiagaraSystem

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``allow_scalability`` (bool):  [Read-Write] Controls whether we allow scalability culling for this component. If enabled, this component's FX may be culled due to things such as distance, visibility, instance counts and performance.
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``apply_impulse_on_damage`` (bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.
- ``asset`` (NiagaraSystem):  [Read-Write]
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
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_gpu_compute_debug`` (bool):  [Read-Write] When true the GPU simulation debug display will enabled, allowing information used during simulation to be visualized.
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
- ``instance_parameter_overrides`` (Map[NiagaraVariableBase, NiagaraVariant]):  [Read-Write]
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
- ``occlusion_query_mode`` (NiagaraOcclusionQueryMode):  [Read-Write]
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
- ``on_system_finished`` (OnNiagaraSystemFinished):  [Read-Write] Called when the particle system is done
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``override_warmup_settings`` (bool):  [Read-Write] When true then this instance will override the system's warmup settings.
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``random_seed_offset`` (int32):  [Read-Write] Offsets the deterministic random seed of all emitters. Used to achieve variety between components, while still achieving determinism.
  WARNINGS:
  - If this value is set in a non-deterministic way, it has the potential to break determinism of the entire system.
  - This value is applied when emitters are activated/reset, and changing them while the emitter is active has no effect.
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
- ``template_parameter_overrides`` (Map[NiagaraVariableBase, NiagaraVariant]):  [Read-Write]
- ``tick_behavior`` (NiagaraTickBehavior):  [Read-Write] Allows you to control how Niagara selects the tick group, changing this while an instance is active will result in not change as it is cached.
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
- ``wait_for_compilation_on_activate`` (bool):  [Read-Write]
- ``warmup_tick_count`` (int32):  [Read-Write] Number of ticks to process for warmup of the system. Total warmup time is WarmupTickCount * WarmupTickDelta.
- ``warmup_tick_delta`` (float):  [Read-Write] Delta time used when ticking the system in warmup mode.

<a id="unreal.NiagaraComponent.auto_manage_attachment"></a>

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

<a id="unreal.NiagaraComponent.auto_attach_weld_simulated_bodies"></a>

#### auto_attach_weld_simulated_bodies

```python
@property
def auto_attach_weld_simulated_bodies() -> bool
```

(bool):  [Read-Write] Option for how we handle bWeldSimulatedBodies when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment

<a id="unreal.NiagaraComponent.auto_attach_weld_simulated_bodies"></a>

#### auto_attach_weld_simulated_bodies

```python
@auto_attach_weld_simulated_bodies.setter
def auto_attach_weld_simulated_bodies(value: bool) -> None
```

<a id="unreal.NiagaraComponent.occlusion_query_mode"></a>

#### occlusion_query_mode

```python
@property
def occlusion_query_mode() -> NiagaraOcclusionQueryMode
```

(NiagaraOcclusionQueryMode):  [Read-Only]

<a id="unreal.NiagaraComponent.on_system_finished"></a>

#### on_system_finished

```python
@property
def on_system_finished() -> OnNiagaraSystemFinished
```

(OnNiagaraSystemFinished):  [Read-Write] Called when the particle system is done

<a id="unreal.NiagaraComponent.on_system_finished"></a>

#### on_system_finished

```python
@on_system_finished.setter
def on_system_finished(value: OnNiagaraSystemFinished) -> None
```

<a id="unreal.NiagaraComponent.auto_attach_parent"></a>

#### auto_attach_parent

```python
@property
def auto_attach_parent() -> SceneComponent
```

(SceneComponent):  [Read-Only] Component we automatically attach to when activated, if bAutoManageAttachment is true.
If null during registration, we assign the existing AttachParent and defer attachment until we activate.
see: bAutoManageAttachment

<a id="unreal.NiagaraComponent.auto_attach_socket_name"></a>

#### auto_attach_socket_name

```python
@property
def auto_attach_socket_name() -> Name
```

(Name):  [Read-Write] Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment

<a id="unreal.NiagaraComponent.auto_attach_socket_name"></a>

#### auto_attach_socket_name

```python
@auto_attach_socket_name.setter
def auto_attach_socket_name(value: Name) -> None
```

<a id="unreal.NiagaraComponent.auto_attach_location_rule"></a>

#### auto_attach_location_rule

```python
@property
def auto_attach_location_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.NiagaraComponent.auto_attach_location_rule"></a>

#### auto_attach_location_rule

```python
@auto_attach_location_rule.setter
def auto_attach_location_rule(value: AttachmentRule) -> None
```

<a id="unreal.NiagaraComponent.auto_attach_rotation_rule"></a>

#### auto_attach_rotation_rule

```python
@property
def auto_attach_rotation_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.NiagaraComponent.auto_attach_rotation_rule"></a>

#### auto_attach_rotation_rule

```python
@auto_attach_rotation_rule.setter
def auto_attach_rotation_rule(value: AttachmentRule) -> None
```

<a id="unreal.NiagaraComponent.auto_attach_scale_rule"></a>

#### auto_attach_scale_rule

```python
@property
def auto_attach_scale_rule() -> AttachmentRule
```

(AttachmentRule):  [Read-Write] Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.
see: bAutoManageAttachment, EAttachmentRule

<a id="unreal.NiagaraComponent.auto_attach_scale_rule"></a>

#### auto_attach_scale_rule

```python
@auto_attach_scale_rule.setter
def auto_attach_scale_rule(value: AttachmentRule) -> None
```

<a id="unreal.NiagaraComponent.allow_scalability"></a>

#### allow_scalability

```python
@property
def allow_scalability() -> bool
```

(bool):  [Read-Write] Controls whether we allow scalability culling for this component. If enabled, this component's FX may be culled due to things such as distance, visibility, instance counts and performance.

<a id="unreal.NiagaraComponent.allow_scalability"></a>

#### allow_scalability

```python
@allow_scalability.setter
def allow_scalability(value: bool) -> None
```

<a id="unreal.NiagaraComponent.set_variable_vec4"></a>

#### set_variable_vec4

```python
def set_variable_vec4(variable_name: Name, value: Vector4) -> None
```

x.set_variable_vec4(variable_name, value) -> None
Sets a Niagara Vector4 parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Vector4):

<a id="unreal.NiagaraComponent.set_variable_vec3"></a>

#### set_variable_vec3

```python
def set_variable_vec3(variable_name: Name, value: Vector) -> None
```

x.set_variable_vec3(variable_name, value) -> None
Sets a Niagara Vector3 parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Vector):

<a id="unreal.NiagaraComponent.set_variable_vec2"></a>

#### set_variable_vec2

```python
def set_variable_vec2(variable_name: Name, value: Vector2D) -> None
```

x.set_variable_vec2(variable_name, value) -> None
Sets a Niagara Vector2 parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Vector2D):

<a id="unreal.NiagaraComponent.set_variable_texture_render_target"></a>

#### set_variable_texture_render_target

```python
def set_variable_texture_render_target(
        variable_name: Name,
        texture_render_target: TextureRenderTarget) -> None
```

x.set_variable_texture_render_target(variable_name, texture_render_target) -> None
Set Variable Texture Render Target

Args:
    variable_name (Name): 
    texture_render_target (TextureRenderTarget):

<a id="unreal.NiagaraComponent.set_variable_texture"></a>

#### set_variable_texture

```python
def set_variable_texture(variable_name: Name, texture: Texture) -> None
```

x.set_variable_texture(variable_name, texture) -> None
Set Variable Texture

Args:
    variable_name (Name): 
    texture (Texture):

<a id="unreal.NiagaraComponent.set_variable_static_mesh"></a>

#### set_variable_static_mesh

```python
def set_variable_static_mesh(variable_name: Name, value: StaticMesh) -> None
```

x.set_variable_static_mesh(variable_name, value) -> None
Set Variable Static Mesh

Args:
    variable_name (Name): 
    value (StaticMesh):

<a id="unreal.NiagaraComponent.set_variable_quat"></a>

#### set_variable_quat

```python
def set_variable_quat(variable_name: Name, value: Quat) -> None
```

x.set_variable_quat(variable_name, value) -> None
Sets a Niagara quaternion parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Quat):

<a id="unreal.NiagaraComponent.set_variable_position"></a>

#### set_variable_position

```python
def set_variable_position(variable_name: Name, value: Vector) -> None
```

x.set_variable_position(variable_name, value) -> None
Sets a Niagara Position parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Vector):

<a id="unreal.NiagaraComponent.set_variable_object"></a>

#### set_variable_object

```python
def set_variable_object(variable_name: Name, object: Object) -> None
```

x.set_variable_object(variable_name, object) -> None
Set Variable Object

Args:
    variable_name (Name): 
    object (Object):

<a id="unreal.NiagaraComponent.set_variable_matrix"></a>

#### set_variable_matrix

```python
def set_variable_matrix(variable_name: Name, value: Matrix) -> None
```

x.set_variable_matrix(variable_name, value) -> None
Sets a Niagara matrix parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (Matrix):

<a id="unreal.NiagaraComponent.set_variable_material"></a>

#### set_variable_material

```python
def set_variable_material(variable_name: Name,
                          object: MaterialInterface) -> None
```

x.set_variable_material(variable_name, object) -> None
Set Variable Material

Args:
    variable_name (Name): 
    object (MaterialInterface):

<a id="unreal.NiagaraComponent.set_variable_linear_color"></a>

#### set_variable_linear_color

```python
def set_variable_linear_color(variable_name: Name, value: LinearColor) -> None
```

x.set_variable_linear_color(variable_name, value) -> None
Sets a Niagara FLinearColor parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (LinearColor):

<a id="unreal.NiagaraComponent.set_variable_int"></a>

#### set_variable_int

```python
def set_variable_int(variable_name: Name, value: int) -> None
```

x.set_variable_int(variable_name, value) -> None
Sets a Niagara int parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (int32):

<a id="unreal.NiagaraComponent.set_variable_float"></a>

#### set_variable_float

```python
def set_variable_float(variable_name: Name, value: float) -> None
```

x.set_variable_float(variable_name, value) -> None
Sets a Niagara float parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (float):

<a id="unreal.NiagaraComponent.set_variable_bool"></a>

#### set_variable_bool

```python
def set_variable_bool(variable_name: Name, value: bool) -> None
```

x.set_variable_bool(variable_name, value) -> None
Sets a Niagara bool parameter by name, overriding locally if necessary.

Args:
    variable_name (Name): 
    value (bool):

<a id="unreal.NiagaraComponent.set_variable_actor"></a>

#### set_variable_actor

```python
def set_variable_actor(variable_name: Name, actor: Actor) -> None
```

x.set_variable_actor(variable_name, actor) -> None
Set Variable Actor

Args:
    variable_name (Name): 
    actor (Actor):

<a id="unreal.NiagaraComponent.set_tick_behavior"></a>

#### set_tick_behavior

```python
def set_tick_behavior(new_tick_behavior: NiagaraTickBehavior) -> None
```

x.set_tick_behavior(new_tick_behavior) -> None
Set Tick Behavior

Args:
    new_tick_behavior (NiagaraTickBehavior):

<a id="unreal.NiagaraComponent.set_system_fixed_bounds"></a>

#### set_system_fixed_bounds

```python
def set_system_fixed_bounds(local_bounds: Box) -> None
```

x.set_system_fixed_bounds(local_bounds) -> None
Sets the fixed bounds for the system instance, this overrides all other bounds.
The box is expected to be in local space not world space.
A default uninitialized box will clear the fixed bounds and revert back to system fixed / dynamic bounds.

Args:
    local_bounds (Box):

<a id="unreal.NiagaraComponent.set_sim_cache"></a>

#### set_sim_cache

```python
def set_sim_cache(sim_cache: NiagaraSimCache,
                  reset_system: bool = False) -> None
```

x.set_sim_cache(sim_cache, reset_system=False) -> None
Sets the simulation cache to use for the component.
A null SimCache parameter will clear the active simulation cache.
When clearing a simulation cache that has been running you may wish to reset or continue, this option is only
valid when using a full simulation cache.  A renderer only cache will always reset as we can not continue the
simulation due to missing simulation data.

Args:
    sim_cache (NiagaraSimCache): 
    reset_system (bool):

<a id="unreal.NiagaraComponent.set_seek_delta"></a>

#### set_seek_delta

```python
def set_seek_delta(seek_delta: float) -> None
```

x.set_seek_delta(seek_delta) -> None
Sets the delta value which is used when seeking from the current age, to the desired age.  This is only relevant
      when using the DesiredAge age update mode.

Args:
    seek_delta (float):

<a id="unreal.NiagaraComponent.set_rendering_enabled"></a>

#### set_rendering_enabled

```python
def set_rendering_enabled(rendering_enabled: bool) -> None
```

x.set_rendering_enabled(rendering_enabled) -> None
Sets whether or not rendering is enabled for this component.

Args:
    rendering_enabled (bool):

<a id="unreal.NiagaraComponent.set_random_seed_offset"></a>

#### set_random_seed_offset

```python
def set_random_seed_offset(new_random_seed_offset: int) -> None
```

x.set_random_seed_offset(new_random_seed_offset) -> None
Set Random Seed Offset

Args:
    new_random_seed_offset (int32):

<a id="unreal.NiagaraComponent.set_preview_lod_distance"></a>

#### set_preview_lod_distance

```python
def set_preview_lod_distance(enable_preview_lod_distance: bool,
                             preview_lod_distance: float,
                             preview_max_distance: float) -> None
```

x.set_preview_lod_distance(enable_preview_lod_distance, preview_lod_distance, preview_max_distance) -> None
Set Preview LODDistance

Args:
    enable_preview_lod_distance (bool): 
    preview_lod_distance (float): 
    preview_max_distance (float):

<a id="unreal.NiagaraComponent.set_paused"></a>

#### set_paused

```python
def set_paused(paused: bool) -> None
```

x.set_paused(paused) -> None
Set Paused

Args:
    paused (bool):

<a id="unreal.NiagaraComponent.set_occlusion_query_mode"></a>

#### set_occlusion_query_mode

```python
def set_occlusion_query_mode(mode: NiagaraOcclusionQueryMode) -> None
```

x.set_occlusion_query_mode(mode) -> None
Set Occlusion Query Mode

Args:
    mode (NiagaraOcclusionQueryMode):

<a id="unreal.NiagaraComponent.set_niagara_variable_vec4"></a>

#### set_niagara_variable_vec4

```python
def set_niagara_variable_vec4(variable_name: str, value: Vector4) -> None
```

x.set_niagara_variable_vec4(variable_name, value) -> None
Set Niagara Variable Vec 4

Args:
    variable_name (str): 
    value (Vector4):

<a id="unreal.NiagaraComponent.set_niagara_variable_vec3"></a>

#### set_niagara_variable_vec3

```python
def set_niagara_variable_vec3(variable_name: str, value: Vector) -> None
```

x.set_niagara_variable_vec3(variable_name, value) -> None
Set Niagara Variable Vec 3

Args:
    variable_name (str): 
    value (Vector):

<a id="unreal.NiagaraComponent.set_niagara_variable_vec2"></a>

#### set_niagara_variable_vec2

```python
def set_niagara_variable_vec2(variable_name: str, value: Vector2D) -> None
```

x.set_niagara_variable_vec2(variable_name, value) -> None
Set Niagara Variable Vec 2

Args:
    variable_name (str): 
    value (Vector2D):

<a id="unreal.NiagaraComponent.set_niagara_variable_quat"></a>

#### set_niagara_variable_quat

```python
def set_niagara_variable_quat(variable_name: str, value: Quat) -> None
```

x.set_niagara_variable_quat(variable_name, value) -> None
Set Niagara Variable Quat

Args:
    variable_name (str): 
    value (Quat):

<a id="unreal.NiagaraComponent.set_niagara_variable_position"></a>

#### set_niagara_variable_position

```python
def set_niagara_variable_position(variable_name: str, value: Vector) -> None
```

x.set_niagara_variable_position(variable_name, value) -> None
Set Niagara Variable Position

Args:
    variable_name (str): 
    value (Vector):

<a id="unreal.NiagaraComponent.set_niagara_variable_object"></a>

#### set_niagara_variable_object

```python
def set_niagara_variable_object(variable_name: str, object: Object) -> None
```

x.set_niagara_variable_object(variable_name, object) -> None
Set Niagara Variable Object

Args:
    variable_name (str): 
    object (Object):

<a id="unreal.NiagaraComponent.set_niagara_variable_matrix"></a>

#### set_niagara_variable_matrix

```python
def set_niagara_variable_matrix(variable_name: str, value: Matrix) -> None
```

x.set_niagara_variable_matrix(variable_name, value) -> None
Set Niagara Variable Matrix

Args:
    variable_name (str): 
    value (Matrix):

<a id="unreal.NiagaraComponent.set_niagara_variable_linear_color"></a>

#### set_niagara_variable_linear_color

```python
def set_niagara_variable_linear_color(variable_name: str,
                                      value: LinearColor) -> None
```

x.set_niagara_variable_linear_color(variable_name, value) -> None
Set Niagara Variable Linear Color

Args:
    variable_name (str): 
    value (LinearColor):

<a id="unreal.NiagaraComponent.set_niagara_variable_int"></a>

#### set_niagara_variable_int

```python
def set_niagara_variable_int(variable_name: str, value: int) -> None
```

x.set_niagara_variable_int(variable_name, value) -> None
Set Niagara Variable Int

Args:
    variable_name (str): 
    value (int32):

<a id="unreal.NiagaraComponent.set_niagara_variable_float"></a>

#### set_niagara_variable_float

```python
def set_niagara_variable_float(variable_name: str, value: float) -> None
```

x.set_niagara_variable_float(variable_name, value) -> None
Set Niagara Variable Float

Args:
    variable_name (str): 
    value (float):

<a id="unreal.NiagaraComponent.set_niagara_variable_bool"></a>

#### set_niagara_variable_bool

```python
def set_niagara_variable_bool(variable_name: str, value: bool) -> None
```

x.set_niagara_variable_bool(variable_name, value) -> None
Set Niagara Variable Bool

Args:
    variable_name (str): 
    value (bool):

<a id="unreal.NiagaraComponent.set_niagara_variable_actor"></a>

#### set_niagara_variable_actor

```python
def set_niagara_variable_actor(variable_name: str, actor: Actor) -> None
```

x.set_niagara_variable_actor(variable_name, actor) -> None
Set Niagara Variable Actor

Args:
    variable_name (str): 
    actor (Actor):

<a id="unreal.NiagaraComponent.set_max_sim_time"></a>

#### set_max_sim_time

```python
def set_max_sim_time(max_time: float) -> None
```

x.set_max_sim_time(max_time) -> None
Sets the maximum CPU time in seconds we will simulate to the desired age, when we go beyond this limit ticks will be processed in the next frame.
This is only relevant when using the DesiredAge age update mode.
Note: The componet will not be visibile if we have ticks to process and SetCanRenderWhileSeeking is set to true

Args:
    max_time (float):

<a id="unreal.NiagaraComponent.set_lock_desired_age_delta_time_to_seek_delta"></a>

#### set_lock_desired_age_delta_time_to_seek_delta

```python
def set_lock_desired_age_delta_time_to_seek_delta(lock: bool) -> None
```

x.set_lock_desired_age_delta_time_to_seek_delta(lock) -> None
Sets whether or not the delta time used to tick the system instance when using desired age is locked to the seek delta.  When true, the system instance
      will only be ticked when the desired age has changed by more than the seek delta.  When false the system instance will be ticked by the change in desired
      age when not seeking.

Args:
    lock (bool):

<a id="unreal.NiagaraComponent.set_gpu_compute_debug"></a>

#### set_gpu_compute_debug

```python
def set_gpu_compute_debug(enable_debug: bool) -> None
```

x.set_gpu_compute_debug(enable_debug) -> None
Set Gpu Compute Debug

Args:
    enable_debug (bool):

<a id="unreal.NiagaraComponent.set_force_solo"></a>

#### set_force_solo

```python
def set_force_solo(force_solo: bool) -> None
```

x.set_force_solo(force_solo) -> None
Set Force Solo

Args:
    force_solo (bool):

<a id="unreal.NiagaraComponent.set_emitter_fixed_bounds"></a>

#### set_emitter_fixed_bounds

```python
def set_emitter_fixed_bounds(emitter_name: Name, local_bounds: Box) -> None
```

x.set_emitter_fixed_bounds(emitter_name, local_bounds) -> None
Sets the fixed bounds for an emitter instance, this overrides all other bounds.
The box is expected to be in local space not world space.
A default uninitialized box will clear the fixed bounds and revert back to emitter fixed / dynamic bounds.

Args:
    emitter_name (Name): 
    local_bounds (Box):

<a id="unreal.NiagaraComponent.set_desired_age"></a>

#### set_desired_age

```python
def set_desired_age(desired_age: float) -> None
```

x.set_desired_age(desired_age) -> None
Sets the desired age of the System instance.  This is only relevant when using the DesiredAge age update mode.

Args:
    desired_age (float):

<a id="unreal.NiagaraComponent.set_custom_time_dilation"></a>

#### set_custom_time_dilation

```python
def set_custom_time_dilation(dilation: float = 1.000000) -> None
```

x.set_custom_time_dilation(dilation=1.000000) -> None
Sets the custom time dilation value for the component.
Note: This is only available on components that are in solo mode currently.

Args:
    dilation (float):

<a id="unreal.NiagaraComponent.set_can_render_while_seeking"></a>

#### set_can_render_while_seeking

```python
def set_can_render_while_seeking(can_render_while_seeking: bool) -> None
```

x.set_can_render_while_seeking(can_render_while_seeking) -> None
Sets whether or not the system can render while seeking.

Args:
    can_render_while_seeking (bool):

<a id="unreal.NiagaraComponent.set_auto_destroy"></a>

#### set_auto_destroy

```python
def set_auto_destroy(auto_destroy: bool) -> None
```

x.set_auto_destroy(auto_destroy) -> None
Set Auto Destroy

Args:
    auto_destroy (bool):

<a id="unreal.NiagaraComponent.set_asset"></a>

#### set_asset

```python
def set_asset(asset: NiagaraSystem,
              reset_existing_override_parameters: bool = True) -> None
```

x.set_asset(asset, reset_existing_override_parameters=True) -> None
Switch which asset the component is using.
This requires Niagara to wait for concurrent execution and the override parameter store to be synchronized with the new asset.
By default existing parameters are reset when we call SetAsset, modify bResetExistingOverrideParameters to leave existing parameter data as is.

Args:
    asset (NiagaraSystem): 
    reset_existing_override_parameters (bool):

<a id="unreal.NiagaraComponent.set_age_update_mode"></a>

#### set_age_update_mode

```python
def set_age_update_mode(age_update_mode: NiagaraAgeUpdateMode) -> None
```

x.set_age_update_mode(age_update_mode) -> None
Sets the age update mode for the System instance.

Args:
    age_update_mode (NiagaraAgeUpdateMode):

<a id="unreal.NiagaraComponent.seek_to_desired_age"></a>

#### seek_to_desired_age

```python
def seek_to_desired_age(desired_age: float) -> None
```

x.seek_to_desired_age(desired_age) -> None
Sets the desired age of the System instance and designates that this change is a seek.  When seeking to a desired age the
          The component can optionally prevent rendering.

Args:
    desired_age (float):

<a id="unreal.NiagaraComponent.reset_system"></a>

#### reset_system

```python
def reset_system() -> None
```

x.reset_system() -> None
Resets the System to it's initial pre-simulated state.

<a id="unreal.NiagaraComponent.reinitialize_system"></a>

#### reinitialize_system

```python
def reinitialize_system() -> None
```

x.reinitialize_system() -> None
Called on when an external object wishes to force this System to reinitialize itself from the System data.

<a id="unreal.NiagaraComponent.is_paused"></a>

#### is_paused

```python
def is_paused() -> bool
```

x.is_paused() -> bool
Is Paused

Returns:
    bool:

<a id="unreal.NiagaraComponent.init_for_performance_baseline"></a>

#### init_for_performance_baseline

```python
def init_for_performance_baseline() -> None
```

x.init_for_performance_baseline() -> None
Initializes this component for capturing a performance baseline.
This will do things such as disabling distance culling and setting a LODDistance of 0 to ensure the effect is at it's maximum cost.

<a id="unreal.NiagaraComponent.get_tick_behavior"></a>

#### get_tick_behavior

```python
def get_tick_behavior() -> NiagaraTickBehavior
```

x.get_tick_behavior() -> NiagaraTickBehavior
Get Tick Behavior

Returns:
    NiagaraTickBehavior:

<a id="unreal.NiagaraComponent.get_system_fixed_bounds"></a>

#### get_system_fixed_bounds

```python
def get_system_fixed_bounds() -> Box
```

x.get_system_fixed_bounds() -> Box
Gets the fixed bounds for the system instance.
This will return the user set fixed bounds if set, or the systems fixed bounds if set.
Note: The returned box may be invalid if no fixed bounds exist

Returns:
    Box:

<a id="unreal.NiagaraComponent.get_sim_cache"></a>

#### get_sim_cache

```python
def get_sim_cache() -> NiagaraSimCache
```

x.get_sim_cache() -> NiagaraSimCache
Get the active simulation cache, will return null if we do not have an active one.

Returns:
    NiagaraSimCache:

<a id="unreal.NiagaraComponent.get_seek_delta"></a>

#### get_seek_delta

```python
def get_seek_delta() -> float
```

x.get_seek_delta() -> float
Gets the delta value which is used when seeking from the current age, to the desired age.  This is only relevant
      when using the DesiredAge age update mode.

Returns:
    float:

<a id="unreal.NiagaraComponent.get_random_seed_offset"></a>

#### get_random_seed_offset

```python
def get_random_seed_offset() -> int
```

x.get_random_seed_offset() -> int32
Get Random Seed Offset

Returns:
    int32:

<a id="unreal.NiagaraComponent.get_preview_lod_distance_enabled"></a>

#### get_preview_lod_distance_enabled

```python
def get_preview_lod_distance_enabled() -> bool
```

x.get_preview_lod_distance_enabled() -> bool
Get Preview LODDistance Enabled

Returns:
    bool:

<a id="unreal.NiagaraComponent.get_preview_lod_distance"></a>

#### get_preview_lod_distance

```python
def get_preview_lod_distance() -> float
```

x.get_preview_lod_distance() -> float
Get Preview LODDistance

Returns:
    float:

<a id="unreal.NiagaraComponent.get_occlusion_query_mode"></a>

#### get_occlusion_query_mode

```python
def get_occlusion_query_mode() -> NiagaraOcclusionQueryMode
```

x.get_occlusion_query_mode() -> NiagaraOcclusionQueryMode
Get Occlusion Query Mode

Returns:
    NiagaraOcclusionQueryMode:

<a id="unreal.NiagaraComponent.get_max_sim_time"></a>

#### get_max_sim_time

```python
def get_max_sim_time() -> float
```

x.get_max_sim_time() -> float
Get the maximum CPU time in seconds we will simulate to the desired age, when we go beyond this limit ticks will be processed in the next frame.
This is only relevant when using the DesiredAge age update mode.
Note: The componet will not be visibile if we have ticks to process and SetCanRenderWhileSeeking is set to true

Returns:
    float:

<a id="unreal.NiagaraComponent.get_lock_desired_age_delta_time_to_seek_delta"></a>

#### get_lock_desired_age_delta_time_to_seek_delta

```python
def get_lock_desired_age_delta_time_to_seek_delta() -> bool
```

x.get_lock_desired_age_delta_time_to_seek_delta() -> bool
Gets whether or not the delta time used to tick the system instance when using desired age is locked to the seek delta.  When true, the system instance
      will only be ticked when the desired age has changed by more than the seek delta.  When false the system instance will be ticked by the change in desired
      age when not seeking.

Returns:
    bool:

<a id="unreal.NiagaraComponent.get_force_solo"></a>

#### get_force_solo

```python
def get_force_solo() -> bool
```

x.get_force_solo() -> bool
Get Force Solo

Returns:
    bool:

<a id="unreal.NiagaraComponent.get_emitter_fixed_bounds"></a>

#### get_emitter_fixed_bounds

```python
def get_emitter_fixed_bounds(emitter_name: Name) -> Box
```

x.get_emitter_fixed_bounds(emitter_name) -> Box
Gets the fixed bounds for an emitter instance.
This will return the user set fixed bounds if set, or the emitters fixed bounds if set.
Note: The returned box may be invalid if no fixed bounds exist

Args:
    emitter_name (Name): 

Returns:
    Box:

<a id="unreal.NiagaraComponent.get_desired_age"></a>

#### get_desired_age

```python
def get_desired_age() -> float
```

x.get_desired_age() -> float
Gets the desired age of the System instance.  This is only relevant when using the DesiredAge age update mode.

Returns:
    float:

<a id="unreal.NiagaraComponent.get_data_interface"></a>

#### get_data_interface

```python
def get_data_interface(name: str) -> NiagaraDataInterface
```

x.get_data_interface(name) -> NiagaraDataInterface
Get Data Interface

Args:
    name (str): 

Returns:
    NiagaraDataInterface:

<a id="unreal.NiagaraComponent.get_custom_time_dilation"></a>

#### get_custom_time_dilation

```python
def get_custom_time_dilation() -> float
```

x.get_custom_time_dilation() -> float
Get Custom Time Dilation

Returns:
    float:

<a id="unreal.NiagaraComponent.get_asset"></a>

#### get_asset

```python
def get_asset() -> NiagaraSystem
```

x.get_asset() -> NiagaraSystem
Get Asset

Returns:
    NiagaraSystem:

<a id="unreal.NiagaraComponent.get_age_update_mode"></a>

#### get_age_update_mode

```python
def get_age_update_mode() -> NiagaraAgeUpdateMode
```

x.get_age_update_mode() -> NiagaraAgeUpdateMode
Get Age Update Mode

Returns:
    NiagaraAgeUpdateMode:

<a id="unreal.NiagaraComponent.clear_system_fixed_bounds"></a>

#### clear_system_fixed_bounds

```python
def clear_system_fixed_bounds() -> None
```

x.clear_system_fixed_bounds() -> None
Clear any previously set fixed bounds for the system instance.

<a id="unreal.NiagaraComponent.clear_sim_cache"></a>

#### clear_sim_cache

```python
def clear_sim_cache(reset_system: bool = False) -> None
```

x.clear_sim_cache(reset_system=False) -> None
Clear any active simulation cache.
When clearing a simulation cache that has been running you may wish to reset or continue, this option is only
valid when using a full simulation cache.  A renderer only cache will always reset as we can not continue the
simulation due to missing simulation data.

Args:
    reset_system (bool):

<a id="unreal.NiagaraComponent.clear_emitter_fixed_bounds"></a>

#### clear_emitter_fixed_bounds

```python
def clear_emitter_fixed_bounds(emitter_name: Name) -> None
```

x.clear_emitter_fixed_bounds(emitter_name) -> None
Clear any previously set fixed bounds for the emitter instance.

Args:
    emitter_name (Name):

<a id="unreal.NiagaraComponent.advance_simulation_by_time"></a>

#### advance_simulation_by_time

```python
def advance_simulation_by_time(simulate_time: float,
                               tick_delta_seconds: float) -> None
```

x.advance_simulation_by_time(simulate_time, tick_delta_seconds) -> None
Advances this system's simulation by the specified time in seconds and delta time. Advancement is done in whole ticks of TickDeltaSeconds so actual simulated time will be the nearest lower multiple of TickDeltaSeconds.

Args:
    simulate_time (float): 
    tick_delta_seconds (float):

<a id="unreal.NiagaraComponent.advance_simulation"></a>

#### advance_simulation

```python
def advance_simulation(tick_count: int, tick_delta_seconds: float) -> None
```

x.advance_simulation(tick_count, tick_delta_seconds) -> None
Advances this system's simulation by the specified number of ticks and delta time.

Args:
    tick_count (int32): 
    tick_delta_seconds (float):

<a id="unreal.NiagaraCullProxyComponent"></a>