## CesiumGeoreference Objects

```python
class CesiumGeoreference(Actor)
```

Controls how global geospatial coordinates are mapped to coordinates in the
Unreal Engine level. Internally, Cesium uses a global Earth-centered,
Earth-fixed (ECEF) ellipsoid-centered coordinate system, where the ellipsoid
is usually the World Geodetic System 1984 (WGS84) ellipsoid. This is a
right-handed system centered at the Earth's center of mass, where +X is in
the direction of the intersection of the Equator and the Prime Meridian (zero
degrees longitude), +Y is in the direction of the intersection of the Equator
and +90 degrees longitude, and +Z is through the North Pole. This Actor is
used by other Cesium Actors and components to control how this coordinate
system is mapped into an Unreal Engine world and level.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumGeoreference.h

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
- ``cesium_sub_levels`` (Array[CesiumSubLevel]):  [Read-Write]
  deprecated: Create sub-levels by adding a UCesiumSubLevelComponent to an ALevelInstance Actor.
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
- ``ellipsoid`` (CesiumEllipsoid):  [Read-Write] The Ellipsoid being used by this georeference. The ellipsoid informs how
  cartographic coordinates will be interpreted and how they are transformed
  into cartesian coordinates.
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
- ``on_ellipsoid_changed`` (GeoreferenceEllipsoidChanged):  [Read-Write] An event that will be called whenever the georeference's ellipsoid has
  been modified.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_georeference_updated`` (GeoreferenceUpdated):  [Read-Write] A delegate that will be called whenever the Georeference is
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
- ``origin_height`` (double):  [Read-Write] The height of the custom origin placement in meters above the
  ellipsoid.
- ``origin_latitude`` (double):  [Read-Write] The latitude of the custom origin placement in degrees, in the range [-90,
  90]
- ``origin_longitude`` (double):  [Read-Write] The longitude of the custom origin placement in degrees, in the range
  [-180, 180]
- ``origin_placement`` (OriginPlacement):  [Read-Write] The placement of this Actor's origin (coordinate 0,0,0) within the tileset.

  3D Tiles tilesets often use Earth-centered, Earth-fixed coordinates, such
  that the tileset content is in a small bounding volume 6-7 million meters
  (the radius of the Earth) away from the coordinate system origin. This
  property allows an alternative position, other then the tileset's true
  origin, to be treated as the origin for the purpose of this Actor. Using
  this property will preserve vertex precision (and thus avoid jittering)
  much better than setting the Actor's Transform property.
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
- ``root`` (SceneComponent):  [Read-Only] This property mirrors RootComponent, and exists only so that the root
  component's transform is editable in the Editor.
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``scale`` (double):  [Read-Write] The percentage scale of the globe in the Unreal world. If this value is 50,
  for example, one meter on the globe occupies half a meter in the Unreal
  world.
- ``show_load_radii`` (bool):  [Read-Write] Whether to visualize the level loading radii in the editor. Helpful for
  initially positioning the level and choosing a load radius.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``sub_level_camera`` (PlayerCameraManager):  [Read-Write] The camera to use to determine which sub-level is closest, so that one can
  be activated and all others deactivated.
  deprecated: Add a CesiumOriginShiftComponent to the appropriate Actor instead.
  deprecated: Add a CesiumOriginShiftComponent to the appropriate Actor instead.
- ``sub_level_switcher`` (CesiumSubLevelSwitcherComponent):  [Read-Write] The component that allows switching between the sub-levels registered with
  this georeference.
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

<a id="unreal.CesiumGeoreference.on_georeference_updated"></a>

#### on\_georeference\_updated

```python
@property
def on_georeference_updated() -> GeoreferenceUpdated
```

(GeoreferenceUpdated):  [Read-Write] A delegate that will be called whenever the Georeference is
modified in a way that affects its computations.

<a id="unreal.CesiumGeoreference.on_georeference_updated"></a>

#### on\_georeference\_updated

```python
@on_georeference_updated.setter
def on_georeference_updated(value: GeoreferenceUpdated) -> None
```

<a id="unreal.CesiumGeoreference.on_ellipsoid_changed"></a>

#### on\_ellipsoid\_changed

```python
@property
def on_ellipsoid_changed() -> GeoreferenceEllipsoidChanged
```

(GeoreferenceEllipsoidChanged):  [Read-Write] An event that will be called whenever the georeference's ellipsoid has
been modified.

<a id="unreal.CesiumGeoreference.on_ellipsoid_changed"></a>

#### on\_ellipsoid\_changed

```python
@on_ellipsoid_changed.setter
def on_ellipsoid_changed(value: GeoreferenceEllipsoidChanged) -> None
```

