## WorldOriginAnchor Objects

```python
class WorldOriginAnchor(Actor)
```

World Origin Anchor

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WorldOriginAnchor.h

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
- ``anchor_type`` (AnchorType):  [Read-Write] 默认的投影方式
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
- ``earth_radius`` (double):  [Read-Write] 正球体的半径 用于经纬度转换 单位为厘米
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
- ``origin_altitude`` (double):  [Read-Write] Origin 的高度(m)
- ``origin_at_planet_center`` (bool):  [Read-Write] Origin 中心是否在球的中央 否则为球体表面 需要指定经纬度
- ``origin_latitude`` (double):  [Read-Write] Origin 的纬度
- ``origin_longitude`` (double):  [Read-Write] Origin 的经度
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
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
- ``use_actor_transform_as_origin`` (bool):  [Read-Write] 是否使用Actor自身Transform作为球心 如果为true 将不会使用Origin计算球心Transform
- ``world_center_transform`` (Transform):  [Read-Write] 地球的Transform，Ecef坐标，Z为北极点，用于在地球有旋转的时候做转换

<a id="unreal.WorldOriginAnchor.anchor_type"></a>

#### anchor\_type

```python
@property
def anchor_type() -> AnchorType
```

(AnchorType):  [Read-Write] 默认的投影方式

<a id="unreal.WorldOriginAnchor.anchor_type"></a>

#### anchor\_type

```python
@anchor_type.setter
def anchor_type(value: AnchorType) -> None
```

<a id="unreal.WorldOriginAnchor.world_center_transform"></a>

#### world\_center\_transform

```python
@property
def world_center_transform() -> Transform
```

(Transform):  [Read-Write] 地球的Transform，Ecef坐标，Z为北极点，用于在地球有旋转的时候做转换

<a id="unreal.WorldOriginAnchor.world_center_transform"></a>

#### world\_center\_transform

```python
@world_center_transform.setter
def world_center_transform(value: Transform) -> None
```

<a id="unreal.WorldOriginAnchor.origin_at_planet_center"></a>

#### origin\_at\_planet\_center

```python
@property
def origin_at_planet_center() -> bool
```

(bool):  [Read-Write] Origin 中心是否在球的中央 否则为球体表面 需要指定经纬度

<a id="unreal.WorldOriginAnchor.origin_at_planet_center"></a>

#### origin\_at\_planet\_center

```python
@origin_at_planet_center.setter
def origin_at_planet_center(value: bool) -> None
```

<a id="unreal.WorldOriginAnchor.origin_longitude"></a>

#### origin\_longitude

```python
@property
def origin_longitude() -> float
```

(double):  [Read-Write] Origin 的经度

<a id="unreal.WorldOriginAnchor.origin_longitude"></a>

#### origin\_longitude

```python
@origin_longitude.setter
def origin_longitude(value: float) -> None
```

<a id="unreal.WorldOriginAnchor.origin_latitude"></a>

#### origin\_latitude

```python
@property
def origin_latitude() -> float
```

(double):  [Read-Write] Origin 的纬度

<a id="unreal.WorldOriginAnchor.origin_latitude"></a>

#### origin\_latitude

```python
@origin_latitude.setter
def origin_latitude(value: float) -> None
```

<a id="unreal.WorldOriginAnchor.origin_altitude"></a>

#### origin\_altitude

```python
@property
def origin_altitude() -> float
```

(double):  [Read-Write] Origin 的高度(m)

<a id="unreal.WorldOriginAnchor.origin_altitude"></a>

#### origin\_altitude

```python
@origin_altitude.setter
def origin_altitude(value: float) -> None
```

<a id="unreal.WorldOriginAnchor.earth_radius"></a>

#### earth\_radius

```python
@property
def earth_radius() -> float
```

(double):  [Read-Write] 正球体的半径 用于经纬度转换 单位为厘米

<a id="unreal.WorldOriginAnchor.earth_radius"></a>

#### earth\_radius

```python
@earth_radius.setter
def earth_radius(value: float) -> None
```

<a id="unreal.WorldOriginAnchor.use_actor_transform_as_origin"></a>

#### use\_actor\_transform\_as\_origin

```python
@property
def use_actor_transform_as_origin() -> bool
```

(bool):  [Read-Write] 是否使用Actor自身Transform作为球心 如果为true 将不会使用Origin计算球心Transform

<a id="unreal.WorldOriginAnchor.use_actor_transform_as_origin"></a>

#### use\_actor\_transform\_as\_origin

```python
@use_actor_transform_as_origin.setter
def use_actor_transform_as_origin(value: bool) -> None
```

<a id="unreal.WorldOriginAnchor.update_sphere_mode_data"></a>

#### update\_sphere\_mode\_data

