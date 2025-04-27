## SkeletalMeshComponent Objects

```python
class SkeletalMeshComponent(SkinnedMeshComponent)
```

SkeletalMeshComponent is used to create an instance of an animated SkeletalMesh asset.
see: https://docs.unrealengine.com/latest/INT/Engine/Content/Types/SkeletalMeshes/
see: USkeletalMesh

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_anim_curve_evaluation`` (bool):  [Read-Write] Disable animation curves for this component. If this is set true, no curves will be processed
- ``allow_cloth_actors`` (bool):  [Read-Write] Toggles creation of cloth simulation. Distinct from the simulation toggle below in that, if off, avoids allocating
  the actors entirely instead of just skipping the simulation step.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``always_use_mesh_deformer`` (bool):  [Read-Write] If true, and if no mesh deformer is set from here or the SkeletalMesh, fall back to the default deformer specified in the project settings, unless DefaultMode is set to "Never" in project settings
- ``anim_blueprint_generated_class`` (type(AnimBlueprintGeneratedClass)):  [Read-Write]
- ``anim_class`` (type(Class)):  [Read-Write] The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime.
- ``animation_data`` (SingleAnimationPlayData):  [Read-Write]
- ``animation_mode`` (AnimationMode):  [Read-Write] Whether to use Animation Blueprint or play Single Animation Asset.
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
- ``cloth_blend_weight`` (float):  [Read-Write] weight to blend between simulated results and key-framed positions
  if weight is 1.0, shows only cloth simulation results and 0.0 will show only skinned results
- ``cloth_geometry_scale`` (float):  [Read-Write] This scale is applied to all cloth geometry (e.g., cloth meshes and collisions) in order to simulate in a different scale space than world.This scale is not applied to distance-based simulation parameters such as MaxDistance.
  This property is currently only read by the cloth solver when creating cloth actors, but may become animatable in the future.
- ``cloth_max_distance_scale`` (float):  [Read-Write]
- ``cloth_teleport_mode`` (ClothingTeleportMode):  [Read-Only] whether we need to teleport cloth. // This property is explicitly hidden from the details panel inside FSkeletalMeshComponentDetails::UpdatePhysicsCategory
- ``cloth_velocity_scale`` (float):  [Read-Write] Scale applied to the component induced velocity of all cloth particles prior to stepping the cloth solver.
  Use 1.0 for fully induced velocity (default), or use 0.0 for no induced velocity, and any other values in between for a reduced induced velocity.
  When set to 0.0, it also provides a way to force the clothing to simulate in local space.
  This value multiplies to individual cloth's velocity scale settings, still allowing for differences in behavior between the various pieces of clothing within the same component.
- ``clothing_simulation_factory`` (type(Class)):  [Read-Write] Class of the object responsible for
- ``collide_with_attached_children`` (bool):  [Read-Write] can't collide with part of attached children if total collision volumes exceed 16 capsules or 32 planes per convex
- ``collide_with_environment`` (bool):  [Read-Write] can't collide with part of environment if total collision volumes exceed 16 capsules or 32 planes per convex
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``component_use_fixed_skel_bounds`` (bool):  [Read-Write] When true, skip using the physics asset etc. and always use the fixed bounds defined in the SkeletalMesh.
- ``consider_all_bodies_for_bounds`` (bool):  [Read-Write] If true, when updating bounds from a PhysicsAsset, consider _all_ BodySetups, not just those flagged with bConsiderForBounds.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``default_animating_rig_override`` (Object):  [Read-Write] Default Animating Rig to Use if bOverrideDefaultAnimatingRig is true
- ``defer_kinematic_bone_update`` (bool):  [Read-Write] Whether animation and world transform updates are deferred. If this is on, the kinematic bodies (scene query data) will not update until the next time the physics simulation is run
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``disable_cloth_simulation`` (bool):  [Read-Write] Disable cloth simulation and play original animation without simulation
- ``disable_morph_target`` (bool):  [Read-Write] Disable Morphtarget for this component.
- ``disable_post_process_blueprint`` (bool):  [Read-Write] Controls whether or not this component will evaluate its post process instance. The post-process
  Instance is dictated by the skeletal mesh so this is used for per-instance control.
- ``disable_rigid_body_anim_node`` (bool):  [Read-Write] Disable rigid body animation nodes and play original animation without simulation
- ``display_bones`` (bool):  [Read-Write] Draw the skeleton hierarchy for this skel mesh.
- ``display_debug_update_rate_optimizations`` (bool):  [Read-Write] Enable on screen debugging of update rate optimization.
  Red = Skipping 0 frames, Green = skipping 1 frame, Blue = skipping 2 frames, black = skipping more than 2 frames.
  todo:: turn this into a console command.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_animation`` (bool):  [Read-Write] Whether the built-in animation of this component should run when the component ticks.
  It is assumed that if this is false then some external system will be animating this mesh.
  Note that disabling animation will also cause cloth simulation not to run and the component's tick to run on any thread.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``enable_per_poly_collision`` (bool):  [Read-Write] Uses skinned data for collision data.
- ``enable_physics_on_dedicated_server`` (bool):  [Read-Write] If true, simulate physics for this component on a dedicated server.
  This should be set if simulating physics and replicating with a dedicated server.
      Note: This property cannot be changed at runtime.
- ``enable_update_rate_optimizations`` (bool):  [Read-Write] if TRUE, Owner will determine how often animation will be updated and evaluated. See AnimUpdateRateTick()
  This allows to skip frames for performance. (For example based on visibility and size on screen).
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_collision_update`` (bool):  [Read-Write] Forces the cloth simulation to constantly update its external collisions, at the expense of performance.
  This will help to prevent missed collisions if the cloth's skeletal mesh component isn't moving,
  and when instead, wind or other moving objects are causing new collision shapes to come into the cloth's vicinity.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``forced_lod_model`` (int32):  [Read-Write]
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``global_anim_rate_scale`` (float):  [Read-Write] Used to scale speed of all animations on this skeletal mesh.
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
- ``kinematic_bones_update_type`` (KinematicBonesUpdateToPhysics):  [Read-Write] If we are running physics, should we update non-simulated bones based on the animation bone positions.
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
- ``no_skeleton_update`` (bool):  [Read-Write] Skips Ticking and Bone Refresh.
- ``on_anim_initialized`` (OnAnimInitialized):  [Read-Write] Broadcast when the components anim instance is initialized
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
- ``on_constraint_broken`` (ConstraintBrokenSignature):  [Read-Write] Notification when constraint is broken.
- ``on_end_cursor_over`` (ComponentEndCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller
- ``on_input_touch_begin`` (ComponentOnInputTouchBeginSignature):  [Read-Write] Event called when a touch input is received over this component when touch events are enabled in the player controller
- ``on_input_touch_end`` (ComponentOnInputTouchEndSignature):  [Read-Write] Event called when a touch input is released over this component when touch events are enabled in the player controller
- ``on_input_touch_enter`` (ComponentBeginTouchOverSignature):  [Read-Write] Event called when a finger is moved over this component when touch over events are enabled in the player controller
- ``on_input_touch_leave`` (ComponentEndTouchOverSignature):  [Read-Write] Event called when a finger is moved off this component when touch over events are enabled in the player controller
- ``on_plastic_deformation`` (PlasticDeformationEventSignature):  [Read-Write] Notification when constraint plasticity drive target changes.
- ``on_released`` (ComponentOnReleasedSignature):  [Read-Write] Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``overlay_material`` (MaterialInterface):  [Read-Write] Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material
- ``overlay_material_max_draw_distance`` (float):  [Read-Write] The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance.
- ``override_default_animating_rig`` (bool):  [Read-Write] If true, DefaultAnimatingRigOverride will be used. If false, use the DefaultAnimatingRig in the SkeletalMesh
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
- ``override_min_lod`` (bool):  [Read-Write] Whether we should use the min lod specified in MinLodModel for this component instead of the min lod in the mesh
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``pause_anims`` (bool):  [Read-Write] pauses this component's animations (doesn't tick them, but still refreshes bones)
- ``per_bone_motion_blur`` (bool):  [Read-Write] If true, use per-bone motion blur on this skeletal mesh (requires additional rendering, can be disabled to save performance).
- ``physics_asset_override`` (PhysicsAsset):  [Read-Write] PhysicsAsset is set in SkeletalMesh by default, but you can override with this value
- ``physics_transform_update_mode`` (PhysicsTransformUpdateMode):  [Read-Write] Whether physics simulation updates component transform.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``post_process_anim_bplod_threshold`` (int32):  [Read-Write] * Max LOD level that post-process AnimBPs are evaluated. Overrides the setting of the same name on the skeletal mesh.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the post-process AnimBP.
  * Setting it to -1 will always evaluate it and disable LODing overrides for this component.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``propagate_curves_to_followers`` (bool):  [Read-Write] If true, propagates calls to ApplyAnimationCurvesToComponent for follower components, only needed if follower components do not tick themselves
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
- ``reset_after_teleport`` (bool):  [Read-Write] reset the clothing after moving the clothing position (called teleport)
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
- ``skeletal_mesh_asset`` (SkeletalMesh):  [Read-Write]
- ``skin_cache_usage`` (Array[SkinCacheUsage]):  [Read-Write] How this Component's LOD uses the skin cache feature. Auto will defer to the asset's (SkeletalMesh) option. If Ray Tracing is enabled, will imply Enabled
- ``skinned_asset`` (SkinnedAsset):  [Read-Write]
- ``skip_bounds_update_when_interpolating`` (bool):  [Read-Write] Whether to skip bounds update when interpolating. Bounds are updated to the target interpolation pose only on ticks when they are evaluated.
- ``skip_kinematic_update_when_interpolating`` (bool):  [Read-Write] Whether to skip UpdateKinematicBonesToAnim() when interpolating. Kinematic bones are updated to the target interpolation pose only on ticks when they are evaluated.
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``streaming_distance_multiplier`` (float):  [Read-Write] Allows adjusting the desired streaming distance of streaming textures that uses UV 0.
  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.
  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).
  Value can be < 0 (from legcay content, or code changes)
- ``sync_attach_parent_lod`` (bool):  [Read-Write] If true, this component uses its parents LOD when attached if available
  ForcedLOD can override this change. By default, it will use parent LOD.