<a id="unreal.CesiumGeoreference.ellipsoid"></a>

#### ellipsoid

```python
@property
def ellipsoid() -> CesiumEllipsoid
```

(CesiumEllipsoid):  [Read-Write] The Ellipsoid being used by this georeference. The ellipsoid informs how
cartographic coordinates will be interpreted and how they are transformed
into cartesian coordinates.

<a id="unreal.CesiumGeoreference.ellipsoid"></a>

#### ellipsoid

```python
@ellipsoid.setter
def ellipsoid(value: CesiumEllipsoid) -> None
```

<a id="unreal.CesiumGeoreference.origin_placement"></a>

#### origin\_placement

```python
@property
def origin_placement() -> OriginPlacement
```

(OriginPlacement):  [Read-Write] The placement of this Actor's origin (coordinate 0,0,0) within the tileset.

3D Tiles tilesets often use Earth-centered, Earth-fixed coordinates, such
that the tileset content is in a small bounding volume 6-7 million meters
(the radius of the Earth) away from the coordinate system origin. This
property allows an alternative position, other then the tileset's true
origin, to be treated as the origin for the purpose of this Actor. Using
this property will preserve vertex precision (and thus avoid jittering)
much better than setting the Actor's Transform property.

<a id="unreal.CesiumGeoreference.origin_placement"></a>

#### origin\_placement

```python
@origin_placement.setter
def origin_placement(value: OriginPlacement) -> None
```

<a id="unreal.CesiumGeoreference.origin_latitude"></a>

#### origin\_latitude

```python
@property
def origin_latitude() -> float
```

(double):  [Read-Write] The latitude of the custom origin placement in degrees, in the range [-90,
90]

<a id="unreal.CesiumGeoreference.origin_latitude"></a>

#### origin\_latitude

```python
@origin_latitude.setter
def origin_latitude(value: float) -> None
```

<a id="unreal.CesiumGeoreference.origin_longitude"></a>

#### origin\_longitude

```python
@property
def origin_longitude() -> float
```

(double):  [Read-Write] The longitude of the custom origin placement in degrees, in the range
[-180, 180]

<a id="unreal.CesiumGeoreference.origin_longitude"></a>

#### origin\_longitude

```python
@origin_longitude.setter
def origin_longitude(value: float) -> None
```

<a id="unreal.CesiumGeoreference.origin_height"></a>

#### origin\_height

```python
@property
def origin_height() -> float
```

(double):  [Read-Write] The height of the custom origin placement in meters above the
ellipsoid.

<a id="unreal.CesiumGeoreference.origin_height"></a>

#### origin\_height

```python
@origin_height.setter
def origin_height(value: float) -> None
```

<a id="unreal.CesiumGeoreference.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(double):  [Read-Write] The percentage scale of the globe in the Unreal world. If this value is 50,
for example, one meter on the globe occupies half a meter in the Unreal
world.

<a id="unreal.CesiumGeoreference.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.CesiumGeoreference.sub_level_camera"></a>

#### sub\_level\_camera

```python
@property
def sub_level_camera() -> PlayerCameraManager
```

(PlayerCameraManager):  [Read-Write] The camera to use to determine which sub-level is closest, so that one can
be activated and all others deactivated.
deprecated: Add a CesiumOriginShiftComponent to the appropriate Actor instead.
deprecated: Add a CesiumOriginShiftComponent to the appropriate Actor instead.

<a id="unreal.CesiumGeoreference.sub_level_camera"></a>

#### sub\_level\_camera

```python
@sub_level_camera.setter
def sub_level_camera(value: PlayerCameraManager) -> None
```

<a id="unreal.CesiumGeoreference.world_origin_camera"></a>

#### world\_origin\_camera

```python
@property
def world_origin_camera() -> PlayerCameraManager
```

deprecated: 'world_origin_camera' was renamed to 'sub_level_camera'.

<a id="unreal.CesiumGeoreference.world_origin_camera"></a>

#### world\_origin\_camera

```python
@world_origin_camera.setter
def world_origin_camera(value: PlayerCameraManager) -> None
```

<a id="unreal.CesiumGeoreference.sub_level_switcher"></a>

#### sub\_level\_switcher

```python
@property
def sub_level_switcher() -> CesiumSubLevelSwitcherComponent
```

(CesiumSubLevelSwitcherComponent):  [Read-Only] The component that allows switching between the sub-levels registered with
this georeference.

<a id="unreal.CesiumGeoreference.show_load_radii"></a>

#### show\_load\_radii

```python
@property
def show_load_radii() -> bool
```

(bool):  [Read-Write] Whether to visualize the level loading radii in the editor. Helpful for
initially positioning the level and choosing a load radius.

