## GeometryCollectionComponent Objects

```python
class GeometryCollectionComponent(MeshComponent)
```

GeometryCollectionComponent

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``abandoned_collision_profile_name`` (Name):  [Read-Write] Whether abandoned particles on the client should continue to have collision (i.e.
  still be in the external/internal acceleration structure).
- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_cull_distance_volume`` (bool):  [Read-Write] Whether to accept cull distance volumes to modify cached cull distance.
- ``allow_removal_on_break`` (bool):  [Read-Write] Allow removal on break for the instance if the rest collection has it enabled
- ``allow_removal_on_sleep`` (bool):  [Read-Write] Allow removal on sleep for the instance if the rest collection has it enabled
- ``always_create_physics_state`` (bool):  [Read-Write] Indicates if we'd like to create physics state all the time (for collision and simulation).
  If you set this to false, it still will create physics state if collision or simulation activated.
  This can help performance if you'd like to avoid overhead of creating physics state when triggers
- ``angular_ether_drag`` (float):  [Read-Write] Uniform angular ether drag.
  deprecated: Use PhysicalMaterial instead.
- ``apply_impulse_on_damage`` (bool):  [Read-Write] True for damage to this component to apply physics impulse, false to opt out of these impulses.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``body_instance`` (BodyInstance):  [Read-Write] Physics scene information for this component, holds a single rigid body with multiple shapes.
- ``bounds_scale`` (float):  [Read-Write] Scales the bounds of the object.
  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.
  Warning: Increasing the bounds of an object will reduce performance and shadow quality!
  Currently only used by StaticMeshComponent and SkeletalMeshComponent.
- ``cache_playback`` (bool):  [Read-Only]
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
- ``chaos_solver_actor`` (ChaosSolverActor):  [Read-Write] Chaos RBD Solver override. Will use the world's default solver actor if null.
- ``cluster_connection_type`` (ClusterConnectionTypeEnum):  [Read-Write]
  deprecated: Connection types are defined on the asset now.
- ``cluster_group_index`` (int32):  [Read-Write] Maximum level for cluster breaks.
- ``collision_group`` (int32):  [Read-Write]
- ``collision_profile_per_level`` (Array[Name]):  [Read-Write] A per-level collision profile name. If the name is set to NONE or an invalid collision profile, nothing will be changed.
  If the there are more levels than elements in this array, then each level will use the index that best matches it.
  For example, if the particle is level 2, and there is only 1 element in the array, then the particle will use the 0th
  collision profile. AbandonedCollisionProfileName will override this on the client when relevant.
- ``collision_sample_fraction`` (float):  [Read-Write] Fraction of collision sample particles to keep
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``consider_for_actor_placement_when_hidden`` (bool):  [Read-Write] If true, this component will be considered for placement when dragging and placing items in the editor even if it is not visible, such as in the case of hidden collision meshes
- ``crumbling_event_includes_children`` (bool):  [Read-Write] If this and bNotifyCrumblings are true, the crumbling events will contain released children indices.
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_primitive_data`` (CustomPrimitiveData):  [Read-Write] Optional user defined default values for the custom primitive data of this primitive
- ``custom_renderer_type`` (type(Class)):  [Read-Write] Custom class type that will be used to render the geometry collection instead of using the native rendering.
- ``damage_model`` (DamageModelTypeEnum):  [Read-Write] Damage model to use for evaluating destruction.
- ``damage_propagation_data`` (GeometryCollectionDamagePropagationData):  [Read-Write] Data about how damage propagation shoudl behave.
- ``damage_threshold`` (Array[float]):  [Read-Write]
- ``density_from_physics_material`` (bool):  [Read-Write] when true, density will be used to compute mass using the assigned physics material
- ``desired_cache_time`` (float):  [Read-Only]
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``emissive_light_source`` (bool):  [Read-Write] Whether the primitive will be used as an emissive light source.
- ``enable_abandon_after_level`` (bool):  [Read-Write] Enables use of ReplicationAbandonAfterLevel to stop providing network updates to
  clients when the updated particle is of a level higher then specified.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether to include this component in HLODs or not.
- ``enable_clustering`` (bool):  [Read-Write]
- ``enable_damage_from_collision`` (bool):  [Read-Write] Whether or not collisions against this geometry collection will apply strain which could cause the geometry collection to fracture.
- ``enable_material_parameter_caching`` (bool):  [Read-Write]
- ``enable_replication`` (bool):  [Read-Write] Per-instance override to enable/disable replication for the geometry collection
- ``enable_run_time_data_collection`` (bool):  [Read-Write]
- ``exclude_for_specific_hlod_levels`` (Array[int32]):  [Read-Write]
  deprecated: WARNING: This property has been deprecated, use the SetExcludedFromHLODLevel/IsExcludedFromHLODLevel functions instead
- ``exclude_from_hlod_levels`` (uint8):  [Read-Write] Which specific HLOD levels this component should be excluded from
- ``exclude_from_light_attachment_group`` (bool):  [Read-Write] If set, then it overrides any bLightAttachmentsAsGroup set in a parent.
- ``fill_collision_underneath_for_navmesh`` (bool):  [Read-Write] If set, navmesh will not be generated under the surface of the geometry
- ``first_person_primitive_type`` (FirstPersonPrimitiveType):  [Read-Write] If this is set to FirstPerson, the camera FirstPersonFieldOfView and FirstPersonScale parameters will be used on this component. These parameters can be used to render the component with a different field of view and a smaller depth range such that clipping with the scene can be avoided. This is useful for rendering first person view geometry.
- ``force_mip_streaming`` (bool):  [Read-Write] If true, forces mips for textures used by this component to be resident when this component's level is loaded.
- ``force_motion_blur`` (bool):  [Read-Write] If ForceMotionBlur is on, motion blur will always be active, even if the GeometryCollection is at rest.
- ``force_update_active_transforms`` (bool):  [Read-Write] Update transforms of active particles even when they are not moving. Has performance implications. Use only when GC is a child of a moving actor, to prevent released particle 'following the actor around'
- ``generate_overlap_events`` (bool):  [Read-Write]
- ``global_crumbling_event_includes_children`` (bool):  [Read-Write] If this and bNotifyGlobalCrumblings are true, the crumbling events will contain released children indices.
- ``gravity_group_index`` (int32):  [Read-Write]
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``hidden_in_scene_capture`` (bool):  [Read-Write] When true, will not be captured by Scene Capture
- ``hlod_batching_policy`` (HLODBatchingPolicy):  [Read-Write] Determines how the geometry of a component will be incorporated in proxy (simplified) HLODs.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``ignore_radial_force`` (bool):  [Read-Write] Will ignore radial forces applied to this component.
- ``ignore_radial_impulse`` (bool):  [Read-Write] Will ignore radial impulses applied to this component.
- ``indirect_lighting_cache_quality`` (IndirectLightingCacheQuality):  [Read-Write] Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time.
- ``initial_angular_velocity`` (Vector):  [Read-Write]
- ``initial_linear_velocity`` (Vector):  [Read-Write]
- ``initial_velocity_type`` (InitialVelocityTypeEnum):  [Read-Write]
- ``initialization_fields`` (Array[FieldSystemActor]):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``light_attachments_as_group`` (bool):  [Read-Write] Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.
  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.
  This is useful for improving performance when multiple movable components are attached together.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this component should be in.  Lights with matching channels will affect the component.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
  Lighting channels are only supported on translucent materials using forward shading (i.e. when not using the translucency lighting volume).
