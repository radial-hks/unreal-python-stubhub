## AesEarth Objects

```python
class AesEarth(Actor)
```

Aes Earth

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesEarth.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_data_path`` (str):  [Read-Write]
- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``asset_folder_path`` (DirectoryPath):  [Read-Write]
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
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
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``earth_global_settings`` (EarthGlobalSettings):  [Read-Write]
- ``earth_ready_timeout`` (float):  [Read-Write] The timeout in seconds to wait for the earth to be ready
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_abs_data_path`` (bool):  [Read-Write] ----- DataDescriptor -----
- ``is_earth_ready`` (bool):  [Read-Only] ----- AesEarth -----
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``max_level`` (int32):  [Read-Only]
- ``min_net_update_frequency`` (float):  [Read-Write]
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
- ``on_earth_is_ready`` (OnEarthReady):  [Read-Write]
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_query_entity_id_completed`` (OnQueryWaterEntityIdCompleted):  [Read-Write]
- ``on_query_water_entity_id_completed`` (OnQueryWaterEntityIdCompleted):  [Read-Write]
- ``on_query_water_entity_tile_id_completed`` (OnQueryWaterEntityTileIdCompleted):  [Read-Write]
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``origin_at_planet_center`` (bool):  [Read-Write]
- ``origin_key_ranges`` (Array[Vector4d]):  [Read-Only]
- ``origin_level`` (int32):  [Read-Only]
- ``origin_location`` (Vector):  [Read-Only]
- ``origin_range`` (Vector4d):  [Read-Only]
- ``override_earth_global_settings`` (bool):  [Read-Write] ----- EarthGlobalSettings -----
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``planet_scope`` (AesPlanetScope):  [Read-Write]
- ``planet_shape`` (AesPlanetShape):  [Read-Write]
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``relative_data_path`` (FilePath):  [Read-Write]
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
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``scalability_earth_global_settings`` (EarthGlobalSettings):  [Read-Only]
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``terrain_component`` (AesTerrainComponent):  [Read-Write] ----- Components -----
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

<a id="unreal.AesEarth.on_earth_is_ready"></a>

#### on\_earth\_is\_ready

```python
@property
def on_earth_is_ready() -> OnEarthReady
```

(OnEarthReady):  [Read-Write]

<a id="unreal.AesEarth.on_earth_is_ready"></a>

#### on\_earth\_is\_ready

```python
@on_earth_is_ready.setter
def on_earth_is_ready(value: OnEarthReady) -> None
```

<a id="unreal.AesEarth.on_query_water_entity_id_completed"></a>

#### on\_query\_water\_entity\_id\_completed

```python
@property
def on_query_water_entity_id_completed() -> OnQueryWaterEntityIdCompleted
```

(OnQueryWaterEntityIdCompleted):  [Read-Write]

<a id="unreal.AesEarth.on_query_water_entity_id_completed"></a>

#### on\_query\_water\_entity\_id\_completed

```python
@on_query_water_entity_id_completed.setter
def on_query_water_entity_id_completed(
        value: OnQueryWaterEntityIdCompleted) -> None
```

<a id="unreal.AesEarth.on_query_water_entity_tile_id_completed"></a>

#### on\_query\_water\_entity\_tile\_id\_completed

```python
@property
def on_query_water_entity_tile_id_completed(
) -> OnQueryWaterEntityTileIdCompleted
```

(OnQueryWaterEntityTileIdCompleted):  [Read-Write]

<a id="unreal.AesEarth.on_query_water_entity_tile_id_completed"></a>

#### on\_query\_water\_entity\_tile\_id\_completed

```python
@on_query_water_entity_tile_id_completed.setter
def on_query_water_entity_tile_id_completed(
        value: OnQueryWaterEntityTileIdCompleted) -> None
```

<a id="unreal.AesEarth.on_query_entity_id_completed"></a>

#### on\_query\_entity\_id\_completed

```python
@property
def on_query_entity_id_completed() -> OnQueryWaterEntityIdCompleted
```

