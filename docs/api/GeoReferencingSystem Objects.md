## GeoReferencingSystem Objects

```python
class GeoReferencingSystem(Info)
```

This AInfos enable you to define a correspondance between the UE origin and an actual geographic location on a planet
Once done it offers different functions to convert coordinates between UE and Geographic coordinates

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: GeoReferencingSystem.h

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
- ``geographic_crs`` (str):  [Read-Write] String that describes the GEOGRAPHIC CRS of choice.
     CRS can be identified by their code (EPSG:4326), a well-known text(WKT) string, or PROJ strings...
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
- ``origin_altitude`` (double):  [Read-Write] Altitude of UE Origin on planet
- ``origin_at_planet_center`` (bool):  [Read-Write] if true, the UE origin is located at the Planet Center, otherwise,
  the UE origin is assuming to be defined at one specific point of
  the planet surface, defined by the properties below.
- ``origin_latitude`` (double):  [Read-Write] Latitude of UE Origin on planet
- ``origin_location_in_projected_crs`` (bool):  [Read-Write] if true, the UE origin georeference is expressed in the PROJECTED CRS.
      (NOT in ECEF ! - Projected worlds are the most frequent use case...)
  if false, the origin is located using geographic coordinates.

  WARNING : the location has to be expressed as Integer values because of accuracy.
  Be very careful about that when authoring your data in external tools !
- ``origin_longitude`` (double):  [Read-Write] Longitude of UE Origin on planet
- ``origin_projected_coordinates_easting`` (double):  [Read-Write] Easting position of UE Origin on planet, express in the Projected CRS Frame
- ``origin_projected_coordinates_northing`` (double):  [Read-Write] Northing position of UE Origin on planet, express in the Projected CRS Frame
- ``origin_projected_coordinates_up`` (double):  [Read-Write] Up position of UE Origin on planet, express in the Projected CRS Frame
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``planet_shape`` (PlanetShape):  [Read-Write] This mode has to be set consistently with the way you authored your ground geometry.
   - For small environments, a projection is often applied and the world is considered as Flat
   - For planet scale environments, projections is not suitable and the geometry is Rounded.
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``projected_crs`` (str):  [Read-Write] String that describes the PROJECTED CRS of choice.
     CRS can be identified by their code (EPSG:4326), a well-known text(WKT) string, or PROJ strings...
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

<a id="unreal.GeoReferencingSystem.planet_shape"></a>

#### planet_shape

```python
@property
def planet_shape() -> PlanetShape
```

(PlanetShape):  [Read-Write] This mode has to be set consistently with the way you authored your ground geometry.
 - For small environments, a projection is often applied and the world is considered as Flat
 - For planet scale environments, projections is not suitable and the geometry is Rounded.

<a id="unreal.GeoReferencingSystem.planet_shape"></a>

#### planet_shape

```python
@planet_shape.setter
def planet_shape(value: PlanetShape) -> None
```

<a id="unreal.GeoReferencingSystem.projected_crs"></a>

#### projected_crs

```python
@property
def projected_crs() -> str
```

(str):  [Read-Write] String that describes the PROJECTED CRS of choice.
   CRS can be identified by their code (EPSG:4326), a well-known text(WKT) string, or PROJ strings...

<a id="unreal.GeoReferencingSystem.projected_crs"></a>

#### projected_crs

```python
@projected_crs.setter
def projected_crs(value: str) -> None
```

<a id="unreal.GeoReferencingSystem.geographic_crs"></a>

#### geographic_crs

```python
@property
def geographic_crs() -> str
```

(str):  [Read-Write] String that describes the GEOGRAPHIC CRS of choice.
   CRS can be identified by their code (EPSG:4326), a well-known text(WKT) string, or PROJ strings...

<a id="unreal.GeoReferencingSystem.geographic_crs"></a>

#### geographic_crs

```python
@geographic_crs.setter
def geographic_crs(value: str) -> None
```

<a id="unreal.GeoReferencingSystem.origin_at_planet_center"></a>

#### origin_at_planet_center

```python
@property
def origin_at_planet_center() -> bool
```

(bool):  [Read-Write] if true, the UE origin is located at the Planet Center, otherwise,
the UE origin is assuming to be defined at one specific point of
the planet surface, defined by the properties below.

