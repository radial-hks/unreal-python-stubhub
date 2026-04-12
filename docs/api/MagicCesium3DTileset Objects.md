## MagicCesium3DTileset Objects

```python
class MagicCesium3DTileset(Cesium3DTileset)
```

Magic Cesium 3DTileset

**C++ Source:**

- **Plugin**: GISCesium
- **Module**: MagicCesium
- **File**: MagicCesiumTileset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_include_tangents`` (bool):  [Read-Write] Whether to always generate a correct tangent space basis for tiles that
  don't have them.

  Normally, a per-vertex tangent space basis is only required for glTF models
  with a normal map. However, a custom, user-supplied material may need a
  tangent space basis for other purposes. When this property is set to true,
  tiles lacking an explicit tangent vector will have one computed
  automatically using the MikkTSpace algorithm. When this property is false,
  load time will be improved by skipping the generation of the tangent
  vector, but the tangent space basis will be unreliable.

  Note that a tileset with "Enable Water Mask" set will include tangents
  for tiles containing water, regardless of the value of this property.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``apply_dpi_scaling`` (ApplyDpiScaling):  [Read-Write] Scale Level-of-Detail by Display DPI. This increases the performance for
  mobile devices and high DPI screens.
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``body_instance`` (BodyInstance):  [Read-Write] Define the collision profile for all the 3D tiles created inside this
  actor.
- ``bounding_volume_pool_component`` (CesiumBoundingVolumePoolComponent):  [Read-Write] The bounding volume pool component that manages occlusion bounding volume
  proxies.
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_manager`` (CesiumCameraManager):  [Read-Write] The actor providing custom cameras for use with this Tileset.

  If this is null, the Tileset will find and use the first
  CesiumCameraManager Actor in the level, or create one if necessary. To get
  the active/effective Camera Manager from Blueprints or C++, use
  ResolvedCameraManager instead.
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``can_enable_occlusion_culling`` (bool):  [Read-Only] This mirrors
  UCesiumRuntimeSettings::EnableExperimentalOcclusionCullingFeature so that
  it can be used as an EditCondition.
- ``cast_shadow`` (bool):  [Read-Write]
- ``cesium_ion_server`` (CesiumIonServer):  [Read-Write] The Cesium ion Server from which this tileset is loaded.
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``create_nav_collision`` (bool):  [Read-Write] Whether to generate navigation collisions for this tileset.

  Enabling this option creates collisions for navigation when a 3D Tiles
  tileset is loaded. It is recommended to set "Runtime Generation" to
  "Static" in the navigation mesh settings in the project settings, as
  collision calculations become very slow.
- ``create_physics_meshes`` (bool):  [Read-Write] Whether to generate physics meshes for this tileset.

  Disabling this option will improve the performance of tile loading, but it
  will no longer be possible to collide with the tileset since the physics
  meshes will not be created.

  Physics meshes cannot be generated for primitives containing points.
- ``credit_system`` (CesiumCreditSystem):  [Read-Write] The actor managing this tileset's content attributions.

  If this is null, the Tileset will find and use the first Credit System
  Actor in the level, or create one if necessary. To get the active/effective
  Credit System from Blueprints or C++, use ResolvedCreditSystem instead.
- ``culled_screen_space_error`` (double):  [Read-Write] The screen-space error to be enforced for tiles that are outside the view
  frustum or hidden in fog.

  When "Enable Frustum Culling" and "Enable Fog Culling" are both true, tiles
  outside the view frustum or hidden in fog are effectively ignored, and so
  their level-of-detail doesn't matter. And in this scenario, this property
  is ignored.

  However, when either of those flags are false, these "would-be-culled"
  tiles continue to be processed, and the question arises of how to handle
  their level-of-detail. When "Enforce Culled Screen Space Error" is false,
  this property is ignored and refinement terminates at these tiles, no
  matter what their current screen-space error. The tiles are available for
  physics, shadows, etc., but their level-of-detail may be very low.

  When set to true, these tiles are refined until they achieve the
  screen-space error specified by this property.