- ``teleport_distance_threshold`` (float):  [Read-Write] Conduct teleportation if the character's movement is greater than this threshold in 1 frame.
  Zero or negative values will skip the check.
  You can also do force teleport manually using ForceNextUpdateTeleport() / ForceNextUpdateTeleportAndReset().
- ``teleport_rotation_threshold`` (float):  [Read-Write] Rotation threshold in degrees, ranging from 0 to 180.
  Conduct teleportation if the character's rotation is greater than this threshold in 1 frame.
  Zero or negative values will skip the check.
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
- ``update_animation_in_editor`` (bool):  [Read-Write] If true, this will Tick until disabled
- ``update_cloth_in_editor`` (bool):  [Read-Write] If true, will play cloth in editor
- ``update_joints_from_animation`` (bool):  [Read-Write] If we should pass joint position to joints each frame, so that they can be used by motorized joints to drive the
  ragdoll based on the animation.
- ``update_mesh_when_kinematic`` (bool):  [Read-Write] If true, then the physics bodies will be used to drive the skeletal mesh even when they are
  kinematic (not simulating), otherwise the skeletal mesh will be driven by the animation input
  when the bodies are kinematic
- ``update_overlaps_on_animation_finalize`` (bool):  [Read-Write] Controls whether blending in physics bones will refresh overlaps on this component, defaults to true but can be disabled in cases where we know anim->physics blending doesn't meaningfully change overlaps
- ``use_as_occluder`` (bool):  [Read-Write] Whether to render the primitive in the depth only pass.
  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
  todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_bounds_from_leader_pose_component`` (bool):  [Read-Write] When true, we will just using the bounds from our LeaderPoseComponent.  This is useful for when we have a Mesh Parented
  to the main SkelMesh (e.g. outline mesh or a full body overdraw effect that is toggled) that is always going to be the same
  bounds as parent.  We want to do no calculations in that case.
- ``use_ref_pose_on_init_anim`` (bool):  [Read-Write] On InitAnim should we set to ref pose (if false use first tick of animation data). If enabled, takes precedence over UAnimationSettings::bTickAnimationOnSkeletalMeshInit
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
- ``wait_for_parallel_cloth_task`` (bool):  [Read-Write] Whether we should stall the Cloth tick task until the cloth simulation is complete. This is required if we want up-to-date
  cloth data on the game thread, for example if we want to generate particles at cloth vertices.

<a id="unreal.SkeletalMeshComponent.skeletal_mesh_asset"></a>

#### skeletal_mesh_asset

