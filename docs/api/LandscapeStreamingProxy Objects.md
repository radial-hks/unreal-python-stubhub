## LandscapeStreamingProxy Objects

```python
class LandscapeStreamingProxy(LandscapeProxy)
```

Landscape Streaming Proxy

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeStreamingProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``affect_distance_field_lighting`` (bool):  [Read-Write] Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. *
- ``affect_dynamic_indirect_lighting`` (bool):  [Read-Write] Controls whether the primitive should influence indirect lighting.
- ``affect_indirect_lighting_while_hidden`` (bool):  [Read-Write] Controls whether the primitive should affect indirect lighting when hidden. This flag is only used if bAffectDynamicIndirectLighting is true.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``bake_material_position_offset_into_collision`` (bool):  [Read-Write] Whether to bake the landscape material's vertical world position offset into the collision heightfield.
                Note: Only z (vertical) offset is supported. XY offsets are ignored.
                Does not work with an XY offset map (mesh collision)
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``body_instance`` (BodyInstance):  [Read-Write] Collision profile settings for this landscape
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``cast_contact_shadow`` (bool):  [Read-Write] Whether the object should cast contact shadows. This flag is only used if CastShadow is true.
- ``cast_dynamic_shadow`` (bool):  [Read-Write] Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. *
- ``cast_far_shadow`` (bool):  [Read-Write] When enabled, the component will be rendering into the far shadow cascades(only for directional lights).  This flag is only used if CastShadow is true.
- ``cast_hidden_shadow`` (bool):  [Read-Write] If true, the primitive will cast shadows even if bHidden is true.  Controls whether the primitive should cast shadows when hidden.  This flag is only used if CastShadow is true.
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the primitive component should cast a shadow or not.
- ``cast_shadow_as_two_sided`` (bool):  [Read-Write] Whether this primitive should cast dynamic shadows as if it were a two sided material.  This flag is only used if CastShadow is true.
- ``cast_static_shadow`` (bool):  [Read-Write] Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true.
- ``collision_mip_level`` (int32):  [Read-Write] Landscape LOD to use for collision tests. Higher numbers use less memory and process faster, but are much less accurate
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_phys_material`` (PhysicalMaterial):  [Read-Write] Default physical material, used when no per-layer values physical materials
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_nanite`` (bool):  [Read-Write] Use Nanite to render landscape as a mesh on supported platforms.
- ``export_lod`` (int32):  [Read-Write] LOD level to use when exporting the landscape to obj or FBX
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``fill_collision_under_landscape_for_navmesh`` (bool):  [Read-Write] Set to true to prevent navmesh generation under the terrain geometry
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events`` (bool):  [Read-Write] If true, Landscape will generate overlap events when other components are overlapping it (eg Begin Overlap).
  Both the Landscape and the other component must have this flag enabled for overlap events to occur.
  see: [Overlap Events](https://docs.unrealengine.com/InteractiveExperiences/Physics/Collision/Overview#overlapandgenerateoverlapevents)
  see: UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap()
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``hlod_material_override`` (MaterialInterface):  [Read-Write] Specify a custom HLOD material to apply to the HLOD mesh. Specifying an HLOD Material Override will result in no texture being baked for the HLOD mesh.
- ``hlod_mesh_source_lod`` (int32):  [Read-Write] Specify which LOD to use for the HLOD mesh if HLODMeshSourceLODPolicy is set to SpecificLOD.
- ``hlod_mesh_source_lod_policy`` (LandscapeHLODMeshSourceLODPolicy):  [Read-Write] Specify how to choose the LOD used as input for the HLOD mesh.
- ``hlod_texture_size`` (int32):  [Read-Write] Specify the texture size to use for the HLOD mesh if HLODTextureSizePolicy is set to SpecificSize. Specifying an HLOD Material Override will disable this option as no texture will be baked.
- ``hlod_texture_size_policy`` (LandscapeHLODTextureSizePolicy):  [Read-Write] Specify how to choose the texture size of the resulting HLOD mesh. Specifying an HLOD Material Override will disable this option as no texture will be baked.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires the project settings "Alpha Output" and "Support Primitive Alpha Holdout".
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``landscape_actor_ref`` (Landscape):  [Read-Write]
- ``landscape_hole_material`` (MaterialInterface):  [Read-Write] Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque)
- ``landscape_material`` (MaterialInterface):  [Read-Write] Combined material used to render the landscape
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``ld_max_draw_distance`` (float):  [Read-Write] Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object.
- ``lighting_channels`` (LightingChannels):  [Read-Write] Channels that this Landscape should be in.  Lights with matching channels will affect the Landscape.
  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing.