<a id="unreal.CesiumGeoreference.show_load_radii"></a>

#### show\_load\_radii

```python
@show_load_radii.setter
def show_load_radii(value: bool) -> None
```

<a id="unreal.CesiumGeoreference.cesium_sub_levels"></a>

#### cesium\_sub\_levels

```python
@property
def cesium_sub_levels() -> Array[CesiumSubLevel]
```

(Array[CesiumSubLevel]):  [Read-Write]
deprecated: Create sub-levels by adding a UCesiumSubLevelComponent to an ALevelInstance Actor.

<a id="unreal.CesiumGeoreference.cesium_sub_levels"></a>

#### cesium\_sub\_levels

```python
@cesium_sub_levels.setter
def cesium_sub_levels(value: Array[CesiumSubLevel]) -> None
```

<a id="unreal.CesiumGeoreference.transform_unreal_rotator_to_east_south_up"></a>

#### transform\_unreal\_rotator\_to\_east\_south\_up

```python
def transform_unreal_rotator_to_east_south_up(
        unreal_rotator: Rotator, unreal_location: Vector) -> Rotator
```

x.transform_unreal_rotator_to_east_south_up(unreal_rotator, unreal_location) -> Rotator
Given a Rotator that transforms an object into the Unreal coordinate
system, returns a new Rotator that transforms that object into an
East-South-Up frame centered at a given location.

In an East-South-Up frame, +X points East, +Y points South, and +Z points
Up. However, the directions of "East", "South", and "Up" in Unreal or ECEF
coordinates vary depending on where on the globe we are talking about.
That is why this function takes a location, expressed in Unreal
coordinates, that defines the origin of the East-South-Up frame of
interest.

The Unreal location and the resulting Rotator should generally not be
relative to the Unreal _world_, but rather be expressed in some parent
Actor's reference frame as defined by its Transform. This way, the chain of
Unreal transforms places and orients the "globe" in the Unreal world.

Args:
    unreal_rotator (Rotator): 
    unreal_location (Vector): 

Returns:
    Rotator:

<a id="unreal.CesiumGeoreference.transform_rotator_unreal_to_east_south_up"></a>

#### transform\_rotator\_unreal\_to\_east\_south\_up

```python
def transform_rotator_unreal_to_east_south_up(
        unreal_rotator: Rotator, unreal_location: Vector) -> Rotator
```

deprecated: 'transform_rotator_unreal_to_east_south_up' was renamed to 'transform_unreal_rotator_to_east_south_up'.

<a id="unreal.CesiumGeoreference.transform_unreal_position_to_longitude_latitude_height"></a>

#### transform\_unreal\_position\_to\_longitude\_latitude\_height

```python
def transform_unreal_position_to_longitude_latitude_height(
        unreal_position: Vector) -> Vector
```

x.transform_unreal_position_to_longitude_latitude_height(unreal_position) -> Vector
Transforms a position in Unreal coordinates into longitude in degrees (x),
latitude in degrees (y), and height above the ellipsoid in meters (z). The
position should generally not be an Unreal _world_ position, but rather a
position expressed in some parent Actor's reference frame as defined by its
transform. This way, the chain of Unreal transforms places and orients the
"globe" in the Unreal world.

Args:
    unreal_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_unreal_to_longitude_latitude_height"></a>

#### inaccurate\_transform\_unreal\_to\_longitude\_latitude\_height

```python
def inaccurate_transform_unreal_to_longitude_latitude_height(
        unreal_position: Vector) -> Vector
```

deprecated: 'inaccurate_transform_unreal_to_longitude_latitude_height' was renamed to 'transform_unreal_position_to_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.transform_unreal_to_longitude_latitude_height"></a>

#### transform\_unreal\_to\_longitude\_latitude\_height

```python
def transform_unreal_to_longitude_latitude_height(
        unreal_position: Vector) -> Vector
```

deprecated: 'transform_unreal_to_longitude_latitude_height' was renamed to 'transform_unreal_position_to_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.transform_unreal_position_to_earth_centered_earth_fixed"></a>

#### transform\_unreal\_position\_to\_earth\_centered\_earth\_fixed

```python
def transform_unreal_position_to_earth_centered_earth_fixed(
        unreal_position: Vector) -> Vector
```

x.transform_unreal_position_to_earth_centered_earth_fixed(unreal_position) -> Vector
Transforms the given position from Unreal coordinates to Earth-Centered,
Earth-Fixed (ECEF). The position should generally not be an Unreal _world_
position, but rather a position expressed in some parent Actor's reference
frame as defined by its transform. This way, the chain of Unreal transforms
places and orients the "globe" in the Unreal world.

Args:
    unreal_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_unreal_to_ecef"></a>

