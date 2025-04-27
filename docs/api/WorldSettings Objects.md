## WorldSettings Objects

```python
class WorldSettings(Info)
```

Actor containing all script accessible world properties.

**C++ Source:**

- **Module**: Engine
- **File**: WorldSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``ai_system_class`` (Class):  [Read-Write]
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``base_navmesh_data_layers`` (Array[DataLayerAsset]):  [Read-Write] A list of runtime data layers that should be included in the base navmesh.
  Editor data layers and actors outside data layers will be included.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``broadphase_settings`` (BroadphaseSettings):  [Read-Write]
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_ambient_zone_settings`` (InteriorSettings):  [Read-Write] Default interior settings applied to sounds that have "apply ambient volumes" set to true on their SoundClass.
- ``default_base_sound_mix`` (SoundMix):  [Read-Write] Default Base SoundMix.
- ``default_color_scale`` (Vector):  [Read-Write] Default color scale for the level
- ``default_game_mode`` (type(Class)):  [Read-Write] The default GameMode to use when starting this map in the game. If this value is NULL, the INI setting for default game type is used.
- ``default_max_distance_field_occlusion_distance`` (float):  [Read-Write] Max occlusion distance used by mesh distance fields, overridden if there is a movable skylight.
- ``default_physics_volume_class`` (type(Class)):  [Read-Write] level specific default physics volume
- ``default_reverb_settings`` (ReverbSettings):  [Read-Write] Default reverb settings used by audio volumes.
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``dynamic_indirect_shadows_self_shadowing_intensity`` (float):  [Read-Write] Controls the intensity of self-shadowing from capsule indirect shadows.
  These types of shadows use approximate occluder representations, so reducing self-shadowing intensity can hide those artifacts.
- ``enable_ai_system`` (bool):  [Read-Write] if set to false AI system will not get created. Use it to disable all AI-related activity on a map
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_large_worlds`` (bool):  [Read-Write]
  deprecated: As of UE 5.1 all worlds are large. Set UE_USE_UE4_WORLD_MAX in EngineDefines.h to alter this.
- ``enable_navigation_system`` (bool):  [Read-Write]
- ``enable_world_bounds_checks`` (bool):  [Read-Write] If true, enables CheckStillInWorld checks
- ``enable_world_composition`` (bool):  [Read-Write] Enables tools for composing a tiled world.
  Level has to be saved and all sub-levels removed before enabling this option.
- ``enable_world_origin_rebasing`` (bool):  [Read-Write] World origin will shift to a camera position when camera goes far away from current origin
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``force_no_precomputed_lighting`` (bool):  [Read-Write] Whether to force lightmaps and other precomputed lighting to not be created even when the engine thinks they are needed.
  This is useful for improving iteration in levels with fully dynamic lighting and shadowing.
  Note that any lighting and shadowing interactions that are usually precomputed will be lost if this is enabled.
- ``force_volumetric_lightmaps_only`` (bool):  [Read-Write] Force precomputed lighting to only use VolumetricLightmaps.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``generate_single_cluster_for_level`` (bool):  [Read-Write] If set to true, all eligible actors in this level will be added to a single cluster representing the entire level (used for small sublevels)
- ``global_distance_field_view_distance`` (float):  [Read-Write] Distance from the camera that the global distance field should cover.
- ``global_gravity_set`` (bool):  [Read-Write] If set to true we will use GlobalGravityZ instead of project setting DefaultGravityZ
- ``global_gravity_z`` (float):  [Read-Write] optional level specific gravity override set by level designer
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hide_enable_streaming_warning`` (bool):  [Read-Write] if set to true, this hide the streaming disabled warning available in the viewport
- ``hierarchical_lod_setup`` (Array[HierarchicalSimplification]):  [Read-Write] Hierarchical LOD Setup
- ``hlod_baking_transform`` (Transform):  [Read-Write] Specify the transform to apply to the source meshes when building HLODs.
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``hlod_setup_asset`` (Class):  [Read-Write] If set overrides the level settings and global project settings
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instanced_foliage_grid_size`` (uint32):  [Read-Write] Size of the grid for instanced foliage actors, only used for partitioned worlds
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``kill_z`` (float):  [Read-Write] any actor falling below this level gets destroyed
- ``kill_z_damage_type`` (type(Class)):  [Read-Write] The type of damage inflicted when a actor falls below KillZ
- ``landscape_spline_meshes_grid_size`` (uint32):  [Read-Write]
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``lightmass_settings`` (LightmassWorldInfoSettings):  [Read-Write] LIGHTMASS RELATED SETTINGS *
- ``max_global_time_dilation`` (float):  [Read-Write] Highest acceptable global time dilation.
- ``max_undilated_frame_time`` (float):  [Read-Write] Largest possible frametime, not considering dilation. Equiv to 1/SlowestFPS.
- ``min_global_time_dilation`` (float):  [Read-Write] Lowest acceptable global time dilation.
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``min_undilated_frame_time`` (float):  [Read-Write] Smallest possible frametime, not considering dilation. Equiv to 1/FastestFPS.
- ``minimize_bsp_sections`` (bool):  [Read-Write] Causes the BSP build to generate as few sections as possible.
  This is useful when you need to reduce draw calls but can reduce texture streaming efficiency and effective lightmap resolution.
  Note - changes require a rebuild to propagate.  Also, be sure to select all surfaces and make sure they all have the same flags to minimize section count.
