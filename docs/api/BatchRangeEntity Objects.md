## BatchRangeEntity Objects

```python
class BatchRangeEntity(WdpActorEntity)
```

Batch Range Entity

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: BatchRangeEntity.h

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
- ``bottom_decal_cubes`` (Array[StaticMeshComponent]):  [Read-Write]
- ``bottom_decals`` (Array[DecalComponent]):  [Read-Write]
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
- ``top_index_u_vs`` (Array[Vector2D]):  [Read-Write]
- ``top_line_instance_mesh`` (HierarchicalInstancedStaticMeshComponent):  [Read-Write]
- ``top_procedural_mesh`` (ProceduralMeshComponent):  [Read-Write]
- ``top_triangles`` (Array[int32]):  [Read-Write]
- ``top_vertices`` (Array[Vector]):  [Read-Write]
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
- ``wall_index_u_vs`` (Array[Vector2D]):  [Read-Write]
- ``wall_length_u_vs`` (Array[Vector2D]):  [Read-Write]
- ``wall_line_instance_mesh`` (HierarchicalInstancedStaticMeshComponent):  [Read-Write]
- ``wall_normals`` (Array[Vector]):  [Read-Write]
- ``wall_procedural_mesh`` (ProceduralMeshComponent):  [Read-Write]
- ``wall_triangles`` (Array[int32]):  [Read-Write]
- ``wall_u_vs`` (Array[Vector2D]):  [Read-Write]
- ``wall_vertices`` (Array[Vector]):  [Read-Write]

<a id="unreal.BatchRangeEntity.bottom_decals"></a>

#### bottom\_decals

```python
@property
def bottom_decals() -> Array[DecalComponent]
```

(Array[DecalComponent]):  [Read-Write]

<a id="unreal.BatchRangeEntity.bottom_decals"></a>

#### bottom\_decals

```python
@bottom_decals.setter
def bottom_decals(value: Array[DecalComponent]) -> None
```

<a id="unreal.BatchRangeEntity.bottom_decal_cubes"></a>

#### bottom\_decal\_cubes

```python
@property
def bottom_decal_cubes() -> Array[StaticMeshComponent]
```

(Array[StaticMeshComponent]):  [Read-Write]

<a id="unreal.BatchRangeEntity.bottom_decal_cubes"></a>

#### bottom\_decal\_cubes

```python
@bottom_decal_cubes.setter
def bottom_decal_cubes(value: Array[StaticMeshComponent]) -> None
```

<a id="unreal.BatchRangeEntity.top_procedural_mesh"></a>

#### top\_procedural\_mesh

```python
@property
def top_procedural_mesh() -> ProceduralMeshComponent
```

(ProceduralMeshComponent):  [Read-Write]

<a id="unreal.BatchRangeEntity.top_procedural_mesh"></a>

#### top\_procedural\_mesh

```python
@top_procedural_mesh.setter
def top_procedural_mesh(value: ProceduralMeshComponent) -> None
```

<a id="unreal.BatchRangeEntity.wall_procedural_mesh"></a>

#### wall\_procedural\_mesh

```python
@property
def wall_procedural_mesh() -> ProceduralMeshComponent
```

(ProceduralMeshComponent):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_procedural_mesh"></a>

#### wall\_procedural\_mesh

```python
@wall_procedural_mesh.setter
def wall_procedural_mesh(value: ProceduralMeshComponent) -> None
```

<a id="unreal.BatchRangeEntity.top_line_instance_mesh"></a>

#### top\_line\_instance\_mesh

```python
@property
def top_line_instance_mesh() -> HierarchicalInstancedStaticMeshComponent
```

(HierarchicalInstancedStaticMeshComponent):  [Read-Write]

<a id="unreal.BatchRangeEntity.top_line_instance_mesh"></a>

#### top\_line\_instance\_mesh

```python
@top_line_instance_mesh.setter
def top_line_instance_mesh(
        value: HierarchicalInstancedStaticMeshComponent) -> None
```

<a id="unreal.BatchRangeEntity.wall_line_instance_mesh"></a>

#### wall\_line\_instance\_mesh

```python
@property
def wall_line_instance_mesh() -> HierarchicalInstancedStaticMeshComponent
```

(HierarchicalInstancedStaticMeshComponent):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_line_instance_mesh"></a>

#### wall\_line\_instance\_mesh

```python
@wall_line_instance_mesh.setter
def wall_line_instance_mesh(
        value: HierarchicalInstancedStaticMeshComponent) -> None
```

<a id="unreal.BatchRangeEntity.top_vertices"></a>

#### top\_vertices

```python
@property
def top_vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.BatchRangeEntity.top_vertices"></a>

#### top\_vertices

```python
@top_vertices.setter
def top_vertices(value: Array[Vector]) -> None
```

<a id="unreal.BatchRangeEntity.top_triangles"></a>

#### top\_triangles

```python
@property
def top_triangles() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.BatchRangeEntity.top_triangles"></a>

#### top\_triangles

```python
@top_triangles.setter
def top_triangles(value: Array[int]) -> None
```

<a id="unreal.BatchRangeEntity.top_index_u_vs"></a>