#### inaccurate\_transform\_unreal\_to\_ecef

```python
def inaccurate_transform_unreal_to_ecef(unreal_position: Vector) -> Vector
```

deprecated: 'inaccurate_transform_unreal_to_ecef' was renamed to 'transform_unreal_position_to_earth_centered_earth_fixed'.

<a id="unreal.CesiumGeoreference.transform_unreal_to_ecef"></a>

#### transform\_unreal\_to\_ecef

```python
def transform_unreal_to_ecef(unreal_position: Vector) -> Vector
```

deprecated: 'transform_unreal_to_ecef' was renamed to 'transform_unreal_position_to_earth_centered_earth_fixed'.

<a id="unreal.CesiumGeoreference.transform_unreal_direction_to_earth_centered_earth_fixed"></a>

#### transform\_unreal\_direction\_to\_earth\_centered\_earth\_fixed

```python
def transform_unreal_direction_to_earth_centered_earth_fixed(
        unreal_direction: Vector) -> Vector
```

x.transform_unreal_direction_to_earth_centered_earth_fixed(unreal_direction) -> Vector
Transforms the given direction vector from Unreal coordinates to
Earth-Centered, Earth-Fixed (ECEF) coordinates. The direction vector should
generally not be an Unreal _world_ vector, but rather a vector expressed in
some parent Actor's reference frame as defined by its transform. This way,
the chain of Unreal transforms places and orients the "globe" in the Unreal
world.

