## AesGeoreference Objects

```python
class AesGeoreference(Info)
```

Aes Georeference

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesGeoreference
- **File**: AesGeoreference.h

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
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
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
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
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
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_georeference_updated`` (AesGeoreferenceUpdated):  [Read-Write] A delegate that will be called whenever the Georeference is
  modified in a way that affects its computations.
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
- ``origin_altitude`` (double):  [Read-Write] Altitude of UE Origin on planet
- ``origin_at_planet_center`` (bool):  [Read-Write] if true, the UE origin is located at the Planet Center, otherwise,
  the UE origin is assuming to be defined at one specific point of
  the planet surface, defined by the properties below.
- ``origin_latitude`` (double):  [Read-Write] Latitude of UE Origin on planet
- ``origin_level`` (int32):  [Read-Write] The level of the origin scope.
- ``origin_longitude`` (double):  [Read-Write] Longitude of UE Origin on planet
- ``origin_range`` (Vector4d):  [Read-Write] The scope range of the origin in the format of Left Longitude, Top Latitude, Right Longitude, Bottom Latitude.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``planet_scope`` (AesPlanetScope):  [Read-Write] The scope of the origin.
- ``planet_shape`` (AesPlanetShape):  [Read-Write] This mode has to be set consistently with the way you authored your ground geometry.
   - For small environments, a projection is often applied and the world is considered as Flat
   - For planet scale environments, projections is not suitable and the geometry is Rounded.
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
- ``role`` (NetRole):  [Read-Only] Describes how much control the local machine has over the actor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
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

<a id="unreal.AesGeoreference.on_georeference_updated"></a>

#### on\_georeference\_updated

```python
@property
def on_georeference_updated() -> AesGeoreferenceUpdated
```

(AesGeoreferenceUpdated):  [Read-Write] A delegate that will be called whenever the Georeference is
modified in a way that affects its computations.

<a id="unreal.AesGeoreference.on_georeference_updated"></a>

#### on\_georeference\_updated

```python
@on_georeference_updated.setter
def on_georeference_updated(value: AesGeoreferenceUpdated) -> None
```

<a id="unreal.AesGeoreference.planet_shape"></a>

#### planet\_shape

```python
@property
def planet_shape() -> AesPlanetShape
```

(AesPlanetShape):  [Read-Only] This mode has to be set consistently with the way you authored your ground geometry.
 - For small environments, a projection is often applied and the world is considered as Flat
 - For planet scale environments, projections is not suitable and the geometry is Rounded.

<a id="unreal.AesGeoreference.origin_at_planet_center"></a>

#### origin\_at\_planet\_center

```python
@property
def origin_at_planet_center() -> bool
```

(bool):  [Read-Only] if true, the UE origin is located at the Planet Center, otherwise,
the UE origin is assuming to be defined at one specific point of
the planet surface, defined by the properties below.

<a id="unreal.AesGeoreference.origin_longitude"></a>

#### origin\_longitude

```python
@property
def origin_longitude() -> float
```

(double):  [Read-Only] Longitude of UE Origin on planet

<a id="unreal.AesGeoreference.origin_latitude"></a>

#### origin\_latitude

```python
@property
def origin_latitude() -> float
```

(double):  [Read-Only] Latitude of UE Origin on planet

<a id="unreal.AesGeoreference.origin_altitude"></a>

#### origin\_altitude

```python
@property
def origin_altitude() -> float
```

(double):  [Read-Only] Altitude of UE Origin on planet

<a id="unreal.AesGeoreference.planet_scope"></a>

#### planet\_scope

```python
@property
def planet_scope() -> AesPlanetScope
```

(AesPlanetScope):  [Read-Only] The scope of the origin.

<a id="unreal.AesGeoreference.origin_level"></a>

#### origin\_level

```python
@property
def origin_level() -> int
```

(int32):  [Read-Only] The level of the origin scope.

<a id="unreal.AesGeoreference.get_world_location_to_world_rotation"></a>

#### get\_world\_location\_to\_world\_rotation

```python
def get_world_location_to_world_rotation(location: Vector) -> Rotator
```

x.get_world_location_to_world_rotation(location) -> Rotator
* 通过空间直角坐标求得空间直角变换
*

Args:
    location (Vector): 空间直角坐标（厘米）

Returns:
    Rotator:

<a id="unreal.AesGeoreference.get_world_location_to_lon_lat"></a>

#### get\_world\_location\_to\_lon\_lat

```python
def get_world_location_to_lon_lat(location: Vector) -> Vector
```

x.get_world_location_to_lon_lat(location) -> Vector
空间直角坐标转经纬度坐标
return:: Lon, Lat, Alt

Args:
    location (Vector): 空间直角坐标（厘米）

Returns:
    Vector:

<a id="unreal.AesGeoreference.get_tile_xy_to_world_transform"></a>

#### get\_tile\_xy\_to\_world\_transform

```python
def get_tile_xy_to_world_transform(tile_x: int, tile_y: int, tile_level: int,
                                   alt: float, offset: Vector2D) -> Transform
```

x.get_tile_xy_to_world_transform(tile_x, tile_y, tile_level, alt, offset) -> Transform
Get Tile XYTo World Transform

