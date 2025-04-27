## SkinnedMeshComponent Objects

```python
class SkinnedMeshComponent(MeshComponent)
```

Skinned mesh component that supports bone skinned mesh rendering.
This class does not support animation.
see: USkeletalMeshComponent

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedMeshComponent.h

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
- ``always_use_mesh_deformer`` (bool):  [Read-Write] If true, and if no mesh deformer is set from here or the SkeletalMesh, fall back to the default deformer specified in the project settings, unless DefaultMode is set to "Never" in project settings
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
- ``capsule_indirect_shadow_min_visibility`` (float):  [Read-Write] Controls how dark the capsule indirect shadow can be.
- ``cast_capsule_direct_shadow`` (bool):  [Read-Write] Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for direct shadowing from lights.
  This type of shadowing is approximate but handles extremely wide area shadowing well.  The softness of the shadow depends on the light's LightSourceAngle / SourceRadius.
  This flag will force bCastInsetShadow to be enabled.
- ``cast_capsule_indirect_shadow`` (bool):  [Read-Write] Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for shadowing indirect lighting (from lightmaps or skylight).
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
- ``component_use_fixed_skel_bounds`` (bool):  [Read-Write] When true, skip using the physics asset etc. and always use the fixed bounds defined in the SkeletalMesh.
- ``consider_all_bodies_for_bounds`` (bool):  [Read-Write] If true, when updating bounds from a PhysicsAsset, consider _all_ BodySetups, not just those flagged with bConsiderForBounds.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``disable_morph_target`` (bool):  [Read-Write] Disable Morphtarget for this component.
- ``display_bones`` (bool):  [Read-Write] Draw the skeleton hierarchy for this skel mesh.
- ``display_debug_update_rate_optimizations`` (bool):  [Read-Write] Enable on screen debugging of update rate optimization.
  Red = Skipping 0 frames, Green = skipping 1 frame, Blue = skipping 2 frames, black = skipping more than 2 frames.
  todo:: turn this into a console command.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``enable_update_rate_optimizations`` (bool):  [Read-Write] if TRUE, Owner will determine how often animation will be updated and evaluated. See AnimUpdateRateTick()
  This allows to skip frames for performance. (For example based on visibility and size on screen).
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``forced_lod_model`` (int32):  [Read-Write]
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``ignore_leader_pose_component_lod`` (bool):  [Read-Write] Flag that when set will ensure UpdateLODStatus will not take the LeaderPoseComponent's current LOD in consideration when determining the correct LOD level (this requires LeaderPoseComponent's LOD to always be >= determined LOD otherwise bone transforms could be missing
- ``ignore_radial_force`` (bool):  [Read-Write] Will ignore radial forces applied to this component.
- ``ignore_radial_impulse`` (bool):  [Read-Write] Will ignore radial impulses applied to this component.
- ``include_component_location_into_bounds`` (bool):  [Read-Write] If true, the Location of this Component will be included into its bounds calculation
  (this can be useful when using SMU_OnlyTickPoseWhenRendered on a character that moves away from the root and no bones are left near the origin of the component)
- ``indirect_lighting_cache_quality`` (IndirectLightingCacheQuality):  [Read-Write] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``leader_pose_component`` (SkinnedMeshComponent):  [Read-Write] If set, this SkeletalMeshComponent will not use its SpaceBase for bone transform, but will
  use the component space transforms from the LeaderPoseComponent. This is used when constructing a character using multiple skeletal meshes sharing the same
  skeleton within the same Actor.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``mesh_deformer`` (MeshDeformer):  [Read-Write] The mesh deformer to use. If no mesh deformer is set from here or the SkeletalMesh, then we fall back to the fixed function deformation, unless AlwaysUseMeshDeformer is turned on.
- ``mesh_deformer_instance`` (MeshDeformerInstance):  [Read-Write]
  deprecated: Use the GetMeshDeformerInstance function instead
- ``mesh_deformer_instance_settings`` (MeshDeformerInstanceSettings):  [Read-Only] Object containing instance settings for the bound MeshDeformer.
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``min_lod_model`` (int32):  [Read-Write] This is the min LOD that this component will use.  (e.g. if set to 2 then only 2+ LOD Models will be used.) This is useful to set on
  meshes which are known to be a certain distance away and still want to have better LODs when zoomed in on them.
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
- ``overlay_material`` (MaterialInterface):  [Read-Write] Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material
- ``overlay_material_max_draw_distance`` (float):  [Read-Write] The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
- ``override_min_lod`` (bool):  [Read-Write] Whether we should use the min lod specified in MinLodModel for this component instead of the min lod in the mesh
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``per_bone_motion_blur`` (bool):  [Read-Write] If true, use per-bone motion blur on this skeletal mesh (requires additional rendering, can be disabled to save performance).
- ``physics_asset_override`` (PhysicsAsset):  [Read-Write] PhysicsAsset is set in SkeletalMesh by default, but you can override with this value
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
- ``render_static`` (bool):  [Read-Write] If true, render as static in reference pose.
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
- ``set_mesh_deformer`` (bool):  [Read-Write] If true, MeshDeformer will be used. If false, use the default mesh deformer on the SkeletalMesh.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``skeletal_mesh`` (SkeletalMesh):  [Read-Write]
  deprecated: Use USkeletalMeshComponent::GetSkeletalMeshAsset() or GetSkinnedAsset() instead.
- ``skin_cache_usage`` (Array[SkinCacheUsage]):  [Read-Write] How this Component's LOD uses the skin cache feature. Auto will defer to the asset's (SkeletalMesh) option. If Ray Tracing is enabled, will imply Enabled
- ``skinned_asset`` (SkinnedAsset):  [Read-Write]
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``streaming_distance_multiplier`` (float):  [Read-Write] Allows adjusting the desired streaming distance of streaming textures that uses UV 0.
  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.
  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).
  Value can be < 0 (from legcay content, or code changes)