- ``lightmap_type`` (LightmapType):  [Read-Write]
- ``linear_ether_drag`` (float):  [Read-Write] Uniform linear ether drag.
  deprecated: Use PhysicalMaterial instead.
- ``max_cluster_level`` (int32):  [Read-Write] Maximum level for cluster breaks.
- ``max_simulated_level`` (int32):  [Read-Write] The maximum level to create rigid bodies that could be simulated.
        Example: If we have a Geometry Collection with 2 levels, where:
        0 = Root
        1 = Clusters
        2 = Leaf Nodes
        A setting of '1' would only generate a physics representation of the Root transform and Level 1 clusters.
        The leaf nodes on Level 2 would never be created on the solver, and would therefore never be considered as part of the simulation.
- ``min_draw_distance`` (float):  [Read-Write] The minimum distance at which the primitive should be rendered,
  measured in world space units from the center of the primitive's bounding sphere to the camera position.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``multi_body_overlap`` (bool):  [Read-Write] If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will
  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another component/body. This flag has no
  influence on single body components.
- ``never_distance_cull`` (bool):  [Read-Write] When enabled this object will not be culled by distance. This is ignored if a child of a HLOD.
- ``notify_breaks`` (bool):  [Read-Write] If true, this component will generate breaking events that other systems may subscribe to.
- ``notify_collisions`` (bool):  [Read-Write] If true, this component will generate collision events that other systems may subscribe to.
- ``notify_crumblings`` (bool):  [Read-Write] If true, this component will generate crumbling events that other systems may subscribe to.
- ``notify_geometry_collection_physics_loading_state_change`` (NotifyGeometryCollectionPhysicsLoadingStateChange):  [Read-Write]
- ``notify_geometry_collection_physics_state_change`` (NotifyGeometryCollectionPhysicsStateChange):  [Read-Write]
- ``notify_global_breaks`` (bool):  [Read-Write] If true, this component will generate breaking events that will be listened by the global event relay.
- ``notify_global_collisions`` (bool):  [Read-Write] If true, this component will generate collision events  that will be listened by the global event relay.
- ``notify_global_crumblings`` (bool):  [Read-Write] If true, this component will generate crumbling events  that will be listened by the global event relay.
- ``notify_global_removals`` (bool):  [Read-Write] If true, this component will generate removal events  that will be listened by the global event relay.
- ``notify_removals`` (bool):  [Read-Write] If true, this component will generate removal events that other systems may subscribe to.
- ``notify_trailing`` (bool):  [Read-Write] If true, this component will generate trailing events that other systems may subscribe to.
- ``object_type`` (ObjectStateTypeEnum):  [Read-Write] ObjectType defines how to initialize the rigid objects state, Kinematic, Sleeping, Dynamic.
- ``on_begin_cursor_over`` (ComponentBeginCursorOverSignature):  [Read-Write] Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller
- ``on_chaos_break_event`` (OnChaosBreakEvent):  [Read-Write]
- ``on_chaos_crumbling_event`` (OnChaosCrumblingEvent):  [Read-Write]
- ``on_chaos_physics_collision`` (OnChaosPhysicsCollision):  [Read-Write]
- ``on_chaos_removal_event`` (OnChaosRemovalEvent):  [Read-Write]
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
- ``one_way_interaction_level`` (int32):  [Read-Write] All bodies with a level greater than or equal to this will have One-Way Interaction enabled and act like debris (will not apply forces to non-debris bodies)
  Set to -1 to disable (no bodies will have One-Way Interaction enabled)
- ``only_owner_see`` (bool):  [Read-Write] If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly.
- ``overlay_material`` (MaterialInterface):  [Read-Write] Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material
- ``overlay_material_max_draw_distance`` (float):  [Read-Write] The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance.
- ``override_custom_renderer`` (bool):  [Read-Write] If true, CustomRendererType will be used. If false, CustomRendererType comes from the RestCollection.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] Material overrides.
- ``owner_no_see`` (bool):  [Read-Write] If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly.
- ``physical_material`` (ChaosPhysicalMaterial):  [Read-Write] Physical Properties
  deprecated: Physical material now derived from render materials, for instance overrides use PhysicalMaterialOverride.
- ``physical_material_override`` (PhysicalMaterial):  [Read-Write]
  deprecated: Physical material now derived from render materials, for instance overrides use Colliisons PhysicalMaterialOverride.
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
- ``replication_abandon_after_level`` (int32):  [Read-Write] If replicating - the cluster level after which replication will not happen
  see: bEnableAbandonAfterLevel
- ``replication_abandon_cluster_level`` (int32):  [Read-Write] If replicating - the cluster level to stop sending corrections for geometry collection chunks.
  recommended for smaller leaf levels when the size of the objects means they are no longer
  gameplay relevant to cut down on required bandwidth to update a collection.
  See: bEnableAbandonAfterLevel
  deprecated: GeometryCollection now uses ReplicationAbandonAfterLevel instead of ReplicationAbandonClusterLevel.
- ``replication_max_position_and_velocity_correction_level`` (int32):  [Read-Write] If replicating - the maximum level where clusters will have their position and velocity send over to the client for tracking and correcting
  When breaking, client will only receive the initial break velocity
  This helps save bandwidth where only the destruction state of the GC is to be replicated but the falling pieces do not need to be tracked precisely
  note: This will have an effect only if set to a value less than ReplicationAbandonAfterLevel
  see: ReplicationAbandonAfterLevel
- ``rest_collection`` (GeometryCollection):  [Read-Write]
- ``return_material_on_move`` (bool):  [Read-Write] If true, component sweeps will return the material in their hit result.
  see: MoveComponent(), FHitResult
- ``run_time_data_collection_guid`` (Guid):  [Read-Write]
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw the mesh for this actor.
  The material also needs to be set up to output to a virtual texture.
- ``self_shadow_only`` (bool):  [Read-Write] When enabled, the component will only cast a shadow on itself and not other components in the world.
  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_bone_colors`` (bool):  [Read-Write] Display Bone Colors instead of assigned materials
- ``simulating`` (bool):  [Read-Write]
  deprecated: GeometryCollection now abides the bSimulatePhysics flag from the base class.
- ``single_sample_shadow_from_stationary_lights`` (bool):  [Read-Write] Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.
  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.
  This is currently only used on stationary directional lights.
- ``static_when_not_moveable`` (bool):  [Read-Write] When false, the underlying physics body will contain all sim data (mass, inertia tensor, etc) even if mobility is not set to Moveable
- ``store_velocities`` (bool):  [Read-Write] If true, this component will save linear and angular velocities on its DynamicCollection.
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
- ``update_component_transform_to_root_bone`` (bool):  [Read-Write] Relocate the component so that the original offset to the root bone is maintained
  This only works when the root bone is moving whole being dynamically simulated
  Note: Once the root element is broken, the component will no longer update its position
- ``update_navigation_in_tick`` (bool):  [Read-Write]
- ``use_as_occluder`` (bool):  [Read-Write] Whether to render the primitive in the depth only pass.
  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.
  todo: if any rendering features rely on a complete depth only pass, this variable needs to go away.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_material_damage_modifiers`` (bool):  [Read-Write] When on , use the modifiers on the material to adjust the user defined damage threshold values
- ``use_root_proxy_for_navigation`` (bool):  [Read-Write]
- ``use_size_specific_damage_threshold`` (bool):  [Read-Write] Damage threshold for clusters at different levels.
- ``use_static_mesh_collision_for_traces`` (bool):  [Read-Write] todo(chaos): Remove the ability to change this at runtime, as we'll want to use this at cook time instead
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