- ``nanite_settings`` (NaniteSettings):  [Read-Write] NANITE SETTINGS *
- ``navigation_data_builder_loading_cell_size`` (uint32):  [Read-Write] Loading cell size used when building navigation data iteratively.
  The actual cell size used will be rounded using the NavigationDataChunkGridSize.
  It's recommended to use a value as high as the hardware memory allows to load.
- ``navigation_data_chunk_grid_size`` (uint32):  [Read-Write] Size of the grid for navigation data chunk actors
- ``navigation_system_config`` (NavigationSystemConfig):  [Read-Write] Holds parameters for NavigationSystem's creation. Set to Null will result
      in NavigationSystem instance not being created for this world. Note that
      if set NavigationSystemConfigOverride will be used instead.
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
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
- ``override_base_material`` (MaterialInterface):  [Read-Write] If set overrides the project-wide base material used for Proxy Materials
- ``override_default_broadphase_settings`` (bool):  [Read-Write]
- ``packed_light_and_shadow_map_texture_size`` (int32):  [Read-Write] Maximum size of textures for packed light and shadow maps
- ``physics_collision_handler_class`` (type(Class)):  [Read-Write] optional level specific collision handler
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``place_cells_only_along_camera_tracks`` (bool):  [Read-Write] Whether to place visibility cells only along camera tracks or only above shadow casting surfaces.
- ``precompute_visibility`` (bool):  [Read-Write] Whether to place visibility cells inside Precomputed Visibility Volumes and along camera tracks in this level.
  Precomputing visibility reduces rendering thread time at the cost of some runtime memory and somewhat increased lighting build times.
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
- ``reuse_address_and_port`` (bool):  [Read-Write] Whether to configure the listening socket to allow reuse of the address and port. If this is true, be sure no other
  servers can run on the same port, otherwise this can lead to undefined behavior since packets will go to two servers.
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``show_instanced_foliage_grid`` (bool):  [Read-Write]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
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
- ``use_client_side_level_streaming_volumes`` (bool):  [Read-Write] Enables client-side streaming volumes instead of server-side.
  Expected usage scenario: server has all streaming levels always loaded, clients independently stream levels in/out based on streaming volumes.
- ``visibility_aggressiveness`` (VisibilityAggressiveness):  [Read-Write] Determines how aggressive precomputed visibility should be.
  More aggressive settings cull more objects but also cause more visibility errors like popping.
- ``visibility_cell_size`` (int32):  [Read-Write] World space size of precomputed visibility cells in x and y.
  Smaller sizes produce more effective occlusion culling at the cost of increased runtime memory usage and lighting build times.
- ``volumetric_lightmap_loading_range`` (float):  [Read-Write] Range in which volumetric lightmaps will be loaded.
- ``world_partition`` (WorldPartition):  [Read-Only]
- ``world_to_meters`` (float):  [Read-Write] scale of 1uu to 1m in real world measurements, for HMD and other physically tracked devices (e.g. 1uu = 1cm would be 100.0)

<a id="unreal.WorldSettings.enable_world_bounds_checks"></a>

#### enable_world_bounds_checks

```python
@property
def enable_world_bounds_checks() -> bool
```

(bool):  [Read-Only] If true, enables CheckStillInWorld checks

<a id="unreal.WorldSettings.enable_navigation_system"></a>

#### enable_navigation_system