- ``sync_attach_parent_lod`` (bool):  [Read-Write] If true, this component uses its parents LOD when attached if available
  ForcedLOD can override this change. By default, it will use parent LOD.
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
- ``use_bounds_from_leader_pose_component`` (bool):  [Read-Write] When true, we will just using the bounds from our LeaderPoseComponent.  This is useful for when we have a Mesh Parented
  to the main SkelMesh (e.g. outline mesh or a full body overdraw effect that is toggled) that is always going to be the same
  bounds as parent.  We want to do no calculations in that case.
- ``use_screen_render_state_for_update`` (bool):  [Read-Write] If set, use the screen render flag instead of the default render flag when processing offscreen-rendering optimizations
  (such as VisibilityBasedAnimTickOption) that look to reduce animation work when the mesh is not rendered.
  Using this option can result in meshes that are occlusion culled ceasing to perform animation work.
  Note that this can however result in shadows not being animated when meshes are not directly visible.
- ``virtual_texture_cull_mips`` (int8):  [Read-Write] Number of lower mips in the runtime virtual texture to skip for rendering this primitive.
  Larger values reduce the effective draw distance in the runtime virtual texture.
  This culling method doesn't take into account primitive size or virtual texture size.
- ``virtual_texture_lod_bias`` (int8):  [Read-Write] Bias to the LOD selected for rendering to runtime virtual textures.
- ``virtual_texture_min_coverage`` (int8):  [Read-Write] Set the minimum pixel coverage before culling from the runtime virtual texture.
  Larger values reduce the effective draw distance in the runtime virtual texture.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``visibility_based_anim_tick_option`` (VisibilityBasedAnimTickOption):  [Read-Write] * This is tick animation frequency option based on this component rendered or not or using montage
  *  You can change this default value in the INI file
  * Mostly related with performance
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``visible_in_ray_tracing`` (bool):  [Read-Write] If true, this component will be visible in ray tracing effects. Turning this off will remove it from ray traced reflections, shadows, etc.
- ``visible_in_real_time_sky_captures`` (bool):  [Read-Write] If true, this component will be visible in real-time sky light reflection captures.
- ``visible_in_reflection_captures`` (bool):  [Read-Write] If true, this component will be visible in reflection captures.
- ``visible_in_scene_capture_only`` (bool):  [Read-Write] When true, will only be visible in Scene Capture

<a id="unreal.SkinnedMeshComponent.skeletal_mesh"></a>

#### skeletal_mesh

```python
@property
def skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Only]
deprecated: Use USkeletalMeshComponent::GetSkeletalMeshAsset() or GetSkinnedAsset() instead.

<a id="unreal.SkinnedMeshComponent.skinned_asset"></a>

#### skinned_asset

```python
@property
def skinned_asset() -> SkinnedAsset
```

(SkinnedAsset):  [Read-Only]

<a id="unreal.SkinnedMeshComponent.leader_pose_component"></a>

#### leader_pose_component

```python
@property
def leader_pose_component() -> SkinnedMeshComponent
```

(SkinnedMeshComponent):  [Read-Only] If set, this SkeletalMeshComponent will not use its SpaceBase for bone transform, but will
use the component space transforms from the LeaderPoseComponent. This is used when constructing a character using multiple skeletal meshes sharing the same
skeleton within the same Actor.

<a id="unreal.SkinnedMeshComponent.master_pose_component"></a>

#### master_pose_component

```python
@property
def master_pose_component() -> SkinnedMeshComponent
```

deprecated: 'master_pose_component' was renamed to 'leader_pose_component'.

<a id="unreal.SkinnedMeshComponent.skin_cache_usage"></a>

#### skin_cache_usage

```python
@property
def skin_cache_usage() -> Array[SkinCacheUsage]
```

(Array[SkinCacheUsage]):  [Read-Only] How this Component's LOD uses the skin cache feature. Auto will defer to the asset's (SkeletalMesh) option. If Ray Tracing is enabled, will imply Enabled

<a id="unreal.SkinnedMeshComponent.set_mesh_deformer"></a>

#### set_mesh_deformer

```python
@property
def set_mesh_deformer() -> bool
```

(bool):  [Read-Only] If true, MeshDeformer will be used. If false, use the default mesh deformer on the SkeletalMesh.

<a id="unreal.SkinnedMeshComponent.mesh_deformer"></a>

#### mesh_deformer

```python
@property
def mesh_deformer() -> MeshDeformer
```

(MeshDeformer):  [Read-Only] The mesh deformer to use. If no mesh deformer is set from here or the SkeletalMesh, then we fall back to the fixed function deformation, unless AlwaysUseMeshDeformer is turned on.

<a id="unreal.SkinnedMeshComponent.always_use_mesh_deformer"></a>

#### always_use_mesh_deformer

```python
@property
def always_use_mesh_deformer() -> bool
```

(bool):  [Read-Only] If true, and if no mesh deformer is set from here or the SkeletalMesh, fall back to the default deformer specified in the project settings, unless DefaultMode is set to "Never" in project settings

<a id="unreal.SkinnedMeshComponent.mesh_deformer_instance_settings"></a>

#### mesh_deformer_instance_settings

```python
@property
def mesh_deformer_instance_settings() -> MeshDeformerInstanceSettings
```

(MeshDeformerInstanceSettings):  [Read-Only] Object containing instance settings for the bound MeshDeformer.

<a id="unreal.SkinnedMeshComponent.mesh_deformer_instance"></a>

#### mesh_deformer_instance

```python
@property
def mesh_deformer_instance() -> MeshDeformerInstance
```

(MeshDeformerInstance):  [Read-Only]
deprecated: Use the GetMeshDeformerInstance function instead

<a id="unreal.SkinnedMeshComponent.physics_asset_override"></a>

#### physics_asset_override

```python
@property
def physics_asset_override() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Only] PhysicsAsset is set in SkeletalMesh by default, but you can override with this value

<a id="unreal.SkinnedMeshComponent.forced_lod_model"></a>