(OnQueryWaterEntityIdCompleted):  [Read-Write]

<a id="unreal.AesEarth.on_query_entity_id_completed"></a>

#### on\_query\_entity\_id\_completed

```python
@on_query_entity_id_completed.setter
def on_query_entity_id_completed(value: OnQueryWaterEntityIdCompleted) -> None
```

<a id="unreal.AesEarth.earth_ready_timeout"></a>

#### earth\_ready\_timeout

```python
@property
def earth_ready_timeout() -> float
```

(float):  [Read-Only] The timeout in seconds to wait for the earth to be ready

<a id="unreal.AesEarth.set_water_entity_visibility"></a>

#### set\_water\_entity\_visibility

```python
def set_water_entity_visibility(feature_id: int, new_visibility: bool) -> bool
```

x.set_water_entity_visibility(feature_id, new_visibility) -> bool
Set Water Entity Visibility

Args:
    feature_id (int32): 
    new_visibility (bool): 

Returns:
    bool:

<a id="unreal.AesEarth.set_water_entity_outline"></a>

#### set\_water\_entity\_outline

```python
def set_water_entity_outline(feature_id: int,
                             new_outline: bool,
                             color: Color = [0, 0, 255, 255]) -> bool
```

x.set_water_entity_outline(feature_id, new_outline, color=[0, 0, 255, 255]) -> bool
Set Water Entity Outline

Args:
    feature_id (int32): 
    new_outline (bool): 
    color (Color): 

Returns:
    bool:

<a id="unreal.AesEarth.set_water_entity_high_light"></a>

#### set\_water\_entity\_high\_light

```python
def set_water_entity_high_light(feature_id: int,
                                new_high_light: bool,
                                color: Color = [0, 255, 255, 255]) -> bool
```

x.set_water_entity_high_light(feature_id, new_high_light, color=[0, 255, 255, 255]) -> bool
Set Water Entity High Light

Args:
    feature_id (int32): 
    new_high_light (bool): 
    color (Color): 

Returns:
    bool:

<a id="unreal.AesEarth.set_show_water_mesh"></a>

#### set\_show\_water\_mesh

```python
def set_show_water_mesh(show_water_mesh: bool) -> None
```

x.set_show_water_mesh(show_water_mesh) -> None
Set Show Water Mesh

Args:
    show_water_mesh (bool):

<a id="unreal.AesEarth.set_show_only_collision"></a>

#### set\_show\_only\_collision

```python
def set_show_only_collision(show_only_collision: bool) -> None
```

x.set_show_only_collision(show_only_collision) -> None
Set Show Only Collision

Args:
    show_only_collision (bool):

<a id="unreal.AesEarth.set_relative_data_path"></a>

#### set\_relative\_data\_path

```python
def set_relative_data_path(relative_data_path: str) -> bool
```

x.set_relative_data_path(relative_data_path) -> bool
get data path

Args:
    relative_data_path (str): 

Returns:
    bool:

<a id="unreal.AesEarth.set_model_lib_folder_path"></a>

#### set\_model\_lib\_folder\_path

```python
def set_model_lib_folder_path(model_lib_folder_path: str) -> None
```

x.set_model_lib_folder_path(model_lib_folder_path) -> None
Set Model Lib Folder Path

Args:
    model_lib_folder_path (str):

<a id="unreal.AesEarth.set_lod_view_actors"></a>

#### set\_lod\_view\_actors

```python
def set_lod_view_actors(lod_view_actors: Array[Actor]) -> None
```

x.set_lod_view_actors(lod_view_actors) -> None
Set LODView Actors

Args:
    lod_view_actors (Array[Actor]):

<a id="unreal.AesEarth.set_layer_visibility"></a>

#### set\_layer\_visibility

```python
def set_layer_visibility(target_layer: EarthLayerType,
                         new_visibility: bool) -> bool
```

x.set_layer_visibility(target_layer, new_visibility) -> bool
Set Layer Visibility

Args:
    target_layer (EarthLayerType): 
    new_visibility (bool): 

Returns:
    bool:

<a id="unreal.AesEarth.set_layer_collision_visibility"></a>

#### set\_layer\_collision\_visibility

```python
def set_layer_collision_visibility(target_layer: EarthLayerType,
                                   use_collision: bool) -> bool
```

x.set_layer_collision_visibility(target_layer, use_collision) -> bool
Set Layer Collision Visibility

Args:
    target_layer (EarthLayerType): 
    use_collision (bool): 

Returns:
    bool:

<a id="unreal.AesEarth.set_earth_visibility"></a>

#### set\_earth\_visibility

```python
def set_earth_visibility(new_visibility: bool) -> bool
```

x.set_earth_visibility(new_visibility) -> bool
Set Earth Visibility

Args:
    new_visibility (bool): 

Returns:
    bool:

<a id="unreal.AesEarth.set_earth_collision_visibility"></a>

#### set\_earth\_collision\_visibility

```python
def set_earth_collision_visibility(use_collision: bool) -> bool
```

x.set_earth_collision_visibility(use_collision) -> bool
Set Earth Collision Visibility

Args:
    use_collision (bool): 

Returns:
    bool:

<a id="unreal.AesEarth.set_changeset_folder_path"></a>

#### set\_changeset\_folder\_path

```python
def set_changeset_folder_path(changeset_folder_path: str) -> None
```

x.set_changeset_folder_path(changeset_folder_path) -> None
Set Changeset Folder Path

Args:
    changeset_folder_path (str):

<a id="unreal.AesEarth.set_changeset_backup_folder_path"></a>

#### set\_changeset\_backup\_folder\_path

```python
def set_changeset_backup_folder_path(
        changeset_backup_folder_path: str) -> None
```

x.set_changeset_backup_folder_path(changeset_backup_folder_path) -> None
Set Changeset Backup Folder Path

Args:
    changeset_backup_folder_path (str):

<a id="unreal.AesEarth.set_absolute_data_path"></a>

#### set\_absolute\_data\_path

```python
def set_absolute_data_path(absolute_data_path: str) -> bool
```

x.set_absolute_data_path(absolute_data_path) -> bool
Set Absolute Data Path

Args:
    absolute_data_path (str): 

Returns:
    bool:

<a id="unreal.AesEarth.refresh_earth_actor"></a>

#### refresh\_earth\_actor

```python
def refresh_earth_actor() -> None
```

x.refresh_earth_actor() -> None
Refresh Earth Actor

<a id="unreal.AesEarth.query_water_entity_id_by_world_location"></a>

#### query\_water\_entity\_id\_by\_world\_location

```python
def query_water_entity_id_by_world_location(world_location: Vector) -> None
```

x.query_water_entity_id_by_world_location(world_location) -> None
Query Water Entity Id by World Location

Args:
    world_location (Vector):

<a id="unreal.AesEarth.query_entity_id_by_world_location"></a>

#### query\_entity\_id\_by\_world\_location

```python
def query_entity_id_by_world_location(producer_name: Name,
                                      world_location: Vector) -> None
```

x.query_entity_id_by_world_location(producer_name, world_location) -> None
Query Entity Id by World Location

Args:
    producer_name (Name): 
    world_location (Vector):

<a id="unreal.AesEarth.get_water_entity_visibility"></a>

#### get\_water\_entity\_visibility

```python
def get_water_entity_visibility(feature_id: int) -> bool
```

x.get_water_entity_visibility(feature_id) -> bool
Get Water Entity Visibility

Args:
    feature_id (int32): 

Returns:
    bool:

<a id="unreal.AesEarth.get_water_entity_outline"></a>

#### get\_water\_entity\_outline

```python
def get_water_entity_outline(feature_id: int) -> bool
```

x.get_water_entity_outline(feature_id) -> bool
Get Water Entity Outline

Args:
    feature_id (int32): 

Returns:
    bool:

<a id="unreal.AesEarth.get_water_entity_high_light"></a>

#### get\_water\_entity\_high\_light

```python
def get_water_entity_high_light(feature_id: int) -> bool
```