<a id="unreal.GeometryCollectionComponent.chaos_solver_actor"></a>

#### chaos_solver_actor

```python
@property
def chaos_solver_actor() -> ChaosSolverActor
```

(ChaosSolverActor):  [Read-Write] Chaos RBD Solver override. Will use the world's default solver actor if null.

<a id="unreal.GeometryCollectionComponent.chaos_solver_actor"></a>

#### chaos_solver_actor

```python
@chaos_solver_actor.setter
def chaos_solver_actor(value: ChaosSolverActor) -> None
```

<a id="unreal.GeometryCollectionComponent.rest_collection"></a>

#### rest_collection

```python
@property
def rest_collection() -> GeometryCollection
```

(GeometryCollection):  [Read-Only]

<a id="unreal.GeometryCollectionComponent.initialization_fields"></a>

#### initialization_fields

```python
@property
def initialization_fields() -> Array[FieldSystemActor]
```

(Array[FieldSystemActor]):  [Read-Only]

<a id="unreal.GeometryCollectionComponent.simulating"></a>

#### simulating

```python
@property
def simulating() -> bool
```

(bool):  [Read-Write]
deprecated: GeometryCollection now abides the bSimulatePhysics flag from the base class.

<a id="unreal.GeometryCollectionComponent.simulating"></a>

#### simulating

```python
@simulating.setter
def simulating(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.object_type"></a>

#### object_type

```python
@property
def object_type() -> ObjectStateTypeEnum
```

(ObjectStateTypeEnum):  [Read-Write] ObjectType defines how to initialize the rigid objects state, Kinematic, Sleeping, Dynamic.

<a id="unreal.GeometryCollectionComponent.object_type"></a>

#### object_type

```python
@object_type.setter
def object_type(value: ObjectStateTypeEnum) -> None
```

<a id="unreal.GeometryCollectionComponent.gravity_group_index"></a>

#### gravity_group_index

```python
@property
def gravity_group_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.gravity_group_index"></a>

#### gravity_group_index

```python
@gravity_group_index.setter
def gravity_group_index(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.one_way_interaction_level"></a>

#### one_way_interaction_level

```python
@property
def one_way_interaction_level() -> int
```

(int32):  [Read-Write] All bodies with a level greater than or equal to this will have One-Way Interaction enabled and act like debris (will not apply forces to non-debris bodies)
Set to -1 to disable (no bodies will have One-Way Interaction enabled)

<a id="unreal.GeometryCollectionComponent.one_way_interaction_level"></a>

#### one_way_interaction_level

```python
@one_way_interaction_level.setter
def one_way_interaction_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.density_from_physics_material"></a>

#### density_from_physics_material

```python
@property
def density_from_physics_material() -> bool
```

(bool):  [Read-Write] when true, density will be used to compute mass using the assigned physics material

<a id="unreal.GeometryCollectionComponent.density_from_physics_material"></a>

#### density_from_physics_material