- ``lightmass_settings`` (LightmassPrimitiveSettings):  [Read-Write] The Lightmass settings for this object.
- ``lod0_distribution_setting`` (float):  [Read-Write] The distribution setting used to change the LOD 0 generation, 1.25 is the normal distribution, numbers influence directly the LOD0 proportion on screen.
- ``lod0_screen_size`` (float):  [Read-Write] This is the starting screen size used to calculate the distribution. You can increase the value if you want less LOD0 component, and you use very large landscape component.
- ``lod_blend_range`` (float):  [Read-Write] This controls the area that blends LOD between neighboring sections. At 1.0 it blends across the entire section, and lower numbers reduce the blend region to be closer to the boundary.
- ``lod_distribution_setting`` (float):  [Read-Write] The distribution setting used to change the LOD generation, 3 is the normal distribution, small number mean you want your last LODs to take more screen space and big number mean you want your first LODs to take more screen space.
- ``lod_group_key`` (uint32):  [Read-Write] Specifies the LOD Group (Zero is No Group). All landscapes in the same group calculate their LOD together, allowing matching border LODs to fix geometry seams.
- ``max_lod_level`` (int32):  [Read-Write] Max LOD level to use when rendering, -1 means the max available
- ``max_painted_layers_per_component`` (int32):  [Read-Write]
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``nanite_lod_index`` (int32):  [Read-Write] LOD level of the landscape when generating the Nanite mesh. Mostly there for debug reasons, since Nanite is meant to allow high density meshes, we want to use 0 most of the times.
- ``nanite_max_edge_length_factor`` (float):  [Read-Write]
- ``nanite_position_precision`` (int32):  [Read-Write]
- ``nanite_skirt_depth`` (float):  [Read-Write]
- ``nanite_skirt_enabled`` (bool):  [Read-Write]
- ``navigation_geometry_gathering_mode`` (NavDataGatheringMode):  [Read-Write]
- ``negative_z_bounds_extension`` (float):  [Read-Write] Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
  Extension value in the negative Z axis, positive value increases bound size
  Note that this can also be overridden per-component when the component is selected with the component select tool
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``non_nanite_virtual_shadow_map_constant_depth_bias`` (float):  [Read-Write] Constant bias to handle the worst artifacts of the continuous LOD morphing when rendering to VSM.
  Only applies when using non-Nanite landscape and VSM.