x.get_water_entity_high_light(feature_id) -> bool
Get Water Entity High Light

Args:
    feature_id (int32): 

Returns:
    bool:

<a id="unreal.AesEarth.get_show_water_mesh"></a>

#### get\_show\_water\_mesh

```python
def get_show_water_mesh() -> bool
```

x.get_show_water_mesh() -> bool
Get Show Water Mesh

Returns:
    bool:

<a id="unreal.AesEarth.get_origin_location"></a>

#### get\_origin\_location

```python
def get_origin_location() -> Vector
```

x.get_origin_location() -> Vector
Get Origin Location

Returns:
    Vector:

<a id="unreal.AesEarth.get_near_point"></a>

#### get\_near\_point

```python
def get_near_point(origin_point: Vector) -> Optional[Vector]
```

x.get_near_point(origin_point) -> Vector or None
Get Near Point

Args:
    origin_point (Vector): 

Returns:
    Vector or None: 

    out_point (Vector):

<a id="unreal.AesEarth.get_model_lib_folder_path"></a>

#### get\_model\_lib\_folder\_path

```python
def get_model_lib_folder_path() -> str
```

x.get_model_lib_folder_path() -> str
Get Model Lib Folder Path

Returns:
    str:

<a id="unreal.AesEarth.get_layer_visibility"></a>

#### get\_layer\_visibility

```python
def get_layer_visibility(target_layer: EarthLayerType) -> bool
```

x.get_layer_visibility(target_layer) -> bool
Get Layer Visibility

Args:
    target_layer (EarthLayerType): 

Returns:
    bool:

<a id="unreal.AesEarth.get_layer_collision_visibility"></a>

#### get\_layer\_collision\_visibility

```python
def get_layer_collision_visibility(target_layer: EarthLayerType) -> bool
```

x.get_layer_collision_visibility(target_layer) -> bool
Get Layer Collision Visibility

Args:
    target_layer (EarthLayerType): 

Returns:
    bool:

<a id="unreal.AesEarth.get_earth_is_ready"></a>

#### get\_earth\_is\_ready

```python
def get_earth_is_ready() -> bool
```

x.get_earth_is_ready() -> bool
Get Earth Is Ready

Returns:
    bool:

<a id="unreal.AesEarth.get_changeset_folder_path"></a>

#### get\_changeset\_folder\_path

```python
def get_changeset_folder_path() -> str
```

x.get_changeset_folder_path() -> str
Get Changeset Folder Path

Returns:
    str:

<a id="unreal.AesEarth.get_changeset_backup_folder_path"></a>

#### get\_changeset\_backup\_folder\_path

```python
def get_changeset_backup_folder_path() -> str
```

x.get_changeset_backup_folder_path() -> str
Get Changeset Backup Folder Path

Returns:
    str:

<a id="unreal.AesEarth.clear_lod_view_actors"></a>

#### clear\_lod\_view\_actors

```python
def clear_lod_view_actors() -> None
```

x.clear_lod_view_actors() -> None
Clear LODView Actors

<a id="unreal.AesEarth.clear_all_water_entity_visibility"></a>

#### clear\_all\_water\_entity\_visibility

```python
def clear_all_water_entity_visibility() -> bool
```

x.clear_all_water_entity_visibility() -> bool
Clear All Water Entity Visibility

Returns:
    bool:

<a id="unreal.AesEarth.clear_all_water_entity_outline"></a>

#### clear\_all\_water\_entity\_outline

```python
def clear_all_water_entity_outline() -> bool
```

x.clear_all_water_entity_outline() -> bool
Clear All Water Entity Outline

Returns:
    bool:

<a id="unreal.AesEarth.clear_all_water_entity_high_light"></a>

#### clear\_all\_water\_entity\_high\_light

```python
def clear_all_water_entity_high_light() -> bool
```

x.clear_all_water_entity_high_light() -> bool
Clear All Water Entity High Light

Returns:
    bool:

<a id="unreal.AesEarthBlueprintFunctionLibrary"></a>