```python
@property
def skeletal_mesh_asset() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write]

<a id="unreal.SkeletalMeshComponent.skeletal_mesh_asset"></a>

#### skeletal_mesh_asset

```python
@skeletal_mesh_asset.setter
def skeletal_mesh_asset(value: SkeletalMesh) -> None
```

<a id="unreal.SkeletalMeshComponent.anim_blueprint_generated_class"></a>

#### anim_blueprint_generated_class

```python
@property
def anim_blueprint_generated_class() -> AnimBlueprintGeneratedClass
```

(type(AnimBlueprintGeneratedClass)):  [Read-Only]

<a id="unreal.SkeletalMeshComponent.animation_blueprint"></a>

#### animation_blueprint

```python
@property
def animation_blueprint() -> AnimBlueprintGeneratedClass
```

deprecated: 'animation_blueprint' was renamed to 'anim_blueprint_generated_class'.

<a id="unreal.SkeletalMeshComponent.anim_class"></a>

#### anim_class

```python
@property
def anim_class() -> Class
```

(type(Class)):  [Read-Only] The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime.

<a id="unreal.SkeletalMeshComponent.animation_data"></a>

#### animation_data

```python
@property
def animation_data() -> SingleAnimationPlayData
```

(SingleAnimationPlayData):  [Read-Write]

<a id="unreal.SkeletalMeshComponent.animation_data"></a>

#### animation_data

```python
@animation_data.setter
def animation_data(value: SingleAnimationPlayData) -> None
```

<a id="unreal.SkeletalMeshComponent.global_anim_rate_scale"></a>

#### global_anim_rate_scale

```python
@property
def global_anim_rate_scale() -> float
```

(float):  [Read-Write] Used to scale speed of all animations on this skeletal mesh.

<a id="unreal.SkeletalMeshComponent.global_anim_rate_scale"></a>

#### global_anim_rate_scale

```python
@global_anim_rate_scale.setter
def global_anim_rate_scale(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.kinematic_bones_update_type"></a>

#### kinematic_bones_update_type

```python
@property
def kinematic_bones_update_type() -> KinematicBonesUpdateToPhysics
```

(KinematicBonesUpdateToPhysics):  [Read-Write] If we are running physics, should we update non-simulated bones based on the animation bone positions.

<a id="unreal.SkeletalMeshComponent.kinematic_bones_update_type"></a>

#### kinematic_bones_update_type

```python
@kinematic_bones_update_type.setter
def kinematic_bones_update_type(value: KinematicBonesUpdateToPhysics) -> None
```

<a id="unreal.SkeletalMeshComponent.physics_transform_update_mode"></a>

#### physics_transform_update_mode

```python
@property
def physics_transform_update_mode() -> PhysicsTransformUpdateMode
```

(PhysicsTransformUpdateMode):  [Read-Write] Whether physics simulation updates component transform.

<a id="unreal.SkeletalMeshComponent.physics_transform_update_mode"></a>

#### physics_transform_update_mode

```python
@physics_transform_update_mode.setter
def physics_transform_update_mode(value: PhysicsTransformUpdateMode) -> None
```

<a id="unreal.SkeletalMeshComponent.cloth_teleport_mode"></a>

#### cloth_teleport_mode

```python
@property
def cloth_teleport_mode() -> ClothingTeleportMode
```

(ClothingTeleportMode):  [Read-Only] whether we need to teleport cloth. // This property is explicitly hidden from the details panel inside FSkeletalMeshComponentDetails::UpdatePhysicsCategory

<a id="unreal.SkeletalMeshComponent.animation_mode"></a>

#### animation_mode

```python
@property
def animation_mode() -> AnimationMode
```

(AnimationMode):  [Read-Only] Whether to use Animation Blueprint or play Single Animation Asset.

<a id="unreal.SkeletalMeshComponent.disable_post_process_blueprint"></a>

#### disable_post_process_blueprint

```python
@property
def disable_post_process_blueprint() -> bool
```

(bool):  [Read-Write] Controls whether or not this component will evaluate its post process instance. The post-process
Instance is dictated by the skeletal mesh so this is used for per-instance control.

<a id="unreal.SkeletalMeshComponent.disable_post_process_blueprint"></a>

#### disable_post_process_blueprint

```python
@disable_post_process_blueprint.setter
def disable_post_process_blueprint(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.enable_physics_on_dedicated_server"></a>

#### enable_physics_on_dedicated_server

```python
@property
def enable_physics_on_dedicated_server() -> bool
```

(bool):  [Read-Write] If true, simulate physics for this component on a dedicated server.
This should be set if simulating physics and replicating with a dedicated server.
    Note: This property cannot be changed at runtime.

<a id="unreal.SkeletalMeshComponent.enable_physics_on_dedicated_server"></a>

#### enable_physics_on_dedicated_server

```python
@enable_physics_on_dedicated_server.setter
def enable_physics_on_dedicated_server(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.update_mesh_when_kinematic"></a>

#### update_mesh_when_kinematic

```python
@property
def update_mesh_when_kinematic() -> bool
```

(bool):  [Read-Write] If true, then the physics bodies will be used to drive the skeletal mesh even when they are
kinematic (not simulating), otherwise the skeletal mesh will be driven by the animation input
when the bodies are kinematic

<a id="unreal.SkeletalMeshComponent.update_mesh_when_kinematic"></a>

#### update_mesh_when_kinematic

```python
@update_mesh_when_kinematic.setter
def update_mesh_when_kinematic(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.update_joints_from_animation"></a>

#### update_joints_from_animation

```python
@property
def update_joints_from_animation() -> bool
```

(bool):  [Read-Write] If we should pass joint position to joints each frame, so that they can be used by motorized joints to drive the
ragdoll based on the animation.

<a id="unreal.SkeletalMeshComponent.update_joints_from_animation"></a>

#### update_joints_from_animation

```python
@update_joints_from_animation.setter
def update_joints_from_animation(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.allow_cloth_actors"></a>

#### allow_cloth_actors

```python
@property
def allow_cloth_actors() -> bool
```

(bool):  [Read-Write] Toggles creation of cloth simulation. Distinct from the simulation toggle below in that, if off, avoids allocating
the actors entirely instead of just skipping the simulation step.

<a id="unreal.SkeletalMeshComponent.allow_cloth_actors"></a>

#### allow_cloth_actors

```python
@allow_cloth_actors.setter
def allow_cloth_actors(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.disable_cloth_simulation"></a>

#### disable_cloth_simulation

```python
@property
def disable_cloth_simulation() -> bool
```

(bool):  [Read-Write] Disable cloth simulation and play original animation without simulation

<a id="unreal.SkeletalMeshComponent.disable_cloth_simulation"></a>

#### disable_cloth_simulation

```python
@disable_cloth_simulation.setter
def disable_cloth_simulation(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.collide_with_environment"></a>

#### collide_with_environment

```python
@property
def collide_with_environment() -> bool
```

(bool):  [Read-Write] can't collide with part of environment if total collision volumes exceed 16 capsules or 32 planes per convex

<a id="unreal.SkeletalMeshComponent.collide_with_environment"></a>

#### collide_with_environment

```python
@collide_with_environment.setter
def collide_with_environment(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.collide_with_attached_children"></a>

#### collide_with_attached_children

```python
@property
def collide_with_attached_children() -> bool
```

(bool):  [Read-Write] can't collide with part of attached children if total collision volumes exceed 16 capsules or 32 planes per convex

<a id="unreal.SkeletalMeshComponent.collide_with_attached_children"></a>

#### collide_with_attached_children

```python
@collide_with_attached_children.setter
def collide_with_attached_children(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.force_collision_update"></a>

#### force_collision_update

```python
@property
def force_collision_update() -> bool
```

(bool):  [Read-Write] Forces the cloth simulation to constantly update its external collisions, at the expense of performance.
This will help to prevent missed collisions if the cloth's skeletal mesh component isn't moving,
and when instead, wind or other moving objects are causing new collision shapes to come into the cloth's vicinity.

<a id="unreal.SkeletalMeshComponent.force_collision_update"></a>

#### force_collision_update

```python
@force_collision_update.setter
def force_collision_update(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.cloth_velocity_scale"></a>

#### cloth_velocity_scale

```python
@property
def cloth_velocity_scale() -> float
```

(float):  [Read-Write] Scale applied to the component induced velocity of all cloth particles prior to stepping the cloth solver.
Use 1.0 for fully induced velocity (default), or use 0.0 for no induced velocity, and any other values in between for a reduced induced velocity.
When set to 0.0, it also provides a way to force the clothing to simulate in local space.
This value multiplies to individual cloth's velocity scale settings, still allowing for differences in behavior between the various pieces of clothing within the same component.

<a id="unreal.SkeletalMeshComponent.cloth_velocity_scale"></a>

#### cloth_velocity_scale

```python
@cloth_velocity_scale.setter
def cloth_velocity_scale(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.reset_after_teleport"></a>

#### reset_after_teleport

```python
@property
def reset_after_teleport() -> bool
```

(bool):  [Read-Write] reset the clothing after moving the clothing position (called teleport)

<a id="unreal.SkeletalMeshComponent.reset_after_teleport"></a>

#### reset_after_teleport

```python
@reset_after_teleport.setter
def reset_after_teleport(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.defer_kinematic_bone_update"></a>

#### defer_kinematic_bone_update

```python
@property
def defer_kinematic_bone_update() -> bool
```

(bool):  [Read-Only] Whether animation and world transform updates are deferred. If this is on, the kinematic bodies (scene query data) will not update until the next time the physics simulation is run

<a id="unreal.SkeletalMeshComponent.no_skeleton_update"></a>

#### no_skeleton_update

```python
@property
def no_skeleton_update() -> bool
```

(bool):  [Read-Write] Skips Ticking and Bone Refresh.

<a id="unreal.SkeletalMeshComponent.no_skeleton_update"></a>

#### no_skeleton_update

```python
@no_skeleton_update.setter
def no_skeleton_update(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.pause_anims"></a>

#### pause_anims

```python
@property
def pause_anims() -> bool
```

(bool):  [Read-Write] pauses this component's animations (doesn't tick them, but still refreshes bones)

<a id="unreal.SkeletalMeshComponent.pause_anims"></a>

#### pause_anims

```python
@pause_anims.setter
def pause_anims(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.enable_animation"></a>

#### enable_animation

```python
@property
def enable_animation() -> bool
```

(bool):  [Read-Only] Whether the built-in animation of this component should run when the component ticks.
It is assumed that if this is false then some external system will be animating this mesh.
Note that disabling animation will also cause cloth simulation not to run and the component's tick to run on any thread.

<a id="unreal.SkeletalMeshComponent.enable_per_poly_collision"></a>

#### enable_per_poly_collision

```python
@property
def enable_per_poly_collision() -> bool
```

(bool):  [Read-Only] Uses skinned data for collision data.

<a id="unreal.SkeletalMeshComponent.propagate_curves_to_followers"></a>

#### propagate_curves_to_followers

```python
@property
def propagate_curves_to_followers() -> bool
```

(bool):  [Read-Write] If true, propagates calls to ApplyAnimationCurvesToComponent for follower components, only needed if follower components do not tick themselves

<a id="unreal.SkeletalMeshComponent.propagate_curves_to_followers"></a>

#### propagate_curves_to_followers

```python
@propagate_curves_to_followers.setter
def propagate_curves_to_followers(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.b_propagate_curves_to_slaves"></a>

#### b_propagate_curves_to_slaves

```python
@property
def b_propagate_curves_to_slaves() -> bool
```

deprecated: 'b_propagate_curves_to_slaves' was renamed to 'propagate_curves_to_followers'.

<a id="unreal.SkeletalMeshComponent.b_propagate_curves_to_slaves"></a>

#### b_propagate_curves_to_slaves

```python
@b_propagate_curves_to_slaves.setter
def b_propagate_curves_to_slaves(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.skip_kinematic_update_when_interpolating"></a>

#### skip_kinematic_update_when_interpolating

```python
@property
def skip_kinematic_update_when_interpolating() -> bool
```

(bool):  [Read-Write] Whether to skip UpdateKinematicBonesToAnim() when interpolating. Kinematic bones are updated to the target interpolation pose only on ticks when they are evaluated.

<a id="unreal.SkeletalMeshComponent.skip_kinematic_update_when_interpolating"></a>

#### skip_kinematic_update_when_interpolating

```python
@skip_kinematic_update_when_interpolating.setter
def skip_kinematic_update_when_interpolating(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.skip_bounds_update_when_interpolating"></a>

#### skip_bounds_update_when_interpolating

```python
@property
def skip_bounds_update_when_interpolating() -> bool
```

(bool):  [Read-Write] Whether to skip bounds update when interpolating. Bounds are updated to the target interpolation pose only on ticks when they are evaluated.

<a id="unreal.SkeletalMeshComponent.skip_bounds_update_when_interpolating"></a>

#### skip_bounds_update_when_interpolating

```python
@skip_bounds_update_when_interpolating.setter
def skip_bounds_update_when_interpolating(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.cloth_blend_weight"></a>

#### cloth_blend_weight

```python
@property
def cloth_blend_weight() -> float
```

(float):  [Read-Write] weight to blend between simulated results and key-framed positions
if weight is 1.0, shows only cloth simulation results and 0.0 will show only skinned results

<a id="unreal.SkeletalMeshComponent.cloth_blend_weight"></a>

#### cloth_blend_weight

```python
@cloth_blend_weight.setter
def cloth_blend_weight(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.wait_for_parallel_cloth_task"></a>

#### wait_for_parallel_cloth_task

```python
@property
def wait_for_parallel_cloth_task() -> bool
```

(bool):  [Read-Write] Whether we should stall the Cloth tick task until the cloth simulation is complete. This is required if we want up-to-date
cloth data on the game thread, for example if we want to generate particles at cloth vertices.

<a id="unreal.SkeletalMeshComponent.wait_for_parallel_cloth_task"></a>

#### wait_for_parallel_cloth_task

```python
@wait_for_parallel_cloth_task.setter
def wait_for_parallel_cloth_task(value: bool) -> None
```

<a id="unreal.SkeletalMeshComponent.cloth_max_distance_scale"></a>

#### cloth_max_distance_scale

```python
@property
def cloth_max_distance_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.SkeletalMeshComponent.cloth_max_distance_scale"></a>

#### cloth_max_distance_scale

```python
@cloth_max_distance_scale.setter
def cloth_max_distance_scale(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.cloth_geometry_scale"></a>

#### cloth_geometry_scale

```python
@property
def cloth_geometry_scale() -> float
```

(float):  [Read-Write] This scale is applied to all cloth geometry (e.g., cloth meshes and collisions) in order to simulate in a different scale space than world.This scale is not applied to distance-based simulation parameters such as MaxDistance.
This property is currently only read by the cloth solver when creating cloth actors, but may become animatable in the future.

<a id="unreal.SkeletalMeshComponent.cloth_geometry_scale"></a>

#### cloth_geometry_scale

```python
@cloth_geometry_scale.setter
def cloth_geometry_scale(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.post_process_anim_bplod_threshold"></a>

#### post_process_anim_bplod_threshold

```python
@property
def post_process_anim_bplod_threshold() -> int
```

(int32):  [Read-Write] * Max LOD level that post-process AnimBPs are evaluated. Overrides the setting of the same name on the skeletal mesh.
* For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the post-process AnimBP.
* Setting it to -1 will always evaluate it and disable LODing overrides for this component.

<a id="unreal.SkeletalMeshComponent.post_process_anim_bplod_threshold"></a>

#### post_process_anim_bplod_threshold

```python
@post_process_anim_bplod_threshold.setter
def post_process_anim_bplod_threshold(value: int) -> None
```

<a id="unreal.SkeletalMeshComponent.on_constraint_broken"></a>

#### on_constraint_broken

```python
@property
def on_constraint_broken() -> ConstraintBrokenSignature
```

(ConstraintBrokenSignature):  [Read-Write] Notification when constraint is broken.

<a id="unreal.SkeletalMeshComponent.on_constraint_broken"></a>

#### on_constraint_broken

```python
@on_constraint_broken.setter
def on_constraint_broken(value: ConstraintBrokenSignature) -> None
```

<a id="unreal.SkeletalMeshComponent.on_plastic_deformation"></a>

#### on_plastic_deformation

```python
@property
def on_plastic_deformation() -> PlasticDeformationEventSignature
```

(PlasticDeformationEventSignature):  [Read-Write] Notification when constraint plasticity drive target changes.

<a id="unreal.SkeletalMeshComponent.on_plastic_deformation"></a>

#### on_plastic_deformation

```python
@on_plastic_deformation.setter
def on_plastic_deformation(value: PlasticDeformationEventSignature) -> None
```

<a id="unreal.SkeletalMeshComponent.teleport_distance_threshold"></a>

#### teleport_distance_threshold

```python
@property
def teleport_distance_threshold() -> float
```

(float):  [Read-Write] Conduct teleportation if the character's movement is greater than this threshold in 1 frame.
Zero or negative values will skip the check.
You can also do force teleport manually using ForceNextUpdateTeleport() / ForceNextUpdateTeleportAndReset().

<a id="unreal.SkeletalMeshComponent.teleport_distance_threshold"></a>

#### teleport_distance_threshold

```python
@teleport_distance_threshold.setter
def teleport_distance_threshold(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.teleport_rotation_threshold"></a>

#### teleport_rotation_threshold

```python
@property
def teleport_rotation_threshold() -> float
```

(float):  [Read-Write] Rotation threshold in degrees, ranging from 0 to 180.
Conduct teleportation if the character's rotation is greater than this threshold in 1 frame.
Zero or negative values will skip the check.

<a id="unreal.SkeletalMeshComponent.teleport_rotation_threshold"></a>

#### teleport_rotation_threshold

```python
@teleport_rotation_threshold.setter
def teleport_rotation_threshold(value: float) -> None
```

<a id="unreal.SkeletalMeshComponent.on_anim_initialized"></a>

#### on_anim_initialized

```python
@property
def on_anim_initialized() -> OnAnimInitialized
```

(OnAnimInitialized):  [Read-Write] Broadcast when the components anim instance is initialized

<a id="unreal.SkeletalMeshComponent.on_anim_initialized"></a>

#### on_anim_initialized

```python
@on_anim_initialized.setter
def on_anim_initialized(value: OnAnimInitialized) -> None
```

<a id="unreal.SkeletalMeshComponent.default_animating_rig_override"></a>

#### default_animating_rig_override

```python
@property
def default_animating_rig_override() -> Object
```

(Object):  [Read-Write] Default Animating Rig to Use if bOverrideDefaultAnimatingRig is true

<a id="unreal.SkeletalMeshComponent.default_animating_rig_override"></a>

#### default_animating_rig_override

```python
@default_animating_rig_override.setter
def default_animating_rig_override(value: Object) -> None
```

<a id="unreal.SkeletalMeshComponent.unlink_anim_class_layers"></a>

#### unlink_anim_class_layers

```python
def unlink_anim_class_layers(class_: Class) -> None
```

x.unlink_anim_class_layers(class_) -> None
Runs through all layer nodes, attempting to find layer nodes that are currently running the specified class, then resets each to its default value.
State sharing rules are as with SetLayerOverlay.
If InClass is null, does nothing.

Args:
    class_ (type(Class)):

<a id="unreal.SkeletalMeshComponent.clear_layer_overlay"></a>

#### clear_layer_overlay

```python
def clear_layer_overlay(class_: Class) -> None
```

deprecated: 'clear_layer_overlay' was renamed to 'unlink_anim_class_layers'.

<a id="unreal.SkeletalMeshComponent.unbind_cloth_from_leader_pose_component"></a>

#### unbind_cloth_from_leader_pose_component

```python
def unbind_cloth_from_leader_pose_component(
        restore_simulation_space: bool = True) -> None
```

x.unbind_cloth_from_leader_pose_component(restore_simulation_space=True) -> None
If this component has a valid LeaderPoseComponent and has previously had its cloth bound to the
MCP, this function will unbind the cloth and resume simulation.

Args:
    restore_simulation_space (bool): if true and the leader pose cloth was originally simulating in world space, we will restore this setting. This will cause the leader component to reset which may be undesirable.

<a id="unreal.SkeletalMeshComponent.unbind_cloth_from_master_pose_component"></a>

#### unbind_cloth_from_master_pose_component

```python
def unbind_cloth_from_master_pose_component(
        restore_simulation_space: bool = True) -> None
```

deprecated: 'unbind_cloth_from_master_pose_component' was renamed to 'unbind_cloth_from_leader_pose_component'.

<a id="unreal.SkeletalMeshComponent.toggle_disable_post_process_blueprint"></a>

#### toggle_disable_post_process_blueprint

```python
def toggle_disable_post_process_blueprint() -> None
```

x.toggle_disable_post_process_blueprint() -> None
Toggles whether the post process blueprint will run for this component

<a id="unreal.SkeletalMeshComponent.term_bodies_below"></a>

#### term_bodies_below

```python
def term_bodies_below(parent_bone_name: Name) -> None
```

x.term_bodies_below(parent_bone_name) -> None
Terminate physics on all bodies below the named bone, effectively disabling collision forever. If you terminate, you won't be able to re-init later.

Args:
    parent_bone_name (Name):

<a id="unreal.SkeletalMeshComponent.suspend_clothing_simulation"></a>

#### suspend_clothing_simulation

```python
def suspend_clothing_simulation() -> None
```

x.suspend_clothing_simulation() -> None
Stops simulating clothing, but does not show clothing ref pose. Keeps the last known simulation state

<a id="unreal.SkeletalMeshComponent.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

<a id="unreal.SkeletalMeshComponent.snapshot_pose"></a>

#### snapshot_pose

```python
def snapshot_pose(snapshot: PoseSnapshot) -> PoseSnapshot
```

x.snapshot_pose(snapshot) -> PoseSnapshot
Takes a snapshot of this skeletal mesh component's pose and saves it to the specified snapshot.
The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
and then used it at LOD0 any bones not in LOD1 will use the reference pose

Args:
    snapshot (PoseSnapshot): 

Returns:
    PoseSnapshot: 

    snapshot (PoseSnapshot):

<a id="unreal.SkeletalMeshComponent.set_update_cloth_in_editor"></a>

#### set_update_cloth_in_editor

```python
def set_update_cloth_in_editor(new_update_state: bool) -> None
```

x.set_update_cloth_in_editor(new_update_state) -> None
Sets whether or not to animate cloth in the editor. Requires Update Animation In Editor to also be true.
This is supported only in the editor

Args:
    new_update_state (bool):

<a id="unreal.SkeletalMeshComponent.set_update_animation_in_editor"></a>

#### set_update_animation_in_editor

```python
def set_update_animation_in_editor(new_update_state: bool) -> None
```

x.set_update_animation_in_editor(new_update_state) -> None
Sets whether or not to force tick component in order to update animation and refresh transform for this component
This is supported only in the editor

Args:
    new_update_state (bool):

<a id="unreal.SkeletalMeshComponent.set_skeletal_mesh_asset"></a>

#### set_skeletal_mesh_asset

```python
def set_skeletal_mesh_asset(new_mesh: SkeletalMesh) -> None
```

x.set_skeletal_mesh_asset(new_mesh) -> None
Set the SkeletalMesh rendered for this mesh.

Args:
    new_mesh (SkeletalMesh):

<a id="unreal.SkeletalMeshComponent.set_position"></a>

#### set_position

```python
def set_position(pos: float, fire_notifies: bool = True) -> None
```

x.set_position(pos, fire_notifies=True) -> None
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Args:
    pos (float): 
    fire_notifies (bool):

<a id="unreal.SkeletalMeshComponent.set_play_rate"></a>

#### set_play_rate

```python
def set_play_rate(rate: float) -> None
```

x.set_play_rate(rate) -> None
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Args:
    rate (float):

<a id="unreal.SkeletalMeshComponent.set_physics_blend_weight"></a>

#### set_physics_blend_weight

```python
def set_physics_blend_weight(physics_blend_weight: float) -> None
```

x.set_physics_blend_weight(physics_blend_weight) -> None
This is global set up for setting physics blend weight
This does multiple things automatically
If PhysicsBlendWeight == 1.f, it will enable Simulation, and if PhysicsBlendWeight == 0.f, it will disable Simulation.
Also it will respect each body's setup, so if the body is fixed, it won't simulate. Vice versa
So if you'd like all bodies to change manually, do not use this function, but SetAllBodiesPhysicsBlendWeight

Args:
    physics_blend_weight (float):

<a id="unreal.SkeletalMeshComponent.set_override_post_process_anim_bp"></a>

#### set_override_post_process_anim_bp

```python
def set_override_post_process_anim_bp(
        post_process_anim_blueprint: Class,
        reinit_anim_instances: bool = True) -> None
```

x.set_override_post_process_anim_bp(post_process_anim_blueprint, reinit_anim_instances=True) -> None
Set the post-processing AnimBP to be used for this skeletal mesh component.
In case an override post-processing AnimBP is set, the one set in skeletal mesh asset will be ignored and not used.

Args:
    post_process_anim_blueprint (type(Class)): 
    reinit_anim_instances (bool): Can be false when called e.g. from the construction script in a Blueprint. True when this is called while the game is running and the anim instances need to be re-initialized.

<a id="unreal.SkeletalMeshComponent.set_notify_rigid_body_collision_below"></a>

#### set_notify_rigid_body_collision_below

```python
def set_notify_rigid_body_collision_below(
        new_notify_rigid_body_collision: bool,
        bone_name: Name = "None",
        include_self: bool = True) -> None
```

x.set_notify_rigid_body_collision_below(new_notify_rigid_body_collision, bone_name="None", include_self=True) -> None
Changes the value of bNotifyRigidBodyCollision on all bodies below a given bone

Args:
    new_notify_rigid_body_collision (bool): The value to assign to bNotifyRigidBodyCollision
    bone_name (Name): Name of the body to turn hit notifies on (and below)
    include_self (bool): Whether to modify the given body (useful for roots with multiple children)

<a id="unreal.SkeletalMeshComponent.set_morph_target"></a>

#### set_morph_target

```python
def set_morph_target(morph_target_name: Name,
                     value: float,
                     remove_zero_weight: bool = True) -> None
```

x.set_morph_target(morph_target_name, value, remove_zero_weight=True) -> None
Set Morph Target with Name and Value(0-1)

Args:
    morph_target_name (Name): 
    value (float): 
    remove_zero_weight (bool): : Used by editor code when it should stay in the active list with zero weight

<a id="unreal.SkeletalMeshComponent.set_enable_physics_blending"></a>

#### set_enable_physics_blending

```python
def set_enable_physics_blending(new_blend_physics: bool) -> None
```

x.set_enable_physics_blending(new_blend_physics) -> None
Disable physics blending of bones *

Args:
    new_blend_physics (bool):

<a id="unreal.SkeletalMeshComponent.set_enable_gravity_on_all_bodies_below"></a>

#### set_enable_gravity_on_all_bodies_below

```python
def set_enable_gravity_on_all_bodies_below(enable_gravity: bool,
                                           bone_name: Name,
                                           include_self: bool = True) -> None
```

x.set_enable_gravity_on_all_bodies_below(enable_gravity, bone_name, include_self=True) -> None
Enables or disables gravity to all bodies below the given bone.
NAME_None indicates all bodies will be edited.
In that case, consider using UPrimitiveComponent::EnableGravity.

Args:
    enable_gravity (bool): Whether gravity should be enabled or disabled.
    bone_name (Name): The name of the top most bone.
    include_self (bool): Whether the bone specified should be edited.

<a id="unreal.SkeletalMeshComponent.set_enable_body_gravity"></a>

#### set_enable_body_gravity

```python
def set_enable_body_gravity(enable_gravity: bool, bone_name: Name) -> None
```

x.set_enable_body_gravity(enable_gravity, bone_name) -> None
Enables or disables gravity for the given bone.
NAME_None indicates the root body will be edited.
If the bone name given is otherwise invalid, nothing happens.

Args:
    enable_gravity (bool): Whether gravity should be enabled or disabled.
    bone_name (Name): The name of the bone to modify.

<a id="unreal.SkeletalMeshComponent.set_disable_anim_curves"></a>

#### set_disable_anim_curves

```python
def set_disable_anim_curves(disable_anim_curves: bool) -> None
```

x.set_disable_anim_curves(disable_anim_curves) -> None
Set Disable Anim Curves

Args:
    disable_anim_curves (bool):

<a id="unreal.SkeletalMeshComponent.set_constraint_profile_for_all"></a>

#### set_constraint_profile_for_all

```python
def set_constraint_profile_for_all(profile_name: Name,
                                   default_if_not_found: bool = False) -> None
```

x.set_constraint_profile_for_all(profile_name, default_if_not_found=False) -> None
Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset for all constraints. If profile name is not found the joint is set to use the default constraint profile.

Args:
    profile_name (Name): 
    default_if_not_found (bool):

<a id="unreal.SkeletalMeshComponent.set_constraint_profile"></a>

#### set_constraint_profile

```python
def set_constraint_profile(joint_name: Name,
                           profile_name: Name,
                           default_if_not_found: bool = False) -> None
```

x.set_constraint_profile(joint_name, profile_name, default_if_not_found=False) -> None
Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset. If profile name is not found the joint is set to use the default constraint profile.

Args:
    joint_name (Name): 
    profile_name (Name): 
    default_if_not_found (bool):

<a id="unreal.SkeletalMeshComponent.set_cloth_max_distance_scale"></a>

#### set_cloth_max_distance_scale

```python
def set_cloth_max_distance_scale(scale: float) -> None
```

x.set_cloth_max_distance_scale(scale) -> None
Set Cloth Max Distance Scale

Args:
    scale (float):

<a id="unreal.SkeletalMeshComponent.set_body_simulate_physics"></a>

#### set_body_simulate_physics

```python
def set_body_simulate_physics(bone_name: Name, simulate: bool) -> None
```

x.set_body_simulate_physics(bone_name, simulate) -> None
Set a single bone to be simulated (or not)

Args:
    bone_name (Name): 
    simulate (bool):

<a id="unreal.SkeletalMeshComponent.set_body_notify_rigid_body_collision"></a>

#### set_body_notify_rigid_body_collision

```python
def set_body_notify_rigid_body_collision(new_notify_rigid_body_collision: bool,
                                         bone_name: Name = "None") -> None
```

x.set_body_notify_rigid_body_collision(new_notify_rigid_body_collision, bone_name="None") -> None
Changes the value of bNotifyRigidBodyCollision for a given body

Args:
    new_notify_rigid_body_collision (bool): The value to assign to bNotifyRigidBodyCollision
    bone_name (Name): Name of the body to turn hit notifies on/off. None implies root body

<a id="unreal.SkeletalMeshComponent.set_anim_instance_class"></a>

#### set_anim_instance_class

```python
def set_anim_instance_class(new_class: Class) -> None
```

x.set_anim_instance_class(new_class) -> None
Set the anim instance class. Clears and re-initializes the anim instance with the new class and sets animation mode to 'AnimationBlueprint'

Args:
    new_class (type(Class)):

<a id="unreal.SkeletalMeshComponent.set_anim_blueprint"></a>

#### set_anim_blueprint

```python
def set_anim_blueprint(new_class: Class) -> None
```

deprecated: 'set_anim_blueprint' was renamed to 'set_anim_instance_class'.

<a id="unreal.SkeletalMeshComponent.set_anim_class"></a>

#### set_anim_class

```python
def set_anim_class(new_class: Class) -> None
```

deprecated: 'set_anim_class' was renamed to 'set_anim_instance_class'.

<a id="unreal.SkeletalMeshComponent.k2_set_anim_instance_class"></a>

#### k2_set_anim_instance_class

```python
def k2_set_anim_instance_class(new_class: Class) -> None
```

deprecated: 'k2_set_anim_instance_class' was renamed to 'set_anim_instance_class'.

<a id="unreal.SkeletalMeshComponent.set_animation_mode"></a>

#### set_animation_mode

```python
def set_animation_mode(animation_mode: AnimationMode,
                       force_init_anim_script_instance: bool = True) -> None
```

x.set_animation_mode(animation_mode, force_init_anim_script_instance=True) -> None
Set the Animation Mode

Args:
    animation_mode (AnimationMode): : Requested AnimationMode
    force_init_anim_script_instance (bool): : Init AnimScriptInstance if the AnimationMode is AnimationBlueprint even if the new animation mode is the same as current (this allows to use BP construction script to do this)

<a id="unreal.SkeletalMeshComponent.set_animation"></a>

#### set_animation

```python
def set_animation(new_anim_to_play: AnimationAsset) -> None
```

x.set_animation(new_anim_to_play) -> None
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Args:
    new_anim_to_play (AnimationAsset):

<a id="unreal.SkeletalMeshComponent.set_angular_limits"></a>

#### set_angular_limits

```python
def set_angular_limits(bone_name: Name, swing1_limit_angle: float,
                       twist_limit_angle: float,
                       swing2_limit_angle: float) -> None
```

x.set_angular_limits(bone_name, swing1_limit_angle, twist_limit_angle, swing2_limit_angle) -> None
Sets the Angular Motion Ranges for a named constraint

Args:
    bone_name (Name): Name of bone to adjust constraint ranges for
    swing1_limit_angle (float): Size of limit in degrees, 0 means locked, 180 means free
    twist_limit_angle (float): Size of limit in degrees, 0 means locked, 180 means free
    swing2_limit_angle (float): Size of limit in degrees, 0 means locked, 180 means free

<a id="unreal.SkeletalMeshComponent.set_allow_rigid_body_anim_node"></a>

#### set_allow_rigid_body_anim_node

```python
def set_allow_rigid_body_anim_node(allow: bool,
                                   reinit_anim: bool = True) -> None
```

x.set_allow_rigid_body_anim_node(allow, reinit_anim=True) -> None
Sets whether or not to allow rigid body animation nodes for this component

Args:
    allow (bool): 
    reinit_anim (bool):

<a id="unreal.SkeletalMeshComponent.set_allowed_anim_curves_evaluation"></a>

#### set_allowed_anim_curves_evaluation

```python
def set_allowed_anim_curves_evaluation(list: Array[Name], allow: bool) -> None
```

x.set_allowed_anim_curves_evaluation(list, allow) -> None
resets, and then only allow the following list to be allowed/disallowed

Args:
    list (Array[Name]): 
    allow (bool):

<a id="unreal.SkeletalMeshComponent.set_allow_cloth_actors"></a>

#### set_allow_cloth_actors

```python
def set_allow_cloth_actors(allow: bool) -> None
```

x.set_allow_cloth_actors(allow) -> None
Sets whether cloth assets should be created/simulated in this component.
This will update the conditional flag and you will want to call RecreateClothingActors for it to take effect.

Args:
    allow (bool): Whether to allow the creation of cloth assets and simulation.

<a id="unreal.SkeletalMeshComponent.set_allow_anim_curve_evaluation"></a>

#### set_allow_anim_curve_evaluation

```python
def set_allow_anim_curve_evaluation(allow: bool) -> None
```

x.set_allow_anim_curve_evaluation(allow) -> None
Set Allow Anim Curve Evaluation

Args:
    allow (bool):

<a id="unreal.SkeletalMeshComponent.set_all_motors_angular_velocity_drive"></a>

#### set_all_motors_angular_velocity_drive

```python
def set_all_motors_angular_velocity_drive(
        enable_swing_drive: bool,
        enable_twist_drive: bool,
        skip_custom_physics_type: bool = False) -> None
```

x.set_all_motors_angular_velocity_drive(enable_swing_drive, enable_twist_drive, skip_custom_physics_type=False) -> None
Enable or Disable AngularVelocityDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

Args:
    enable_swing_drive (bool): 
    enable_twist_drive (bool): 
    skip_custom_physics_type (bool):

<a id="unreal.SkeletalMeshComponent.set_all_motors_angular_position_drive"></a>

#### set_all_motors_angular_position_drive

```python
def set_all_motors_angular_position_drive(
        enable_swing_drive: bool,
        enable_twist_drive: bool,
        skip_custom_physics_type: bool = False) -> None
```

x.set_all_motors_angular_position_drive(enable_swing_drive, enable_twist_drive, skip_custom_physics_type=False) -> None
Enable or Disable AngularPositionDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

Args:
    enable_swing_drive (bool): 
    enable_twist_drive (bool): 
    skip_custom_physics_type (bool):

<a id="unreal.SkeletalMeshComponent.set_all_motors_angular_drive_params"></a>

#### set_all_motors_angular_drive_params

```python
def set_all_motors_angular_drive_params(
        spring: float,
        damping: float,
        force_limit: float,
        skip_custom_physics_type: bool = False) -> None
```

x.set_all_motors_angular_drive_params(spring, damping, force_limit, skip_custom_physics_type=False) -> None
Set Angular Drive motors params for all constraint instances

Args:
    spring (float): 
    damping (float): 
    force_limit (float): 
    skip_custom_physics_type (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_simulate_physics"></a>

#### set_all_bodies_simulate_physics

```python
def set_all_bodies_simulate_physics(new_simulate: bool) -> None
```

x.set_all_bodies_simulate_physics(new_simulate) -> None
Set bSimulatePhysics to true for all bone bodies. Does not change the component bSimulatePhysics flag.

Args:
    new_simulate (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_physics_blend_weight"></a>

#### set_all_bodies_physics_blend_weight

```python
def set_all_bodies_physics_blend_weight(
        physics_blend_weight: float,
        skip_custom_physics_type: bool = False) -> None
```

x.set_all_bodies_physics_blend_weight(physics_blend_weight, skip_custom_physics_type=False) -> None
Set All Bodies Physics Blend Weight

Args:
    physics_blend_weight (float): 
    skip_custom_physics_type (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_below_simulate_physics"></a>

#### set_all_bodies_below_simulate_physics

```python
def set_all_bodies_below_simulate_physics(bone_name: Name,
                                          new_simulate: bool,
                                          include_self: bool = True) -> None
```

x.set_all_bodies_below_simulate_physics(bone_name, new_simulate, include_self=True) -> None
Set all of the bones below passed in bone to be simulated

Args:
    bone_name (Name): 
    new_simulate (bool): 
    include_self (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_below_physics_disabled"></a>

#### set_all_bodies_below_physics_disabled

```python
def set_all_bodies_below_physics_disabled(bone_name: Name,
                                          disabled: bool,
                                          include_self: bool = True) -> None
```

x.set_all_bodies_below_physics_disabled(bone_name, disabled, include_self=True) -> None
[WARNING: Chaos Only]
Set all of the bones below passed in bone to be disabled or not for the associated physics solver
Bodies will not be colliding or be part of the physics simulation.
This is different from SetAllBodiesBelowSimulatePhysics that changes bodies to Kinematic/simulated

Args:
    bone_name (Name): 
    disabled (bool): 
    include_self (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_below_physics_blend_weight"></a>

#### set_all_bodies_below_physics_blend_weight

```python
def set_all_bodies_below_physics_blend_weight(
        bone_name: Name,
        physics_blend_weight: float,
        skip_custom_physics_type: bool = False,
        include_self: bool = True) -> None
```

x.set_all_bodies_below_physics_blend_weight(bone_name, physics_blend_weight, skip_custom_physics_type=False, include_self=True) -> None
Set all of the bones below passed in bone to be simulated

Args:
    bone_name (Name): 
    physics_blend_weight (float): 
    skip_custom_physics_type (bool): 
    include_self (bool):

<a id="unreal.SkeletalMeshComponent.set_all_bodies_below_linear_velocity"></a>

#### set_all_bodies_below_linear_velocity

```python
def set_all_bodies_below_linear_velocity(bone_name: Name,
                                         linear_velocity: Vector,
                                         include_self: bool = True) -> None
```

x.set_all_bodies_below_linear_velocity(bone_name, linear_velocity, include_self=True) -> None
set the linear velocity of the child bodies to match that of the given parent bone

Args:
    bone_name (Name): 
    linear_velocity (Vector): 
    include_self (bool):

<a id="unreal.SkeletalMeshComponent.resume_clothing_simulation"></a>

#### resume_clothing_simulation

```python
def resume_clothing_simulation() -> None
```

x.resume_clothing_simulation() -> None
Resumes a previously suspended clothing simulation, teleporting the clothing on the next tick

<a id="unreal.SkeletalMeshComponent.reset_cloth_teleport_mode"></a>

#### reset_cloth_teleport_mode

```python
def reset_cloth_teleport_mode() -> None
```

x.reset_cloth_teleport_mode() -> None
Reset the teleport mode of a next update to 'Continuous'

<a id="unreal.SkeletalMeshComponent.reset_cloth_collision_sources"></a>

#### reset_cloth_collision_sources

```python
def reset_cloth_collision_sources() -> None
```

x.reset_cloth_collision_sources() -> None
Remove all cloth collision sources

<a id="unreal.SkeletalMeshComponent.reset_anim_instance_dynamics"></a>

#### reset_anim_instance_dynamics

```python
def reset_anim_instance_dynamics(
        teleport_type: TeleportType = TeleportType.RESET_PHYSICS) -> None
```

x.reset_anim_instance_dynamics(teleport_type=TeleportType.RESET_PHYSICS) -> None
Informs any active anim instances (main instance, linked instances, post instance) that a dynamics reset is required
for example if a teleport occurs.

Args:
    teleport_type (TeleportType):

<a id="unreal.SkeletalMeshComponent.reset_allowed_anim_curve_evaluation"></a>

#### reset_allowed_anim_curve_evaluation

```python
def reset_allowed_anim_curve_evaluation() -> None
```

x.reset_allowed_anim_curve_evaluation() -> None
By reset, it will allow all the curves to be evaluated

<a id="unreal.SkeletalMeshComponent.reset_all_bodies_simulate_physics"></a>

#### reset_all_bodies_simulate_physics

```python
def reset_all_bodies_simulate_physics() -> None
```

x.reset_all_bodies_simulate_physics() -> None
Allows you to reset bodies Simulate state based on where bUsePhysics is set to true in the BodySetup.

<a id="unreal.SkeletalMeshComponent.remove_cloth_collision_sources"></a>

#### remove_cloth_collision_sources

```python
def remove_cloth_collision_sources(
        source_component: SkeletalMeshComponent) -> None
```

x.remove_cloth_collision_sources(source_component) -> None
Remove a cloth collision source defined by a component

Args:
    source_component (SkeletalMeshComponent):

<a id="unreal.SkeletalMeshComponent.remove_cloth_collision_source"></a>

#### remove_cloth_collision_source

```python
def remove_cloth_collision_source(source_component: SkeletalMeshComponent,
                                  source_physics_asset: PhysicsAsset) -> None
```

x.remove_cloth_collision_source(source_component, source_physics_asset) -> None
Remove a cloth collision source defined by both a component and a physics asset

Args:
    source_component (SkeletalMeshComponent): 
    source_physics_asset (PhysicsAsset):

<a id="unreal.SkeletalMeshComponent.recreate_clothing_actors"></a>

#### recreate_clothing_actors

```python
def recreate_clothing_actors() -> None
```

x.recreate_clothing_actors() -> None
Destroys and recreates the clothing actors in the current simulation

<a id="unreal.SkeletalMeshComponent.play_animation"></a>

#### play_animation

```python
def play_animation(new_anim_to_play: AnimationAsset, looping: bool) -> None
```

x.play_animation(new_anim_to_play, looping) -> None
Animation play functions
       *
       * These changes status of animation instance, which is transient data, which means it won't serialize with this component
       * Because of that reason, it is not safe to be used during construction script
       * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Args:
    new_anim_to_play (AnimationAsset): 
    looping (bool):

<a id="unreal.SkeletalMeshComponent.play"></a>

#### play

```python
def play(looping: bool) -> None
```

x.play(looping) -> None
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Args:
    looping (bool):

<a id="unreal.SkeletalMeshComponent.override_animation_data"></a>

#### override_animation_data

```python
def override_animation_data(anim_to_play: AnimationAsset,
                            is_looping: bool = True,
                            is_playing: bool = True,
                            position: float = 0.000000,
                            play_rate: float = 1.000000) -> None
```

x.override_animation_data(anim_to_play, is_looping=True, is_playing=True, position=0.000000, play_rate=1.000000) -> None
This overrides current AnimationData parameter in the SkeletalMeshComponent. This will serialize when the component serialize
so it can be used during construction script. However note that this will override current existing data
This can be useful if you'd like to make a blueprint with custom default animation per component
This sets single player mode, which means you can't use AnimBlueprint with it

Args:
    anim_to_play (AnimationAsset): 
    is_looping (bool): 
    is_playing (bool): 
    position (float): 
    play_rate (float):

<a id="unreal.SkeletalMeshComponent.link_anim_graph_by_tag"></a>

#### link_anim_graph_by_tag

```python
def link_anim_graph_by_tag(tag: Name, class_: Class) -> None
```

x.link_anim_graph_by_tag(tag, class_) -> None
Runs through all nodes, attempting to find linked instance by name/tag, then sets the class of each node if the tag matches

Args:
    tag (Name): 
    class_ (type(Class)):

<a id="unreal.SkeletalMeshComponent.set_sub_instance_class_by_tag"></a>

#### set_sub_instance_class_by_tag

```python
def set_sub_instance_class_by_tag(tag: Name, class_: Class) -> None
```

deprecated: 'set_sub_instance_class_by_tag' was renamed to 'link_anim_graph_by_tag'.

<a id="unreal.SkeletalMeshComponent.link_anim_class_layers"></a>

#### link_anim_class_layers

```python
def link_anim_class_layers(class_: Class) -> None
```

x.link_anim_class_layers(class_) -> None
Runs through all layer nodes, attempting to find layer nodes that are implemented by the specified class, then sets up a linked instance of the class for each.
Allocates one linked instance to run each of the groups specified in the class, so state is shared. If a layer is not grouped (ie. NAME_None), then state is not shared
and a separate linked instance is allocated for each layer node.
If InClass is null, then all layers are reset to their defaults.

Args:
    class_ (type(Class)):

<a id="unreal.SkeletalMeshComponent.set_layer_overlay"></a>

#### set_layer_overlay

```python
def set_layer_overlay(class_: Class) -> None
```

deprecated: 'set_layer_overlay' was renamed to 'link_anim_class_layers'.

<a id="unreal.SkeletalMeshComponent.get_closest_point_on_physics_asset"></a>

#### get_closest_point_on_physics_asset

```python
def get_closest_point_on_physics_asset(
        world_position: Vector
) -> Optional[Tuple[Vector, Vector, Name, float]]
```

x.get_closest_point_on_physics_asset(world_position) -> (closest_world_position=Vector, normal=Vector, bone_name=Name, distance=float) or None
Given a world position, find the closest point on the physics asset. Note that this is independent of collision and welding. This is based purely on animation position

Args:
    world_position (Vector): The point we want the closest point to (i.e. for all bodies in the physics asset, find the one that has a point closest to WorldPosition)

Returns:
    tuple or None: true if we found a closest point

    closest_world_position (Vector): 

    normal (Vector): 

    bone_name (Name): 

    distance (float):

<a id="unreal.SkeletalMeshComponent.is_playing"></a>

#### is_playing

```python
def is_playing() -> bool
```

x.is_playing() -> bool
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.is_clothing_simulation_suspended"></a>

#### is_clothing_simulation_suspended

```python
def is_clothing_simulation_suspended() -> bool
```

x.is_clothing_simulation_suspended() -> bool
Gets whether or not the clothing simulation is currently suspended

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.is_body_gravity_enabled"></a>

#### is_body_gravity_enabled

```python
def is_body_gravity_enabled(bone_name: Name) -> bool
```

x.is_body_gravity_enabled(bone_name) -> bool
Checks whether or not gravity is enabled on the given bone.
NAME_None indicates the root body should be queried.
If the bone name given is otherwise invalid, false is returned.

Args:
    bone_name (Name): The name of the bone to check.

Returns:
    bool: True if gravity is enabled on the bone.

<a id="unreal.SkeletalMeshComponent.has_valid_animation_instance"></a>

#### has_valid_animation_instance

```python
def has_valid_animation_instance() -> bool
```

x.has_valid_animation_instance() -> bool
Returns whether there are any valid instances to run, currently this means whether we have
have an animation instance or a post process instance available to process.

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.get_transform_attribute_ref"></a>

#### get_transform_attribute_ref

```python
def get_transform_attribute_ref(
    bone_name: Name,
    attribute_name: Name,
    out_value: Transform,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[Transform]
```

x.get_transform_attribute_ref(bone_name, attribute_name, out_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> Transform or None
Get FTransform type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    out_value (Transform): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    Transform or None: Whether or not the atttribute was successfully retrieved

    out_value (Transform): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_transform_attribute"></a>

#### get_transform_attribute

```python
def get_transform_attribute(
    bone_name: Name,
    attribute_name: Name,
    default_value: Transform,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[Transform]
```

x.get_transform_attribute(bone_name, attribute_name, default_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> Transform or None
Get FTransform type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    default_value (Transform): 
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    Transform or None: Whether or not the atttribute was successfully retrieved

    out_value (Transform): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_string_attribute_ref"></a>

#### get_string_attribute_ref

```python
def get_string_attribute_ref(
    bone_name: Name,
    attribute_name: Name,
    out_value: str,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[str]
```

x.get_string_attribute_ref(bone_name, attribute_name, out_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> str or None
Get string type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    out_value (str): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    str or None: Whether or not the atttribute was successfully retrieved

    out_value (str): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_string_attribute"></a>

#### get_string_attribute

```python
def get_string_attribute(
    bone_name: Name,
    attribute_name: Name,
    default_value: str,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[str]
```

x.get_string_attribute(bone_name, attribute_name, default_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> str or None
Get string type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    default_value (str): In case the attribute could not be found
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    str or None: Whether or not the atttribute was successfully retrieved

    out_value (str): Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_skeletal_mesh_asset"></a>

#### get_skeletal_mesh_asset

```python
def get_skeletal_mesh_asset() -> SkeletalMesh
```

x.get_skeletal_mesh_asset() -> SkeletalMesh
Get the SkeletalMesh rendered for this mesh.

Returns:
    SkeletalMesh:

<a id="unreal.SkeletalMeshComponent.get_skeletal_center_of_mass"></a>

#### get_skeletal_center_of_mass

```python
def get_skeletal_center_of_mass() -> Vector
```

x.get_skeletal_center_of_mass() -> Vector
Returns the center of mass of the skeletal mesh, instead of the root body's location

Returns:
    Vector:

<a id="unreal.SkeletalMeshComponent.get_post_process_instance"></a>

#### get_post_process_instance

```python
def get_post_process_instance() -> AnimInstance
```

x.get_post_process_instance() -> AnimInstance
Returns the active post process instance is one is available. This is set on the mesh that this
component is using, and is evaluated immediately after the main instance.

Returns:
    AnimInstance:

<a id="unreal.SkeletalMeshComponent.get_position"></a>

#### get_position

```python
def get_position() -> float
```

x.get_position() -> float
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Returns:
    float:

<a id="unreal.SkeletalMeshComponent.get_play_rate"></a>

#### get_play_rate

```python
def get_play_rate() -> float
```

x.get_play_rate() -> float
Animation play functions
      *
      * These changes status of animation instance, which is transient data, which means it won't serialize with this component
      * Because of that reason, it is not safe to be used during construction script
      * Please use OverrideAnimationData for construction script. That will override AnimationData to be serialized

Returns:
    float:

<a id="unreal.SkeletalMeshComponent.get_morph_target"></a>

#### get_morph_target

```python
def get_morph_target(morph_target_name: Name) -> float
```

x.get_morph_target(morph_target_name) -> float
Get Morph target with given name

Args:
    morph_target_name (Name): 

Returns:
    float:

<a id="unreal.SkeletalMeshComponent.get_linked_anim_layer_instance_by_group"></a>

#### get_linked_anim_layer_instance_by_group

```python
def get_linked_anim_layer_instance_by_group(group: Name) -> AnimInstance
```

x.get_linked_anim_layer_instance_by_group(group) -> AnimInstance
Gets the layer linked instance corresponding to the specified group

Args:
    group (Name): 

Returns:
    AnimInstance:

<a id="unreal.SkeletalMeshComponent.get_layer_sub_instance_by_group"></a>

#### get_layer_sub_instance_by_group

```python
def get_layer_sub_instance_by_group(group: Name) -> AnimInstance
```

deprecated: 'get_layer_sub_instance_by_group' was renamed to 'get_linked_anim_layer_instance_by_group'.

<a id="unreal.SkeletalMeshComponent.get_linked_anim_layer_instance_by_class"></a>

#### get_linked_anim_layer_instance_by_class

```python
def get_linked_anim_layer_instance_by_class(class_: Class) -> AnimInstance
```

x.get_linked_anim_layer_instance_by_class(class_) -> AnimInstance
Gets the first layer linked instance corresponding to the specified class

Args:
    class_ (type(Class)): 

Returns:
    AnimInstance:

<a id="unreal.SkeletalMeshComponent.get_layer_sub_instance_by_class"></a>

#### get_layer_sub_instance_by_class

```python
def get_layer_sub_instance_by_class(class_: Class) -> AnimInstance
```

deprecated: 'get_layer_sub_instance_by_class' was renamed to 'get_linked_anim_layer_instance_by_class'.

<a id="unreal.SkeletalMeshComponent.get_linked_anim_graph_instances_by_tag"></a>

#### get_linked_anim_graph_instances_by_tag

```python
def get_linked_anim_graph_instances_by_tag(tag: Name) -> Array[AnimInstance]
```

x.get_linked_anim_graph_instances_by_tag(tag) -> Array[AnimInstance]
Get Linked Anim Graph Instances by Tag
deprecated: Tags are unique so this function is no longer supported. Please use GetLinkedAnimGraphInstanceByTag instead

Args:
    tag (Name): 

Returns:
    Array[AnimInstance]: 

    out_linked_instances (Array[AnimInstance]):

<a id="unreal.SkeletalMeshComponent.get_sub_instances_by_tag"></a>

#### get_sub_instances_by_tag

```python
def get_sub_instances_by_tag(tag: Name) -> Array[AnimInstance]
```

deprecated: 'get_sub_instances_by_tag' was renamed to 'get_linked_anim_graph_instances_by_tag'.

<a id="unreal.SkeletalMeshComponent.get_linked_anim_graph_instance_by_tag"></a>

#### get_linked_anim_graph_instance_by_tag

```python
def get_linked_anim_graph_instance_by_tag(tag: Name) -> AnimInstance
```

x.get_linked_anim_graph_instance_by_tag(tag) -> AnimInstance
Returns the a tagged linked instance node. If no linked instances are found or none are tagged with the
supplied name, this will return NULL.

Args:
    tag (Name): 

Returns:
    AnimInstance:

<a id="unreal.SkeletalMeshComponent.get_sub_instance_by_tag"></a>

#### get_sub_instance_by_tag

```python
def get_sub_instance_by_tag(tag: Name) -> AnimInstance
```

deprecated: 'get_sub_instance_by_tag' was renamed to 'get_linked_anim_graph_instance_by_tag'.

<a id="unreal.SkeletalMeshComponent.get_integer_attribute_ref"></a>

#### get_integer_attribute_ref

```python
def get_integer_attribute_ref(
    bone_name: Name,
    attribute_name: Name,
    out_value: int,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[int]
```

x.get_integer_attribute_ref(bone_name, attribute_name, out_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> int32 or None
Get integer type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    out_value (int32): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    int32 or None: Whether or not the atttribute was successfully retrieved

    out_value (int32): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_integer_attribute"></a>

#### get_integer_attribute

```python
def get_integer_attribute(
    bone_name: Name,
    attribute_name: Name,
    default_value: int,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[int]
```

x.get_integer_attribute(bone_name, attribute_name, default_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> int32 or None
Get integer type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    default_value (int32): In case the attribute could not be found
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    int32 or None: Whether or not the atttribute was successfully retrieved

    out_value (int32): Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_float_attribute_ref"></a>

#### get_float_attribute_ref

```python
def get_float_attribute_ref(
    bone_name: Name,
    attribute_name: Name,
    out_value: float,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[float]
```

x.get_float_attribute_ref(bone_name, attribute_name, out_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> float or None
Get float type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    out_value (float): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    float or None: Whether or not the atttribute was successfully retrieved

    out_value (float): (reference) Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_float_attribute"></a>

#### get_float_attribute

```python
def get_float_attribute(
    bone_name: Name,
    attribute_name: Name,
    default_value: float,
    lookup_type: CustomBoneAttributeLookup = CustomBoneAttributeLookup.
    BONE_ONLY
) -> Optional[float]
```

x.get_float_attribute(bone_name, attribute_name, default_value, lookup_type=CustomBoneAttributeLookup.BONE_ONLY) -> float or None
Get float type attribute value.

Args:
    bone_name (Name): Name of the bone to retrieve try and retrieve the attribute from
    attribute_name (Name): Name of the attribute to retrieve
    default_value (float): In case the attribute could not be found
    lookup_type (CustomBoneAttributeLookup): Determines how the attribute is retrieved from the specified BoneName (see ECustomBoneAttributeLookup)

Returns:
    float or None: Whether or not the atttribute was successfully retrieved

    out_value (float): Retrieved attribute value if found, otherwise is set to DefaultValue

<a id="unreal.SkeletalMeshComponent.get_disable_anim_curves"></a>

#### get_disable_anim_curves

```python
def get_disable_anim_curves() -> bool
```

x.get_disable_anim_curves() -> bool
Get Disable Anim Curves

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.get_default_animating_rig"></a>

#### get_default_animating_rig

```python
def get_default_animating_rig() -> Object
```

x.get_default_animating_rig() -> Object
Get Default Animating Rig

Returns:
    Object:

<a id="unreal.SkeletalMeshComponent.get_current_joint_angles"></a>

#### get_current_joint_angles

```python
def get_current_joint_angles(bone_name: Name) -> Tuple[float, float, float]
```

x.get_current_joint_angles(bone_name) -> (swing1_angle=float, twist_angle=float, swing2_angle=float)
Gets the current Angular state for a named bone constraint

Args:
    bone_name (Name): Name of bone to get constraint ranges for

Returns:
    tuple: 

    swing1_angle (float): current angular state of the constraint

    twist_angle (float): current angular state of the constraint

    swing2_angle (float): current angular state of the constraint

<a id="unreal.SkeletalMeshComponent.get_constraints_from_body"></a>

#### get_constraints_from_body

```python
def get_constraints_from_body(
        body_name: Name, parent_constraints: bool, child_constraints: bool,
        includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
```

x.get_constraints_from_body(body_name, parent_constraints, child_constraints, includes_terminated) -> Array[ConstraintInstanceAccessor]
Gets all the constraints attached to a body

Args:
    body_name (Name): name of the body to get the attached constraints from
    parent_constraints (bool): return constraints where BodyName is the child of the constraint
    child_constraints (bool): return constraints where BodyName is the parent of the constraint
    includes_terminated (bool): 

Returns:
    Array[ConstraintInstanceAccessor]: 

    out_constraints (Array[ConstraintInstanceAccessor]): returned list of constraints matching the parameters

<a id="unreal.SkeletalMeshComponent.get_constraints"></a>

#### get_constraints

```python
def get_constraints(
        includes_terminated: bool) -> Array[ConstraintInstanceAccessor]
```

x.get_constraints(includes_terminated) -> Array[ConstraintInstanceAccessor]
Gets all the constraints

Args:
    includes_terminated (bool): 

Returns:
    Array[ConstraintInstanceAccessor]: 

    out_constraints (Array[ConstraintInstanceAccessor]): returned list of constraints matching the parameters

<a id="unreal.SkeletalMeshComponent.get_constraint_by_name"></a>

#### get_constraint_by_name

```python
def get_constraint_by_name(
        constraint_name: Name,
        includes_terminated: bool) -> ConstraintInstanceAccessor
```

x.get_constraint_by_name(constraint_name, includes_terminated) -> ConstraintInstanceAccessor
Gets a constraint by its name

Args:
    constraint_name (Name): name of the constraint
    includes_terminated (bool): 

Returns:
    ConstraintInstanceAccessor:

<a id="unreal.SkeletalMeshComponent.get_cloth_max_distance_scale"></a>

#### get_cloth_max_distance_scale

```python
def get_cloth_max_distance_scale() -> float
```

x.get_cloth_max_distance_scale() -> float
Get/Set the max distance scale of clothing mesh vertices

Returns:
    float:

<a id="unreal.SkeletalMeshComponent.get_clothing_simulation_interactor"></a>

#### get_clothing_simulation_interactor

```python
def get_clothing_simulation_interactor() -> ClothingSimulationInteractor
```

x.get_clothing_simulation_interactor() -> ClothingSimulationInteractor
Get the current interactor for a clothing simulation, if the current simulation supports runtime interaction.

Returns:
    ClothingSimulationInteractor:

<a id="unreal.SkeletalMeshComponent.get_bone_mass"></a>

#### get_bone_mass

```python
def get_bone_mass(bone_name: Name = "None", scale_mass: bool = True) -> float
```

x.get_bone_mass(bone_name="None", scale_mass=True) -> float
Returns the mass (in kg) of the given bone

Args:
    bone_name (Name): Name of the body to return. 'None' indicates root body.
    scale_mass (bool): If true, the mass is scaled by the bone's MassScale.

Returns:
    float:

<a id="unreal.SkeletalMeshComponent.get_bone_linear_velocity"></a>

#### get_bone_linear_velocity

```python
def get_bone_linear_velocity(bone_name: Name) -> Vector
```

x.get_bone_linear_velocity(bone_name) -> Vector
Get Bone Linear Velocity

Args:
    bone_name (Name): 

Returns:
    Vector:

<a id="unreal.SkeletalMeshComponent.get_anim_instance"></a>

#### get_anim_instance

```python
def get_anim_instance() -> AnimInstance
```

x.get_anim_instance() -> AnimInstance
Returns the animation instance that is driving the class (if available). This is typically an instance of
the class set as AnimBlueprintGeneratedClass (generated by an animation blueprint)
Since this instance is transient, it is not safe to be used during construction script

Returns:
    AnimInstance:

<a id="unreal.SkeletalMeshComponent.get_animation_mode"></a>

#### get_animation_mode

```python
def get_animation_mode() -> AnimationMode
```

x.get_animation_mode() -> AnimationMode
Get Animation Mode

Returns:
    AnimationMode:

<a id="unreal.SkeletalMeshComponent.get_allow_rigid_body_anim_node"></a>

#### get_allow_rigid_body_anim_node

```python
def get_allow_rigid_body_anim_node() -> bool
```

x.get_allow_rigid_body_anim_node() -> bool
Get Allow Rigid Body Anim Node

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.get_allowed_anim_curve_evaluate"></a>

#### get_allowed_anim_curve_evaluate

```python
def get_allowed_anim_curve_evaluate() -> bool
```

x.get_allowed_anim_curve_evaluate() -> bool
Get Allowed Anim Curve Evaluate

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.get_allow_cloth_actors"></a>

#### get_allow_cloth_actors

```python
def get_allow_cloth_actors() -> bool
```

x.get_allow_cloth_actors() -> bool
Get Allow Cloth Actors

Returns:
    bool:

<a id="unreal.SkeletalMeshComponent.force_cloth_next_update_teleport_and_reset"></a>

#### force_cloth_next_update_teleport_and_reset

```python
def force_cloth_next_update_teleport_and_reset() -> None
```

x.force_cloth_next_update_teleport_and_reset() -> None
Used to indicate we should force 'teleport and reset' during the next call to UpdateClothState.
This can be used to reset it from a bad state or by a teleport where the old state is not important anymore.

<a id="unreal.SkeletalMeshComponent.force_cloth_next_update_teleport"></a>

#### force_cloth_next_update_teleport

```python
def force_cloth_next_update_teleport() -> None
```

x.force_cloth_next_update_teleport() -> None
Used to indicate we should force 'teleport' during the next call to UpdateClothState,
This will transform positions and velocities and thus keep the simulation state, just translate it to a new pose.

<a id="unreal.SkeletalMeshComponent.find_constraint_bone_name"></a>

#### find_constraint_bone_name

```python
def find_constraint_bone_name(constraint_index: int) -> Name
```

x.find_constraint_bone_name(constraint_index) -> Name
Find Constraint Name from index

Args:
    constraint_index (int32): Index of constraint to look for

Returns:
    Name: Constraint Joint Name

<a id="unreal.SkeletalMeshComponent.clear_morph_targets"></a>

#### clear_morph_targets

```python
def clear_morph_targets() -> None
```

x.clear_morph_targets() -> None
Clear all Morph Target that are set to this mesh

<a id="unreal.SkeletalMeshComponent.break_constraint"></a>

#### break_constraint

```python
def break_constraint(impulse: Vector, hit_location: Vector,
                     bone_name: Name) -> None
```

x.break_constraint(impulse, hit_location, bone_name) -> None
Break a constraint off a Gore mesh.

Args:
    impulse (Vector): vector of impulse
    hit_location (Vector): location of the hit
    bone_name (Name): Name of bone to break constraint for

<a id="unreal.SkeletalMeshComponent.bind_cloth_to_leader_pose_component"></a>

#### bind_cloth_to_leader_pose_component

```python
def bind_cloth_to_leader_pose_component() -> None
```

x.bind_cloth_to_leader_pose_component() -> None
If this component has a valid LeaderPoseComponent then this function makes cloth items on the follower component
take the transforms of the cloth items on the leader component instead of simulating separately.
Note: This will FORCE any cloth actor on the leader component to simulate in local space. Also The meshes used in the components must be identical for the cloth to bind correctly

<a id="unreal.SkeletalMeshComponent.bind_cloth_to_master_pose_component"></a>

#### bind_cloth_to_master_pose_component

```python
def bind_cloth_to_master_pose_component() -> None
```

deprecated: 'bind_cloth_to_master_pose_component' was renamed to 'bind_cloth_to_leader_pose_component'.

<a id="unreal.SkeletalMeshComponent.allow_anim_curve_evaluation"></a>

#### allow_anim_curve_evaluation

```python
def allow_anim_curve_evaluation(name_of_curve: Name, allow: bool) -> None
```

x.allow_anim_curve_evaluation(name_of_curve, allow) -> None
Allow Anim Curve Evaluation

Args:
    name_of_curve (Name): 
    allow (bool):

<a id="unreal.SkeletalMeshComponent.add_impulse_to_all_bodies_below"></a>

#### add_impulse_to_all_bodies_below

```python
def add_impulse_to_all_bodies_below(impulse: Vector,
                                    bone_name: Name = "None",
                                    vel_change: bool = False,
                                    include_self: bool = True) -> None
```

x.add_impulse_to_all_bodies_below(impulse, bone_name="None", vel_change=False, include_self=True) -> None
Add impulse to all single rigid bodies below. Good for one time instant burst.

Args:
    impulse (Vector): Magnitude and direction of impulse to apply.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body.
    vel_change (bool): If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no effect).
    include_self (bool): If false, Force is only applied to bodies below but not given bone name.

<a id="unreal.SkeletalMeshComponent.add_force_to_all_bodies_below"></a>

#### add_force_to_all_bodies_below

```python
def add_force_to_all_bodies_below(force: Vector,
                                  bone_name: Name = "None",
                                  accel_change: bool = False,
                                  include_self: bool = True) -> None
```

x.add_force_to_all_bodies_below(force, bone_name="None", accel_change=False, include_self=True) -> None
Add a force to all rigid bodies below.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Args:
    force (Vector): Force vector to apply. Magnitude indicates strength of force.
    bone_name (Name): If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body.
    accel_change (bool): If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).
    include_self (bool): If false, Force is only applied to bodies below but not given bone name.

<a id="unreal.SkeletalMeshComponent.add_cloth_collision_source"></a>

#### add_cloth_collision_source

```python
def add_cloth_collision_source(source_component: SkeletalMeshComponent,
                               source_physics_asset: PhysicsAsset) -> None
```

x.add_cloth_collision_source(source_component, source_physics_asset) -> None
Add a collision source for the cloth on this component.
Each cloth tick, the collision defined by the physics asset, transformed by the bones in the source
component, will be applied to cloth.

Args:
    source_component (SkeletalMeshComponent): The component to extract collision transforms from
    source_physics_asset (PhysicsAsset): The physics asset that defines the collision primitives (that will be transformed by InSourceComponent's bones)

<a id="unreal.SkeletalMeshComponent.accumulate_all_bodies_below_physics_blend_weight"></a>

#### accumulate_all_bodies_below_physics_blend_weight

```python
def accumulate_all_bodies_below_physics_blend_weight(
        bone_name: Name,
        add_physics_blend_weight: float,
        skip_custom_physics_type: bool = False) -> None
```

x.accumulate_all_bodies_below_physics_blend_weight(bone_name, add_physics_blend_weight, skip_custom_physics_type=False) -> None
Accumulate AddPhysicsBlendWeight to physics blendweight for all of the bones below passed in bone to be simulated

Args:
    bone_name (Name): 
    add_physics_blend_weight (float): 
    skip_custom_physics_type (bool):

<a id="unreal.SingleAnimSkeletalComponent"></a>