#### top\_index\_u\_vs

```python
@property
def top_index_u_vs() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.BatchRangeEntity.top_index_u_vs"></a>

#### top\_index\_u\_vs

```python
@top_index_u_vs.setter
def top_index_u_vs(value: Array[Vector2D]) -> None
```

<a id="unreal.BatchRangeEntity.wall_vertices"></a>

#### wall\_vertices

```python
@property
def wall_vertices() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_vertices"></a>

#### wall\_vertices

```python
@wall_vertices.setter
def wall_vertices(value: Array[Vector]) -> None
```

<a id="unreal.BatchRangeEntity.wall_triangles"></a>

#### wall\_triangles

```python
@property
def wall_triangles() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_triangles"></a>

#### wall\_triangles

```python
@wall_triangles.setter
def wall_triangles(value: Array[int]) -> None
```

<a id="unreal.BatchRangeEntity.wall_normals"></a>

#### wall\_normals

```python
@property
def wall_normals() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_normals"></a>

#### wall\_normals

```python
@wall_normals.setter
def wall_normals(value: Array[Vector]) -> None
```

<a id="unreal.BatchRangeEntity.wall_u_vs"></a>

#### wall\_u\_vs

```python
@property
def wall_u_vs() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_u_vs"></a>

#### wall\_u\_vs

```python
@wall_u_vs.setter
def wall_u_vs(value: Array[Vector2D]) -> None
```

<a id="unreal.BatchRangeEntity.wall_index_u_vs"></a>

#### wall\_index\_u\_vs

```python
@property
def wall_index_u_vs() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_index_u_vs"></a>

#### wall\_index\_u\_vs

```python
@wall_index_u_vs.setter
def wall_index_u_vs(value: Array[Vector2D]) -> None
```

<a id="unreal.BatchRangeEntity.wall_length_u_vs"></a>

#### wall\_length\_u\_vs

```python
@property
def wall_length_u_vs() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.BatchRangeEntity.wall_length_u_vs"></a>

#### wall\_length\_u\_vs

```python
@wall_length_u_vs.setter
def wall_length_u_vs(value: Array[Vector2D]) -> None
```

<a id="unreal.BatchRangeEntity.store_triangles_to_texture"></a>

#### store\_triangles\_to\_texture

```python
def store_triangles_to_texture(bottom_triangles: Array[int],
                               bottom_vertexes: Array[Vector], min_x: float,
                               max_x: float, min_y: float, max_y: float,
                               use32_texture: bool) -> Texture2D
```

x.store_triangles_to_texture(bottom_triangles, bottom_vertexes, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Triangles to Texture

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

<a id="unreal.BatchRangeEntity.store_points_to_texture"></a>

#### store\_points\_to\_texture

```python
def store_points_to_texture(points_array: Array[Vector], min_x: float,
                            max_x: float, min_y: float, max_y: float,
                            use32_texture: bool) -> Texture2D
```

x.store_points_to_texture(points_array, min_x, max_x, min_y, max_y, use32_texture) -> Texture2D
Store Points to Texture

Args:
    points_array (Array[Vector]): 
    min_x (double): 
    max_x (double): 
    min_y (double): 
    max_y (double): 
    use32_texture (bool): 

Returns:
    Texture2D:

<a id="unreal.BatchRangeEntity.init_batch_range_params"></a>

#### init\_batch\_range\_params

```python
def init_batch_range_params(range_type: str, bottom_type: str,
                            range_hight: float, range_bottom_width: float,
                            range_color: str, fill_color: str) -> bool
```

x.init_batch_range_params(range_type, bottom_type, range_hight, range_bottom_width, range_color, fill_color) -> bool
Init Batch Range Params

Args:
    range_type (str): 
    bottom_type (str): 
    range_hight (float): 
    range_bottom_width (float): 
    range_color (str): 
    fill_color (str): 

Returns:
    bool:

<a id="unreal.BatchRangeEntity.horizontal_data"></a>

#### horizontal\_data

```python
def horizontal_data(
    out_ring_points: Array[Vector]
) -> Tuple[float, float, float, float, float, float]
```

x.horizontal_data(out_ring_points) -> (double, min_x=double, max_x=double, min_y=double, max_y=double, min_z=double)
Horizontal Data

Args:
    out_ring_points (Array[Vector]): 

Returns:
    tuple: 

    min_x (double): 

    max_x (double): 

    min_y (double): 

    max_y (double): 

    min_z (double):

<a id="unreal.BatchRangeEntity.get_owner_world"></a>

#### get\_owner\_world

```python
def get_owner_world() -> Actor
```

x.get_owner_world() -> Actor
Get Owner World

Returns:
    Actor:

<a id="unreal.BatchRangeEntity.create_single_range_part"></a>

#### create\_single\_range\_part

```python
def create_single_range_part(out_ring_points: Array[Vector],
                             inner_loop_array: Array[BatchRangeVectorArray],
                             bottom_vertexes: Array[Vector2D],
                             bottom_trianges: Array[int], range_offset: Vector,
                             range_index: int) -> bool
