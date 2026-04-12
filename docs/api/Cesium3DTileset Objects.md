## Cesium3DTileset Objects

```python
class Cesium3DTileset(Actor)
```

Cesium 3DTileset

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: Cesium3DTileset.h

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

<a id="unreal.Cesium3DTileset.mobility"></a>

#### mobility

```python
@property
def mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Write]
deprecated: Use the Mobility property on the RootComponent instead.

<a id="unreal.Cesium3DTileset.mobility"></a>

#### mobility

```python
@mobility.setter
def mobility(value: ComponentMobility) -> None
```

<a id="unreal.Cesium3DTileset.georeference"></a>

#### georeference

```python
@property
def georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the actor's
coordinate system relates to the coordinate system in this Unreal Engine
level.

If this is null, the Tileset will find and use the first Georeference
Actor in the level, or create one if necessary. To get the active/effective
Georeference from Blueprints or C++, use ResolvedGeoreference instead.

<a id="unreal.Cesium3DTileset.georeference"></a>

#### georeference

```python
@georeference.setter
def georeference(value: CesiumGeoreference) -> None
```

<a id="unreal.Cesium3DTileset.resolved_georeference"></a>

#### resolved\_georeference

```python
@property
def resolved_georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Only] The resolved georeference used by this Tileset. This is not serialized
because it may point to a Georeference in the PersistentLevel while this
tileset is in a sublevel. If the Georeference property is specified,
however then this property will have the same value.

This property will be null before ResolveGeoreference is called.

<a id="unreal.Cesium3DTileset.credit_system"></a>

#### credit\_system

```python
@property
def credit_system() -> CesiumCreditSystem
```

(CesiumCreditSystem):  [Read-Write] The actor managing this tileset's content attributions.

If this is null, the Tileset will find and use the first Credit System
Actor in the level, or create one if necessary. To get the active/effective
Credit System from Blueprints or C++, use ResolvedCreditSystem instead.

<a id="unreal.Cesium3DTileset.credit_system"></a>

#### credit\_system

```python
@credit_system.setter
def credit_system(value: CesiumCreditSystem) -> None
```

<a id="unreal.Cesium3DTileset.resolved_credit_system"></a>

#### resolved\_credit\_system

```python
@property
def resolved_credit_system() -> CesiumCreditSystem
```

(CesiumCreditSystem):  [Read-Only] The resolved Credit System used by this Tileset. This is not serialized
because it may point to a Credit System in the PersistentLevel while this
tileset is in a sublevel. If the CreditSystem property is specified,
however then this property will have the same value.

This property will be null before ResolveCreditSystem is called.

<a id="unreal.Cesium3DTileset.camera_manager"></a>

#### camera\_manager

```python
@property
def camera_manager() -> CesiumCameraManager
```

(CesiumCameraManager):  [Read-Write] The actor providing custom cameras for use with this Tileset.

If this is null, the Tileset will find and use the first
CesiumCameraManager Actor in the level, or create one if necessary. To get
the active/effective Camera Manager from Blueprints or C++, use
ResolvedCameraManager instead.

<a id="unreal.Cesium3DTileset.camera_manager"></a>

#### camera\_manager

```python
@camera_manager.setter
def camera_manager(value: CesiumCameraManager) -> None
```

<a id="unreal.Cesium3DTileset.resolved_camera_manager"></a>

#### resolved\_camera\_manager

```python
@property
def resolved_camera_manager() -> CesiumCameraManager
```

(CesiumCameraManager):  [Read-Only] The resolved Camera Manager used by this Tileset. This is not serialized
because it may point to a Camera Manager in the PersistentLevel while this
tileset is in a sublevel. If the CameraManager property is specified,
however then this property will have the same value.

This property will be null before ResolveCameraManager is called.

<a id="unreal.Cesium3DTileset.bounding_volume_pool_component"></a>

#### bounding\_volume\_pool\_component

```python
@property
def bounding_volume_pool_component() -> CesiumBoundingVolumePoolComponent
```

(CesiumBoundingVolumePoolComponent):  [Read-Only] The bounding volume pool component that manages occlusion bounding volume
proxies.

<a id="unreal.Cesium3DTileset.show_credits_on_screen"></a>

#### show\_credits\_on\_screen

```python
@property
def show_credits_on_screen() -> bool
```

(bool):  [Read-Write] Whether or not to show this tileset's credits on screen.

<a id="unreal.Cesium3DTileset.show_credits_on_screen"></a>

#### show\_credits\_on\_screen

```python
@show_credits_on_screen.setter
def show_credits_on_screen(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.maximum_screen_space_error"></a>

#### maximum\_screen\_space\_error

```python
@property
def maximum_screen_space_error() -> float
```

(double):  [Read-Write] The maximum number of pixels of error when rendering this tileset.

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

<a id="unreal.Cesium3DTileset.maximum_screen_space_error"></a>

#### maximum\_screen\_space\_error

```python
@maximum_screen_space_error.setter
def maximum_screen_space_error(value: float) -> None
```

<a id="unreal.Cesium3DTileset.apply_dpi_scaling"></a>

#### apply\_dpi\_scaling

```python
@property
def apply_dpi_scaling() -> ApplyDpiScaling
```

(ApplyDpiScaling):  [Read-Write] Scale Level-of-Detail by Display DPI. This increases the performance for
mobile devices and high DPI screens.

<a id="unreal.Cesium3DTileset.apply_dpi_scaling"></a>

#### apply\_dpi\_scaling

```python
@apply_dpi_scaling.setter
def apply_dpi_scaling(value: ApplyDpiScaling) -> None
```

<a id="unreal.Cesium3DTileset.preload_ancestors"></a>

#### preload\_ancestors

```python
@property
def preload_ancestors() -> bool
```

(bool):  [Read-Write] Whether to preload ancestor tiles.

Setting this to true optimizes the zoom-out experience and provides more
detail in newly-exposed areas when panning. The down side is that it
requires loading more tiles.

<a id="unreal.Cesium3DTileset.preload_ancestors"></a>

#### preload\_ancestors

```python
@preload_ancestors.setter
def preload_ancestors(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.preload_siblings"></a>

#### preload\_siblings

```python
@property
def preload_siblings() -> bool
```

(bool):  [Read-Write] Whether to preload sibling tiles.

Setting this to true causes tiles with the same parent as a rendered tile
to be loaded, even if they are culled. Setting this to true may provide a
better panning experience at the cost of loading more tiles.

<a id="unreal.Cesium3DTileset.preload_siblings"></a>

#### preload\_siblings

```python
@preload_siblings.setter
def preload_siblings(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.forbid_holes"></a>

#### forbid\_holes

```python
@property
def forbid_holes() -> bool
```

(bool):  [Read-Write] Whether to unrefine back to a parent tile when a child isn't done loading.

When this is set to true, the tileset will guarantee that the tileset will
never be rendered with holes in place of tiles that are not yet loaded,
even though the tile that is rendered instead may have low resolution. When
false, overall loading will be faster, but newly-visible parts of the
tileset may initially be blank.

<a id="unreal.Cesium3DTileset.forbid_holes"></a>

#### forbid\_holes

```python
@forbid_holes.setter
def forbid_holes(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.maximum_simultaneous_tile_loads"></a>

#### maximum\_simultaneous\_tile\_loads

```python
@property
def maximum_simultaneous_tile_loads() -> int
```

(int32):  [Read-Write] The maximum number of tiles that may be loaded at once.

When new parts of the tileset become visible, the tasks to load the
corresponding tiles are put into a queue. This value determines how
many of these tasks are processed at the same time. A higher value
may cause the tiles to be loaded and rendered more quickly, at the
cost of a higher network- and processing load.

<a id="unreal.Cesium3DTileset.maximum_simultaneous_tile_loads"></a>

#### maximum\_simultaneous\_tile\_loads

```python
@maximum_simultaneous_tile_loads.setter
def maximum_simultaneous_tile_loads(value: int) -> None
```

<a id="unreal.Cesium3DTileset.maximum_cached_bytes"></a>

#### maximum\_cached\_bytes

```python
@property
def maximum_cached_bytes() -> int
```

(int64):  [Read-Write]
brief: The maximum number of bytes that may be cached. Note that this value, even if 0, will never cause tiles that are needed for rendering to be unloaded. However, if the total number of loaded bytes is greater than this value, tiles will be unloaded until the total is under this number or until only required tiles remain, whichever comes first.

<a id="unreal.Cesium3DTileset.maximum_cached_bytes"></a>

#### maximum\_cached\_bytes

```python
@maximum_cached_bytes.setter
def maximum_cached_bytes(value: int) -> None
```

<a id="unreal.Cesium3DTileset.loading_descendant_limit"></a>

#### loading\_descendant\_limit

```python
@property
def loading_descendant_limit() -> int
```

(int32):  [Read-Write] The number of loading descendents a tile should allow before deciding to
render itself instead of waiting.

Setting this to 0 will cause each level of detail to be loaded
successively. This will increase the overall loading time, but cause
additional detail to appear more gradually. Setting this to a high value
like 1000 will decrease the overall time until the desired level of detail
is achieved, but this high-detail representation will appear at once, as
soon as it is loaded completely.

<a id="unreal.Cesium3DTileset.loading_descendant_limit"></a>

#### loading\_descendant\_limit

```python
@loading_descendant_limit.setter
def loading_descendant_limit(value: int) -> None
```

<a id="unreal.Cesium3DTileset.enable_frustum_culling"></a>

#### enable\_frustum\_culling

```python
@property
def enable_frustum_culling() -> bool
```

(bool):  [Read-Write] Whether to cull tiles that are outside the frustum.

By default this is true, meaning that tiles that are not visible with the
current camera configuration will be ignored. It can be set to false, so
that these tiles are still considered for loading, refinement and
rendering.

This will cause more tiles to be loaded, but helps to avoid holes and
provides a more consistent mesh, which may be helpful for physics.

Note that this will always be disabled if UseLodTransitions is set to true.

<a id="unreal.Cesium3DTileset.enable_frustum_culling"></a>

#### enable\_frustum\_culling

```python
@enable_frustum_culling.setter
def enable_frustum_culling(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.enable_fog_culling"></a>

#### enable\_fog\_culling

```python
@property
def enable_fog_culling() -> bool
```

(bool):  [Read-Write] Whether to cull tiles that are occluded by fog.

This does not refer to the atmospheric fog of the Unreal Engine,
but to an internal representation of fog: Depending on the height
of the camera above the ground, tiles that are far away (close to
the horizon) will be culled when this flag is enabled.

Note that this will always be disabled if UseLodTransitions is set to true.

<a id="unreal.Cesium3DTileset.enable_fog_culling"></a>

#### enable\_fog\_culling

```python
@enable_fog_culling.setter
def enable_fog_culling(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.enforce_culled_screen_space_error"></a>

#### enforce\_culled\_screen\_space\_error

```python
@property
def enforce_culled_screen_space_error() -> bool
```

(bool):  [Read-Write] Whether a specified screen-space error should be enforced for tiles that
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

<a id="unreal.Cesium3DTileset.enforce_culled_screen_space_error"></a>

#### enforce\_culled\_screen\_space\_error

```python
@enforce_culled_screen_space_error.setter
def enforce_culled_screen_space_error(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.culled_screen_space_error"></a>

#### culled\_screen\_space\_error

```python
@property
def culled_screen_space_error() -> float
```

(double):  [Read-Write] The screen-space error to be enforced for tiles that are outside the view
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

<a id="unreal.Cesium3DTileset.culled_screen_space_error"></a>

#### culled\_screen\_space\_error

```python
@culled_screen_space_error.setter
def culled_screen_space_error(value: float) -> None
```

<a id="unreal.Cesium3DTileset.enable_occlusion_culling"></a>

#### enable\_occlusion\_culling

```python
@property
def enable_occlusion_culling() -> bool
```

(bool):  [Read-Write] Whether to cull tiles that are occluded.

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

<a id="unreal.Cesium3DTileset.enable_occlusion_culling"></a>

#### enable\_occlusion\_culling

```python
@enable_occlusion_culling.setter
def enable_occlusion_culling(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.occlusion_pool_size"></a>

#### occlusion\_pool\_size

```python
@property
def occlusion_pool_size() -> int
```

(int32):  [Read-Write] The number of CesiumBoundingVolumeComponents to use for querying the
occlusion state of traversed tiles.

Only applicable when EnableOcclusionCulling is enabled.

<a id="unreal.Cesium3DTileset.occlusion_pool_size"></a>

#### occlusion\_pool\_size

```python
@occlusion_pool_size.setter
def occlusion_pool_size(value: int) -> None
```

<a id="unreal.Cesium3DTileset.delay_refinement_for_occlusion"></a>

#### delay\_refinement\_for\_occlusion

```python
@property
def delay_refinement_for_occlusion() -> bool
```

(bool):  [Read-Write] Whether to wait for valid occlusion results before refining tiles.

Only applicable when EnableOcclusionCulling is enabled. When this option
is enabled, there may be small delays before tiles are refined, but there
may be an overall performance advantage by avoiding loads of descendants
that will be found to be occluded.

<a id="unreal.Cesium3DTileset.delay_refinement_for_occlusion"></a>

#### delay\_refinement\_for\_occlusion

```python
@delay_refinement_for_occlusion.setter
def delay_refinement_for_occlusion(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.suspend_update"></a>

#### suspend\_update

```python
@property
def suspend_update() -> bool
```

(bool):  [Read-Write] Pauses level-of-detail and culling updates of this tileset.

<a id="unreal.Cesium3DTileset.suspend_update"></a>

#### suspend\_update

```python
@suspend_update.setter
def suspend_update(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.body_instance"></a>

#### body\_instance

```python
@property
def body_instance() -> BodyInstance
```

(BodyInstance):  [Read-Only] Define the collision profile for all the 3D tiles created inside this
actor.

<a id="unreal.Cesium3DTileset.on_tileset_loaded"></a>

#### on\_tileset\_loaded

```python
@property
def on_tileset_loaded() -> CompletedLoadTrigger
```

(CompletedLoadTrigger):  [Read-Write] A delegate that will be called whenever the tileset is fully loaded.

<a id="unreal.Cesium3DTileset.on_tileset_loaded"></a>

#### on\_tileset\_loaded

```python
@on_tileset_loaded.setter
def on_tileset_loaded(value: CompletedLoadTrigger) -> None
```

<a id="unreal.Cesium3DTileset.use_lod_transitions"></a>

#### use\_lod\_transitions

```python
@property
def use_lod_transitions() -> bool
```

(bool):  [Read-Write] Use a dithering effect when transitioning between tiles of different LODs.

When this is set to true, Frustrum Culling and Fog Culling are always
disabled.

<a id="unreal.Cesium3DTileset.use_lod_transitions"></a>

#### use\_lod\_transitions

```python
@use_lod_transitions.setter
def use_lod_transitions(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.lod_transition_length"></a>

#### lod\_transition\_length

```python
@property
def lod_transition_length() -> float
```

(float):  [Read-Write] How long dithered LOD transitions between different tiles should take, in
seconds.

Only relevant if UseLodTransitions is true.

<a id="unreal.Cesium3DTileset.lod_transition_length"></a>

#### lod\_transition\_length

```python
@lod_transition_length.setter
def lod_transition_length(value: float) -> None
```

<a id="unreal.Cesium3DTileset.tile_cover_color"></a>

#### tile\_cover\_color

```python
@property
def tile_cover_color() -> LinearColor
```

(LinearColor):  [Read-Write] 材质叠加颜色

<a id="unreal.Cesium3DTileset.tile_cover_color"></a>

#### tile\_cover\_color

```python
@tile_cover_color.setter
def tile_cover_color(value: LinearColor) -> None
```

<a id="unreal.Cesium3DTileset.load_progress"></a>

#### load\_progress

```python
@property
def load_progress() -> float
```

(float):  [Read-Only]

<a id="unreal.Cesium3DTileset.tileset_source"></a>

#### tileset\_source

```python
@property
def tileset_source() -> TilesetSource
```

(TilesetSource):  [Read-Write] The type of source from which to load this tileset.

<a id="unreal.Cesium3DTileset.tileset_source"></a>

#### tileset\_source

```python
@tileset_source.setter
def tileset_source(value: TilesetSource) -> None
```

<a id="unreal.Cesium3DTileset.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write] The URL of this tileset's "tileset.json" file.

If this property is specified, the ion asset ID and token are ignored.

<a id="unreal.Cesium3DTileset.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.Cesium3DTileset.ion_asset_id"></a>

#### ion\_asset\_id

```python
@property
def ion_asset_id() -> int
```

(int64):  [Read-Write] The ID of the Cesium ion asset to use.

This property is ignored if the Url is specified.

<a id="unreal.Cesium3DTileset.ion_asset_id"></a>

#### ion\_asset\_id

```python
@ion_asset_id.setter
def ion_asset_id(value: int) -> None
```

<a id="unreal.Cesium3DTileset.ion_access_token"></a>

#### ion\_access\_token

```python
@property
def ion_access_token() -> str
```

(str):  [Read-Write] The access token to use to access the Cesium ion resource.

<a id="unreal.Cesium3DTileset.ion_access_token"></a>

#### ion\_access\_token

```python
@ion_access_token.setter
def ion_access_token(value: str) -> None
```

<a id="unreal.Cesium3DTileset.ion_asset_endpoint_url"></a>

#### ion\_asset\_endpoint\_url

```python
@property
def ion_asset_endpoint_url() -> str
```

(str):  [Read-Write]
deprecated: Use CesiumIonServer instead.

<a id="unreal.Cesium3DTileset.ion_asset_endpoint_url"></a>

#### ion\_asset\_endpoint\_url

```python
@ion_asset_endpoint_url.setter
def ion_asset_endpoint_url(value: str) -> None
```

<a id="unreal.Cesium3DTileset.cesium_ion_server"></a>

#### cesium\_ion\_server

```python
@property
def cesium_ion_server() -> CesiumIonServer
```

(CesiumIonServer):  [Read-Write] The Cesium ion Server from which this tileset is loaded.

<a id="unreal.Cesium3DTileset.cesium_ion_server"></a>

#### cesium\_ion\_server

```python
@cesium_ion_server.setter
def cesium_ion_server(value: CesiumIonServer) -> None
```

<a id="unreal.Cesium3DTileset.create_physics_meshes"></a>

#### create\_physics\_meshes

```python
@property
def create_physics_meshes() -> bool
```

(bool):  [Read-Write] Whether to generate physics meshes for this tileset.

Disabling this option will improve the performance of tile loading, but it
will no longer be possible to collide with the tileset since the physics
meshes will not be created.

Physics meshes cannot be generated for primitives containing points.

<a id="unreal.Cesium3DTileset.create_physics_meshes"></a>

#### create\_physics\_meshes

```python
@create_physics_meshes.setter
def create_physics_meshes(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.create_nav_collision"></a>

#### create\_nav\_collision

```python
@property
def create_nav_collision() -> bool
```

(bool):  [Read-Write] Whether to generate navigation collisions for this tileset.

Enabling this option creates collisions for navigation when a 3D Tiles
tileset is loaded. It is recommended to set "Runtime Generation" to
"Static" in the navigation mesh settings in the project settings, as
collision calculations become very slow.

<a id="unreal.Cesium3DTileset.create_nav_collision"></a>

#### create\_nav\_collision

```python
@create_nav_collision.setter
def create_nav_collision(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.always_include_tangents"></a>

#### always\_include\_tangents

```python
@property
def always_include_tangents() -> bool
```

(bool):  [Read-Write] Whether to always generate a correct tangent space basis for tiles that
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

<a id="unreal.Cesium3DTileset.always_include_tangents"></a>

#### always\_include\_tangents

```python
@always_include_tangents.setter
def always_include_tangents(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.generate_smooth_normals"></a>

#### generate\_smooth\_normals

```python
@property
def generate_smooth_normals() -> bool
```

(bool):  [Read-Write] Whether to generate smooth normals when normals are missing in the glTF.

According to the Gltf spec: "When normals are not specified, client
implementations should calculate flat normals." However, calculating flat
normals requires duplicating vertices. This option allows the gltfs to be
sent with explicit smooth normals when the original gltf was missing
normals.

<a id="unreal.Cesium3DTileset.generate_smooth_normals"></a>

#### generate\_smooth\_normals

```python
@generate_smooth_normals.setter
def generate_smooth_normals(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.enable_water_mask"></a>

#### enable\_water\_mask

```python
@property
def enable_water_mask() -> bool
```

(bool):  [Read-Write] Whether to request and render the water mask.

Currently only applicable for quantized-mesh tilesets that support the
water mask extension.

<a id="unreal.Cesium3DTileset.enable_water_mask"></a>

#### enable\_water\_mask

```python
@enable_water_mask.setter
def enable_water_mask(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.ignore_khr_materials_unlit"></a>

#### ignore\_khr\_materials\_unlit

```python
@property
def ignore_khr_materials_unlit() -> bool
```

(bool):  [Read-Write] Whether to ignore the KHR_materials_unlit extension on the glTF tiles in
this tileset, if it exists, and instead render with standard lighting and
shadows. This property will have no effect if the tileset does not have any
tiles that use this extension.

The KHR_materials_unlit extension is often applied to photogrammetry
tilesets because lighting and shadows are already baked into their
textures.

<a id="unreal.Cesium3DTileset.ignore_khr_materials_unlit"></a>

#### ignore\_khr\_materials\_unlit

```python
@ignore_khr_materials_unlit.setter
def ignore_khr_materials_unlit(value: bool) -> None
```

<a id="unreal.Cesium3DTileset.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] A custom Material to use to render opaque elements in this tileset, in
order to implement custom visual effects.

The custom material should generally be created by copying the Material
Instance "MI_CesiumThreeOverlaysAndClipping" and customizing the copy as
desired.

<a id="unreal.Cesium3DTileset.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.Cesium3DTileset.translucent_material"></a>

#### translucent\_material

```python
@property
def translucent_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] A custom Material to use to render translucent elements of the tileset, in
order to implement custom visual effects.

The custom material should generally be created by copying the Material
Instance "MI_CesiumThreeOverlaysAndClippingTranslucent" and customizing the
copy as desired. Make sure that its Material Property Overrides -> Blend
Mode is set to "Translucent".

<a id="unreal.Cesium3DTileset.translucent_material"></a>

#### translucent\_material

```python
@translucent_material.setter
def translucent_material(value: MaterialInterface) -> None
```

<a id="unreal.Cesium3DTileset.water_material"></a>

#### water\_material

```python
@property
def water_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] A custom Material to use to render this tileset in areas where the
watermask is, in order to implement custom visual effects.
Currently only applicable for quantized-mesh tilesets that support the
water mask extension.

The custom material should generally be created by copying the Material
Instance "MI_CesiumThreeOverlaysAndClippingAndWater" and customizing the
copy as desired.

<a id="unreal.Cesium3DTileset.water_material"></a>

#### water\_material

```python
@water_material.setter
def water_material(value: MaterialInterface) -> None
```

<a id="unreal.Cesium3DTileset.custom_depth_parameters"></a>

#### custom\_depth\_parameters

```python
@property
def custom_depth_parameters() -> CustomDepthParameters
```

(CustomDepthParameters):  [Read-Write]

<a id="unreal.Cesium3DTileset.custom_depth_parameters"></a>

#### custom\_depth\_parameters

```python
@custom_depth_parameters.setter
def custom_depth_parameters(value: CustomDepthParameters) -> None
```

<a id="unreal.Cesium3DTileset.point_cloud_shading"></a>

#### point\_cloud\_shading

```python
@property
def point_cloud_shading() -> CesiumPointCloudShading
```

(CesiumPointCloudShading):  [Read-Write] If this tileset contains points, their appearance can be configured with
these point cloud shading parameters.

These settings are not supported on mobile platforms.

<a id="unreal.Cesium3DTileset.point_cloud_shading"></a>

#### point\_cloud\_shading

```python
@point_cloud_shading.setter
def point_cloud_shading(value: CesiumPointCloudShading) -> None
```

<a id="unreal.Cesium3DTileset.stop_movie_sequencer"></a>

#### stop\_movie\_sequencer

```python
def stop_movie_sequencer() -> None
```

x.stop_movie_sequencer() -> None
Stop Movie Sequencer

<a id="unreal.Cesium3DTileset.set_mobility"></a>

#### set\_mobility

```python
def set_mobility(new_mobility: ComponentMobility) -> None
```

x.set_mobility(new_mobility) -> None
Set Mobility
deprecated: Function 'SetMobility' is deprecated.

Args:
    new_mobility (ComponentMobility):

<a id="unreal.Cesium3DTileset.set_georeference"></a>

#### set\_georeference

```python
def set_georeference(new_georeference: CesiumGeoreference) -> None
```

x.set_georeference(new_georeference) -> None

copydoc: ACesium3DTileset::Georeference

Args:
    new_georeference (CesiumGeoreference):

<a id="unreal.Cesium3DTileset.set_credit_system"></a>

#### set\_credit\_system

```python
def set_credit_system(new_credit_system: CesiumCreditSystem) -> None
```

x.set_credit_system(new_credit_system) -> None

copydoc: ACesium3DTileset::CreditSystem

Args:
    new_credit_system (CesiumCreditSystem):

<a id="unreal.Cesium3DTileset.resolve_georeference"></a>

#### resolve\_georeference

```python
def resolve_georeference() -> CesiumGeoreference
```

x.resolve_georeference() -> CesiumGeoreference
Resolves the Cesium Georeference to use with this Actor. Returns
the value of the Georeference property if it is set. Otherwise, finds a
Georeference in the World and returns it, creating it if necessary. The
resolved Georeference is cached so subsequent calls to this function will
return the same instance.

Returns:
    CesiumGeoreference:

<a id="unreal.Cesium3DTileset.resolve_credit_system"></a>

#### resolve\_credit\_system

```python
def resolve_credit_system() -> CesiumCreditSystem
```

x.resolve_credit_system() -> CesiumCreditSystem
Resolves the Cesium Credit System to use with this Actor. Returns
the value of the CreditSystem property if it is set. Otherwise, finds a
Credit System in the World and returns it, creating it if necessary. The
resolved Credit System is cached so subsequent calls to this function will
return the same instance.

Returns:
    CesiumCreditSystem:

<a id="unreal.Cesium3DTileset.resolve_camera_manager"></a>

#### resolve\_camera\_manager

```python
def resolve_camera_manager() -> CesiumCameraManager
```

x.resolve_camera_manager() -> CesiumCameraManager
Resolves the Cesium Camera Manager to use with this Actor. Returns
the value of the CameraManager property if it is set. Otherwise, finds a
Camera Manager in the World and returns it, creating it if necessary. The
resolved Camera Manager is cached so subsequent calls to this function will
return the same instance.

Returns:
    CesiumCameraManager:

<a id="unreal.Cesium3DTileset.refresh_tileset"></a>

#### refresh\_tileset

```python
def refresh_tileset() -> None
```

x.refresh_tileset() -> None
Refreshes this tileset, ensuring that all materials and other settings are
applied. It is not usually necessary to invoke this, but when
behind-the-scenes changes are made and not reflected in the tileset, this
function can help.

<a id="unreal.Cesium3DTileset.play_movie_sequencer"></a>

#### play\_movie\_sequencer

```python
def play_movie_sequencer() -> None
```

x.play_movie_sequencer() -> None
Play Movie Sequencer

<a id="unreal.Cesium3DTileset.pause_movie_sequencer"></a>

#### pause\_movie\_sequencer

```python
def pause_movie_sequencer() -> None
```

x.pause_movie_sequencer() -> None
Pause Movie Sequencer

<a id="unreal.Cesium3DTileset.invalidate_resolved_georeference"></a>

#### invalidate\_resolved\_georeference

```python
def invalidate_resolved_georeference() -> None
```

x.invalidate_resolved_georeference() -> None
Invalidates the cached resolved georeference, unsubscribing from it and
setting it to null. The next time ResolveGeoreference is called, the
Georeference will be re-resolved and re-subscribed.

<a id="unreal.Cesium3DTileset.invalidate_resolved_credit_system"></a>

#### invalidate\_resolved\_credit\_system

```python
def invalidate_resolved_credit_system() -> None
```

x.invalidate_resolved_credit_system() -> None
Invalidates the cached resolved Credit System, setting it to null. The next
time ResolveCreditSystem is called, the Credit System will be re-resolved.

<a id="unreal.Cesium3DTileset.invalidate_resolved_camera_manager"></a>

#### invalidate\_resolved\_camera\_manager

```python
def invalidate_resolved_camera_manager() -> None
```

x.invalidate_resolved_camera_manager() -> None
Invalidates the cached resolved Camera Manager, setting it to null. The
next time ResolveCameraManager is called, the Camera Manager will be
re-resolved.

<a id="unreal.Cesium3DTileset.get_mobility"></a>

#### get\_mobility

```python
def get_mobility() -> ComponentMobility
```

x.get_mobility() -> ComponentMobility
Get Mobility
deprecated: Function 'GetMobility' is deprecated.

Returns:
    ComponentMobility:

<a id="unreal.Cesium3DTileset.get_georeference"></a>

#### get\_georeference

```python
def get_georeference() -> CesiumGeoreference
```

x.get_georeference() -> CesiumGeoreference

copydoc: ACesium3DTileset::Georeference

Returns:
    CesiumGeoreference:

<a id="unreal.Cesium3DTileset.get_credit_system"></a>

#### get\_credit\_system

```python
def get_credit_system() -> CesiumCreditSystem
```

x.get_credit_system() -> CesiumCreditSystem

copydoc: ACesium3DTileset::CreditSystem

Returns:
    CesiumCreditSystem:

<a id="unreal.Cesium3DTilesetRoot"></a>