Args:
    unreal_direction (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.transform_longitude_latitude_height_to_ecef"></a>

#### transform\_longitude\_latitude\_height\_to\_ecef

```python
def transform_longitude_latitude_height_to_ecef(
        longitude_latitude_height: Vector) -> Vector
```

x.transform_longitude_latitude_height_to_ecef(longitude_latitude_height) -> Vector
Transforms the given longitude in degrees (x), latitude in
degrees (y), and height above the ellipsoid in meters (z) into
Earth-Centered, Earth-Fixed (ECEF) coordinates.
deprecated: Use LongitudeLatitudeHeightToEllipsoidCenteredEllipsoidFixed on UCesiumEllipsoid instead.

Args:
    longitude_latitude_height (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_longitude_latitude_height_to_ecef"></a>

#### inaccurate\_transform\_longitude\_latitude\_height\_to\_ecef

```python
def inaccurate_transform_longitude_latitude_height_to_ecef(
        longitude_latitude_height: Vector) -> Vector
```

deprecated: 'inaccurate_transform_longitude_latitude_height_to_ecef' was renamed to 'transform_longitude_latitude_height_to_ecef'.

<a id="unreal.CesiumGeoreference.transform_longitude_latitude_height_position_to_unreal"></a>

#### transform\_longitude\_latitude\_height\_position\_to\_unreal

```python
def transform_longitude_latitude_height_position_to_unreal(
        longitude_latitude_height: Vector) -> Vector
```

x.transform_longitude_latitude_height_position_to_unreal(longitude_latitude_height) -> Vector
Transforms the given longitude in degrees (x), latitude in
degrees (y), and height above the ellipsoid in meters (z) into Unreal
coordinates. The resulting position should generally not be interpreted as
an Unreal _world_ position, but rather a position expressed in some parent
Actor's reference frame as defined by its transform. This way, the chain of
Unreal transforms places and orients the "globe" in the Unreal world.

Args:
    longitude_latitude_height (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_longitude_latitude_height_to_unreal"></a>

#### inaccurate\_transform\_longitude\_latitude\_height\_to\_unreal

```python
def inaccurate_transform_longitude_latitude_height_to_unreal(
        longitude_latitude_height: Vector) -> Vector
```

deprecated: 'inaccurate_transform_longitude_latitude_height_to_unreal' was renamed to 'transform_longitude_latitude_height_position_to_unreal'.

<a id="unreal.CesiumGeoreference.transform_longitude_latitude_height_to_unreal"></a>

#### transform\_longitude\_latitude\_height\_to\_unreal

```python
def transform_longitude_latitude_height_to_unreal(
        longitude_latitude_height: Vector) -> Vector
```

deprecated: 'transform_longitude_latitude_height_to_unreal' was renamed to 'transform_longitude_latitude_height_position_to_unreal'.

<a id="unreal.CesiumGeoreference.transform_ecef_to_longitude_latitude_height"></a>

#### transform\_ecef\_to\_longitude\_latitude\_height

```python
def transform_ecef_to_longitude_latitude_height(ecef: Vector) -> Vector
```

x.transform_ecef_to_longitude_latitude_height(ecef) -> Vector
Transforms the given Earth-Centered, Earth-Fixed (ECEF) coordinates into
Ellipsoid longitude in degrees (x), latitude in degrees (y), and height
above the ellipsoid in meters (z).
deprecated: Use EllipsoidCenteredEllipsoidFixedToLongitudeLatitudeHeight on UCesiumEllipsoid instead.

Args:
    ecef (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_ecef_to_longitude_latitude_height"></a>

#### inaccurate\_transform\_ecef\_to\_longitude\_latitude\_height

```python
def inaccurate_transform_ecef_to_longitude_latitude_height(
        ecef: Vector) -> Vector
```

deprecated: 'inaccurate_transform_ecef_to_longitude_latitude_height' was renamed to 'transform_ecef_to_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.transform_east_south_up_rotator_to_unreal"></a>

#### transform\_east\_south\_up\_rotator\_to\_unreal

```python
def transform_east_south_up_rotator_to_unreal(
        east_south_up_rotator: Rotator, unreal_location: Vector) -> Rotator
```

x.transform_east_south_up_rotator_to_unreal(east_south_up_rotator, unreal_location) -> Rotator
Given a Rotator that transforms an object into the East-South-Up frame
centered at a given location, returns a new Rotator that transforms that
object into Unreal coordinates.

In an East-South-Up frame, +X points East, +Y points South, and +Z points
Up. However, the directions of "East", "South", and "Up" in Unreal or ECEF
coordinates vary depending on where on the globe we are talking about.
That is why this function takes a location, expressed in Unreal
coordinates, that defines the origin of the East-South-Up frame of
interest.

The Unreal location and the resulting Rotator should generally not be
relative to the Unreal _world_, but rather be expressed in some parent
Actor's reference frame as defined by its Transform. This way, the chain of
Unreal transforms places and orients the "globe" in the Unreal world.

Args:
    east_south_up_rotator (Rotator): 
    unreal_location (Vector): 

Returns:
    Rotator:

<a id="unreal.CesiumGeoreference.transform_rotator_east_south_up_to_unreal"></a>

#### transform\_rotator\_east\_south\_up\_to\_unreal

```python
def transform_rotator_east_south_up_to_unreal(
        east_south_up_rotator: Rotator, unreal_location: Vector) -> Rotator
```

deprecated: 'transform_rotator_east_south_up_to_unreal' was renamed to 'transform_east_south_up_rotator_to_unreal'.

<a id="unreal.CesiumGeoreference.transform_earth_centered_earth_fixed_position_to_unreal"></a>

#### transform\_earth\_centered\_earth\_fixed\_position\_to\_unreal

```python
def transform_earth_centered_earth_fixed_position_to_unreal(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

x.transform_earth_centered_earth_fixed_position_to_unreal(earth_centered_earth_fixed_position) -> Vector
Transforms a position in Earth-Centered, Earth-Fixed (ECEF) coordinates
into Unreal coordinates. The resulting position should generally not be
interpreted as an Unreal _world_ position, but rather a position expressed
in some parent Actor's reference frame as defined by its transform. This
way, the chain of Unreal transforms places and orients the "globe" in the
Unreal world.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_transform_ecef_to_unreal"></a>

#### inaccurate\_transform\_ecef\_to\_unreal

```python
def inaccurate_transform_ecef_to_unreal(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

deprecated: 'inaccurate_transform_ecef_to_unreal' was renamed to 'transform_earth_centered_earth_fixed_position_to_unreal'.

<a id="unreal.CesiumGeoreference.transform_ecef_to_unreal"></a>

#### transform\_ecef\_to\_unreal

```python
def transform_ecef_to_unreal(
        earth_centered_earth_fixed_position: Vector) -> Vector
```

deprecated: 'transform_ecef_to_unreal' was renamed to 'transform_earth_centered_earth_fixed_position_to_unreal'.

<a id="unreal.CesiumGeoreference.transform_earth_centered_earth_fixed_direction_to_unreal"></a>

#### transform\_earth\_centered\_earth\_fixed\_direction\_to\_unreal

```python
def transform_earth_centered_earth_fixed_direction_to_unreal(
        earth_centered_earth_fixed_direction: Vector) -> Vector
```

x.transform_earth_centered_earth_fixed_direction_to_unreal(earth_centered_earth_fixed_direction) -> Vector
Transforms a direction vector in Earth-Centered, Earth-Fixed (ECEF)
coordinates into Unreal coordinates. The resulting direction vector should
generally not be interpreted as an Unreal _world_ vector, but rather a
vector expressed in some parent Actor's reference frame as defined by its
transform. This way, the chain of Unreal transforms places and orients the
"globe" in the Unreal world.

Args:
    earth_centered_earth_fixed_direction (Vector): 

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.set_origin_longitude_latitude_height"></a>

#### set\_origin\_longitude\_latitude\_height

```python
def set_origin_longitude_latitude_height(
        target_longitude_latitude_height: Vector) -> None
```

x.set_origin_longitude_latitude_height(target_longitude_latitude_height) -> None
This aligns the specified longitude in degrees (X), latitude in
degrees (Y), and height above the ellipsoid in meters (Z) to the Unreal
origin. That is, it moves the globe so that these coordinates exactly fall
on the origin. Only valid if the placement type is Cartographic Origin
(i.e. Longitude / Latitude / Height).

Args:
    target_longitude_latitude_height (Vector):

<a id="unreal.CesiumGeoreference.inaccurate_set_georeference_origin"></a>

#### inaccurate\_set\_georeference\_origin

```python
def inaccurate_set_georeference_origin(
        target_longitude_latitude_height: Vector) -> None
```

deprecated: 'inaccurate_set_georeference_origin' was renamed to 'set_origin_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.inaccurate_set_georeference_origin_longitude_latitude_height"></a>

#### inaccurate\_set\_georeference\_origin\_longitude\_latitude\_height

```python
def inaccurate_set_georeference_origin_longitude_latitude_height(
        target_longitude_latitude_height: Vector) -> None
```

deprecated: 'inaccurate_set_georeference_origin_longitude_latitude_height' was renamed to 'set_origin_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.set_georeference_origin_longitude_latitude_height"></a>

#### set\_georeference\_origin\_longitude\_latitude\_height

```python
def set_georeference_origin_longitude_latitude_height(
        target_longitude_latitude_height: Vector) -> None
```

deprecated: 'set_georeference_origin_longitude_latitude_height' was renamed to 'set_origin_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.set_origin_earth_centered_earth_fixed"></a>

#### set\_origin\_earth\_centered\_earth\_fixed

```python
def set_origin_earth_centered_earth_fixed(
        target_earth_centered_earth_fixed: Vector) -> None
```

x.set_origin_earth_centered_earth_fixed(target_earth_centered_earth_fixed) -> None
This aligns the specified Earth-Centered, Earth-Fixed (ECEF) coordinates to
the Unreal origin. That is, it moves the globe so that these coordinates
exactly fall on the origin. Only valid if the placement type is
Cartographic Origin (i.e. Longitude / Latitude / Height). Note that if the
provided ECEF coordiantes are near the center of the Earth so that
Longitude, Latitude, and Height are undefined, this function will instead
place the origin at 0 degrees longitude, 0 degrees latitude, and 0 meters
height about the ellipsoid.

Args:
    target_earth_centered_earth_fixed (Vector):

<a id="unreal.CesiumGeoreference.inaccurate_set_georeference_origin_ecef"></a>

#### inaccurate\_set\_georeference\_origin\_ecef

```python
def inaccurate_set_georeference_origin_ecef(
        target_earth_centered_earth_fixed: Vector) -> None
```

deprecated: 'inaccurate_set_georeference_origin_ecef' was renamed to 'set_origin_earth_centered_earth_fixed'.

<a id="unreal.CesiumGeoreference.set_georeference_origin_ecef"></a>

#### set\_georeference\_origin\_ecef

```python
def set_georeference_origin_ecef(
        target_earth_centered_earth_fixed: Vector) -> None
```

deprecated: 'set_georeference_origin_ecef' was renamed to 'set_origin_earth_centered_earth_fixed'.

<a id="unreal.CesiumGeoreference.get_origin_longitude_latitude_height"></a>

#### get\_origin\_longitude\_latitude\_height

```python
def get_origin_longitude_latitude_height() -> Vector
```

x.get_origin_longitude_latitude_height() -> Vector
Returns the georeference origin position as an FVector where `X` is
longitude (degrees), `Y` is latitude (degrees), and `Z` is height above the
ellipsoid (meters). Only valid if the placement type is Cartographic Origin
(i.e. Longitude / Latitude / Height).

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.inaccurate_get_georeference_origin_longitude_latitude_height"></a>

#### inaccurate\_get\_georeference\_origin\_longitude\_latitude\_height

```python
def inaccurate_get_georeference_origin_longitude_latitude_height() -> Vector
```

deprecated: 'inaccurate_get_georeference_origin_longitude_latitude_height' was renamed to 'get_origin_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.get_georeference_origin_longitude_latitude_height"></a>

#### get\_georeference\_origin\_longitude\_latitude\_height

```python
def get_georeference_origin_longitude_latitude_height() -> Vector
```

deprecated: 'get_georeference_origin_longitude_latitude_height' was renamed to 'get_origin_longitude_latitude_height'.

<a id="unreal.CesiumGeoreference.get_origin_earth_centered_earth_fixed"></a>

#### get\_origin\_earth\_centered\_earth\_fixed

```python
def get_origin_earth_centered_earth_fixed() -> Vector
```

x.get_origin_earth_centered_earth_fixed() -> Vector
Returns the georeference origin position as an FVector in Earth-Centerd,
Earth-Fixed (ECEF) coordinates. Only valid if the placement type is
Cartographic Origin (i.e. Longitude / Latitude / Height).

Returns:
    Vector:

<a id="unreal.CesiumGeoreference.get_default_georeference_for_actor"></a>

#### get\_default\_georeference\_for\_actor

```python
@classmethod
def get_default_georeference_for_actor(cls,
                                       actor: Actor) -> CesiumGeoreference
```

X.get_default_georeference_for_actor(actor) -> CesiumGeoreference
Finds and returns the CesiumGeoreference suitable for use with the given
Actor. It searches in the following order:

1. A CesiumGeoreference that is an attachment parent of the given Actor.
2. A CesiumGeoreference that is tagged with "DEFAULT_GEOREFERENCE" and
found in the PersistentLevel.
3. A CesiumGeoreference with the name "CesiumGeoreferenceDefault" and found
in the PersistentLevel.
4. Any CesiumGeoreference in the PersistentLevel.

If no CesiumGeoreference is found with this search, a new one is created in
the persistent level and given the "DEFAULT_GEOREFERENCE" tag.

Args:
    actor (Actor): 

Returns:
    CesiumGeoreference:

<a id="unreal.CesiumGeoreference.get_default_georeference"></a>

#### get\_default\_georeference

```python
@classmethod
def get_default_georeference(
        cls, world_context_object: Object) -> CesiumGeoreference
```

X.get_default_georeference(world_context_object) -> CesiumGeoreference
Finds and returns a CesiumGeoreference in the world. It searches in the
following order:

1. A CesiumGeoreference that is tagged with "DEFAULT_GEOREFERENCE" and
found in the PersistentLevel.
2. A CesiumGeoreference with the name "CesiumGeoreferenceDefault" and found
in the PersistentLevel.
3. Any CesiumGeoreference in the PersistentLevel.

If no CesiumGeoreference is found with this search, a new one is created in
the persistent level and given the "DEFAULT_GEOREFERENCE" tag.

Args:
    world_context_object (Object): 

Returns:
    CesiumGeoreference:

<a id="unreal.CesiumGeoreference.compute_unreal_to_east_south_up_transformation"></a>

#### compute\_unreal\_to\_east\_south\_up\_transformation

```python
def compute_unreal_to_east_south_up_transformation(
        unreal_location: Vector) -> Matrix
```

x.compute_unreal_to_east_south_up_transformation(unreal_location) -> Matrix
Computes the matrix that transforms from the Unreal frame to an
East-South-Up frame centered at a given location. The location is expressed
in Unreal coordinates. To use an Earth-Centered, Earth-Fixed position
instead, use
ComputeEastSouthUpAtEarthCenteredEarthFixedPositionToUnrealTransformation.

In an East-South-Up frame, +X points East, +Y points South, and +Z points
Up. However, the directions of "East", "South", and "Up" in Unreal or ECEF
coordinates vary depending on where on the globe we are talking about.
That is why this function takes a location, expressed in Unreal
coordinates, that defines the origin of the East-South-Up frame of
interest.

The Unreal location and the resulting matrix should generally not be
relative to the Unreal _world_, but rather be expressed in some parent
Actor's reference frame as defined by its Transform. This way, the chain of
Unreal transforms places and orients the "globe" in the Unreal world.

Args:
    unreal_location (Vector): 

Returns:
    Matrix:

<a id="unreal.CesiumGeoreference.compute_unreal_to_earth_centered_earth_fixed_transformation"></a>

#### compute\_unreal\_to\_earth\_centered\_earth\_fixed\_transformation

```python
def compute_unreal_to_earth_centered_earth_fixed_transformation() -> Matrix
```

x.compute_unreal_to_earth_centered_earth_fixed_transformation() -> Matrix
Computes the transformation matrix from the Unreal coordinate system to the
Earth-Centered, Earth-Fixed (ECEF) coordinate system. The Unreal
coordinates should generally not be interpreted as Unreal _world_
coordinates, but rather a coordinate system based on some parent Actor's
reference frame as defined by its transform. This way, the chain of Unreal
transforms places and orients the "globe" in the Unreal world.

Returns:
    Matrix:

<a id="unreal.CesiumGeoreference.compute_east_south_up_to_unreal_transformation"></a>

#### compute\_east\_south\_up\_to\_unreal\_transformation

```python
def compute_east_south_up_to_unreal_transformation(
        unreal_location: Vector) -> Matrix
```

x.compute_east_south_up_to_unreal_transformation(unreal_location) -> Matrix
Computes the matrix that transforms from an East-South-Up frame centered at
a given location to the Unreal frame.

In an East-South-Up frame, +X points East, +Y points South, and +Z points
Up. However, the directions of "East", "South", and "Up" in Unreal or ECEF
coordinates vary depending on where on the globe we are talking about.
That is why this function takes a location, expressed in Unreal
coordinates, that defines the origin of the East-South-Up frame of
interest.

The Unreal location and the resulting matrix should generally not be
relative to the Unreal _world_, but rather be expressed in some parent
Actor's reference frame as defined by its Transform. This way, the chain of
Unreal transforms places and orients the "globe" in the Unreal world.

Args:
    unreal_location (Vector): 

Returns:
    Matrix:

<a id="unreal.CesiumGeoreference.compute_east_south_up_to_unreal"></a>

#### compute\_east\_south\_up\_to\_unreal

```python
def compute_east_south_up_to_unreal(unreal_location: Vector) -> Matrix
```

deprecated: 'compute_east_south_up_to_unreal' was renamed to 'compute_east_south_up_to_unreal_transformation'.

<a id="unreal.CesiumGeoreference.compute_east_south_up_at_earth_centered_earth_fixed_position_to_unreal_transformation"></a>

#### compute\_east\_south\_up\_at\_earth\_centered\_earth\_fixed\_position\_to\_unreal\_transformation

```python
def compute_east_south_up_at_earth_centered_earth_fixed_position_to_unreal_transformation(
        earth_centered_earth_fixed_position: Vector) -> Matrix
```

x.compute_east_south_up_at_earth_centered_earth_fixed_position_to_unreal_transformation(earth_centered_earth_fixed_position) -> Matrix
Computes the matrix that transforms from an East-South-Up frame centered at
a given location to the Unreal frame. The location is expressed as an
Earth-Centered, Earth-Fixed (ECEF) position. To use an Unreal position
instead, use ComputeUnrealToEastSouthUpTransformation.

In an East-South-Up frame, +X points East, +Y points South, and +Z points
Up. However, the directions of "East", "South", and "Up" in Unreal or ECEF
coordinates vary depending on where on the globe we are talking about.
That is why this function takes a location, expressed in ECEF
coordinates, that defines the origin of the East-South-Up frame of
interest.

The resulting matrix should generally not be relative to the Unreal
_world_, but rather be expressed in some parent Actor's reference frame as
defined by its Transform. This way, the chain of Unreal transforms places
and orients the "globe" in the Unreal world.

Args:
    earth_centered_earth_fixed_position (Vector): 

Returns:
    Matrix:

<a id="unreal.CesiumGeoreference.compute_east_north_up_to_ecef"></a>

#### compute\_east\_north\_up\_to\_ecef

```python
def compute_east_north_up_to_ecef(ecef: Vector) -> Matrix
```

x.compute_east_north_up_to_ecef(ecef) -> Matrix
Computes the rotation matrix from the local East-North-Up to
Earth-Centered, Earth-Fixed (ECEF) at the specified ECEF location.
deprecated: Use EastNorthUpToEllipsoidCenteredEllipsoidFixed on UCesiumEllipsoid instead.

Args:
    ecef (Vector): 

Returns:
    Matrix:

<a id="unreal.CesiumGeoreference.inaccurate_compute_east_north_up_to_ecef"></a>

#### inaccurate\_compute\_east\_north\_up\_to\_ecef

```python
def inaccurate_compute_east_north_up_to_ecef(ecef: Vector) -> Matrix
```

deprecated: 'inaccurate_compute_east_north_up_to_ecef' was renamed to 'compute_east_north_up_to_ecef'.

<a id="unreal.CesiumGeoreference.compute_earth_centered_earth_fixed_to_unreal_transformation"></a>

#### compute\_earth\_centered\_earth\_fixed\_to\_unreal\_transformation

```python
def compute_earth_centered_earth_fixed_to_unreal_transformation() -> Matrix
```

x.compute_earth_centered_earth_fixed_to_unreal_transformation() -> Matrix
Computes the transformation matrix from the Earth-Centered, Earth-Fixed
(ECEF) coordinate system to the Unreal coordinate system. The Unreal
coordinates should generally not be interpreted as Unreal _world_
coordinates, but rather a coordinate system based on some parent Actor's
reference frame as defined by its transform. This way, the chain of Unreal
transforms places and orients the "globe" in the Unreal world.

Returns:
    Matrix:

<a id="unreal.CesiumGlobeAnchorComponent"></a>