<a id="unreal.GeoReferencingSystem.origin_at_planet_center"></a>

#### origin_at_planet_center

```python
@origin_at_planet_center.setter
def origin_at_planet_center(value: bool) -> None
```

<a id="unreal.GeoReferencingSystem.origin_location_in_projected_crs"></a>

#### origin_location_in_projected_crs

```python
@property
def origin_location_in_projected_crs() -> bool
```

(bool):  [Read-Write] if true, the UE origin georeference is expressed in the PROJECTED CRS.
    (NOT in ECEF ! - Projected worlds are the most frequent use case...)
if false, the origin is located using geographic coordinates.

WARNING : the location has to be expressed as Integer values because of accuracy.
Be very careful about that when authoring your data in external tools !

<a id="unreal.GeoReferencingSystem.origin_location_in_projected_crs"></a>

#### origin_location_in_projected_crs

```python
@origin_location_in_projected_crs.setter
def origin_location_in_projected_crs(value: bool) -> None
```

<a id="unreal.GeoReferencingSystem.origin_latitude"></a>

#### origin_latitude

```python
@property
def origin_latitude() -> float
```

(double):  [Read-Write] Latitude of UE Origin on planet

<a id="unreal.GeoReferencingSystem.origin_latitude"></a>

#### origin_latitude