- ``non_nanite_virtual_shadow_map_invalidation_height_error_threshold`` (float):  [Read-Write] For non-Nanite landscape, cached VSM pages need to be invalidated when continuous LOD morphing introduces a height difference that is too large between the current landscape component's profile and the one that was used when the shadow was shadow was last cached.
  This height threshold (in Unreal units) controls this invalidation rate (a smaller threshold will reduce the likeliness of shadow artifacts, but will make the invalidations occur more frequently, which is not desirable in terms of performance.
  Disabled if 0.0.
  Only applies when using non-Nanite landscape and VSM.
- ``non_nanite_virtual_shadow_map_invalidation_screen_size_limit`` (float):  [Read-Write] Screen size under which VSM invalidation stops occurring.
  As the height difference between 2 mip levels increases when the LOD level increases (because of undersampling), VSM pages tend to be invalidated more frequently even though it's getting less and less relevant to do so, since this will mean that the screen size of the landscape section decreases, thus the artifacts actually become less noticeable.
  We therefore artificially attenuate the VSM invalidation rate as the screen size decreases, to avoid invalidating VSM pages too often, as it becomes less and less impactful.
  A higher value will accentuate this attenuation (better performance but more artifacts) and vice versa.
  If 0.0, the attenuation of the VSM invalidation rate will be disabled entirely.
  Only applies when using non-Nanite landscape and VSM.
- ``on_actor_begin_overlap`` (ActorBeginOverlapSignature):  [Read-Write] Called when another actor begins to overlap this actor, for example a player walking into a trigger.
  For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_end_overlap`` (ActorEndOverlapSignature):  [Read-Write] Called when another actor stops overlapping this actor.
  note: Components on both this and the other Actor must have bGenerateOverlapEvents set to true to generate overlap events.
- ``on_actor_hit`` (ActorHitSignature):  [Read-Write] Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.
  note: For collisions during physics simulation to generate hit events, 'Simulation Generates Hit Events' must be enabled.
- ``on_begin_cursor_over`` (ActorBeginCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.
- ``on_clicked`` (ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.
- ``on_destroyed`` (ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``per_lod_override_materials`` (Array[LandscapePerLODMaterialOverride]):  [Read-Write]
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``positive_z_bounds_extension`` (float):  [Read-Write] Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
  Extension value in the positive Z axis, positive value increases bound size
  Note that this can also be overridden per-component when the component is selected with the component select tool
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
- ``render_custom_depth`` (bool):  [Read-Write] If true, the Landscape will be rendered in the CustomDepth pass (usually used for outlines)
- ``replay_rewindable`` (bool):  [Read-Write] If true, this actor will only be destroyed during scrubbing if the replay is set to a time before the actor existed.
  Otherwise, RewindForReplay will be called if we detect the actor needs to be reset.
  Note, this Actor must not be destroyed by gamecode, and RollbackViaDeletion may not be used.
- ``replicate_movement`` (bool):  [Read-Write] If true, replicate movement/location related properties.
  Actor must also be set to replicate.
  see: SetReplicates()
  see: https://docs.unrealengine.com/InteractiveExperiences/Networking/Actors
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects and the replicated actor components list
  When false the replication system will instead call the virtual ReplicateSubobjects() function where the subobjects and actor components need to be manually replicated.
- ``replicated_movement`` (RepMovement):  [Read-Write] Used for replication of our RootComponent's position and velocity
- ``replicates`` (bool):  [Read-Write] If true, this actor will replicate to remote machines
  see: SetReplicates()
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``runtime_virtual_textures`` (Array[RuntimeVirtualTexture]):  [Read-Write] Array of runtime virtual textures into which we draw this landscape.
  The material also needs to be set up to output to a virtual texture.
- ``scalable_lod0_distribution_setting`` (PerQualityLevelFloat):  [Read-Write] Scalable (per-quality) version of 'LOD 0'.
- ``scalable_lod0_screen_size`` (PerQualityLevelFloat):  [Read-Write] Scalable (per-quality) version of 'LOD 0 Screen Size'.
- ``scalable_lod_distribution_setting`` (PerQualityLevelFloat):  [Read-Write] Scalable (per-quality) version of 'Other LODs'.
- ``set_create_runtime_virtual_texture_volumes`` (bool):  [Read-Only] Placeholder for details customization button.
- ``shadow_cache_invalidation_behavior`` (ShadowCacheInvalidationBehavior):  [Read-Write] Control shadow invalidation behavior, in particular with respect to Virtual Shadow Maps and material effects like World Position Offset.
- ``simple_collision_mip_level`` (int32):  [Read-Write] If set higher than the "Collision Mip Level", this specifies the Landscape LOD to use for "simple collision" tests, otherwise the "Collision Mip Level" is used for both simple and complex collision.
  Does not work with an XY offset map (mesh collision)
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``static_lighting_lod`` (int32):  [Read-Write] LOD level to use when running lightmass (increase to 1 or 2 for large landscapes to stop lightmass crashing)
- ``static_lighting_resolution`` (float):  [Read-Write] The resolution to cache lighting at, in texels/quad in one axis
  Total resolution would be changed by StaticLightingResolution*StaticLightingResolution
  Automatically calculate proper value for removing seams
- ``streaming_distance_multiplier`` (float):  [Read-Write] Allows artists to adjust the distance where textures using UV 0 are streamed in/out.
  1.0 is the default, whereas a higher value increases the streamed-in resolution.
  Value can be < 0 (from legcay content, or code changes)
- ``strip_grass_when_cooked_client`` (bool):  [Read-Write] Strip Grass data when cooked for client
- ``strip_grass_when_cooked_server`` (bool):  [Read-Write] Strip Grass data when cooked for server
- ``strip_physics_when_cooked_client`` (bool):  [Read-Write] Strip Physics/collision components when cooked for client
- ``strip_physics_when_cooked_server`` (bool):  [Read-Write] Strip Physics/collision components when cooked for server
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``target_layers`` (Map[Name, LandscapeTargetLayerSettings]):  [Read-Only]
- ``update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Write] Condition for calling UpdateOverlaps() to initialize overlap state when loaded in during level streaming.
  If set to 'UseConfigDefault', the default specified in ini (displayed in 'DefaultUpdateOverlapsMethodDuringLevelStreaming') will be used.
  If overlaps are not initialized, this actor and attached components will not have an initial state of what objects are touching it,
  and overlap events may only come in once one of those objects update overlaps themselves (for example when moving).
  However if an object touching it *does* initialize state, both objects will know about their touching state with each other.
  This can be a potentially large performance savings during level loading and streaming, and is safe if the object and others initially
  overlapping it do not need the overlap state because they will not trigger overlap notifications.

  Note that if 'bGenerateOverlapEventsDuringLevelStreaming' is true, overlaps are always updated in this case, but that flag
  determines whether the Begin/End overlap events are triggered.
  see: bGenerateOverlapEventsDuringLevelStreaming, DefaultUpdateOverlapsMethodDuringLevelStreaming, GetUpdateOverlapsMethodDuringLevelStreaming()
- ``use_compressed_heightmap_storage`` (bool):  [Read-Write] Enable compressed heightmap texture storage.
- ``use_dynamic_material_instance`` (bool):  [Read-Write] When set to true it will generate MaterialInstanceDynamic for each components, so material can be changed at runtime
- ``use_landscape_for_culling_invisible_hlod_vertices`` (bool):  [Read-Write] Flag whether or not this Landscape's surface can be used for culling hidden triangles *
- ``use_material_position_offset_in_static_lighting`` (bool):  [Read-Write] Whether to use the landscape material's vertical world position offset when calculating static lighting.
  Note: Only z (vertical) offset is supported. XY offsets are ignored.
  Does not work correctly with an XY offset map (mesh collision)
- ``use_scalable_lod_settings`` (bool):  [Read-Write] Allows to specify LOD distribution settings per quality level. Using this will ignore the r.LandscapeLOD0DistributionScale CVar.
- ``used_for_navigation`` (bool):  [Read-Write] Hints navigation system whether this landscape will ever be navigated on. true by default, but make sure to set it to false for faraway, background landscapes
- ``virtual_texture_lod_bias`` (int32):  [Read-Write] Bias to the LOD selected for rendering to runtime virtual textures.
  Higher values reduce vertex count when rendering to the runtime virtual texture.
- ``virtual_texture_num_lods`` (int32):  [Read-Write] Number of mesh levels to use when rendering landscape into runtime virtual texture.
  Lower values reduce vertex count when rendering to the runtime virtual texture but decrease accuracy when using values that require vertex interpolation.
- ``virtual_texture_render_pass_type`` (RuntimeVirtualTextureMainPassType):  [Read-Write] Controls if this component draws in the main pass as well as in the virtual texture.
- ``virtual_texture_render_with_quad`` (bool):  [Read-Write] Use a single quad to render this landscape to runtime virtual texture pages.
  This is the fastest path but it only gives correct results if the runtime virtual texture orientation is aligned with the landscape.
  If the two are unaligned we need to render to the virtual texture using LODs with sufficient density.
- ``virtual_texture_render_with_quad_hq`` (bool):  [Read-Write] Use highest quality heightmap interpolation when using a single quad to render this landscape to runtime virtual texture pages.
  This also requires the project setting: r.VT.RVT.HighQualityPerPixelHeight.

<a id="unreal.MaterialExpression"></a>