#### forced_lod_model

```python
@property
def forced_lod_model() -> int
```

(int32):  [Read-Only]

<a id="unreal.SkinnedMeshComponent.min_lod_model"></a>

#### min_lod_model

```python
@property
def min_lod_model() -> int
```

(int32):  [Read-Only] This is the min LOD that this component will use.  (e.g. if set to 2 then only 2+ LOD Models will be used.) This is useful to set on
meshes which are known to be a certain distance away and still want to have better LODs when zoomed in on them.

<a id="unreal.SkinnedMeshComponent.streaming_distance_multiplier"></a>

#### streaming_distance_multiplier

```python
@property
def streaming_distance_multiplier() -> float
```

(float):  [Read-Write] Allows adjusting the desired streaming distance of streaming textures that uses UV 0.
1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.
A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).
Value can be < 0 (from legcay content, or code changes)

<a id="unreal.SkinnedMeshComponent.streaming_distance_multiplier"></a>

#### streaming_distance_multiplier

```python
@streaming_distance_multiplier.setter
def streaming_distance_multiplier(value: float) -> None
```

<a id="unreal.SkinnedMeshComponent.visibility_based_anim_tick_option"></a>

#### visibility_based_anim_tick_option

```python
@property
def visibility_based_anim_tick_option() -> VisibilityBasedAnimTickOption
```

(VisibilityBasedAnimTickOption):  [Read-Write] * This is tick animation frequency option based on this component rendered or not or using montage
*  You can change this default value in the INI file
* Mostly related with performance

<a id="unreal.SkinnedMeshComponent.visibility_based_anim_tick_option"></a>

#### visibility_based_anim_tick_option

```python
@visibility_based_anim_tick_option.setter
def visibility_based_anim_tick_option(
        value: VisibilityBasedAnimTickOption) -> None
```

<a id="unreal.SkinnedMeshComponent.mesh_component_update_flag"></a>

#### mesh_component_update_flag

```python
@property
def mesh_component_update_flag() -> VisibilityBasedAnimTickOption
```

deprecated: 'mesh_component_update_flag' was renamed to 'visibility_based_anim_tick_option'.

<a id="unreal.SkinnedMeshComponent.mesh_component_update_flag"></a>

#### mesh_component_update_flag

```python
@mesh_component_update_flag.setter
def mesh_component_update_flag(value: VisibilityBasedAnimTickOption) -> None
```

<a id="unreal.SkinnedMeshComponent.override_min_lod"></a>

#### override_min_lod

```python
@property
def override_min_lod() -> bool
```

(bool):  [Read-Only] Whether we should use the min lod specified in MinLodModel for this component instead of the min lod in the mesh

<a id="unreal.SkinnedMeshComponent.use_bounds_from_leader_pose_component"></a>

#### use_bounds_from_leader_pose_component

```python
@property
def use_bounds_from_leader_pose_component() -> bool
```

(bool):  [Read-Write] When true, we will just using the bounds from our LeaderPoseComponent.  This is useful for when we have a Mesh Parented
to the main SkelMesh (e.g. outline mesh or a full body overdraw effect that is toggled) that is always going to be the same
bounds as parent.  We want to do no calculations in that case.

<a id="unreal.SkinnedMeshComponent.use_bounds_from_leader_pose_component"></a>

#### use_bounds_from_leader_pose_component