```python
@origin_latitude.setter
def origin_latitude(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.origin_longitude"></a>

#### origin_longitude

```python
@property
def origin_longitude() -> float
```

(double):  [Read-Write] Longitude of UE Origin on planet

<a id="unreal.GeoReferencingSystem.origin_longitude"></a>

#### origin_longitude

```python
@origin_longitude.setter
def origin_longitude(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.origin_altitude"></a>

#### origin_altitude

```python
@property
def origin_altitude() -> float
```

(double):  [Read-Write] Altitude of UE Origin on planet

<a id="unreal.GeoReferencingSystem.origin_altitude"></a>

#### origin_altitude

```python
@origin_altitude.setter
def origin_altitude(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_easting"></a>

#### origin_projected_coordinates_easting

```python
@property
def origin_projected_coordinates_easting() -> float
```

(double):  [Read-Write] Easting position of UE Origin on planet, express in the Projected CRS Frame

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_easting"></a>

#### origin_projected_coordinates_easting

```python
@origin_projected_coordinates_easting.setter
def origin_projected_coordinates_easting(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_northing"></a>

#### origin_projected_coordinates_northing

```python
@property
def origin_projected_coordinates_northing() -> float
```

(double):  [Read-Write] Northing position of UE Origin on planet, express in the Projected CRS Frame

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_northing"></a>

#### origin_projected_coordinates_northing

```python
@origin_projected_coordinates_northing.setter
def origin_projected_coordinates_northing(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_up"></a>

#### origin_projected_coordinates_up

```python
@property
def origin_projected_coordinates_up() -> float
```

(double):  [Read-Write] Up position of UE Origin on planet, express in the Projected CRS Frame

<a id="unreal.GeoReferencingSystem.origin_projected_coordinates_up"></a>

#### origin_projected_coordinates_up

```python
@origin_projected_coordinates_up.setter
def origin_projected_coordinates_up(value: float) -> None
```

<a id="unreal.GeoReferencingSystem.k2_projected_to_geographic"></a>

#### k2_projected_to_geographic

```python
def k2_projected_to_geographic(
        projected_coordinates: Vector) -> GeographicCoordinates
```

x.k2_projected_to_geographic(projected_coordinates) -> GeographicCoordinates
Convert a Coordinate expressed in PROJECTED CRS to GEOGRAPHIC CRS

Args:
    projected_coordinates (Vector): 

Returns:
    GeographicCoordinates: 

    geographic_coordinates (GeographicCoordinates):

<a id="unreal.GeoReferencingSystem.k2_projected_to_engine"></a>

#### k2_projected_to_engine

```python
def k2_projected_to_engine(projected_coordinates: Vector) -> Vector
```

x.k2_projected_to_engine(projected_coordinates) -> Vector
Convert a Vector expressed in PROJECTED CRS to ENGINE space

Args:
    projected_coordinates (Vector): 

Returns:
    Vector: 

    engine_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_projected_to_ecef"></a>

#### k2_projected_to_ecef

```python
def k2_projected_to_ecef(projected_coordinates: Vector) -> Vector
```

x.k2_projected_to_ecef(projected_coordinates) -> Vector
Convert a Coordinate expressed in PROJECTED CRS to ECEF CRS

Args:
    projected_coordinates (Vector): 

Returns:
    Vector: 

    ecef_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_get_tangent_transform_at_projected_location"></a>

#### k2_get_tangent_transform_at_projected_location

```python
def k2_get_tangent_transform_at_projected_location(
        projected_coordinates: Vector) -> Transform
```

x.k2_get_tangent_transform_at_projected_location(projected_coordinates) -> Transform
Get the the transform to locate an object tangent to Ellipsoid at a specific location

Args:
    projected_coordinates (Vector): 

Returns:
    Transform:

<a id="unreal.GeoReferencingSystem.k2_get_tangent_transform_at_ecef_location"></a>

#### k2_get_tangent_transform_at_ecef_location

```python
def k2_get_tangent_transform_at_ecef_location(
        ecef_coordinates: Vector) -> Transform
```

x.k2_get_tangent_transform_at_ecef_location(ecef_coordinates) -> Transform
Get the the transform to locate an object tangent to Ellipsoid at a specific location

Args:
    ecef_coordinates (Vector): 

Returns:
    Transform:

<a id="unreal.GeoReferencingSystem.k2_get_enu_vectors_at_projected_location"></a>

#### k2_get_enu_vectors_at_projected_location

```python
def k2_get_enu_vectors_at_projected_location(
        projected_coordinates: Vector) -> Tuple[Vector, Vector, Vector]
```

x.k2_get_enu_vectors_at_projected_location(projected_coordinates) -> (east=Vector, north=Vector, up=Vector)
Get the East North Up vectors at a specific location

Args:
    projected_coordinates (Vector): 

Returns:
    tuple: 

    east (Vector): 

    north (Vector): 

    up (Vector):

<a id="unreal.GeoReferencingSystem.k2_get_enu_vectors_at_ecef_location"></a>

#### k2_get_enu_vectors_at_ecef_location

```python
def k2_get_enu_vectors_at_ecef_location(
        ecef_coordinates: Vector) -> Tuple[Vector, Vector, Vector]
```

x.k2_get_enu_vectors_at_ecef_location(ecef_coordinates) -> (east=Vector, north=Vector, up=Vector)
Get the East North Up vectors at a specific location

Args:
    ecef_coordinates (Vector): 

Returns:
    tuple: 

    east (Vector): 

    north (Vector): 

    up (Vector):

<a id="unreal.GeoReferencingSystem.k2_get_ecefenu_vectors_at_ecef_location"></a>

#### k2_get_ecefenu_vectors_at_ecef_location

```python
def k2_get_ecefenu_vectors_at_ecef_location(
        ecef_coordinates: Vector) -> Tuple[Vector, Vector, Vector]
```

x.k2_get_ecefenu_vectors_at_ecef_location(ecef_coordinates) -> (ecef_east=Vector, ecef_north=Vector, ecef_up=Vector)
Get the East North Up vectors at a specific location - Not in engine frame, but in pure ECEF Frame !

Args:
    ecef_coordinates (Vector): 

Returns:
    tuple: 

    ecef_east (Vector): 

    ecef_north (Vector): 

    ecef_up (Vector):

<a id="unreal.GeoReferencingSystem.k2_geographic_to_projected"></a>

#### k2_geographic_to_projected

```python
def k2_geographic_to_projected(
        geographic_coordinates: GeographicCoordinates) -> Vector
```

x.k2_geographic_to_projected(geographic_coordinates) -> Vector
Convert a Coordinate expressed in GEOGRAPHIC CRS to PROJECTED CRS

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    Vector: 

    projected_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_geographic_to_ecef"></a>

#### k2_geographic_to_ecef

```python
def k2_geographic_to_ecef(
        geographic_coordinates: GeographicCoordinates) -> Vector
```

x.k2_geographic_to_ecef(geographic_coordinates) -> Vector
Convert a Coordinate expressed in GEOGRAPHIC CRS to ECEF CRS

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    Vector: 

    ecef_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_engine_to_projected"></a>

#### k2_engine_to_projected

```python
def k2_engine_to_projected(engine_coordinates: Vector) -> Vector
```

x.k2_engine_to_projected(engine_coordinates) -> Vector
Convert a Vector expressed in ENGINE space to the PROJECTED CRS

Args:
    engine_coordinates (Vector): 

Returns:
    Vector: 

    projected_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_engine_to_ecef"></a>

#### k2_engine_to_ecef

```python
def k2_engine_to_ecef(engine_coordinates: Vector) -> Vector
```

x.k2_engine_to_ecef(engine_coordinates) -> Vector
Convert a Vector expressed in ENGINE space to the ECEF CRS

Args:
    engine_coordinates (Vector): 

Returns:
    Vector: 

    ecef_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_ecef_to_projected"></a>

#### k2_ecef_to_projected

```python
def k2_ecef_to_projected(ecef_coordinates: Vector) -> Vector
```

x.k2_ecef_to_projected(ecef_coordinates) -> Vector
Convert a Coordinate expressed in ECEF CRS to PROJECTED CRS

Args:
    ecef_coordinates (Vector): 

Returns:
    Vector: 

    projected_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.k2_ecef_to_geographic"></a>

#### k2_ecef_to_geographic

```python
def k2_ecef_to_geographic(ecef_coordinates: Vector) -> GeographicCoordinates
```

x.k2_ecef_to_geographic(ecef_coordinates) -> GeographicCoordinates
Convert a Coordinate expressed in ECEF CRS to GEOGRAPHIC CRS

Args:
    ecef_coordinates (Vector): 

Returns:
    GeographicCoordinates: 

    geographic_coordinates (GeographicCoordinates):

<a id="unreal.GeoReferencingSystem.k2_ecef_to_engine"></a>

#### k2_ecef_to_engine

```python
def k2_ecef_to_engine(ecef_coordinates: Vector) -> Vector
```

x.k2_ecef_to_engine(ecef_coordinates) -> Vector
Convert a Vector expressed in ECEF CRS to ENGINE space

Args:
    ecef_coordinates (Vector): 

Returns:
    Vector: 

    engine_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.is_crs_string_valid"></a>

#### is_crs_string_valid

```python
def is_crs_string_valid(crs_string: str) -> Optional[str]
```

x.is_crs_string_valid(crs_string) -> str or None
Check if the string corresponds to a valid CRS descriptor

Args:
    crs_string (str): 

Returns:
    str or None: 

    error (str):

<a id="unreal.GeoReferencingSystem.get_tangent_transform_at_geographic_location"></a>

#### get_tangent_transform_at_geographic_location

```python
def get_tangent_transform_at_geographic_location(
        geographic_coordinates: GeographicCoordinates) -> Transform
```

x.get_tangent_transform_at_geographic_location(geographic_coordinates) -> Transform
Get the the transform to locate an object tangent to Ellipsoid at a specific location

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    Transform:

<a id="unreal.GeoReferencingSystem.get_tangent_transform_at_engine_location"></a>

#### get_tangent_transform_at_engine_location

```python
def get_tangent_transform_at_engine_location(
        engine_coordinates: Vector) -> Transform
```

x.get_tangent_transform_at_engine_location(engine_coordinates) -> Transform
Get the the transform to locate an object tangent to Ellipsoid at a specific location

Args:
    engine_coordinates (Vector): 

Returns:
    Transform:

<a id="unreal.GeoReferencingSystem.get_projected_ellipsoid_min_radius"></a>

#### get_projected_ellipsoid_min_radius

```python
def get_projected_ellipsoid_min_radius() -> float
```

x.get_projected_ellipsoid_min_radius() -> double
Find the underlying Projected CRS Ellipsoid and return its minimum radius

Returns:
    double:

<a id="unreal.GeoReferencingSystem.get_projected_ellipsoid_max_radius"></a>

#### get_projected_ellipsoid_max_radius

```python
def get_projected_ellipsoid_max_radius() -> float
```

x.get_projected_ellipsoid_max_radius() -> double
Find the underlying Projected CRS Ellipsoid and return its maximum radius

Returns:
    double:

<a id="unreal.GeoReferencingSystem.get_planet_center_transform"></a>

#### get_planet_center_transform

```python
def get_planet_center_transform() -> Transform
```

x.get_planet_center_transform() -> Transform
Set this transform to an Ellipsoid to have it positioned tangent to the origin.

Returns:
    Transform:

<a id="unreal.GeoReferencingSystem.get_geo_referencing_system"></a>

#### get_geo_referencing_system

```python
@classmethod
def get_geo_referencing_system(
        cls, world_context_object: Object) -> GeoReferencingSystem
```

X.get_geo_referencing_system(world_context_object) -> GeoReferencingSystem
Get Geo Referencing System

Args:
    world_context_object (Object): 

Returns:
    GeoReferencingSystem:

<a id="unreal.GeoReferencingSystem.get_geographic_ellipsoid_min_radius"></a>

#### get_geographic_ellipsoid_min_radius

```python
def get_geographic_ellipsoid_min_radius() -> float
```

x.get_geographic_ellipsoid_min_radius() -> double
Find the underlying Geographic CRS Ellipsoid and return its minimum radius

Returns:
    double:

<a id="unreal.GeoReferencingSystem.get_geographic_ellipsoid_max_radius"></a>

#### get_geographic_ellipsoid_max_radius

```python
def get_geographic_ellipsoid_max_radius() -> float
```

x.get_geographic_ellipsoid_max_radius() -> double
Find the underlying Geographic CRS Ellipsoid and return its maximum radius

Returns:
    double:

<a id="unreal.GeoReferencingSystem.get_enu_vectors_at_geographic_location"></a>

#### get_enu_vectors_at_geographic_location

```python
def get_enu_vectors_at_geographic_location(
    geographic_coordinates: GeographicCoordinates
) -> Tuple[Vector, Vector, Vector]
```

x.get_enu_vectors_at_geographic_location(geographic_coordinates) -> (east=Vector, north=Vector, up=Vector)
Get the East North Up vectors at a specific location

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    tuple: 

    east (Vector): 

    north (Vector): 

    up (Vector):

<a id="unreal.GeoReferencingSystem.get_enu_vectors_at_engine_location"></a>

#### get_enu_vectors_at_engine_location

```python
def get_enu_vectors_at_engine_location(
        engine_coordinates: Vector) -> Tuple[Vector, Vector, Vector]
```

x.get_enu_vectors_at_engine_location(engine_coordinates) -> (east=Vector, north=Vector, up=Vector)
Get the East North Up vectors at a specific location

Args:
    engine_coordinates (Vector): 

Returns:
    tuple: 

    east (Vector): 

    north (Vector): 

    up (Vector):

<a id="unreal.GeoReferencingSystem.geographic_to_engine"></a>

#### geographic_to_engine

```python
def geographic_to_engine(
        geographic_coordinates: GeographicCoordinates) -> Vector
```

x.geographic_to_engine(geographic_coordinates) -> Vector
Convert a Vector expressed in GEOGRAPHIC CRS to ENGINE space

Args:
    geographic_coordinates (GeographicCoordinates): 

Returns:
    Vector: 

    engine_coordinates (Vector):

<a id="unreal.GeoReferencingSystem.engine_to_geographic"></a>

#### engine_to_geographic

```python
def engine_to_geographic(engine_coordinates: Vector) -> GeographicCoordinates
```

x.engine_to_geographic(engine_coordinates) -> GeographicCoordinates
Convert a Vector expressed in ENGINE space to the GEOGRAPHIC CRS

Args:
    engine_coordinates (Vector): 

Returns:
    GeographicCoordinates: 

    geographic_coordinates (GeographicCoordinates):

<a id="unreal.GeoReferencingSystem.apply_settings"></a>

#### apply_settings

```python
def apply_settings() -> None
```

x.apply_settings() -> None
In case you want to change the Origin or CRS definition properties during application execution, you need to call this function to update the internal transformation cache.
Note this is not a recommended practice, because it will not move the level actors accordingly.
Can be useful though if you rebase your actors yourself, or if you want to change one CRS used for displaying coordinates.

<a id="unreal.RoundPlanetPawn"></a>