- ``custom_depth_parameters`` (CustomDepthParameters):  [Read-Write]
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``delay_refinement_for_occlusion`` (bool):  [Read-Write] Whether to wait for valid occlusion results before refining tiles.

  Only applicable when EnableOcclusionCulling is enabled. When this option
  is enabled, there may be small delays before tiles are refined, but there
  may be an overall performance advantage by avoiding loads of descendants
  that will be found to be occluded.
- ``draw_tile_info`` (bool):  [Read-Write] If true, draws debug text above each tile being rendered with information
  about that tile.
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_fog_culling`` (bool):  [Read-Write] Whether to cull tiles that are occluded by fog.

  This does not refer to the atmospheric fog of the Unreal Engine,
  but to an internal representation of fog: Depending on the height
  of the camera above the ground, tiles that are far away (close to
  the horizon) will be culled when this flag is enabled.

  Note that this will always be disabled if UseLodTransitions is set to true.
- ``enable_frustum_culling`` (bool):  [Read-Write] Whether to cull tiles that are outside the frustum.

  By default this is true, meaning that tiles that are not visible with the
  current camera configuration will be ignored. It can be set to false, so
  that these tiles are still considered for loading, refinement and
  rendering.

  This will cause more tiles to be loaded, but helps to avoid holes and
  provides a more consistent mesh, which may be helpful for physics.

  Note that this will always be disabled if UseLodTransitions is set to true.
- ``enable_occlusion_culling`` (bool):  [Read-Write] Whether to cull tiles that are occluded.

  If this option is disabled, check that "Enable Experimental Occlusion
  Culling Feature" is enabled in the Plugins -> Cesium section of the Project
  Settings.

  When enabled, this feature will use Unreal's occlusion system to determine
  if tiles are actually visible on the screen. For tiles found to be
  occluded, the tile will not refine to show descendants, but it will still
  be rendered to avoid holes. This results in less tile loads and less GPU
  resource usage for dense, high-occlusion scenes like ground-level views in
  cities.

  This will not work for tilesets with poorly fit bounding volumes and cause
  more draw calls with very few extra culled tiles. When there is minimal
  occlusion in a scene, such as with terrain tilesets and applications
  focused on top-down views, this feature will yield minimal benefit and
  potentially cause needless overhead.
- ``enable_water_mask`` (bool):  [Read-Write] Whether to request and render the water mask.

  Currently only applicable for quantized-mesh tilesets that support the
  water mask extension.
- ``enforce_culled_screen_space_error`` (bool):  [Read-Write] Whether a specified screen-space error should be enforced for tiles that
  are outside the frustum or hidden in fog.

  When "Enable Frustum Culling" and "Enable Fog Culling" are both true, tiles
  outside the view frustum or hidden in fog are effectively ignored, and so
  their level-of-detail doesn't matter. And in this scenario, this property
  is ignored.

  However, when either of those flags are false, these "would-be-culled"
  tiles continue to be processed, and the question arises of how to handle
  their level-of-detail. When this property is false, refinement terminates
  at these tiles, no matter what their current screen-space error. The tiles
  are available for physics, shadows, etc., but their level-of-detail may
  be very low.

  When set to true, these tiles are refined until they achieve the specified
  "Culled Screen Space Error". This allows control over the minimum quality
  of these would-be-culled tiles.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``forbid_holes`` (bool):  [Read-Write] Whether to unrefine back to a parent tile when a child isn't done loading.

  When this is set to true, the tileset will guarantee that the tileset will
  never be rendered with holes in place of tiles that are not yet loaded,
  even though the tile that is rendered instead may have low resolution. When
  false, overall loading will be faster, but newly-visible parts of the
  tileset may initially be blank.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``generate_smooth_normals`` (bool):  [Read-Write] Whether to generate smooth normals when normals are missing in the glTF.

  According to the Gltf spec: "When normals are not specified, client
  implementations should calculate flat normals." However, calculating flat
  normals requires duplicating vertices. This option allows the gltfs to be
  sent with explicit smooth normals when the original gltf was missing
  normals.