```python
@property
def enable_navigation_system() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WorldSettings.enable_ai_system"></a>

#### enable_ai_system

```python
@property
def enable_ai_system() -> bool
```

(bool):  [Read-Only] if set to false AI system will not get created. Use it to disable all AI-related activity on a map

<a id="unreal.WorldSettings.enable_world_composition"></a>

#### enable_world_composition

```python
@property
def enable_world_composition() -> bool
```

(bool):  [Read-Only] Enables tools for composing a tiled world.
Level has to be saved and all sub-levels removed before enabling this option.

<a id="unreal.WorldSettings.use_client_side_level_streaming_volumes"></a>

#### use_client_side_level_streaming_volumes

```python
@property
def use_client_side_level_streaming_volumes() -> bool
```

(bool):  [Read-Only] Enables client-side streaming volumes instead of server-side.
Expected usage scenario: server has all streaming levels always loaded, clients independently stream levels in/out based on streaming volumes.

<a id="unreal.WorldSettings.enable_world_origin_rebasing"></a>

#### enable_world_origin_rebasing

```python
@property
def enable_world_origin_rebasing() -> bool
```

(bool):  [Read-Only] World origin will shift to a camera position when camera goes far away from current origin

<a id="unreal.WorldSettings.global_gravity_set"></a>

#### global_gravity_set

```python
@property
def global_gravity_set() -> bool
```

(bool):  [Read-Only] If set to true we will use GlobalGravityZ instead of project setting DefaultGravityZ

<a id="unreal.WorldSettings.ai_system_class"></a>

#### ai_system_class

```python
@property
def ai_system_class() -> Class
```

(Class):  [Read-Only]

<a id="unreal.WorldSettings.navigation_system_config"></a>

#### navigation_system_config

```python
@property
def navigation_system_config() -> NavigationSystemConfig
```

(NavigationSystemConfig):  [Read-Only] Holds parameters for NavigationSystem's creation. Set to Null will result
    in NavigationSystem instance not being created for this world. Note that
    if set NavigationSystemConfigOverride will be used instead.

<a id="unreal.WorldSettings.world_to_meters"></a>

#### world_to_meters

```python
@property
def world_to_meters() -> float
```

(float):  [Read-Only] scale of 1uu to 1m in real world measurements, for HMD and other physically tracked devices (e.g. 1uu = 1cm would be 100.0)

<a id="unreal.WorldSettings.kill_z"></a>

#### kill_z

```python
@property
def kill_z() -> float
```

(float):  [Read-Only] any actor falling below this level gets destroyed

<a id="unreal.WorldSettings.kill_z_damage_type"></a>

#### kill_z_damage_type

```python
@property
def kill_z_damage_type() -> Class
```

(type(Class)):  [Read-Only] The type of damage inflicted when a actor falls below KillZ

<a id="unreal.WorldSettings.global_gravity_z"></a>

#### global_gravity_z

```python
@property
def global_gravity_z() -> float
```

(float):  [Read-Only] optional level specific gravity override set by level designer

<a id="unreal.WorldSettings.default_physics_volume_class"></a>

#### default_physics_volume_class

```python
@property
def default_physics_volume_class() -> Class
```

(type(Class)):  [Read-Only] level specific default physics volume

<a id="unreal.WorldSettings.physics_collision_handler_class"></a>

#### physics_collision_handler_class

```python
@property
def physics_collision_handler_class() -> Class
```

(type(Class)):  [Read-Only] optional level specific collision handler

<a id="unreal.WorldSettings.default_game_mode"></a>

#### default_game_mode

```python
@property
def default_game_mode() -> Class
```

(type(Class)):  [Read-Only] The default GameMode to use when starting this map in the game. If this value is NULL, the INI setting for default game type is used.

<a id="unreal.WorldSettings.default_game_type"></a>

#### default_game_type

```python
@property
def default_game_type() -> Class
```

deprecated: 'default_game_type' was renamed to 'default_game_mode'.

<a id="unreal.WorldSettings.default_color_scale"></a>

#### default_color_scale

```python
@property
def default_color_scale() -> Vector
```

(Vector):  [Read-Only] Default color scale for the level

<a id="unreal.WorldSettings.lightmass_settings"></a>

#### lightmass_settings

```python
@property
def lightmass_settings() -> LightmassWorldInfoSettings
```

(LightmassWorldInfoSettings):  [Read-Write] LIGHTMASS RELATED SETTINGS *

<a id="unreal.WorldSettings.lightmass_settings"></a>

#### lightmass_settings

```python
@lightmass_settings.setter
def lightmass_settings(value: LightmassWorldInfoSettings) -> None
```

<a id="unreal.WorldSettings.volumetric_lightmap_loading_range"></a>

#### volumetric_lightmap_loading_range

```python
@property
def volumetric_lightmap_loading_range() -> float
```

(float):  [Read-Write] Range in which volumetric lightmaps will be loaded.

<a id="unreal.WorldSettings.volumetric_lightmap_loading_range"></a>

#### volumetric_lightmap_loading_range

```python
@volumetric_lightmap_loading_range.setter
def volumetric_lightmap_loading_range(value: float) -> None
```

<a id="unreal.WorldSettings.enable_large_worlds"></a>

#### enable_large_worlds

```python
@property
def enable_large_worlds() -> bool
```

(bool):  [Read-Write]
deprecated: As of UE 5.1 all worlds are large. Set UE_USE_UE4_WORLD_MAX in EngineDefines.h to alter this.

<a id="unreal.WorldSettings.enable_large_worlds"></a>

#### enable_large_worlds

```python
@enable_large_worlds.setter
def enable_large_worlds(value: bool) -> None
```

<a id="unreal.WorldSettings.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.WorldSettings.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.WorldSettings.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.WorldInfo"></a>