```python
def update_sphere_mode_data(new_origin_at_center: bool, origin_lon: float,
                            origin_lat: float, origin_alt: float) -> None
```

x.update_sphere_mode_data(new_origin_at_center, origin_lon, origin_lat, origin_alt) -> None
初始化球面模式下的设置 并更新坐标

Args:
    new_origin_at_center (bool): 
    origin_lon (double): 
    origin_lat (double): 
    origin_alt (double):

<a id="unreal.WorldOriginAnchor.init_sphere_mode_transform"></a>

#### init\_sphere\_mode\_transform

```python
def init_sphere_mode_transform() -> None
```

x.init_sphere_mode_transform() -> None
初始化球面模式信息 自动更新Transform数据

<a id="unreal.WorldOriginAnchor.initialize"></a>

#### initialize

```python
def initialize() -> None
```

x.initialize() -> None
初始化函数

<a id="unreal.WorldOriginAnchor.get_world_origin_anchor"></a>

#### get\_world\_origin\_anchor

```python
@classmethod
def get_world_origin_anchor(cls,
                            world_context_object: Object) -> WorldOriginAnchor
```

X.get_world_origin_anchor(world_context_object) -> WorldOriginAnchor
获取WorldOriginAnchor引用，需要在场景中摆放一个，用于球面操作和坐标转换

Args:
    world_context_object (Object): 

Returns:
    WorldOriginAnchor:

<a id="unreal.WorldOriginAnchor.get_world_location_to_lon_lat_sphere"></a>

#### get\_world\_location\_to\_lon\_lat\_sphere

```python
def get_world_location_to_lon_lat_sphere(location: Vector,
                                         radius: float) -> Vector
```

x.get_world_location_to_lon_lat_sphere(location, radius) -> Vector
世界坐标转经纬度 X: Lon Y: Lat Z: Alt 球