- ``georeference`` (CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the actor's
  coordinate system relates to the coordinate system in this Unreal Engine
  level.

  If this is null, the Tileset will find and use the first Georeference
  Actor in the level, or create one if necessary. To get the active/effective
  Georeference from Blueprints or C++, use ResolvedGeoreference instead.
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignore_khr_materials_unlit`` (bool):  [Read-Write] Whether to ignore the KHR_materials_unlit extension on the glTF tiles in
  this tileset, if it exists, and instead render with standard lighting and
  shadows. This property will have no effect if the tileset does not have any
  tiles that use this extension.

  The KHR_materials_unlit extension is often applied to photogrammetry
  tilesets because lighting and shadows are already baked into their
  textures.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``ion_access_token`` (str):  [Read-Write] The access token to use to access the Cesium ion resource.
- ``ion_asset_endpoint_url`` (str):  [Read-Write]
  deprecated: Use CesiumIonServer instead.
- ``ion_asset_id`` (int64):  [Read-Write] The ID of the Cesium ion asset to use.

  This property is ignored if the Url is specified.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``lighting_channels`` (LightingChannels):  [Read-Write]
- ``load_progress`` (float):  [Read-Write]
- ``loading_descendant_limit`` (int32):  [Read-Write] The number of loading descendents a tile should allow before deciding to
  render itself instead of waiting.

  Setting this to 0 will cause each level of detail to be loaded
  successively. This will increase the overall loading time, but cause
  additional detail to appear more gradually. Setting this to a high value
  like 1000 will decrease the overall time until the desired level of detail
  is achieved, but this high-detail representation will appear at once, as
  soon as it is loaded completely.
- ``lod_transition_length`` (float):  [Read-Write] How long dithered LOD transitions between different tiles should take, in
  seconds.

  Only relevant if UseLodTransitions is true.
- ``log_selection_stats`` (bool):  [Read-Write] If true, stats about tile selection are printed to the Output Log.
- ``log_shared_asset_stats`` (bool):  [Read-Write] If true, logs stats on the assets in this tileset's shared asset system to
  the Output Log.
- ``material`` (MaterialInterface):  [Read-Write] A custom Material to use to render opaque elements in this tileset, in
  order to implement custom visual effects.

  The custom material should generally be created by copying the Material
  Instance "MI_CesiumThreeOverlaysAndClipping" and customizing the copy as
  desired.
- ``maximum_cached_bytes`` (int64):  [Read-Write]
  brief: The maximum number of bytes that may be cached. Note that this value, even if 0, will never cause tiles that are needed for rendering to be unloaded. However, if the total number of loaded bytes is greater than this value, tiles will be unloaded until the total is under this number or until only required tiles remain, whichever comes first.
- ``maximum_screen_space_error`` (double):  [Read-Write] The maximum number of pixels of error when rendering this tileset.

  This is used to select an appropriate level-of-detail: A low value
  will cause many tiles with a high level of detail to be loaded,
  causing a finer visual representation of the tiles, but with a
  higher performance cost for loading and rendering. A higher value will
  cause a coarser visual representation, with lower performance
  requirements.

  When a tileset uses the older layer.json / quantized-mesh format rather
  than 3D Tiles, this value is effectively divided by 8.0. So the default
  value of 16.0 corresponds to the standard value for quantized-mesh terrain
  of 2.0.
- ``maximum_simultaneous_tile_loads`` (int32):  [Read-Write] The maximum number of tiles that may be loaded at once.

  When new parts of the tileset become visible, the tasks to load the
  corresponding tiles are put into a queue. This value determines how
  many of these tasks are processed at the same time. A higher value
  may cause the tiles to be loaded and rendered more quickly, at the
  cost of a higher network- and processing load.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``mobility`` (ComponentMobility):  [Read-Write]
  deprecated: Use the Mobility property on the RootComponent instead.
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``occlusion_pool_size`` (int32):  [Read-Write] The number of CesiumBoundingVolumeComponents to use for querying the
  occlusion state of traversed tiles.

  Only applicable when EnableOcclusionCulling is enabled.
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
- ``on_tileset_loaded`` (CompletedLoadTrigger):  [Read-Write] A delegate that will be called whenever the tileset is fully loaded.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``point_cloud_shading`` (CesiumPointCloudShading):  [Read-Write] If this tileset contains points, their appearance can be configured with
  these point cloud shading parameters.

  These settings are not supported on mobile platforms.
- ``preload_ancestors`` (bool):  [Read-Write] Whether to preload ancestor tiles.

  Setting this to true optimizes the zoom-out experience and provides more
  detail in newly-exposed areas when panning. The down side is that it
  requires loading more tiles.
- ``preload_siblings`` (bool):  [Read-Write] Whether to preload sibling tiles.

  Setting this to true causes tiles with the same parent as a rendered tile
  to be loaded, even if they are culled. Setting this to true may provide a
  better panning experience at the cost of loading more tiles.
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relevant_for_level_bounds`` (bool):  [Read-Write] If true, this actor's component's bounds will be included in the level's
  bounding box unless the Actor's class has overridden IsLevelBoundsRelevant
- ``remote_role`` (NetRole):  [Read-Only] Describes how much control the remote machine has over the actor.
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
- ``resolved_camera_manager`` (CesiumCameraManager):  [Read-Write] The resolved Camera Manager used by this Tileset. This is not serialized
  because it may point to a Camera Manager in the PersistentLevel while this
  tileset is in a sublevel. If the CameraManager property is specified,
  however then this property will have the same value.

  This property will be null before ResolveCameraManager is called.
- ``resolved_credit_system`` (CesiumCreditSystem):  [Read-Write] The resolved Credit System used by this Tileset. This is not serialized
  because it may point to a Credit System in the PersistentLevel while this
  tileset is in a sublevel. If the CreditSystem property is specified,
  however then this property will have the same value.

  This property will be null before ResolveCreditSystem is called.
- ``resolved_georeference`` (CesiumGeoreference):  [Read-Only] The resolved georeference used by this Tileset. This is not serialized
  because it may point to a Georeference in the PersistentLevel while this
  tileset is in a sublevel. If the Georeference property is specified,
  however then this property will have the same value.

  This property will be null before ResolveGeoreference is called.
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root`` (SceneComponent):  [Read-Only]
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``show_credits_on_screen`` (bool):  [Read-Write] Whether or not to show this tileset's credits on screen.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``suspend_update`` (bool):  [Read-Write] Pauses level-of-detail and culling updates of this tileset.
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``tile_cover_color`` (LinearColor):  [Read-Write] 材质叠加颜色
- ``tileset_source`` (TilesetSource):  [Read-Write] The type of source from which to load this tileset.
- ``translucent_material`` (MaterialInterface):  [Read-Write] A custom Material to use to render translucent elements of the tileset, in
  order to implement custom visual effects.

  The custom material should generally be created by copying the Material
  Instance "MI_CesiumThreeOverlaysAndClippingTranslucent" and customizing the
  copy as desired. Make sure that its Material Property Overrides -> Blend
  Mode is set to "Translucent".
- ``update_in_editor`` (bool):  [Read-Write] If true, this tileset is ticked/updated in the editor. If false, is only
  ticked while playing (including Play-in-Editor).
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
- ``url`` (str):  [Read-Write] The URL of this tileset's "tileset.json" file.

  If this property is specified, the ion asset ID and token are ignored.
- ``use_lod_transitions`` (bool):  [Read-Write] Use a dithering effect when transitioning between tiles of different LODs.

  When this is set to true, Frustrum Culling and Fog Culling are always
  disabled.
- ``water_material`` (MaterialInterface):  [Read-Write] A custom Material to use to render this tileset in areas where the
  watermask is, in order to implement custom visual effects.
  Currently only applicable for quantized-mesh tilesets that support the
  water mask extension.

  The custom material should generally be created by copying the Material
  Instance "MI_CesiumThreeOverlaysAndClippingAndWater" and customizing the
  copy as desired.

<a id="unreal.UrbanHoudiniAssetFactory"></a>