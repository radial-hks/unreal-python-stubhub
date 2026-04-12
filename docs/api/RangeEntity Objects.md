## RangeEntity Objects

```python
class RangeEntity(WdpActorEntity)
```

Range Entity

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RangeEntity.h

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

<a id="unreal.RangeEntity.store_bottom_triangles_location_to_texture"></a>

#### store\_bottom\_triangles\_location\_to\_texture

```python
def store_bottom_triangles_location_to_texture(
        bottom_triangles: Array[int], bottom_vertexes: Array[Vector],
        min_x: float, max_x: float, min_y: float, max_y: float,
        use32_texture: bool) -> Texture2D
```

x.store_bottom_triangles_location_to_texture(bottom_triangles, bottom_vertexes, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Bottom Triangles Location to Texture

Args:
    bottom_triangles (Array[int32]): 
    bottom_vertexes (Array[Vector]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double): 
    use32_texture (bool): 

Returns:
    Texture2D:

<a id="unreal.RangeEntity.store_bottom_triangles_location"></a>

#### store\_bottom\_triangles\_location

```python
def store_bottom_triangles_location(canvas: Canvas,
                                    bottom_triangles: Array[int],
                                    bottom_vertexes: Array[Vector],
                                    min_x: float, max_x: float, min_y: float,
                                    max_y: float) -> None
```

x.store_bottom_triangles_location(canvas, bottom_triangles, bottom_vertexes, min_x, max_x, min_y, max_y) -> None
Store Bottom Triangles Location

Args:
    canvas (Canvas): 
    bottom_triangles (Array[int32]): 
    bottom_vertexes (Array[Vector]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double):

<a id="unreal.RangeEntity.store_array_points_location_to_texture"></a>

#### store\_array\_points\_location\_to\_texture

```python
def store_array_points_location_to_texture(points_array: Array[Vector],
                                           min_x: float, max_x: float,
                                           min_y: float, max_y: float,
                                           use32_texture: bool) -> Texture2D
```

x.store_array_points_location_to_texture(points_array, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Array Points Location to Texture

Args:
    points_array (Array[Vector]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double): 
    use32_texture (bool): 

Returns:
    Texture2D:

<a id="unreal.RangeEntity.store_array_points_location"></a>

#### store\_array\_points\_location

```python
def store_array_points_location(points_array: Array[Vector], canvas: Canvas,
                                min_x: float, max_x: float, min_y: float,
                                max_y: float) -> None
```

x.store_array_points_location(points_array, canvas, min_x, max_x, min_y, max_y) -> None
Store Array Points Location

Args:
    points_array (Array[Vector]): 
    canvas (Canvas): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double):

<a id="unreal.RangeEntity.set_type"></a>

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

<a id="unreal.RangeEntity.set_stroke_weight"></a>

#### set\_stroke\_weight

```python
def set_stroke_weight(stroke_weight: float) -> bool
```

x.set_stroke_weight(stroke_weight) -> bool
Set Stroke Weight

Args:
    stroke_weight (float): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_polygon_for_procedural_mesh"></a>

#### set\_polygon\_for\_procedural\_mesh

```python
def set_polygon_for_procedural_mesh(out_ring_points: Array[Vector],
                                    inner_loop_array: Array[Str_VectorArray],
                                    bottom_vertexes: Array[Vector2D],
                                    bottom_trianges: Array[int]) -> bool
```

x.set_polygon_for_procedural_mesh(out_ring_points, inner_loop_array, bottom_vertexes, bottom_trianges) -> bool
Set Polygon for Procedural Mesh

Args:
    out_ring_points (Array[Vector]): 
    inner_loop_array (Array[Str_VectorArray]): 
    bottom_vertexes (Array[Vector2D]): 
    bottom_trianges (Array[int32]): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_polygon"></a>

#### set\_polygon

```python
def set_polygon(polygon: Array[Vector], ignore_index: Array[int]) -> bool
```

x.set_polygon(polygon, ignore_index) -> bool
Set Polygon

Args:
    polygon (Array[Vector]): 
    ignore_index (Array[int32]): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_height"></a>

#### set\_height

```python
def set_height(height: float) -> bool
```

x.set_height(height) -> bool
Set Height

Args:
    height (float): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_fill_area_type"></a>

#### set\_fill\_area\_type

```python
def set_fill_area_type(fill_area_type: str) -> bool
```

x.set_fill_area_type(fill_area_type) -> bool
Set Fill Area Type

Args:
    fill_area_type (str): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_fill_area_color"></a>

#### set\_fill\_area\_color

```python
def set_fill_area_color(fill_area_color: str) -> bool
```

x.set_fill_area_color(fill_area_color) -> bool
Set Fill Area Color

Args:
    fill_area_color (str): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_coord_z"></a>

#### set\_coord\_z

```python
def set_coord_z(new_coord_z: float) -> bool
```

x.set_coord_z(new_coord_z) -> bool
Set Coord Z

Args:
    new_coord_z (double): 

Returns:
    bool:

<a id="unreal.RangeEntity.set_color"></a>

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

<a id="unreal.RangeEntity.horizontal_location"></a>

#### horizontal\_location

```python
def horizontal_location(
    out_ring_points: Array[Vector]
) -> Tuple[float, float, float, float, float, float]
```

x.horizontal_location(out_ring_points) -> (double, min_x=double, max_x=double, min_y=double, max_y=double, min_z=double)
Horizontal Location

Args:
    out_ring_points (Array[Vector]): 

Returns:
    tuple: 

    min_x (double): 

    max_x (double): 

    min_y (double): 

    max_y (double): 

    min_z (double):

<a id="unreal.RangeEntity.get_owner_world"></a>

#### get\_owner\_world

```python
def get_owner_world() -> Actor
```

x.get_owner_world() -> Actor
Get Owner World

Returns:
    Actor:

<a id="unreal.RangeEntity.create_range_for_procedural_mesh"></a>

#### create\_range\_for\_procedural\_mesh

```python
def create_range_for_procedural_mesh(out_ring_points: Array[Vector],
                                     inner_loop_array: Array[Str_VectorArray],
                                     bottom_vertexes: Array[Vector2D],
                                     bottom_trianges: Array[int],
                                     range_type: str, bottom_type: str,
                                     range_hight: float,
                                     range_bottom_width: float,
                                     range_color: str,
                                     fill_area_color: str) -> bool
```

x.create_range_for_procedural_mesh(out_ring_points, inner_loop_array, bottom_vertexes, bottom_trianges, range_type, bottom_type, range_hight, range_bottom_width, range_color, fill_area_color) -> bool
Create Range for Procedural Mesh

Args:
    out_ring_points (Array[Vector]): 
    inner_loop_array (Array[Str_VectorArray]): 
    bottom_vertexes (Array[Vector2D]): 
    bottom_trianges (Array[int32]): 
    range_type (str): 
    bottom_type (str): 
    range_hight (float): 
    range_bottom_width (float): 
    range_color (str): 
    fill_area_color (str): 

Returns:
    bool:

<a id="unreal.RangeEntity.create_range"></a>

#### create\_range

```python
def create_range(points: Array[Vector], ignore_index: Array[int],
                 range_type: str, bottom_type: str, range_hight: float,
                 range_bottom_width: float, range_color: str) -> bool
```

x.create_range(points, ignore_index, range_type, bottom_type, range_hight, range_bottom_width, range_color) -> bool
Create Range

Args:
    points (Array[Vector]): 
    ignore_index (Array[int32]): 
    range_type (str): 
    bottom_type (str): 
    range_hight (float): 
    range_bottom_width (float): 
    range_color (str): 

Returns:
    bool:

<a id="unreal.RangeEntity.collate_points_data"></a>

#### collate\_points\_data

```python
def collate_points_data(
    out_ring_points: Array[Vector], wall_trianguate: Array[int],
    area: Array[Vector], bottom: Array[Vector], bottom2d: Array[Vector2D],
    min_z: float, range_height: float
) -> Tuple[Array[Vector], Array[int], Array[Vector], Array[Vector]]
```

x.collate_points_data(out_ring_points, wall_trianguate, area, bottom, bottom2d, min_z, range_height) -> (out_ring_points=Array[Vector], wall_trianguate=Array[int32], area=Array[Vector], bottom=Array[Vector])
Collate Points Data

Args:
    out_ring_points (Array[Vector]): 
    wall_trianguate (Array[int32]): 
    area (Array[Vector]): 
    bottom (Array[Vector]): 
    bottom2d (Array[Vector2D]): 
    min_z (double): 
    range_height (double): 

Returns:
    tuple: 

    out_ring_points (Array[Vector]): 

    wall_trianguate (Array[int32]): 

    area (Array[Vector]): 

    bottom (Array[Vector]):

<a id="unreal.RangeEntity.calculate_array_wall_mesh_data"></a>

#### calculate\_array\_wall\_mesh\_data

```python
def calculate_array_wall_mesh_data(
    points_distance: Array[float], local_points: Array[Vector],
    wall_normal: Array[Vector], local_u_vs: Array[Vector2D],
    local_trianguate: Array[int], wall_points: Array[Vector],
    wall_trianguate: Array[int], spline_length: float
) -> Tuple[Array[Vector], Array[Vector], Array[Vector2D], Array[int]]
```

x.calculate_array_wall_mesh_data(points_distance, local_points, wall_normal, local_u_vs, local_trianguate, wall_points, wall_trianguate, spline_length) -> (local_points=Array[Vector], wall_normal=Array[Vector], local_u_vs=Array[Vector2D], local_trianguate=Array[int32])
Calculate Array Wall Mesh Data

Args:
    points_distance (Array[double]): 
    local_points (Array[Vector]): 
    wall_normal (Array[Vector]): 
    local_u_vs (Array[Vector2D]): 
    local_trianguate (Array[int32]): 
    wall_points (Array[Vector]): 
    wall_trianguate (Array[int32]): 
    spline_length (float): 

Returns:
    tuple: 

    local_points (Array[Vector]): 

    wall_normal (Array[Vector]): 

    local_u_vs (Array[Vector2D]): 

    local_trianguate (Array[int32]):

<a id="unreal.RangeEntity.calculate_array_instance_mesh_data"></a>

#### calculate\_array\_instance\_mesh\_data

```python
def calculate_array_instance_mesh_data(
        points_array: Array[Vector], range_height: float,
        bottom_bound_radius: float
) -> Tuple[Array[Transform], Array[Transform]]
```

x.calculate_array_instance_mesh_data(points_array, range_height, bottom_bound_radius) -> (wall_transforms=Array[Transform], top_transforms=Array[Transform])
Calculate Array Instance Mesh Data

Args:
    points_array (Array[Vector]): 
    range_height (double): 
    bottom_bound_radius (double): 

Returns:
    tuple: 

    wall_transforms (Array[Transform]): 

    top_transforms (Array[Transform]):

<a id="unreal.RangeEntity.add_point_to_spline_array"></a>

#### add\_point\_to\_spline\_array

```python
def add_point_to_spline_array(
    out_ring_points: Array[Vector], wall_points: Array[Vector],
    points_array: Array[Vector], points_distance: Array[float], min_z: float,
    range_height: float
) -> Tuple[float, Array[Vector], Array[Vector], Array[float]]
```

x.add_point_to_spline_array(out_ring_points, wall_points, points_array, points_distance, min_z, range_height) -> (float, wall_points=Array[Vector], points_array=Array[Vector], points_distance=Array[double])
Add Point to Spline Array

Args:
    out_ring_points (Array[Vector]): 
    wall_points (Array[Vector]): 
    points_array (Array[Vector]): 
    points_distance (Array[double]): 
    min_z (double): 
    range_height (double): 

Returns:
    tuple: 

    wall_points (Array[Vector]): 

    points_array (Array[Vector]): 

    points_distance (Array[double]):

<a id="unreal.RasterEntity"></a>