Args:
    location (Vector): 
    radius (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_world_location_to_lon_lat_geo_ref"></a>

#### get\_world\_location\_to\_lon\_lat\_geo\_ref

```python
def get_world_location_to_lon_lat_geo_ref(location: Vector) -> Vector
```

x.get_world_location_to_lon_lat_geo_ref(location) -> Vector
世界坐标转经纬度 X: Lon Y: Lat Z: Alt GeoReferencingSystem

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_world_location_to_lon_lat_cesium"></a>

#### get\_world\_location\_to\_lon\_lat\_cesium

```python
def get_world_location_to_lon_lat_cesium(location: Vector) -> Vector
```

x.get_world_location_to_lon_lat_cesium(location) -> Vector
世界坐标转经纬度 X: Lon Y: Lat Z: Alt Cesium

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_world_location_to_lon_lat_aes6"></a>

#### get\_world\_location\_to\_lon\_lat\_aes6

```python
def get_world_location_to_lon_lat_aes6(location: Vector) -> Vector
```

x.get_world_location_to_lon_lat_aes6(location) -> Vector
世界坐标转经纬度 X: Lon Y: Lat Z: Alt Aes6

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_world_location_to_lon_lat"></a>

#### get\_world\_location\_to\_lon\_lat

```python
def get_world_location_to_lon_lat(location: Vector) -> Vector
```

x.get_world_location_to_lon_lat(location) -> Vector
世界坐标转经纬度 X: Lon Y: Lat Z: 高度-单位为米  通用

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_world_center"></a>

#### get\_world\_center

```python
def get_world_center() -> Vector
```

x.get_world_center() -> Vector
获取地球中心点

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_surface_direction_sphere"></a>

#### get\_surface\_direction\_sphere

```python
def get_surface_direction_sphere(location: Vector) -> Vector
```

x.get_surface_direction_sphere(location) -> Vector
获取球面朝天空的方向

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_surface_direction"></a>

#### get\_surface\_direction

```python
def get_surface_direction(location: Vector) -> Vector
```

x.get_surface_direction(location) -> Vector
获取球面朝天空的方向

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_lon_lat_to_world_location_sphere"></a>

#### get\_lon\_lat\_to\_world\_location\_sphere

```python
def get_lon_lat_to_world_location_sphere(lon: float, lat: float, alt: float,
                                         radius: float) -> Vector
```

x.get_lon_lat_to_world_location_sphere(lon, lat, alt, radius) -> Vector
经纬度转到世界坐标 球面

Args:
    lon (double): 
    lat (double): 
    alt (double): 
    radius (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_lon_lat_to_world_location_geo_ref"></a>

#### get\_lon\_lat\_to\_world\_location\_geo\_ref

```python
def get_lon_lat_to_world_location_geo_ref(lon: float, lat: float,
                                          alt: float) -> Vector
```

x.get_lon_lat_to_world_location_geo_ref(lon, lat, alt) -> Vector
经纬度转到世界坐标 GeoReferencingSystem

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_lon_lat_to_world_location_cesium"></a>

#### get\_lon\_lat\_to\_world\_location\_cesium

```python
def get_lon_lat_to_world_location_cesium(lon: float, lat: float,
                                         alt: float) -> Vector
```

x.get_lon_lat_to_world_location_cesium(lon, lat, alt) -> Vector
经纬度转到世界坐标 Cesium

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_lon_lat_to_world_location_aes6"></a>

#### get\_lon\_lat\_to\_world\_location\_aes6

```python
def get_lon_lat_to_world_location_aes6(lon: float, lat: float,
                                       alt: float) -> Vector
```

x.get_lon_lat_to_world_location_aes6(lon, lat, alt) -> Vector
经纬度转到世界坐标 Aes6

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_lon_lat_to_world_location"></a>

#### get\_lon\_lat\_to\_world\_location

```python
def get_lon_lat_to_world_location(lon: float, lat: float,
                                  alt: float) -> Vector
```

x.get_lon_lat_to_world_location(lon, lat, alt) -> Vector
经纬度转到世界坐标 高度单位为米 通用

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_is_planet_world"></a>

#### get\_is\_planet\_world

```python
def get_is_planet_world() -> bool
```

x.get_is_planet_world() -> bool
当前是否在地球操作模式 根据AnchorType自动判断

Returns:
    bool:

<a id="unreal.WorldOriginAnchor.get_gravity_direction"></a>

#### get\_gravity\_direction

```python
def get_gravity_direction(location: Vector) -> Vector
```

x.get_gravity_direction(location) -> Vector
获取重力方向

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.get_east_south_up_rotation_sphere"></a>

#### get\_east\_south\_up\_rotation\_sphere

```python
def get_east_south_up_rotation_sphere(location: Vector) -> Rotator
```

x.get_east_south_up_rotation_sphere(location) -> Rotator
获取EastSouthUp方向的Transform，Z朝天空，X 朝向正东，-Y 朝向正北 正球

Args:
    location (Vector): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.get_east_south_up_rotation_geo_ref"></a>

#### get\_east\_south\_up\_rotation\_geo\_ref

```python
def get_east_south_up_rotation_geo_ref(location: Vector) -> Rotator
```

x.get_east_south_up_rotation_geo_ref(location) -> Rotator
获取EastSouthUp方向的Transform，Z朝天空，X 朝向正东，-Y 朝向正北 GeoReferencingSystem

Args:
    location (Vector): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.get_east_south_up_rotation_cesium"></a>

#### get\_east\_south\_up\_rotation\_cesium

```python
def get_east_south_up_rotation_cesium(location: Vector) -> Rotator
```

x.get_east_south_up_rotation_cesium(location) -> Rotator
获取EastSouthUp方向的Transform，Z朝天空，X 朝向正东，-Y 朝向正北 Cesium

Args:
    location (Vector): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.get_east_south_up_rotation_aes6"></a>

#### get\_east\_south\_up\_rotation\_aes6

```python
def get_east_south_up_rotation_aes6(location: Vector) -> Rotator
```

x.get_east_south_up_rotation_aes6(location) -> Rotator
获取EastSouthUp方向的Transform，Z朝天空，X 朝向正东，-Y 朝向正北 Aes6

Args:
    location (Vector): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.get_east_south_up_rotation"></a>

#### get\_east\_south\_up\_rotation

```python
def get_east_south_up_rotation(location: Vector) -> Rotator
```

x.get_east_south_up_rotation(location) -> Rotator
获取EastSouthUp方向的Transform，Z朝天空，X 朝向正东，-Y 朝向正北 通用

Args:
    location (Vector): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.get_earth_center_transform_geo_ref"></a>

#### get\_earth\_center\_transform\_geo\_ref

```python
def get_earth_center_transform_geo_ref() -> Transform
```

x.get_earth_center_transform_geo_ref() -> Transform
获取地球中心点Transform GeoReferencingSystem

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.get_earth_center_transform_cesium"></a>

#### get\_earth\_center\_transform\_cesium

```python
def get_earth_center_transform_cesium() -> Transform
```

x.get_earth_center_transform_cesium() -> Transform
获取地球中心点Transform Cesium

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.get_earth_center_transform_aes6"></a>

#### get\_earth\_center\_transform\_aes6

```python
def get_earth_center_transform_aes6() -> Transform
```

x.get_earth_center_transform_aes6() -> Transform
获取地球中心点Transform Aes6

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.get_earth_center_transform"></a>

#### get\_earth\_center\_transform

```python
def get_earth_center_transform() -> Transform
```

x.get_earth_center_transform() -> Transform
获取地球中心点Transform 通用

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.get_altitude_at_location"></a>

#### get\_altitude\_at\_location

```python
def get_altitude_at_location(location: Vector) -> float
```

x.get_altitude_at_location(location) -> double
获取海拔高度

Args:
    location (Vector): 

Returns:
    double:

<a id="unreal.WorldOriginAnchor.convert_surface_rotation_to_world"></a>

#### convert\_surface\_rotation\_to\_world

```python
def convert_surface_rotation_to_world(location: Vector,
                                      rotation: Rotator) -> Rotator
```

x.convert_surface_rotation_to_world(location, rotation) -> Rotator
将地表空间转换成世界空间 需要指定一个位移判断地表

Args:
    location (Vector): 
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.convert_rotation_to_surface_space"></a>

#### convert\_rotation\_to\_surface\_space

```python
def convert_rotation_to_surface_space(location: Vector,
                                      rotation: Rotator) -> Rotator
```

x.convert_rotation_to_surface_space(location, rotation) -> Rotator
将世界空间的旋转转换为地表方向的旋转 需要指定一个位移以判断地表

Args:
    location (Vector): 
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.WorldOriginAnchor.convert_lon_lat_alt_to_camera_data"></a>

#### convert\_lon\_lat\_alt\_to\_camera\_data

```python
def convert_lon_lat_alt_to_camera_data(
    longtude: float,
    latitude: float,
    altitude: float,
    surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]
) -> Optional[CoreCameraData]
```

x.convert_lon_lat_alt_to_camera_data(longtude, latitude, altitude, surface_rotation=[0.000000, -45.000000, 0.000000]) -> CoreCameraData or None
将经纬度高度和旋转转换为相机参数

Args:
    longtude (double): 
    latitude (double): 
    altitude (double): 
    surface_rotation (Rotator): 

Returns:
    CoreCameraData or None: 

    out_camera_data (CoreCameraData):

<a id="unreal.WorldOriginAnchor.convert_focus_to_lon_lat_alt_to_camera_data"></a>

#### convert\_focus\_to\_lon\_lat\_alt\_to\_camera\_data

```python
def convert_focus_to_lon_lat_alt_to_camera_data(
    target_longtude: float,
    target_latitude: float,
    target_altitude: float,
    distance: float = 1000.000000,
    surface_rotation: Rotator = [0.000000, -45.000000, 0.000000]
) -> Optional[CoreCameraData]
```

x.convert_focus_to_lon_lat_alt_to_camera_data(target_longtude, target_latitude, target_altitude, distance=1000.000000, surface_rotation=[0.000000, -45.000000, 0.000000]) -> CoreCameraData or None
计算看向一个经纬度高度点加上距离和旋转 转换为相机参数

Args:
    target_longtude (double): 
    target_latitude (double): 
    target_altitude (double): 
    distance (double): 
    surface_rotation (Rotator): 

Returns:
    CoreCameraData or None: 

    out_camera_data (CoreCameraData):

<a id="unreal.WorldOriginAnchor.calc_world_center_transform"></a>

#### calc\_world\_center\_transform

```python
def calc_world_center_transform(lon: float, lat: float,
                                alt: float) -> Transform
```

x.calc_world_center_transform(lon, lat, alt) -> Transform
输入原点的经纬度坐标 反向计算球心的Transform

Args:
    lon (double): 
    lat (double): 
    alt (double): 

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.calc_origin_from_sphere_center_transform"></a>

#### calc\_origin\_from\_sphere\_center\_transform

```python
def calc_origin_from_sphere_center_transform(transform: Transform) -> Vector
```

x.calc_origin_from_sphere_center_transform(transform) -> Vector
输入球心ECEF坐标 反向计算出Origin X=Long Y=Lat Z=Alt(m)

Args:
    transform (Transform): 

Returns:
    Vector:

<a id="unreal.WorldOriginAnchor.calc_move_on_sphere_surface"></a>

#### calc\_move\_on\_sphere\_surface

```python
def calc_move_on_sphere_surface(current: Transform, world_dir: Vector,
                                distance: float) -> Transform
```

x.calc_move_on_sphere_surface(current, world_dir, distance) -> Transform
计算在球表面移动一段距离后的新Transform

Args:
    current (Transform): 
    world_dir (Vector): 
    distance (double): 

Returns:
    Transform:

<a id="unreal.WorldOriginAnchor.calc_move_along_surface"></a>

#### calc\_move\_along\_surface

```python
def calc_move_along_surface(start: Vector,
                            surface_dir: Vector) -> Tuple[Vector, Rotator]
```

x.calc_move_along_surface(start, surface_dir) -> (out_location=Vector, out_delta_rotation=Rotator)
计算沿着平面方向移动后的位置和产生的旋转变化，方向会被限制在平面上，SurfaceDir的长度就是运动距离

Args:
    start (Vector): 
    surface_dir (Vector): 

Returns:
    tuple: 

    out_location (Vector): 

    out_delta_rotation (Rotator):

<a id="unreal.ActionManager"></a>