Args:
    tile_x (int32): 
    tile_y (int32): 
    tile_level (int32): 
    alt (double): 
    offset (Vector2D): 

Returns:
    Transform:

<a id="unreal.AesGeoreference.get_tile_xy_to_world_location"></a>

#### get\_tile\_xy\_to\_world\_location

```python
def get_tile_xy_to_world_location(tile_x: int, tile_y: int, tile_level: int,
                                  alt: float, offset: Vector2D) -> Vector
```

x.get_tile_xy_to_world_location(tile_x, tile_y, tile_level, alt, offset) -> Vector
Get Tile XYTo World Location

Args:
    tile_x (int32): 
    tile_y (int32): 
    tile_level (int32): 
    alt (double): 
    offset (Vector2D): 

Returns:
    Vector:

<a id="unreal.AesGeoreference.get_quad_key_to_world_transform"></a>

#### get\_quad\_key\_to\_world\_transform

```python
def get_quad_key_to_world_transform(
        quad_key: str,
        alt: float = 0.000000,
        offset: Vector2D = [0.000000, 0.000000]) -> Transform
```

x.get_quad_key_to_world_transform(quad_key, alt=0.000000, offset=[0.000000, 0.000000]) -> Transform
Get Quad Key to World Transform

Args:
    quad_key (str): 
    alt (double): 
    offset (Vector2D): 

Returns:
    Transform:

<a id="unreal.AesGeoreference.get_quad_key_to_world_location"></a>

#### get\_quad\_key\_to\_world\_location

```python
def get_quad_key_to_world_location(
        quad_key: str,
        alt: float = 0.000000,
        offset: Vector2D = [0.000000, 0.000000]) -> Vector
```

x.get_quad_key_to_world_location(quad_key, alt=0.000000, offset=[0.000000, 0.000000]) -> Vector
Get Quad Key to World Location

Args:
    quad_key (str): 
    alt (double): 
    offset (Vector2D): 

Returns:
    Vector:

<a id="unreal.AesGeoreference.get_quad_key_to_local_bound"></a>

#### get\_quad\_key\_to\_local\_bound

```python
def get_quad_key_to_local_bound(quad_key: str,
                                min_alt: float = 0.000000,
                                max_alt: float = 10000.000000) -> Box
```

x.get_quad_key_to_local_bound(quad_key, min_alt=0.000000, max_alt=10000.000000) -> Box
Get Quad Key to Local Bound

Args:
    quad_key (str): 
    min_alt (double): 
    max_alt (double): 

Returns:
    Box:

<a id="unreal.AesGeoreference.get_planet_radius"></a>

#### get\_planet\_radius

```python
def get_planet_radius() -> float
```

x.get_planet_radius() -> double
*  Gets the planet radius in centimeters.

Returns:
    double:

<a id="unreal.AesGeoreference.get_planet_center_transform"></a>

#### get\_planet\_center\_transform

```python
def get_planet_center_transform() -> Transform
```

x.get_planet_center_transform() -> Transform
*  Gets the planet center transform.

Returns:
    Transform:

<a id="unreal.AesGeoreference.get_lon_lat_to_world_transform"></a>

#### get\_lon\_lat\_to\_world\_transform

```python
def get_lon_lat_to_world_transform(lon: float,
                                   lat: float,
                                   alt: float = 0.000000) -> Transform
```

x.get_lon_lat_to_world_transform(lon, lat, alt=0.000000) -> Transform
Get Lon Lat to World Transform

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Transform:

<a id="unreal.AesGeoreference.get_lon_lat_to_world_rotation"></a>

#### get\_lon\_lat\_to\_world\_rotation

```python
def get_lon_lat_to_world_rotation(lon: float, lat: float) -> Rotator
```

x.get_lon_lat_to_world_rotation(lon, lat) -> Rotator
通过经纬度坐标求得空间直角变换

Args:
    lon (double): 经度
    lat (double): 纬度

Returns:
    Rotator:

<a id="unreal.AesGeoreference.get_lon_lat_to_world_location"></a>

#### get\_lon\_lat\_to\_world\_location

```python
def get_lon_lat_to_world_location(lon: float,
                                  lat: float,
                                  alt: float = 0.000000) -> Vector
```

x.get_lon_lat_to_world_location(lon, lat, alt=0.000000) -> Vector
经纬度坐标转空间直角坐标

Args:
    lon (double): 经度
    lat (double): 纬度
    alt (double): 海拔高度（厘米）

Returns:
    Vector:

<a id="unreal.AesGeoreference.get_default_georeference"></a>

#### get\_default\_georeference

```python
@classmethod
def get_default_georeference(cls,
                             world_context_object: Object) -> AesGeoreference
```

X.get_default_georeference(world_context_object) -> AesGeoreference
获取GeoReference 但是不会从Earth初始化数据

Args:
    world_context_object (Object): 

Returns:
    AesGeoreference:

<a id="unreal.AesGeoreference.calc_planet_center_transform"></a>

#### calc\_planet\_center\_transform

```python
def calc_planet_center_transform() -> Transform
```

x.calc_planet_center_transform() -> Transform
Calc Planet Center Transform

Returns:
    Transform:

<a id="unreal.AesGeoReferencingSystemProvider"></a>