```python
@use_bounds_from_leader_pose_component.setter
def use_bounds_from_leader_pose_component(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.b_use_bounds_from_master_pose_component"></a>

#### b_use_bounds_from_master_pose_component

```python
@property
def b_use_bounds_from_master_pose_component() -> bool
```

deprecated: 'b_use_bounds_from_master_pose_component' was renamed to 'use_bounds_from_leader_pose_component'.

<a id="unreal.SkinnedMeshComponent.b_use_bounds_from_master_pose_component"></a>

#### b_use_bounds_from_master_pose_component

```python
@b_use_bounds_from_master_pose_component.setter
def b_use_bounds_from_master_pose_component(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.include_component_location_into_bounds"></a>

#### include_component_location_into_bounds

```python
@property
def include_component_location_into_bounds() -> bool
```

(bool):  [Read-Only] If true, the Location of this Component will be included into its bounds calculation
(this can be useful when using SMU_OnlyTickPoseWhenRendered on a character that moves away from the root and no bones are left near the origin of the component)

<a id="unreal.SkinnedMeshComponent.disable_morph_target"></a>

#### disable_morph_target

```python
@property
def disable_morph_target() -> bool
```

(bool):  [Read-Write] Disable Morphtarget for this component.

<a id="unreal.SkinnedMeshComponent.disable_morph_target"></a>

#### disable_morph_target

```python
@disable_morph_target.setter
def disable_morph_target(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.per_bone_motion_blur"></a>

#### per_bone_motion_blur

```python
@property
def per_bone_motion_blur() -> bool
```

(bool):  [Read-Only] If true, use per-bone motion blur on this skeletal mesh (requires additional rendering, can be disabled to save performance).

<a id="unreal.SkinnedMeshComponent.component_use_fixed_skel_bounds"></a>

#### component_use_fixed_skel_bounds

```python
@property
def component_use_fixed_skel_bounds() -> bool
```

(bool):  [Read-Write] When true, skip using the physics asset etc. and always use the fixed bounds defined in the SkeletalMesh.

<a id="unreal.SkinnedMeshComponent.component_use_fixed_skel_bounds"></a>

#### component_use_fixed_skel_bounds

```python
@component_use_fixed_skel_bounds.setter
def component_use_fixed_skel_bounds(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.consider_all_bodies_for_bounds"></a>

#### consider_all_bodies_for_bounds

```python
@property
def consider_all_bodies_for_bounds() -> bool
```

(bool):  [Read-Write] If true, when updating bounds from a PhysicsAsset, consider _all_ BodySetups, not just those flagged with bConsiderForBounds.

<a id="unreal.SkinnedMeshComponent.consider_all_bodies_for_bounds"></a>

#### consider_all_bodies_for_bounds

```python
@consider_all_bodies_for_bounds.setter
def consider_all_bodies_for_bounds(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.sync_attach_parent_lod"></a>

#### sync_attach_parent_lod

```python
@property
def sync_attach_parent_lod() -> bool
```

(bool):  [Read-Write] If true, this component uses its parents LOD when attached if available
ForcedLOD can override this change. By default, it will use parent LOD.

<a id="unreal.SkinnedMeshComponent.sync_attach_parent_lod"></a>

#### sync_attach_parent_lod

```python
@sync_attach_parent_lod.setter
def sync_attach_parent_lod(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.cast_capsule_direct_shadow"></a>

#### cast_capsule_direct_shadow

```python
@property
def cast_capsule_direct_shadow() -> bool
```

(bool):  [Read-Only] Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for direct shadowing from lights.
This type of shadowing is approximate but handles extremely wide area shadowing well.  The softness of the shadow depends on the light's LightSourceAngle / SourceRadius.
This flag will force bCastInsetShadow to be enabled.

<a id="unreal.SkinnedMeshComponent.cast_capsule_indirect_shadow"></a>

#### cast_capsule_indirect_shadow

```python
@property
def cast_capsule_indirect_shadow() -> bool
```

(bool):  [Read-Only] Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for shadowing indirect lighting (from lightmaps or skylight).

<a id="unreal.SkinnedMeshComponent.use_screen_render_state_for_update"></a>

#### use_screen_render_state_for_update

```python
@property
def use_screen_render_state_for_update() -> bool
```

(bool):  [Read-Write] If set, use the screen render flag instead of the default render flag when processing offscreen-rendering optimizations
(such as VisibilityBasedAnimTickOption) that look to reduce animation work when the mesh is not rendered.
Using this option can result in meshes that are occlusion culled ceasing to perform animation work.
Note that this can however result in shadows not being animated when meshes are not directly visible.

<a id="unreal.SkinnedMeshComponent.use_screen_render_state_for_update"></a>

#### use_screen_render_state_for_update

```python
@use_screen_render_state_for_update.setter
def use_screen_render_state_for_update(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.enable_update_rate_optimizations"></a>

#### enable_update_rate_optimizations

```python
@property
def enable_update_rate_optimizations() -> bool
```

(bool):  [Read-Write] if TRUE, Owner will determine how often animation will be updated and evaluated. See AnimUpdateRateTick()
This allows to skip frames for performance. (For example based on visibility and size on screen).

<a id="unreal.SkinnedMeshComponent.enable_update_rate_optimizations"></a>

#### enable_update_rate_optimizations

```python
@enable_update_rate_optimizations.setter
def enable_update_rate_optimizations(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.display_debug_update_rate_optimizations"></a>

#### display_debug_update_rate_optimizations

```python
@property
def display_debug_update_rate_optimizations() -> bool
```

(bool):  [Read-Write] Enable on screen debugging of update rate optimization.
Red = Skipping 0 frames, Green = skipping 1 frame, Blue = skipping 2 frames, black = skipping more than 2 frames.
todo:: turn this into a console command.

<a id="unreal.SkinnedMeshComponent.display_debug_update_rate_optimizations"></a>

#### display_debug_update_rate_optimizations

```python
@display_debug_update_rate_optimizations.setter
def display_debug_update_rate_optimizations(value: bool) -> None
```

<a id="unreal.SkinnedMeshComponent.render_static"></a>

#### render_static

```python
@property
def render_static() -> bool
```

(bool):  [Read-Only] If true, render as static in reference pose.

<a id="unreal.SkinnedMeshComponent.ignore_leader_pose_component_lod"></a>

#### ignore_leader_pose_component_lod

```python
@property
def ignore_leader_pose_component_lod() -> bool
```

(bool):  [Read-Only] Flag that when set will ensure UpdateLODStatus will not take the LeaderPoseComponent's current LOD in consideration when determining the correct LOD level (this requires LeaderPoseComponent's LOD to always be >= determined LOD otherwise bone transforms could be missing

<a id="unreal.SkinnedMeshComponent.b_ignore_master_pose_component_lod"></a>

#### b_ignore_master_pose_component_lod

```python
@property
def b_ignore_master_pose_component_lod() -> bool
```

deprecated: 'b_ignore_master_pose_component_lod' was renamed to 'ignore_leader_pose_component_lod'.

<a id="unreal.SkinnedMeshComponent.capsule_indirect_shadow_min_visibility"></a>

#### capsule_indirect_shadow_min_visibility

```python
@property
def capsule_indirect_shadow_min_visibility() -> float
```

(float):  [Read-Only] Controls how dark the capsule indirect shadow can be.

<a id="unreal.SkinnedMeshComponent.unset_mesh_deformer"></a>

#### unset_mesh_deformer

```python
def unset_mesh_deformer() -> None
```

x.unset_mesh_deformer() -> None
Unset any MeshDeformer applied to this Component.

<a id="unreal.SkinnedMeshComponent.unload_skin_weight_profile"></a>

#### unload_skin_weight_profile

```python
def unload_skin_weight_profile(profile_name: Name) -> None
```

x.unload_skin_weight_profile(profile_name) -> None
Unload a Skin Weight Profile's skin weight buffer (if created)

Args:
    profile_name (Name):

<a id="unreal.SkinnedMeshComponent.un_hide_bone_by_name"></a>

#### un_hide_bone_by_name

```python
def un_hide_bone_by_name(bone_name: Name) -> None
```

x.un_hide_bone_by_name(bone_name) -> None
UnHide the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
Compared to HideBone By Index - This keeps track of list of bones and update when LOD changes

Args:
    bone_name (Name): Name of bone to unhide

<a id="unreal.SkinnedMeshComponent.transform_to_bone_space"></a>

#### transform_to_bone_space

```python
def transform_to_bone_space(bone_name: Name, position: Vector,
                            rotation: Rotator) -> Tuple[Vector, Rotator]
```

x.transform_to_bone_space(bone_name, position, rotation) -> (out_position=Vector, out_rotation=Rotator)
Transform a location/rotation from world space to bone relative space.
This is handy if you know the location in world space for a bone attachment, as AttachComponent takes location/rotation in bone-relative space.

Args:
    bone_name (Name): Name of bone
    position (Vector): Input position
    rotation (Rotator): Input rotation

Returns:
    tuple: 

    out_position (Vector): (out) Transformed position

    out_rotation (Rotator): (out) Transformed rotation

<a id="unreal.SkinnedMeshComponent.transform_from_bone_space"></a>

#### transform_from_bone_space

```python
def transform_from_bone_space(bone_name: Name, position: Vector,
                              rotation: Rotator) -> Tuple[Vector, Rotator]
```

x.transform_from_bone_space(bone_name, position, rotation) -> (out_position=Vector, out_rotation=Rotator)
Transform a location/rotation in bone relative space to world space.

Args:
    bone_name (Name): Name of bone
    position (Vector): Input position
    rotation (Rotator): Input rotation

Returns:
    tuple: 

    out_position (Vector): (out) Transformed position

    out_rotation (Rotator): (out) Transformed rotation

<a id="unreal.SkinnedMeshComponent.show_material_section"></a>

#### show_material_section

```python
def show_material_section(material_id: int, section_index: int, show: bool,
                          lod_index: int) -> None
```

x.show_material_section(material_id, section_index, show, lod_index) -> None
Allows hiding of a particular material (by ID) on this instance of a SkeletalMesh.

Args:
    material_id (int32): Index of the material show/hide
    section_index (int32): 
    show (bool): True to show the material, false to hide it
    lod_index (int32): Index of the LOD to modify material visibility within

<a id="unreal.SkinnedMeshComponent.show_all_material_sections"></a>

#### show_all_material_sections

```python
def show_all_material_sections(lod_index: int) -> None
```

x.show_all_material_sections(lod_index) -> None
Clear any material visibility modifications made by ShowMaterialSection

Args:
    lod_index (int32):

<a id="unreal.SkinnedMeshComponent.set_vertex_color_override_linear_color"></a>

#### set_vertex_color_override_linear_color

```python
def set_vertex_color_override_linear_color(
        lod_index: int, vertex_colors: Array[LinearColor]) -> None
```

x.set_vertex_color_override_linear_color(lod_index, vertex_colors) -> None
Allow override of vertex colors on a per-component basis, taking array of Blueprint-friendly LinearColors.

Args:
    lod_index (int32): 
    vertex_colors (Array[LinearColor]):

<a id="unreal.SkinnedMeshComponent.set_skin_weight_profile"></a>

#### set_skin_weight_profile

```python
def set_skin_weight_profile(
        profile_name: Name,
        layer: SkinWeightProfileLayer = SkinWeightProfileLayer.PRIMARY
) -> bool
```

x.set_skin_weight_profile(profile_name, layer=SkinWeightProfileLayer.PRIMARY) -> bool
Set up an override skin weight profile for this component on the given layer.
The values from the secondary layer (if set to have a profile) are applied first, followed by the values from the primary layer.
Since skin weight profiles are stored as sparse data, where only weight values different from the base are kept in storage, it's
possible to set up layers such that they don't interfere with one another.

Args:
    profile_name (Name): 
    layer (SkinWeightProfileLayer): 

Returns:
    bool:

<a id="unreal.SkinnedMeshComponent.set_skin_weight_override"></a>

#### set_skin_weight_override

```python
def set_skin_weight_override(
        lod_index: int, skin_weights: Array[SkelMeshSkinWeightInfo]) -> None
```

x.set_skin_weight_override(lod_index, skin_weights) -> None
Allow override of skin weights on a per-component basis.

Args:
    lod_index (int32): 
    skin_weights (Array[SkelMeshSkinWeightInfo]):

<a id="unreal.SkinnedMeshComponent.set_skinned_asset_and_update"></a>

#### set_skinned_asset_and_update

```python
def set_skinned_asset_and_update(new_mesh: SkinnedAsset,
                                 reinit_pose: bool = True) -> None
```

x.set_skinned_asset_and_update(new_mesh, reinit_pose=True) -> None
Change the SkinnedAsset that is rendered for this Component. Will re-initialize the animation tree etc.

Args:
    new_mesh (SkinnedAsset): New mesh to set for this component
    reinit_pose (bool): Whether we should keep current pose or reinitialize.

<a id="unreal.SkinnedMeshComponent.set_skeletal_mesh"></a>

#### set_skeletal_mesh

```python
def set_skeletal_mesh(new_mesh: SkinnedAsset,
                      reinit_pose: bool = True) -> None
```

deprecated: 'set_skeletal_mesh' was renamed to 'set_skinned_asset_and_update'.

<a id="unreal.SkinnedMeshComponent.set_render_static"></a>

#### set_render_static

```python
def set_render_static(new_value: bool) -> None
```

x.set_render_static(new_value) -> None
Set whether this skinned mesh should be rendered as static mesh in a reference pose

Args:
    new_value (bool):

<a id="unreal.SkinnedMeshComponent.set_physics_asset"></a>

#### set_physics_asset

```python
def set_physics_asset(new_physics_asset: PhysicsAsset,
                      force_re_init: bool = False) -> None
```

x.set_physics_asset(new_physics_asset, force_re_init=False) -> None
Override the Physics Asset of the mesh. It uses SkeletalMesh.PhysicsAsset, but if you'd like to override use this function

Args:
    new_physics_asset (PhysicsAsset): New PhysicsAsset
    force_re_init (bool): Force reinitialize

<a id="unreal.SkinnedMeshComponent.set_min_lod"></a>

#### set_min_lod

```python
def set_min_lod(new_min_lod: int) -> None
```

x.set_min_lod(new_min_lod) -> None
Set Min LOD
deprecated: Use USkinnedMeshComponent::OverrideMinLOD() instead.

Args:
    new_min_lod (int32):

<a id="unreal.SkinnedMeshComponent.set_mesh_deformer"></a>

#### set_mesh_deformer

```python
def set_mesh_deformer(mesh_deformer: MeshDeformer) -> None
```

x.set_mesh_deformer(mesh_deformer) -> None
Change the MeshDeformer that is used for this Component.

Args:
    mesh_deformer (MeshDeformer): New mesh deformer to set for this component

<a id="unreal.SkinnedMeshComponent.set_leader_pose_component"></a>

#### set_leader_pose_component

```python
def set_leader_pose_component(new_leader_bone_component: SkinnedMeshComponent,
                              force_update: bool = False,
                              follower_should_tick_pose: bool = False) -> None
```

x.set_leader_pose_component(new_leader_bone_component, force_update=False, follower_should_tick_pose=False) -> None
Set LeaderPoseComponent for this component

Args:
    new_leader_bone_component (SkinnedMeshComponent): New LeaderPoseComponent
    force_update (bool): If false, the function will be skipped if NewLeaderBoneComponent is the same as currently setup (default)
    follower_should_tick_pose (bool): If false, Follower components will not execute TickPose (default)

<a id="unreal.SkinnedMeshComponent.set_master_pose_component"></a>

#### set_master_pose_component

```python
def set_master_pose_component(new_leader_bone_component: SkinnedMeshComponent,
                              force_update: bool = False,
                              follower_should_tick_pose: bool = False) -> None
```

deprecated: 'set_master_pose_component' was renamed to 'set_leader_pose_component'.

<a id="unreal.SkinnedMeshComponent.set_forced_lod"></a>

#### set_forced_lod

```python
def set_forced_lod(new_forced_lod: int) -> None
```

x.set_forced_lod(new_forced_lod) -> None
Set ForcedLodModel of the mesh component

Args:
    new_forced_lod (int32): Set new ForcedLODModel that forces to set the incoming LOD. Range from [1, Max Number of LOD]. This will affect in the next tick update.

<a id="unreal.SkinnedMeshComponent.set_cast_capsule_indirect_shadow"></a>

#### set_cast_capsule_indirect_shadow

```python
def set_cast_capsule_indirect_shadow(new_value: bool) -> None
```

x.set_cast_capsule_indirect_shadow(new_value) -> None
Set Cast Capsule Indirect Shadow

Args:
    new_value (bool):

<a id="unreal.SkinnedMeshComponent.set_cast_capsule_direct_shadow"></a>

#### set_cast_capsule_direct_shadow

```python
def set_cast_capsule_direct_shadow(new_value: bool) -> None
```

x.set_cast_capsule_direct_shadow(new_value) -> None
Set Cast Capsule Direct Shadow

Args:
    new_value (bool):

<a id="unreal.SkinnedMeshComponent.set_capsule_indirect_shadow_min_visibility"></a>

#### set_capsule_indirect_shadow_min_visibility

```python
def set_capsule_indirect_shadow_min_visibility(new_value: float) -> None
```

x.set_capsule_indirect_shadow_min_visibility(new_value) -> None
Set Capsule Indirect Shadow Min Visibility

Args:
    new_value (float):

<a id="unreal.SkinnedMeshComponent.set_always_use_mesh_deformer"></a>

#### set_always_use_mesh_deformer

```python
def set_always_use_mesh_deformer(
        should_always_use_mesh_deformer: bool) -> None
```

x.set_always_use_mesh_deformer(should_always_use_mesh_deformer) -> None
Always use a MeshDeformer as long as one can be found in the project settings

Args:
    should_always_use_mesh_deformer (bool): Always use mesh deformer for this component

<a id="unreal.SkinnedMeshComponent.override_min_lod"></a>

#### override_min_lod

```python
def override_min_lod(new_min_lod: int) -> None
```

x.override_min_lod(new_min_lod) -> None
Override the Min LOD of the mesh component

Args:
    new_min_lod (int32): Override new MinLodModel that make sure the LOD does not go below of this value. Range from [0, Max Number of LOD - 1]. This will affect in the next tick update.

<a id="unreal.SkinnedMeshComponent.is_using_skin_weight_profile"></a>

#### is_using_skin_weight_profile

```python
def is_using_skin_weight_profile() -> bool
```

x.is_using_skin_weight_profile() -> bool
Check whether a skin weight profile is currently set on any layer.

Returns:
    bool:

<a id="unreal.SkinnedMeshComponent.is_material_section_shown"></a>

#### is_material_section_shown

```python
def is_material_section_shown(material_id: int, lod_index: int) -> bool
```

x.is_material_section_shown(material_id, lod_index) -> bool
Returns whether a specific material section is currently hidden on this component (by using ShowMaterialSection)

Args:
    material_id (int32): 
    lod_index (int32): 

Returns:
    bool:

<a id="unreal.SkinnedMeshComponent.is_bone_hidden_by_name"></a>

#### is_bone_hidden_by_name

```python
def is_bone_hidden_by_name(bone_name: Name) -> bool
```

x.is_bone_hidden_by_name(bone_name) -> bool
Determines if the specified bone is hidden.

Args:
    bone_name (Name): Name of bone to check

Returns:
    bool: true if hidden

<a id="unreal.SkinnedMeshComponent.hide_bone_by_name"></a>

#### hide_bone_by_name

```python
def hide_bone_by_name(bone_name: Name, phys_body_option: PhysBodyOp) -> None
```

x.hide_bone_by_name(bone_name, phys_body_option) -> None
Hides the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
Compared to HideBone By Index - This keeps track of list of bones and update when LOD changes

Args:
    bone_name (Name): Name of bone to hide
    phys_body_option (PhysBodyOp): Option for physics bodies that attach to the bones to be hidden

<a id="unreal.SkinnedMeshComponent.get_twist_and_swing_angle_of_delta_rotation_from_ref_pose"></a>

#### get_twist_and_swing_angle_of_delta_rotation_from_ref_pose

```python
def get_twist_and_swing_angle_of_delta_rotation_from_ref_pose(
        bone_name: Name) -> Optional[Tuple[float, float]]
```

x.get_twist_and_swing_angle_of_delta_rotation_from_ref_pose(bone_name) -> (out_twist_angle=float, out_swing_angle=float) or None
Get Twist and Swing Angle in Degree of Delta Rotation from Reference Pose in Local space

First this function gets rotation of current, and rotation of ref pose in local space, and
And gets twist/swing angle value from refpose aligned.

Args:
    bone_name (Name): Name of the bone

Returns:
    tuple or None: true if succeed. False otherwise. Often due to incorrect bone name.

    out_twist_angle (float): TwistAngle in degree

    out_swing_angle (float): SwingAngle in degree

<a id="unreal.SkinnedMeshComponent.get_socket_bone_name"></a>

#### get_socket_bone_name

```python
def get_socket_bone_name(socket_name: Name) -> Name
```

x.get_socket_bone_name(socket_name) -> Name
Returns bone name linked to a given named socket on the skeletal mesh component.
If you're unsure to deal with sockets or bones names, you can use this function to filter through, and always return the bone name.

Args:
    socket_name (Name): 

Returns:
    Name: bone name

<a id="unreal.SkinnedMeshComponent.get_skinned_asset"></a>

#### get_skinned_asset

```python
def get_skinned_asset() -> SkinnedAsset
```

x.get_skinned_asset() -> SkinnedAsset
Get the SkinnedAsset rendered for this mesh.

Returns:
    SkinnedAsset: the SkinnedAsset set to this mesh.

<a id="unreal.SkinnedMeshComponent.get_skeletal_mesh_deprecated"></a>

#### get_skeletal_mesh_deprecated

```python
def get_skeletal_mesh_deprecated() -> SkeletalMesh
```

x.get_skeletal_mesh_deprecated() -> SkeletalMesh
Get Skeletal Mesh DEPRECATED
deprecated: Use USkeletalMeshComponent::GetSkeletalMeshAsset() or GetSkinnedAsset() instead.

Returns:
    SkeletalMesh:

<a id="unreal.SkinnedMeshComponent.get_ref_pose_transform"></a>

#### get_ref_pose_transform

```python
def get_ref_pose_transform(bone_index: int) -> Transform
```

x.get_ref_pose_transform(bone_index) -> Transform
Gets the local-space transform of a bone in the reference pose.

Args:
    bone_index (int32): Index of the bone

Returns:
    Transform: Local space reference transform

<a id="unreal.SkinnedMeshComponent.get_ref_pose_position"></a>

#### get_ref_pose_position

```python
def get_ref_pose_position(bone_index: int) -> Vector
```

x.get_ref_pose_position(bone_index) -> Vector
Gets the local-space position of a bone in the reference pose.

Args:
    bone_index (int32): Index of the bone

Returns:
    Vector: Local space reference position

<a id="unreal.SkinnedMeshComponent.get_predicted_lod_level"></a>

#### get_predicted_lod_level

```python
def get_predicted_lod_level() -> int
```

x.get_predicted_lod_level() -> int32
Get predicted LOD level. This value is usually calculated in UpdateLODStatus, but can be modified by skeletal mesh streaming.

Returns:
    int32:

<a id="unreal.SkinnedMeshComponent.get_parent_bone"></a>

#### get_parent_bone

```python
def get_parent_bone(bone_name: Name) -> Name
```

x.get_parent_bone(bone_name) -> Name
Get Parent Bone of the input bone

Args:
    bone_name (Name): Name of the bone

Returns:
    Name: the name of the parent bone for the specified bone. Returns 'None' if the bone does not exist or it is the root bone

<a id="unreal.SkinnedMeshComponent.get_num_lo_ds"></a>

#### get_num_lo_ds

```python
def get_num_lo_ds() -> int
```

x.get_num_lo_ds() -> int32
Get the number of LODs on this component

Returns:
    int32:

<a id="unreal.SkinnedMeshComponent.get_num_bones"></a>

#### get_num_bones

```python
def get_num_bones() -> int
```

x.get_num_bones() -> int32
Returns the number of bones in the skeleton.

Returns:
    int32:

<a id="unreal.SkinnedMeshComponent.get_mesh_deformer_instance"></a>

#### get_mesh_deformer_instance

```python
def get_mesh_deformer_instance() -> MeshDeformerInstance
```

x.get_mesh_deformer_instance() -> MeshDeformerInstance
Get Mesh Deformer Instance

Returns:
    MeshDeformerInstance:

<a id="unreal.SkinnedMeshComponent.get_forced_lod"></a>

#### get_forced_lod

```python
def get_forced_lod() -> int
```

x.get_forced_lod() -> int32
Get ForcedLodModel of the mesh component. Note that the actual forced LOD level is the return value minus one and zero means no forced LOD

Returns:
    int32:

<a id="unreal.SkinnedMeshComponent.get_delta_transform_from_ref_pose"></a>

#### get_delta_transform_from_ref_pose

```python
def get_delta_transform_from_ref_pose(bone_name: Name,
                                      base_name: Name = "None") -> Transform
```

x.get_delta_transform_from_ref_pose(bone_name, base_name="None") -> Transform
Get delta transform from reference pose based on BaseNode.
This uses last frame up-to-date transform, so it will have a frame delay if you use this info in the AnimGraph

Args:
    bone_name (Name): Name of the bone
    base_name (Name): Name of the base bone - if none, it will use parent as a base

Returns:
    Transform: the delta transform from refpose in that given space (BaseName)

<a id="unreal.SkinnedMeshComponent.get_current_skin_weight_profile_name"></a>

#### get_current_skin_weight_profile_name

```python
def get_current_skin_weight_profile_name(
        layer: SkinWeightProfileLayer = SkinWeightProfileLayer.PRIMARY
) -> Name
```

x.get_current_skin_weight_profile_name(layer=SkinWeightProfileLayer.PRIMARY) -> Name
Return the name of the skin weight profile that is currently set on the given layer, otherwise returns 'None'

Args:
    layer (SkinWeightProfileLayer): 

Returns:
    Name:

<a id="unreal.SkinnedMeshComponent.get_current_skin_weight_profile_layer_names"></a>

#### get_current_skin_weight_profile_layer_names

```python
def get_current_skin_weight_profile_layer_names() -> Array[Name]
```

x.get_current_skin_weight_profile_layer_names() -> Array[Name]
Return the names of the skin weight profiles for all the layers

Returns:
    Array[Name]:

<a id="unreal.SkinnedMeshComponent.get_bone_transform"></a>

#### get_bone_transform

```python
def get_bone_transform(
    bone_name: Name,
    transform_space: RelativeTransformSpace = RelativeTransformSpace.RTS_WORLD
) -> Transform
```

x.get_bone_transform(bone_name, transform_space=RelativeTransformSpace.RTS_WORLD) -> Transform
Get world-space bone transform.

Args:
    bone_name (Name): Name of the the bone to get the transform
    transform_space (RelativeTransformSpace): 

Returns:
    Transform: Bone transform in world space if bone is found. Otherwise it will return component's transform in world space.

<a id="unreal.SkinnedMeshComponent.get_bone_name"></a>

#### get_bone_name

```python
def get_bone_name(bone_index: int) -> Name
```

x.get_bone_name(bone_index) -> Name
Get Bone Name from index

Args:
    bone_index (int32): Index of the bone

Returns:
    Name: the name of the bone at the specified index

<a id="unreal.SkinnedMeshComponent.get_bone_index"></a>

#### get_bone_index

```python
def get_bone_index(bone_name: Name) -> int
```

x.get_bone_index(bone_name) -> int32
Find the index of bone by name. Looks in the current SkeletalMesh being used by this SkeletalMeshComponent.
see: USkeletalMesh::GetBoneIndex.

Args:
    bone_name (Name): Name of bone to look up

Returns:
    int32: Index of the named bone in the current SkeletalMesh. Will return INDEX_NONE if bone not found.

<a id="unreal.SkinnedMeshComponent.match_ref_bone"></a>

#### match_ref_bone

```python
def match_ref_bone(bone_name: Name) -> int
```

deprecated: 'match_ref_bone' was renamed to 'get_bone_index'.

<a id="unreal.SkinnedMeshComponent.get_always_use_mesh_deformer"></a>

#### get_always_use_mesh_deformer

```python
def get_always_use_mesh_deformer() -> bool
```

x.get_always_use_mesh_deformer() -> bool
Returns whether the component is set to always use a mesh deformer if one can be found in the project settings

Returns:
    bool:

<a id="unreal.SkinnedMeshComponent.find_closest_bone_k2"></a>

#### find_closest_bone_k2

```python
def find_closest_bone_k2(
        test_location: Vector,
        ignore_scale: float = 0.000000,
        require_physics_asset: bool = False) -> Tuple[Name, Vector]
```

x.find_closest_bone_k2(test_location, ignore_scale=0.000000, require_physics_asset=False) -> (Name, bone_location=Vector)
finds the closest bone to the given location

Args:
    test_location (Vector): the location to test against
    ignore_scale (float): (optional) if specified, only bones with scaling larger than the specified factor are considered
    require_physics_asset (bool): (optional) if true, only bones with physics will be considered

Returns:
    Vector: the name of the bone that was found, or 'None' if no bone was found

    bone_location (Vector): (optional, out) if specified, set to the world space location of the bone that was found, or (0,0,0) if no bone was found

<a id="unreal.SkinnedMeshComponent.clear_vertex_color_override"></a>

#### clear_vertex_color_override

```python
def clear_vertex_color_override(lod_index: int) -> None
```

x.clear_vertex_color_override(lod_index) -> None
Clear any applied vertex color override

Args:
    lod_index (int32):

<a id="unreal.SkinnedMeshComponent.clear_skin_weight_profile"></a>

#### clear_skin_weight_profile

```python
def clear_skin_weight_profile(
        layer: SkinWeightProfileLayer = SkinWeightProfileLayer.PRIMARY
) -> None
```

x.clear_skin_weight_profile(layer=SkinWeightProfileLayer.PRIMARY) -> None
Clear the skin weight profile from the given layer on this component, in case it is set. If no profile is set for the layer,
then this call does nothing.

Args:
    layer (SkinWeightProfileLayer):

<a id="unreal.SkinnedMeshComponent.clear_skin_weight_override"></a>

#### clear_skin_weight_override

```python
def clear_skin_weight_override(lod_index: int) -> None
```

x.clear_skin_weight_override(lod_index) -> None
Clear any applied skin weight override

Args:
    lod_index (int32):

<a id="unreal.SkinnedMeshComponent.clear_all_skin_weight_profiles"></a>

#### clear_all_skin_weight_profiles

```python
def clear_all_skin_weight_profiles() -> None
```

x.clear_all_skin_weight_profiles() -> None
Clear the skin Weight Profile from all layers on this component. If no profiles are set for any layer, then this call does nothing.

<a id="unreal.SkinnedMeshComponent.bone_is_child_of"></a>

#### bone_is_child_of

```python
def bone_is_child_of(bone_name: Name, parent_bone_name: Name) -> bool
```

x.bone_is_child_of(bone_name, parent_bone_name) -> bool
Tests if BoneName is child of (or equal to) ParentBoneName.

Args:
    bone_name (Name): Name of the bone
    parent_bone_name (Name): 

Returns:
    bool: true if child (strictly, not same). false otherwise Note - will return false if ChildBoneIndex is the same as ParentBoneIndex ie. must be strictly a child.

<a id="unreal.SkeletalMeshComponent"></a>