```

x.create_single_range_part(out_ring_points, inner_loop_array, bottom_vertexes, bottom_trianges, range_offset, range_index) -> bool
Create Single Range Part

Args:
    out_ring_points (Array[Vector]): 
    inner_loop_array (Array[BatchRangeVectorArray]): 
    bottom_vertexes (Array[Vector2D]): 
    bottom_trianges (Array[int32]): 
    range_offset (Vector): 
    range_index (int32): 

Returns:
    bool:

<a id="unreal.BatchRangeEntity.create_merged_range_part"></a>

#### create\_merged\_range\_part

```python
def create_merged_range_part() -> bool
```

x.create_merged_range_part() -> bool
Create Merged Range Part

Returns:
    bool:

<a id="unreal.BatchRangeEntity.collate_single_wall_base_data"></a>

#### collate\_single\_wall\_base\_data

```python
def collate_single_wall_base_data(
    out_ring_points: Array[Vector], wall_points: Array[Vector],
    loop_trianguate: Array[int], loop_points: Array[Vector],
    points_distance: Array[float], range_offset: Vector, min_z: float,
    range_height: float
) -> Tuple[float, Array[Vector], Array[int], Array[Vector], Array[float]]
```

x.collate_single_wall_base_data(out_ring_points, wall_points, loop_trianguate, loop_points, points_distance, range_offset, min_z, range_height) -> (float, wall_points=Array[Vector], loop_trianguate=Array[int32], loop_points=Array[Vector], points_distance=Array[double])
Collate Single Wall Base Data

Args:
    out_ring_points (Array[Vector]): 
    wall_points (Array[Vector]): 
    loop_trianguate (Array[int32]): 
    loop_points (Array[Vector]): 
    points_distance (Array[double]): 
    range_offset (Vector): 
    min_z (double): 
    range_height (double): 

Returns:
    tuple: 

    wall_points (Array[Vector]): 

    loop_trianguate (Array[int32]): 

    loop_points (Array[Vector]): 

    points_distance (Array[double]):

<a id="unreal.BatchRangeEntity.collate_single_area_data"></a>

#### collate\_single\_area\_data

```python
def collate_single_area_data(out_ring_points: Array[Vector],
                             bottom2d: Array[Vector2D],
                             bottom_triangles: Array[int],
                             range_offset: Vector, min_z: float,
                             range_height: float,
                             range_index: int) -> Tuple[float, Array[Vector]]
```

x.collate_single_area_data(out_ring_points, bottom2d, bottom_triangles, range_offset, min_z, range_height, range_index) -> (float, out_ring_points=Array[Vector])
Collate Single Area Data

Args:
    out_ring_points (Array[Vector]): 
    bottom2d (Array[Vector2D]): 
    bottom_triangles (Array[int32]): 
    range_offset (Vector): 
    min_z (double): 
    range_height (double): 
    range_index (int32): 

Returns:
    Array[Vector]: 

    out_ring_points (Array[Vector]):

<a id="unreal.BatchRangeEntity.collate_decal_data"></a>

#### collate\_decal\_data

```python
def collate_decal_data(bottom: Array[Vector], bottom2d: Array[Vector2D],
                       min_z: float) -> Array[Vector]
```

x.collate_decal_data(bottom, bottom2d, min_z) -> Array[Vector]
Collate Decal Data

Args:
    bottom (Array[Vector]): 
    bottom2d (Array[Vector2D]): 
    min_z (double): 

Returns:
    Array[Vector]: 

    bottom (Array[Vector]):

<a id="unreal.BatchRangeEntity.calculate_wall_line_mesh_data"></a>

#### calculate\_wall\_line\_mesh\_data

```python
def calculate_wall_line_mesh_data(
        points_array: Array[Vector], range_offset: Vector, range_height: float,
        bottom_bound_radius: float
) -> Tuple[Array[Transform], Array[Transform]]
```

x.calculate_wall_line_mesh_data(points_array, range_offset, range_height, bottom_bound_radius) -> (wall_transforms=Array[Transform], top_transforms=Array[Transform])
Calculate Wall Line Mesh Data

Args:
    points_array (Array[Vector]): 
    range_offset (Vector): 
    range_height (double): 
    bottom_bound_radius (double): 

Returns:
    tuple: 

    wall_transforms (Array[Transform]): 

    top_transforms (Array[Transform]):

<a id="unreal.BatchRangeEntity.caculate_single_wall_mesh_data"></a>

#### caculate\_single\_wall\_mesh\_data

```python
def caculate_single_wall_mesh_data(wall_points: Array[Vector],
                                   loop_distance: Array[float],
                                   loop_trianguate: Array[int],
                                   range_index: int,
                                   range_length_factor: float,
                                   spline_length: float) -> None
```

x.caculate_single_wall_mesh_data(wall_points, loop_distance, loop_trianguate, range_index, range_length_factor, spline_length) -> None
Caculate Single Wall Mesh Data

Args:
    wall_points (Array[Vector]): 
    loop_distance (Array[double]): 
    loop_trianguate (Array[int32]): 
    range_index (int32): 
    range_length_factor (float): 
    spline_length (float):

<a id="unreal.BlueprintFunctionLibraryAPI"></a>