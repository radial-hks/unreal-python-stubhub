## PathEntity Objects

```python
class PathEntity(WdpActorEntity)
```

FString PathEid

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: PathEntity.h

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
- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]
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
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``procedural_mesh_component`` (ProceduralMeshComponent):  [Read-Write]
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
- ``spline_component`` (SplineComponent):  [Read-Write] UPROPERTY(BlueprintReadWrite, Category = CoveringApi)
                 bool bBoxType;
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

<a id="unreal.PathEntity.spline_component"></a>

#### spline\_component

```python
@property
def spline_component() -> SplineComponent
```

(SplineComponent):  [Read-Write] UPROPERTY(BlueprintReadWrite, Category = CoveringApi)
               bool bBoxType;

<a id="unreal.PathEntity.spline_component"></a>

#### spline\_component

```python
@spline_component.setter
def spline_component(value: SplineComponent) -> None
```

<a id="unreal.PathEntity.procedural_mesh_component"></a>

#### procedural\_mesh\_component

```python
@property
def procedural_mesh_component() -> ProceduralMeshComponent
```

(ProceduralMeshComponent):  [Read-Write]

<a id="unreal.PathEntity.procedural_mesh_component"></a>

#### procedural\_mesh\_component

```python
@procedural_mesh_component.setter
def procedural_mesh_component(value: ProceduralMeshComponent) -> None
```

<a id="unreal.PathEntity.update_procedural_mesh_width"></a>

#### update\_procedural\_mesh\_width

```python
def update_procedural_mesh_width(center_points: Array[Vector],
                                 width: float) -> Array[Vector]
```

x.update_procedural_mesh_width(center_points, width) -> Array[Vector]
Update Procedural Mesh Width

Args:
    center_points (Array[Vector]): 
    width (float): 

Returns:
    Array[Vector]: 

    vertexes (Array[Vector]):

<a id="unreal.PathEntity.set_width"></a>

#### set\_width

```python
def set_width(width: float) -> bool
```

x.set_width(width) -> bool
Set Width

Args:
    width (float): 

Returns:
    bool:

<a id="unreal.PathEntity.set_type"></a>

#### set\_type

```python
def set_type(type: str) -> bool
```

x.set_type(type) -> bool
Set Type

Args:
    type (str): 

Returns:
    bool:

<a id="unreal.PathEntity.set_speedup_factor"></a>

#### set\_speedup\_factor

```python
def set_speedup_factor(speedup_factor: float) -> bool
```

x.set_speedup_factor(speedup_factor) -> bool
Set Speedup Factor

Args:
    speedup_factor (float): 

Returns:
    bool:

<a id="unreal.PathEntity.set_polyline"></a>

#### set\_polyline

```python
def set_polyline(polyline: Array[Vector]) -> bool
```

x.set_polyline(polyline) -> bool
Set Polyline

Args:
    polyline (Array[Vector]): 

Returns:
    bool:

<a id="unreal.PathEntity.set_pass_color"></a>

#### set\_pass\_color

```python
def set_pass_color(color: str) -> bool
```

x.set_pass_color(color) -> bool
Set Pass Color

Args:
    color (str): 

Returns:
    bool:

<a id="unreal.PathEntity.set_opacity"></a>

#### set\_opacity

```python
def set_opacity(opacity: float) -> bool
```

x.set_opacity(opacity) -> bool
Set Opacity

Args:
    opacity (float): 

Returns:
    bool:

<a id="unreal.PathEntity.set_movement_percent"></a>

#### set\_movement\_percent

```python
def set_movement_percent(percent: float) -> None
```

x.set_movement_percent(percent) -> None
Set Movement Percent

Args:
    percent (float):

<a id="unreal.PathEntity.set_color"></a>

#### set\_color

```python
def set_color(color: str) -> bool
```

x.set_color(color) -> bool
Set Color

Args:
    color (str): 

Returns:
    bool:

<a id="unreal.PathEntity.notify_path_modify"></a>

#### notify\_path\_modify

```python
def notify_path_modify() -> None
```

x.notify_path_modify() -> None
Notify Path Modify

<a id="unreal.PathEntity.notify_movement_start"></a>

#### notify\_movement\_start

```python
def notify_movement_start(reverse: bool) -> None
```

x.notify_movement_start(reverse) -> None
Notify Movement Start

Args:
    reverse (bool):

<a id="unreal.PathEntity.modify_param_func"></a>

#### modify\_param\_func

```python
def modify_param_func(coordinates: Array[Vector], method: str,
                      index: Array[int]) -> bool
```

x.modify_param_func(coordinates, method, index) -> bool
Modify Param Func

Args:
    coordinates (Array[Vector]): 
    method (str): 
    index (Array[int32]): 

Returns:
    bool:

<a id="unreal.PathEntity.get_path_raw_points"></a>

#### get\_path\_raw\_points

```python
def get_path_raw_points() -> Optional[Array[Vector]]
```

x.get_path_raw_points() -> Array[Vector] or None
Get Path Raw Points

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.PathEntity.get_path_draw_points_map"></a>