```python
@density_from_physics_material.setter
def density_from_physics_material(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.force_motion_blur"></a>

#### force_motion_blur

```python
@property
def force_motion_blur() -> bool
```

(bool):  [Read-Write] If ForceMotionBlur is on, motion blur will always be active, even if the GeometryCollection is at rest.

<a id="unreal.GeometryCollectionComponent.force_motion_blur"></a>

#### force_motion_blur

```python
@force_motion_blur.setter
def force_motion_blur(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.enable_clustering"></a>

#### enable_clustering

```python
@property
def enable_clustering() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.enable_clustering"></a>

#### enable_clustering

```python
@enable_clustering.setter
def enable_clustering(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.cluster_group_index"></a>

#### cluster_group_index

```python
@property
def cluster_group_index() -> int
```

(int32):  [Read-Write] Maximum level for cluster breaks.

<a id="unreal.GeometryCollectionComponent.cluster_group_index"></a>

#### cluster_group_index

```python
@cluster_group_index.setter
def cluster_group_index(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.max_cluster_level"></a>

#### max_cluster_level

```python
@property
def max_cluster_level() -> int
```

(int32):  [Read-Write] Maximum level for cluster breaks.

<a id="unreal.GeometryCollectionComponent.max_cluster_level"></a>

#### max_cluster_level

```python
@max_cluster_level.setter
def max_cluster_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.max_simulated_level"></a>

#### max_simulated_level

```python
@property
def max_simulated_level() -> int
```

(int32):  [Read-Write] The maximum level to create rigid bodies that could be simulated.
      Example: If we have a Geometry Collection with 2 levels, where:
      0 = Root
      1 = Clusters
      2 = Leaf Nodes
      A setting of '1' would only generate a physics representation of the Root transform and Level 1 clusters.
      The leaf nodes on Level 2 would never be created on the solver, and would therefore never be considered as part of the simulation.

<a id="unreal.GeometryCollectionComponent.max_simulated_level"></a>

#### max_simulated_level

```python
@max_simulated_level.setter
def max_simulated_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.damage_model"></a>

#### damage_model

```python
@property
def damage_model() -> DamageModelTypeEnum
```

(DamageModelTypeEnum):  [Read-Write] Damage model to use for evaluating destruction.

<a id="unreal.GeometryCollectionComponent.damage_model"></a>

#### damage_model

```python
@damage_model.setter
def damage_model(value: DamageModelTypeEnum) -> None
```

<a id="unreal.GeometryCollectionComponent.damage_threshold"></a>

#### damage_threshold

```python
@property
def damage_threshold() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.damage_threshold"></a>

#### damage_threshold

```python
@damage_threshold.setter
def damage_threshold(value: Array[float]) -> None
```

<a id="unreal.GeometryCollectionComponent.use_size_specific_damage_threshold"></a>

#### use_size_specific_damage_threshold

```python
@property
def use_size_specific_damage_threshold() -> bool
```

(bool):  [Read-Write] Damage threshold for clusters at different levels.

<a id="unreal.GeometryCollectionComponent.use_size_specific_damage_threshold"></a>

#### use_size_specific_damage_threshold

```python
@use_size_specific_damage_threshold.setter
def use_size_specific_damage_threshold(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.use_material_damage_modifiers"></a>

#### use_material_damage_modifiers

```python
@property
def use_material_damage_modifiers() -> bool
```

(bool):  [Read-Write] When on , use the modifiers on the material to adjust the user defined damage threshold values

<a id="unreal.GeometryCollectionComponent.use_material_damage_modifiers"></a>

#### use_material_damage_modifiers

```python
@use_material_damage_modifiers.setter
def use_material_damage_modifiers(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.damage_propagation_data"></a>

#### damage_propagation_data

```python
@property
def damage_propagation_data() -> GeometryCollectionDamagePropagationData
```

(GeometryCollectionDamagePropagationData):  [Read-Write] Data about how damage propagation shoudl behave.

<a id="unreal.GeometryCollectionComponent.damage_propagation_data"></a>

#### damage_propagation_data

```python
@damage_propagation_data.setter
def damage_propagation_data(
        value: GeometryCollectionDamagePropagationData) -> None
```

<a id="unreal.GeometryCollectionComponent.enable_damage_from_collision"></a>

#### enable_damage_from_collision

```python
@property
def enable_damage_from_collision() -> bool
```

(bool):  [Read-Write] Whether or not collisions against this geometry collection will apply strain which could cause the geometry collection to fracture.

<a id="unreal.GeometryCollectionComponent.enable_damage_from_collision"></a>

#### enable_damage_from_collision

```python
@enable_damage_from_collision.setter
def enable_damage_from_collision(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.allow_removal_on_sleep"></a>

#### allow_removal_on_sleep

```python
@property
def allow_removal_on_sleep() -> bool
```

(bool):  [Read-Write] Allow removal on sleep for the instance if the rest collection has it enabled

<a id="unreal.GeometryCollectionComponent.allow_removal_on_sleep"></a>

#### allow_removal_on_sleep

```python
@allow_removal_on_sleep.setter
def allow_removal_on_sleep(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.allow_removal_on_break"></a>

#### allow_removal_on_break

```python
@property
def allow_removal_on_break() -> bool
```

(bool):  [Read-Write] Allow removal on break for the instance if the rest collection has it enabled

<a id="unreal.GeometryCollectionComponent.allow_removal_on_break"></a>

#### allow_removal_on_break

```python
@allow_removal_on_break.setter
def allow_removal_on_break(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.force_update_active_transforms"></a>

#### force_update_active_transforms

```python
@property
def force_update_active_transforms() -> bool
```

(bool):  [Read-Write] Update transforms of active particles even when they are not moving. Has performance implications. Use only when GC is a child of a moving actor, to prevent released particle 'following the actor around'

<a id="unreal.GeometryCollectionComponent.force_update_active_transforms"></a>

#### force_update_active_transforms

```python
@force_update_active_transforms.setter
def force_update_active_transforms(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.cluster_connection_type"></a>

#### cluster_connection_type

```python
@property
def cluster_connection_type() -> ClusterConnectionTypeEnum
```

(ClusterConnectionTypeEnum):  [Read-Write]
deprecated: Connection types are defined on the asset now.

<a id="unreal.GeometryCollectionComponent.cluster_connection_type"></a>

#### cluster_connection_type

```python
@cluster_connection_type.setter
def cluster_connection_type(value: ClusterConnectionTypeEnum) -> None
```

<a id="unreal.GeometryCollectionComponent.collision_group"></a>

#### collision_group

```python
@property
def collision_group() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.collision_group"></a>

#### collision_group

```python
@collision_group.setter
def collision_group(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.collision_sample_fraction"></a>

#### collision_sample_fraction

```python
@property
def collision_sample_fraction() -> float
```

(float):  [Read-Write] Fraction of collision sample particles to keep

<a id="unreal.GeometryCollectionComponent.collision_sample_fraction"></a>

#### collision_sample_fraction

```python
@collision_sample_fraction.setter
def collision_sample_fraction(value: float) -> None
```

<a id="unreal.GeometryCollectionComponent.linear_ether_drag"></a>

#### linear_ether_drag

```python
@property
def linear_ether_drag() -> float
```

(float):  [Read-Write] Uniform linear ether drag.
deprecated: Use PhysicalMaterial instead.

<a id="unreal.GeometryCollectionComponent.linear_ether_drag"></a>

#### linear_ether_drag

```python
@linear_ether_drag.setter
def linear_ether_drag(value: float) -> None
```

<a id="unreal.GeometryCollectionComponent.physical_material"></a>

#### physical_material

```python
@property
def physical_material() -> ChaosPhysicalMaterial
```

(ChaosPhysicalMaterial):  [Read-Write] Physical Properties
deprecated: Physical material now derived from render materials, for instance overrides use PhysicalMaterialOverride.

<a id="unreal.GeometryCollectionComponent.physical_material"></a>

#### physical_material

```python
@physical_material.setter
def physical_material(value: ChaosPhysicalMaterial) -> None
```

<a id="unreal.GeometryCollectionComponent.initial_velocity_type"></a>

#### initial_velocity_type

```python
@property
def initial_velocity_type() -> InitialVelocityTypeEnum
```

(InitialVelocityTypeEnum):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.initial_velocity_type"></a>

#### initial_velocity_type

```python
@initial_velocity_type.setter
def initial_velocity_type(value: InitialVelocityTypeEnum) -> None
```

<a id="unreal.GeometryCollectionComponent.initial_linear_velocity"></a>

#### initial_linear_velocity

```python
@property
def initial_linear_velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.initial_linear_velocity"></a>

#### initial_linear_velocity

```python
@initial_linear_velocity.setter
def initial_linear_velocity(value: Vector) -> None
```

<a id="unreal.GeometryCollectionComponent.initial_angular_velocity"></a>

#### initial_angular_velocity

```python
@property
def initial_angular_velocity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.initial_angular_velocity"></a>

#### initial_angular_velocity

```python
@initial_angular_velocity.setter
def initial_angular_velocity(value: Vector) -> None
```

<a id="unreal.GeometryCollectionComponent.physical_material_override"></a>

#### physical_material_override

```python
@property
def physical_material_override() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Write]
deprecated: Physical material now derived from render materials, for instance overrides use Colliisons PhysicalMaterialOverride.

<a id="unreal.GeometryCollectionComponent.physical_material_override"></a>

#### physical_material_override

```python
@physical_material_override.setter
def physical_material_override(value: PhysicalMaterial) -> None
```

<a id="unreal.GeometryCollectionComponent.notify_geometry_collection_physics_state_change"></a>

#### notify_geometry_collection_physics_state_change

```python
@property
def notify_geometry_collection_physics_state_change(
) -> NotifyGeometryCollectionPhysicsStateChange
```

(NotifyGeometryCollectionPhysicsStateChange):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.notify_geometry_collection_physics_state_change"></a>

#### notify_geometry_collection_physics_state_change

```python
@notify_geometry_collection_physics_state_change.setter
def notify_geometry_collection_physics_state_change(
        value: NotifyGeometryCollectionPhysicsStateChange) -> None
```

<a id="unreal.GeometryCollectionComponent.notify_geometry_collection_physics_loading_state_change"></a>

#### notify_geometry_collection_physics_loading_state_change

```python
@property
def notify_geometry_collection_physics_loading_state_change(
) -> NotifyGeometryCollectionPhysicsLoadingStateChange
```

(NotifyGeometryCollectionPhysicsLoadingStateChange):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.notify_geometry_collection_physics_loading_state_change"></a>

#### notify_geometry_collection_physics_loading_state_change

```python
@notify_geometry_collection_physics_loading_state_change.setter
def notify_geometry_collection_physics_loading_state_change(
        value: NotifyGeometryCollectionPhysicsLoadingStateChange) -> None
```

<a id="unreal.GeometryCollectionComponent.on_chaos_break_event"></a>

#### on_chaos_break_event

```python
@property
def on_chaos_break_event() -> OnChaosBreakEvent
```

(OnChaosBreakEvent):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.on_chaos_break_event"></a>

#### on_chaos_break_event

```python
@on_chaos_break_event.setter
def on_chaos_break_event(value: OnChaosBreakEvent) -> None
```

<a id="unreal.GeometryCollectionComponent.on_chaos_removal_event"></a>

#### on_chaos_removal_event

```python
@property
def on_chaos_removal_event() -> OnChaosRemovalEvent
```

(OnChaosRemovalEvent):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.on_chaos_removal_event"></a>

#### on_chaos_removal_event

```python
@on_chaos_removal_event.setter
def on_chaos_removal_event(value: OnChaosRemovalEvent) -> None
```

<a id="unreal.GeometryCollectionComponent.on_chaos_crumbling_event"></a>

#### on_chaos_crumbling_event

```python
@property
def on_chaos_crumbling_event() -> OnChaosCrumblingEvent
```

(OnChaosCrumblingEvent):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.on_chaos_crumbling_event"></a>

#### on_chaos_crumbling_event

```python
@on_chaos_crumbling_event.setter
def on_chaos_crumbling_event(value: OnChaosCrumblingEvent) -> None
```

<a id="unreal.GeometryCollectionComponent.desired_cache_time"></a>

#### desired_cache_time

```python
@property
def desired_cache_time() -> float
```

(float):  [Read-Only]

<a id="unreal.GeometryCollectionComponent.cache_playback"></a>

#### cache_playback

```python
@property
def cache_playback() -> bool
```

(bool):  [Read-Only]

<a id="unreal.GeometryCollectionComponent.on_chaos_physics_collision"></a>

#### on_chaos_physics_collision

```python
@property
def on_chaos_physics_collision() -> OnChaosPhysicsCollision
```

(OnChaosPhysicsCollision):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.on_chaos_physics_collision"></a>

#### on_chaos_physics_collision

```python
@on_chaos_physics_collision.setter
def on_chaos_physics_collision(value: OnChaosPhysicsCollision) -> None
```

<a id="unreal.GeometryCollectionComponent.notify_breaks"></a>

#### notify_breaks

```python
@property
def notify_breaks() -> bool
```

(bool):  [Read-Only] If true, this component will generate breaking events that other systems may subscribe to.

<a id="unreal.GeometryCollectionComponent.notify_collisions"></a>

#### notify_collisions

```python
@property
def notify_collisions() -> bool
```

(bool):  [Read-Only] If true, this component will generate collision events that other systems may subscribe to.

<a id="unreal.GeometryCollectionComponent.notify_trailing"></a>

#### notify_trailing

```python
@property
def notify_trailing() -> bool
```

(bool):  [Read-Only] If true, this component will generate trailing events that other systems may subscribe to.

<a id="unreal.GeometryCollectionComponent.notify_removals"></a>

#### notify_removals

```python
@property
def notify_removals() -> bool
```

(bool):  [Read-Only] If true, this component will generate removal events that other systems may subscribe to.

<a id="unreal.GeometryCollectionComponent.notify_crumblings"></a>

#### notify_crumblings

```python
@property
def notify_crumblings() -> bool
```

(bool):  [Read-Only] If true, this component will generate crumbling events that other systems may subscribe to.

<a id="unreal.GeometryCollectionComponent.crumbling_event_includes_children"></a>

#### crumbling_event_includes_children

```python
@property
def crumbling_event_includes_children() -> bool
```

(bool):  [Read-Only] If this and bNotifyCrumblings are true, the crumbling events will contain released children indices.

<a id="unreal.GeometryCollectionComponent.notify_global_breaks"></a>

#### notify_global_breaks

```python
@property
def notify_global_breaks() -> bool
```

(bool):  [Read-Only] If true, this component will generate breaking events that will be listened by the global event relay.

<a id="unreal.GeometryCollectionComponent.notify_global_collisions"></a>

#### notify_global_collisions

```python
@property
def notify_global_collisions() -> bool
```

(bool):  [Read-Only] If true, this component will generate collision events  that will be listened by the global event relay.

<a id="unreal.GeometryCollectionComponent.notify_global_removals"></a>

#### notify_global_removals

```python
@property
def notify_global_removals() -> bool
```

(bool):  [Read-Only] If true, this component will generate removal events  that will be listened by the global event relay.

<a id="unreal.GeometryCollectionComponent.notify_global_crumblings"></a>

#### notify_global_crumblings

```python
@property
def notify_global_crumblings() -> bool
```

(bool):  [Read-Only] If true, this component will generate crumbling events  that will be listened by the global event relay.

<a id="unreal.GeometryCollectionComponent.global_crumbling_event_includes_children"></a>

#### global_crumbling_event_includes_children

```python
@property
def global_crumbling_event_includes_children() -> bool
```

(bool):  [Read-Only] If this and bNotifyGlobalCrumblings are true, the crumbling events will contain released children indices.

<a id="unreal.GeometryCollectionComponent.store_velocities"></a>

#### store_velocities

```python
@property
def store_velocities() -> bool
```

(bool):  [Read-Only] If true, this component will save linear and angular velocities on its DynamicCollection.

<a id="unreal.GeometryCollectionComponent.show_bone_colors"></a>

#### show_bone_colors

```python
@property
def show_bone_colors() -> bool
```

(bool):  [Read-Write] Display Bone Colors instead of assigned materials

<a id="unreal.GeometryCollectionComponent.show_bone_colors"></a>

#### show_bone_colors

```python
@show_bone_colors.setter
def show_bone_colors(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.update_component_transform_to_root_bone"></a>

#### update_component_transform_to_root_bone

```python
@property
def update_component_transform_to_root_bone() -> bool
```

(bool):  [Read-Write] Relocate the component so that the original offset to the root bone is maintained
This only works when the root bone is moving whole being dynamically simulated
Note: Once the root element is broken, the component will no longer update its position

<a id="unreal.GeometryCollectionComponent.update_component_transform_to_root_bone"></a>

#### update_component_transform_to_root_bone

```python
@update_component_transform_to_root_bone.setter
def update_component_transform_to_root_bone(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.use_root_proxy_for_navigation"></a>

#### use_root_proxy_for_navigation

```python
@property
def use_root_proxy_for_navigation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.use_root_proxy_for_navigation"></a>

#### use_root_proxy_for_navigation

```python
@use_root_proxy_for_navigation.setter
def use_root_proxy_for_navigation(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.update_navigation_in_tick"></a>

#### update_navigation_in_tick

```python
@property
def update_navigation_in_tick() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryCollectionComponent.update_navigation_in_tick"></a>

#### update_navigation_in_tick

```python
@update_navigation_in_tick.setter
def update_navigation_in_tick(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.run_time_data_collection_guid"></a>

#### run_time_data_collection_guid

```python
@property
def run_time_data_collection_guid() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.GeometryCollectionComponent.enable_replication"></a>

#### enable_replication

```python
@property
def enable_replication() -> bool
```

(bool):  [Read-Write] Per-instance override to enable/disable replication for the geometry collection

<a id="unreal.GeometryCollectionComponent.enable_replication"></a>

#### enable_replication

```python
@enable_replication.setter
def enable_replication(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.enable_abandon_after_level"></a>

#### enable_abandon_after_level

```python
@property
def enable_abandon_after_level() -> bool
```

(bool):  [Read-Write] Enables use of ReplicationAbandonAfterLevel to stop providing network updates to
clients when the updated particle is of a level higher then specified.

<a id="unreal.GeometryCollectionComponent.enable_abandon_after_level"></a>

#### enable_abandon_after_level

```python
@enable_abandon_after_level.setter
def enable_abandon_after_level(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.abandoned_collision_profile_name"></a>

#### abandoned_collision_profile_name

```python
@property
def abandoned_collision_profile_name() -> Name
```

(Name):  [Read-Write] Whether abandoned particles on the client should continue to have collision (i.e.
still be in the external/internal acceleration structure).

<a id="unreal.GeometryCollectionComponent.abandoned_collision_profile_name"></a>

#### abandoned_collision_profile_name

```python
@abandoned_collision_profile_name.setter
def abandoned_collision_profile_name(value: Name) -> None
```

<a id="unreal.GeometryCollectionComponent.custom_renderer_type"></a>

#### custom_renderer_type

```python
@property
def custom_renderer_type() -> Class
```

(type(Class)):  [Read-Write] Custom class type that will be used to render the geometry collection instead of using the native rendering.

<a id="unreal.GeometryCollectionComponent.custom_renderer_type"></a>

#### custom_renderer_type

```python
@custom_renderer_type.setter
def custom_renderer_type(value: Class) -> None
```

<a id="unreal.GeometryCollectionComponent.override_custom_renderer"></a>

#### override_custom_renderer

```python
@property
def override_custom_renderer() -> bool
```

(bool):  [Read-Write] If true, CustomRendererType will be used. If false, CustomRendererType comes from the RestCollection.

<a id="unreal.GeometryCollectionComponent.override_custom_renderer"></a>

#### override_custom_renderer

```python
@override_custom_renderer.setter
def override_custom_renderer(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.use_static_mesh_collision_for_traces"></a>

#### use_static_mesh_collision_for_traces

```python
@property
def use_static_mesh_collision_for_traces() -> bool
```

(bool):  [Read-Write] todo(chaos): Remove the ability to change this at runtime, as we'll want to use this at cook time instead

<a id="unreal.GeometryCollectionComponent.use_static_mesh_collision_for_traces"></a>

#### use_static_mesh_collision_for_traces

```python
@use_static_mesh_collision_for_traces.setter
def use_static_mesh_collision_for_traces(value: bool) -> None
```

<a id="unreal.GeometryCollectionComponent.replication_abandon_cluster_level"></a>

#### replication_abandon_cluster_level

```python
@property
def replication_abandon_cluster_level() -> int
```

(int32):  [Read-Write] If replicating - the cluster level to stop sending corrections for geometry collection chunks.
recommended for smaller leaf levels when the size of the objects means they are no longer
gameplay relevant to cut down on required bandwidth to update a collection.
See: bEnableAbandonAfterLevel
deprecated: GeometryCollection now uses ReplicationAbandonAfterLevel instead of ReplicationAbandonClusterLevel.

<a id="unreal.GeometryCollectionComponent.replication_abandon_cluster_level"></a>

#### replication_abandon_cluster_level

```python
@replication_abandon_cluster_level.setter
def replication_abandon_cluster_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.collision_profile_per_level"></a>

#### collision_profile_per_level

```python
@property
def collision_profile_per_level() -> Array[Name]
```

(Array[Name]):  [Read-Write] A per-level collision profile name. If the name is set to NONE or an invalid collision profile, nothing will be changed.
If the there are more levels than elements in this array, then each level will use the index that best matches it.
For example, if the particle is level 2, and there is only 1 element in the array, then the particle will use the 0th
collision profile. AbandonedCollisionProfileName will override this on the client when relevant.

<a id="unreal.GeometryCollectionComponent.collision_profile_per_level"></a>

#### collision_profile_per_level

```python
@collision_profile_per_level.setter
def collision_profile_per_level(value: Array[Name]) -> None
```

<a id="unreal.GeometryCollectionComponent.replication_abandon_after_level"></a>

#### replication_abandon_after_level

```python
@property
def replication_abandon_after_level() -> int
```

(int32):  [Read-Write] If replicating - the cluster level after which replication will not happen
see: bEnableAbandonAfterLevel

<a id="unreal.GeometryCollectionComponent.replication_abandon_after_level"></a>

#### replication_abandon_after_level

```python
@replication_abandon_after_level.setter
def replication_abandon_after_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.replication_max_position_and_velocity_correction_level"></a>

#### replication_max_position_and_velocity_correction_level

```python
@property
def replication_max_position_and_velocity_correction_level() -> int
```

(int32):  [Read-Write] If replicating - the maximum level where clusters will have their position and velocity send over to the client for tracking and correcting
When breaking, client will only receive the initial break velocity
This helps save bandwidth where only the destruction state of the GC is to be replicated but the falling pieces do not need to be tracked precisely
note: This will have an effect only if set to a value less than ReplicationAbandonAfterLevel
see: ReplicationAbandonAfterLevel

<a id="unreal.GeometryCollectionComponent.replication_max_position_and_velocity_correction_level"></a>

#### replication_max_position_and_velocity_correction_level

```python
@replication_max_position_and_velocity_correction_level.setter
def replication_max_position_and_velocity_correction_level(value: int) -> None
```

<a id="unreal.GeometryCollectionComponent.angular_ether_drag"></a>

#### angular_ether_drag

```python
@property
def angular_ether_drag() -> float
```

(float):  [Read-Write] Uniform angular ether drag.
deprecated: Use PhysicalMaterial instead.

<a id="unreal.GeometryCollectionComponent.angular_ether_drag"></a>

#### angular_ether_drag

```python
@angular_ether_drag.setter
def angular_ether_drag(value: float) -> None
```

<a id="unreal.GeometryCollectionComponent.set_root_proxy_component_space_transform"></a>

#### set_root_proxy_component_space_transform

```python
def set_root_proxy_component_space_transform(
        index: int, root_proxy_transform: Transform) -> None
```

x.set_root_proxy_component_space_transform(index, root_proxy_transform) -> None
blueprint function to set a specific root proxy local transform
warning: when called from C++ and calling it on multiple root proxies it is recommended to use SetRootProxyLocalTransform instead and then call RefreshCustomRenderer
to avoid the cost of refreshing the renderer each time

Args:
    index (int32): 
    root_proxy_transform (Transform):

<a id="unreal.GeometryCollectionComponent.set_rest_collection"></a>

#### set_rest_collection

```python
def set_rest_collection(rest_collection_in: GeometryCollection,
                        apply_asset_defaults: bool = True) -> None
```

x.set_rest_collection(rest_collection_in, apply_asset_defaults=True) -> None
RestCollection

Args:
    rest_collection_in (GeometryCollection): 
    apply_asset_defaults (bool):

<a id="unreal.GeometryCollectionComponent.set_per_particle_collision_profile_name"></a>

#### set_per_particle_collision_profile_name

```python
def set_per_particle_collision_profile_name(bone_ids: Array[int],
                                            profile_name: Name) -> None
```

x.set_per_particle_collision_profile_name(bone_ids, profile_name) -> None
Set Per Particle Collision Profile Name

Args:
    bone_ids (Array[int32]): 
    profile_name (Name):

<a id="unreal.GeometryCollectionComponent.set_per_level_collision_profile_names"></a>

#### set_per_level_collision_profile_names

```python
def set_per_level_collision_profile_names(profile_names: Array[Name]) -> None
```

x.set_per_level_collision_profile_names(profile_names) -> None
Set Per Level Collision Profile Names

Args:
    profile_names (Array[Name]):

<a id="unreal.GeometryCollectionComponent.set_notify_removals"></a>

#### set_notify_removals

```python
def set_notify_removals(new_notify_removals: bool) -> None
```

x.set_notify_removals(new_notify_removals) -> None
Changes whether or not this component will get future removal notifications.

Args:
    new_notify_removals (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_global_removals"></a>

#### set_notify_global_removals

```python
def set_notify_global_removals(new_notify_global_removals: bool) -> None
```

x.set_notify_global_removals(new_notify_global_removals) -> None
Changes whether or not this component will get future global removal notifications.

Args:
    new_notify_global_removals (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_global_crumblings"></a>

#### set_notify_global_crumblings

```python
def set_notify_global_crumblings(
        new_notify_global_crumblings: bool,
        global_new_crumbling_event_includes_children: bool) -> None
```

x.set_notify_global_crumblings(new_notify_global_crumblings, global_new_crumbling_event_includes_children) -> None
Changes whether or not this component will get future global crumbling notifications.

Args:
    new_notify_global_crumblings (bool): 
    global_new_crumbling_event_includes_children (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_global_collision"></a>

#### set_notify_global_collision

```python
def set_notify_global_collision(new_notify_global_collisions: bool) -> None
```

x.set_notify_global_collision(new_notify_global_collisions) -> None
Changes whether or not this component will get future global collision notifications.

Args:
    new_notify_global_collisions (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_global_breaks"></a>

#### set_notify_global_breaks

```python
def set_notify_global_breaks(new_notify_global_breaks: bool) -> None
```

x.set_notify_global_breaks(new_notify_global_breaks) -> None
Changes whether or not this component will get future global break notifications.

Args:
    new_notify_global_breaks (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_crumblings"></a>

#### set_notify_crumblings

```python
def set_notify_crumblings(
        new_notify_crumblings: bool,
        new_crumbling_event_includes_children: bool = False) -> None
```

x.set_notify_crumblings(new_notify_crumblings, new_crumbling_event_includes_children=False) -> None
Changes whether or not this component will get future crumbling notifications.

Args:
    new_notify_crumblings (bool): 
    new_crumbling_event_includes_children (bool):

<a id="unreal.GeometryCollectionComponent.set_notify_breaks"></a>

#### set_notify_breaks

```python
def set_notify_breaks(new_notify_breaks: bool) -> None
```

x.set_notify_breaks(new_notify_breaks) -> None
Changes whether or not this component will get future break notifications.

Args:
    new_notify_breaks (bool):

<a id="unreal.GeometryCollectionComponent.set_local_rest_transforms"></a>

#### set_local_rest_transforms

```python
def set_local_rest_transforms(transforms: Array[Transform],
                              only_leaves: bool) -> None
```

x.set_local_rest_transforms(transforms, only_leaves) -> None
Set the local rest transform, this may be different from the rest collection
If the geometry collection is already simulating those matrices will be overriden by the physics state updates

Args:
    transforms (Array[Transform]): 
    only_leaves (bool):

<a id="unreal.GeometryCollectionComponent.set_enable_damage_from_collision"></a>

#### set_enable_damage_from_collision

```python
def set_enable_damage_from_collision(value: bool) -> None
```

x.set_enable_damage_from_collision(value) -> None
Set Enable Damage from Collision

Args:
    value (bool):

<a id="unreal.GeometryCollectionComponent.set_anchored_by_transformed_box"></a>

#### set_anchored_by_transformed_box

```python
def set_anchored_by_transformed_box(box: Box,
                                    transform: Transform,
                                    anchored: bool,
                                    max_level: int = -1) -> None
```

x.set_anchored_by_transformed_box(box, transform, anchored, max_level=-1) -> None
Set all pieces within a world transformed bounding box to be anchored or not

Args:
    box (Box): 
    transform (Transform): 
    anchored (bool): 
    max_level (int32):

<a id="unreal.GeometryCollectionComponent.set_anchored_by_index"></a>

#### set_anchored_by_index

```python
def set_anchored_by_index(index: int, anchored: bool) -> None
```

x.set_anchored_by_index(index, anchored) -> None
Set a piece or cluster to be anchored or not

Args:
    index (int32): 
    anchored (bool):

<a id="unreal.GeometryCollectionComponent.set_anchored_by_box"></a>

#### set_anchored_by_box

```python
def set_anchored_by_box(world_space_box: Box,
                        anchored: bool,
                        max_level: int = -1) -> None
```

x.set_anchored_by_box(world_space_box, anchored, max_level=-1) -> None
Set all pieces within a world space bounding box to be anchored or not

Args:
    world_space_box (Box): 
    anchored (bool): 
    max_level (int32):

<a id="unreal.GeometryCollectionComponent.set_abandoned_particle_collision_profile_name"></a>

#### set_abandoned_particle_collision_profile_name

```python
def set_abandoned_particle_collision_profile_name(
        collision_profile: Name) -> None
```

x.set_abandoned_particle_collision_profile_name(collision_profile) -> None
Set Abandoned Particle Collision Profile Name

Args:
    collision_profile (Name):

<a id="unreal.GeometryCollectionComponent.remove_all_anchors"></a>

#### remove_all_anchors

```python
def remove_all_anchors() -> None
```

x.remove_all_anchors() -> None
this will remove anchors on all the pieces ( including the static and kinematic initial states ones ) of the geometry colection

<a id="unreal.GeometryCollectionComponent.receive_physics_collision"></a>

#### receive_physics_collision

```python
def receive_physics_collision(
        collision_info: ChaosPhysicsCollisionInfo) -> None
```

x.receive_physics_collision(collision_info) -> None
Receive Physics Collision

Args:
    collision_info (ChaosPhysicsCollisionInfo):

<a id="unreal.GeometryCollectionComponent.is_root_broken"></a>

#### is_root_broken

```python
def is_root_broken() -> bool
```

x.is_root_broken() -> bool
return true if the root cluster is not longer active at runtime

Returns:
    bool:

<a id="unreal.GeometryCollectionComponent.get_root_initial_transform"></a>

#### get_root_initial_transform

```python
def get_root_initial_transform() -> Transform
```

x.get_root_initial_transform() -> Transform
Get the root item initial transform in world space

Returns:
    Transform:

<a id="unreal.GeometryCollectionComponent.get_root_index"></a>

#### get_root_index

```python
def get_root_index() -> int
```

x.get_root_index() -> int32
Get the root item index of the hierarchy

Returns:
    int32:

<a id="unreal.GeometryCollectionComponent.get_root_current_transform"></a>

#### get_root_current_transform

```python
def get_root_current_transform() -> Transform
```

x.get_root_current_transform() -> Transform
Get the root item current world transform

Returns:
    Transform:

<a id="unreal.GeometryCollectionComponent.get_mass_and_extents"></a>

#### get_mass_and_extents

```python
def get_mass_and_extents(item_index: int) -> Tuple[float, Box]
```

x.get_mass_and_extents(item_index) -> (out_mass=float, out_extents=Box)
Get mass and extent of a specific piece

Args:
    item_index (int32): item index ( from HitResult) of the cluster to get level from

Returns:
    tuple: 

    out_mass (float): 

    out_extents (Box):

<a id="unreal.GeometryCollectionComponent.get_local_rest_transforms"></a>

#### get_local_rest_transforms

```python
def get_local_rest_transforms(
        initial_transforms: bool = False) -> Array[Transform]
```

x.get_local_rest_transforms(initial_transforms=False) -> Array[Transform]
Get the rest transforms in component (local) space  space,
if none have been set by SetLocalRestTransforms or if RestTransform property is empty , then the initial ones are returned

Args:
    initial_transforms (bool): 

Returns:
    Array[Transform]:

<a id="unreal.GeometryCollectionComponent.get_local_bounds"></a>

#### get_local_bounds

```python
def get_local_bounds() -> Box
```

x.get_local_bounds() -> Box
Get local bounds of the geometry collection

Returns:
    Box:

<a id="unreal.GeometryCollectionComponent.get_initial_local_rest_transforms"></a>

#### get_initial_local_rest_transforms

```python
def get_initial_local_rest_transforms() -> Array[Transform]
```

x.get_initial_local_rest_transforms() -> Array[Transform]
Get the initial rest transforms in component (local) space  space,
they are the transforms as defined in the rest collection asset

Returns:
    Array[Transform]:

<a id="unreal.GeometryCollectionComponent.get_initial_level"></a>

#### get_initial_level

```python
def get_initial_level(item_index: int) -> int
```

x.get_initial_level(item_index) -> int32
Get the initial level of a specific piece
Initial level means the level as it is in the unbroken state

Args:
    item_index (int32): item index ( from HitResult) of the cluster to get level from

Returns:
    int32:

<a id="unreal.GeometryCollectionComponent.get_debug_info"></a>

#### get_debug_info

```python
def get_debug_info() -> str
```

x.get_debug_info() -> str
RestCollection

Returns:
    str:

<a id="unreal.GeometryCollectionComponent.force_broken_for_custom_renderer"></a>

#### force_broken_for_custom_renderer

```python
def force_broken_for_custom_renderer(force_broken: bool) -> None
```

x.force_broken_for_custom_renderer(force_broken) -> None
Force any custom renderer to render using the broken/decayed path. This can be set at runtime

Args:
    force_broken (bool):

<a id="unreal.GeometryCollectionComponent.enable_root_proxy_for_custom_renderer"></a>

#### enable_root_proxy_for_custom_renderer

```python
def enable_root_proxy_for_custom_renderer(enable: bool) -> None
```

x.enable_root_proxy_for_custom_renderer(enable) -> None
Enable Root Proxy for Custom Renderer
deprecated: Please use ForceBrokenForCustomRenderer() instead

Args:
    enable (bool):

<a id="unreal.GeometryCollectionComponent.crumble_cluster"></a>

#### crumble_cluster

```python
def crumble_cluster(item_index: int) -> None
```

x.crumble_cluster(item_index) -> None
Crumbe a cluster into all its pieces

Args:
    item_index (int32): item index ( from HitResult) of the cluster to crumble

<a id="unreal.GeometryCollectionComponent.crumble_active_clusters"></a>

#### crumble_active_clusters

```python
def crumble_active_clusters() -> None
```

x.crumble_active_clusters() -> None
Crumbe active clusters for this entire geometry collection
this will apply to internal and regular clusters

<a id="unreal.GeometryCollectionComponent.apply_physics_field"></a>

#### apply_physics_field

```python
def apply_physics_field(enabled: bool,
                        target: GeometryCollectionPhysicsTypeEnum,
                        meta_data: FieldSystemMetaData,
                        field: FieldNodeBase) -> None
```

x.apply_physics_field(enabled, target, meta_data, field) -> None
AddPhysicsField
  This function will dispatch a command to the physics thread to apply
  a generic evaluation of a user defined transient field network. See documentation,
  for examples of how to recreate variations of the above generic
  fields using field networks

Args:
    enabled (bool): Is this force enabled for evaluation.
    target (GeometryCollectionPhysicsTypeEnum): Type of field supported by the solver.
    meta_data (FieldSystemMetaData): Meta data used to assist in evaluation
    field (FieldNodeBase): Base evaluation node for the field network.

<a id="unreal.GeometryCollectionComponent.apply_linear_velocity"></a>

#### apply_linear_velocity

```python
def apply_linear_velocity(item_index: int, linear_velocity: Vector) -> None
```

x.apply_linear_velocity(item_index, linear_velocity) -> None
Apply linear velocity on specific piece

Args:
    item_index (int32): item index ( from HitResult) of the piece to apply velocity on
    linear_velocity (Vector): linear velocity to apply

<a id="unreal.GeometryCollectionComponent.apply_kinematic_field"></a>

#### apply_kinematic_field

```python
def apply_kinematic_field(radius: float, position: Vector) -> None
```

x.apply_kinematic_field(radius, position) -> None
SetDynamicState
  This function will dispatch a command to the physics thread to apply
  a kinematic to dynamic state change for the geo collection particles within the field.

Args:
    radius (float): Radial influence from the position
    position (Vector): The location of the command

<a id="unreal.GeometryCollectionComponent.apply_internal_strain"></a>

#### apply_internal_strain

```python
def apply_internal_strain(item_index: int,
                          location: Vector,
                          radius: float = 0.000000,
                          propagation_depth: int = 0,
                          propagation_factor: float = 1.000000,
                          strain: float = 0.000000) -> None
```

x.apply_internal_strain(item_index, location, radius=0.000000, propagation_depth=0, propagation_factor=1.000000, strain=0.000000) -> None
Apply an internal strain to specific piece of the geometry collection

Args:
    item_index (int32): item index ( from HitResult) of the piece to apply strain on
    location (Vector): world location of where to apply the strain
    radius (float): radius from the location point to apply the strain to ( using the center of mass of the pieces )
    propagation_depth (int32): How many level of connection to follow to propagate the strain through
    propagation_factor (float): when using propagation, the factor to multiply the strain from one level to the other, allowing falloff effect
    strain (float): strain / damage to apply

<a id="unreal.GeometryCollectionComponent.apply_external_strain"></a>

#### apply_external_strain

```python
def apply_external_strain(item_index: int,
                          location: Vector,
                          radius: float = 0.000000,
                          propagation_depth: int = 0,
                          propagation_factor: float = 1.000000,
                          strain: float = 0.000000) -> None
```

x.apply_external_strain(item_index, location, radius=0.000000, propagation_depth=0, propagation_factor=1.000000, strain=0.000000) -> None
Apply an external strain to specific piece of the geometry collection

Args:
    item_index (int32): item index ( from HitResult) of the piece to apply strain on
    location (Vector): world location of where to apply the strain
    radius (float): radius from the location point to apply the strain to ( using the center of mass of the pieces )
    propagation_depth (int32): How many level of connection to follow to propagate the strain through
    propagation_factor (float): when using propagation, the factor to multiply the strain from one level to the other, allowing falloff effect
    strain (float): strain / damage to apply

<a id="unreal.GeometryCollectionComponent.apply_breaking_linear_velocity"></a>

#### apply_breaking_linear_velocity

```python
def apply_breaking_linear_velocity(item_index: int,
                                   linear_velocity: Vector) -> None
```

x.apply_breaking_linear_velocity(item_index, linear_velocity) -> None
Apply linear velocity on breaking pieces for a specific cluster
If ItemIndex does not represent a cluster this will do nothing

Args:
    item_index (int32): item index ( from HitResult) of the cluster owning the breaking pieces to apply velocity on
    linear_velocity (Vector): linear velocity to apply

<a id="unreal.GeometryCollectionComponent.apply_breaking_angular_velocity"></a>

#### apply_breaking_angular_velocity

```python
def apply_breaking_angular_velocity(item_index: int,
                                    angular_velocity: Vector) -> None
```

x.apply_breaking_angular_velocity(item_index, angular_velocity) -> None
Apply linear velocity on breaking pieces for a specific cluster
If ItemIndex does not represent a cluster this will do nothing

Args:
    item_index (int32): item index ( from HitResult) of the cluster owning the breaking pieces to apply velocity on
    angular_velocity (Vector): linear velocity to apply

<a id="unreal.GeometryCollectionComponent.apply_asset_defaults"></a>

#### apply_asset_defaults

```python
def apply_asset_defaults() -> None
```

x.apply_asset_defaults() -> None
Apply default values from asset ( damage related data and physics material )

<a id="unreal.GeometryCollectionComponent.apply_angular_velocity"></a>

#### apply_angular_velocity

```python
def apply_angular_velocity(item_index: int, angular_velocity: Vector) -> None
```

x.apply_angular_velocity(item_index, angular_velocity) -> None
Apply angular velocity on specific piece

Args:
    item_index (int32): item index ( from HitResult) of the piece to apply velocity on
    angular_velocity (Vector): linear velocity to apply

<a id="unreal.GeometryCollectionDebugDrawActor"></a>