#### get\_path\_draw\_points\_map

```python
def get_path_draw_points_map() -> Optional[Map[int, int]]
```

x.get_path_draw_points_map() -> Map[int32, int32] or None
Get Path Draw Points Map

Returns:
    Map[int32, int32] or None: 

    out_map_points (Map[int32, int32]):

<a id="unreal.PathEntity.get_path_draw_points"></a>

#### get\_path\_draw\_points

```python
def get_path_draw_points() -> Optional[Array[Vector]]
```

x.get_path_draw_points() -> Array[Vector] or None
Get Path Draw Points

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.PathEntity.get_owner_world"></a>

#### get\_owner\_world

```python
def get_owner_world() -> Actor
```

x.get_owner_world() -> Actor
Get Owner World

Returns:
    Actor:

<a id="unreal.PathEntity.create_path"></a>

#### create\_path

```python
def create_path(points: Array[Vector], path_type: str, width: float,
                speedup_factor: float, opacity: float, color: str,
                pass_color: str) -> bool
```

x.create_path(points, path_type, width, speedup_factor, opacity, color, pass_color) -> bool
Create Path

Args:
    points (Array[Vector]): 
    path_type (str): 
    width (float): 
    speedup_factor (float): 
    opacity (float): 
    color (str): 
    pass_color (str): 

Returns:
    bool:

<a id="unreal.PathEntity.calculate_interpolation_points"></a>

#### calculate\_interpolation\_points

```python
def calculate_interpolation_points(vector_array: Array[Vector], start: Vector,
                                   mid: Vector, end: Vector, angle: float,
                                   level: int) -> Tuple[int, Array[Vector]]
```

x.calculate_interpolation_points(vector_array, start, mid, end, angle, level) -> (int32, vector_array=Array[Vector])
Calculate Interpolation Points

Args:
    vector_array (Array[Vector]): 
    start (Vector): 
    mid (Vector): 
    end (Vector): 
    angle (float): 
    level (int32): 

Returns:
    Array[Vector]: 

    vector_array (Array[Vector]):

<a id="unreal.PathEntity.caculate_procedural_mesh_data"></a>

#### caculate\_procedural\_mesh\_data

```python
def caculate_procedural_mesh_data(
    original_points: Array[Vector], corner_radius: float, width: float,
    bezier_sample_level: int
) -> Tuple[Array[Vector], Array[int], Array[Vector2D], Array[Vector], Map[
        int, int]]
```

x.caculate_procedural_mesh_data(original_points, corner_radius, width, bezier_sample_level) -> (vertexes=Array[Vector], indexes=Array[int32], u_vs=Array[Vector2D], center_points=Array[Vector], out_map_points=Map[int32, int32])
Caculate Procedural Mesh Data

Args:
    original_points (Array[Vector]): 
    corner_radius (float): 
    width (float): 
    bezier_sample_level (int32): 

Returns:
    tuple: 

    vertexes (Array[Vector]): 

    indexes (Array[int32]): 

    u_vs (Array[Vector2D]): 

    center_points (Array[Vector]): 

    out_map_points (Map[int32, int32]):

<a id="unreal.PathEntity.add_static_mesh_component"></a>

#### add\_static\_mesh\_component

```python
def add_static_mesh_component(class_: Class,
                              relative_transform: Transform,
                              name: Name = "None") -> StaticMeshComponent
```

x.add_static_mesh_component(class_, relative_transform, name="None") -> StaticMeshComponent
Add Static Mesh Component

Args:
    class_ (type(Class)): 
    relative_transform (Transform): 
    name (Name): 

Returns:
    StaticMeshComponent:

<a id="unreal.PathEntity.add_spline_mesh_component"></a>

#### add\_spline\_mesh\_component

```python
def add_spline_mesh_component(class_: Class,
                              relative_transform: Transform,
                              name: Name = "None") -> SplineMeshComponent
```

x.add_spline_mesh_component(class_, relative_transform, name="None") -> SplineMeshComponent
Add Spline Mesh Component

Args:
    class_ (type(Class)): 
    relative_transform (Transform): 
    name (Name): 

Returns:
    SplineMeshComponent:

<a id="unreal.PathEntity.add_points_to_spline"></a>

#### add\_points\_to\_spline

```python
def add_points_to_spline(spline: SplineComponent, vector_array: Array[Vector],
                         first_index: int) -> None
```

x.add_points_to_spline(spline, vector_array, first_index) -> None
Add Points to Spline

Args:
    spline (SplineComponent): 
    vector_array (Array[Vector]): 
    first_index (int32):

<a id="unreal.PathEntity.add_decal_component"></a>

#### add\_decal\_component

```python
def add_decal_component(class_: Class,
                        relative_transform: Transform,
                        name: Name = "None") -> DecalComponent
```

x.add_decal_component(class_, relative_transform, name="None") -> DecalComponent
Add Decal Component

Args:
    class_ (type(Class)): 
    relative_transform (Transform): 
    name (Name): 

Returns:
    DecalComponent:

<a id="unreal.PoiEntity"></a>