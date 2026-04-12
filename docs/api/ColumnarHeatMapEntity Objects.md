## ColumnarHeatMapEntity Objects

```python
class ColumnarHeatMapEntity(WdpActorEntity)
```

Columnar Heat Map Entity

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ColumnarHeatMapEntity.h

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
- ``auto_cycle_time`` (float):  [Read-Write] 为false表示坐标为世界坐标，ture表示物体坐标
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``auto_update_data`` (bool):  [Read-Only]
- ``auto_update_data_open`` (bool):  [Read-Only]
- ``base_height`` (int32):  [Read-Write]
- ``black_white_length`` (int32):  [Read-Only]
- ``black_white_width`` (int32):  [Read-Only]
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``block_length`` (int32):  [Read-Write] 基础底层高度
- ``block_width`` (int32):  [Read-Write] 热力图X轴长度
- ``brightness`` (float):  [Read-Write] 开启蒙板
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``cube_gap`` (float):  [Read-Write] 柱子高度乘数
- ``cube_length`` (int32):  [Read-Write] 热力图Y轴长度
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
- ``instance_static_mesh`` (InstancedStaticMeshComponent):  [Read-Write]
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``location_is_normalization`` (bool):  [Read-Write] 为false则调用强度归一化
- ``location_is_space_position`` (bool):  [Read-Write] 为false则调用坐标归一化
- ``max_height`` (int32):  [Read-Write] 柱子边长
- ``metallic`` (float):  [Read-Write] 自发光亮度
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
- ``open_mask`` (bool):  [Read-Write] 描边最大可视距离，过大会出现闪烁
- ``open_stroke`` (bool):  [Read-Write]
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``pixels_block_white_data_array`` (Array[Color]):  [Read-Only]
- ``pixels_data_array`` (Array[Color]):  [Read-Only] 粗糙度
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
- ``roughness`` (float):  [Read-Write] 高光
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``specular`` (float):  [Read-Write] 金属属性
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``strength_gain`` (float):  [Read-Write] 柱子间隙
- ``strength_is_normalization`` (bool):  [Read-Write] 指定最大强度
- ``strength_max_value`` (float):  [Read-Write] 强度作用范围
- ``stroke_visibility_distance`` (float):  [Read-Write] 开启描边
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

<a id="unreal.ColumnarHeatMapEntity.instance_static_mesh"></a>

#### instance\_static\_mesh

```python
@property
def instance_static_mesh() -> InstancedStaticMeshComponent
```

(InstancedStaticMeshComponent):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntity.instance_static_mesh"></a>

#### instance\_static\_mesh

```python
@instance_static_mesh.setter
def instance_static_mesh(value: InstancedStaticMeshComponent) -> None
```

<a id="unreal.ColumnarHeatMapEntity.base_height"></a>

#### base\_height

```python
@property
def base_height() -> int
```

(int32):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntity.base_height"></a>

#### base\_height

```python
@base_height.setter
def base_height(value: int) -> None
```

<a id="unreal.ColumnarHeatMapEntity.block_length"></a>

#### block\_length

```python
@property
def block_length() -> int
```

(int32):  [Read-Write] 基础底层高度

<a id="unreal.ColumnarHeatMapEntity.block_length"></a>

#### block\_length

```python
@block_length.setter
def block_length(value: int) -> None
```

<a id="unreal.ColumnarHeatMapEntity.block_width"></a>

#### block\_width

```python
@property
def block_width() -> int
```

(int32):  [Read-Write] 热力图X轴长度

<a id="unreal.ColumnarHeatMapEntity.block_width"></a>

#### block\_width

```python
@block_width.setter
def block_width(value: int) -> None
```

<a id="unreal.ColumnarHeatMapEntity.cube_length"></a>

#### cube\_length

```python
@property
def cube_length() -> int
```

(int32):  [Read-Write] 热力图Y轴长度

<a id="unreal.ColumnarHeatMapEntity.cube_length"></a>

#### cube\_length

```python
@cube_length.setter
def cube_length(value: int) -> None
```

<a id="unreal.ColumnarHeatMapEntity.max_height"></a>

#### max\_height

```python
@property
def max_height() -> int
```

(int32):  [Read-Write] 柱子边长

<a id="unreal.ColumnarHeatMapEntity.max_height"></a>

#### max\_height

```python
@max_height.setter
def max_height(value: int) -> None
```

<a id="unreal.ColumnarHeatMapEntity.cube_gap"></a>

#### cube\_gap

```python
@property
def cube_gap() -> float
```

(float):  [Read-Write] 柱子高度乘数

<a id="unreal.ColumnarHeatMapEntity.cube_gap"></a>

#### cube\_gap

```python
@cube_gap.setter
def cube_gap(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.strength_gain"></a>

#### strength\_gain

```python
@property
def strength_gain() -> float
```

(float):  [Read-Write] 柱子间隙

<a id="unreal.ColumnarHeatMapEntity.strength_gain"></a>

#### strength\_gain

```python
@strength_gain.setter
def strength_gain(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.strength_max_value"></a>

#### strength\_max\_value

```python
@property
def strength_max_value() -> float
```

(float):  [Read-Write] 强度作用范围

<a id="unreal.ColumnarHeatMapEntity.strength_max_value"></a>

#### strength\_max\_value

```python
@strength_max_value.setter
def strength_max_value(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.strength_is_normalization"></a>

#### strength\_is\_normalization

```python
@property
def strength_is_normalization() -> bool
```

(bool):  [Read-Write] 指定最大强度

<a id="unreal.ColumnarHeatMapEntity.strength_is_normalization"></a>

#### strength\_is\_normalization

```python
@strength_is_normalization.setter
def strength_is_normalization(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntity.location_is_normalization"></a>

#### location\_is\_normalization

```python
@property
def location_is_normalization() -> bool
```

(bool):  [Read-Write] 为false则调用强度归一化

<a id="unreal.ColumnarHeatMapEntity.location_is_normalization"></a>

#### location\_is\_normalization

```python
@location_is_normalization.setter
def location_is_normalization(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntity.location_is_space_position"></a>

#### location\_is\_space\_position

```python
@property
def location_is_space_position() -> bool
```

(bool):  [Read-Write] 为false则调用坐标归一化

<a id="unreal.ColumnarHeatMapEntity.location_is_space_position"></a>

#### location\_is\_space\_position

```python
@location_is_space_position.setter
def location_is_space_position(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntity.auto_cycle_time"></a>

#### auto\_cycle\_time

```python
@property
def auto_cycle_time() -> float
```

(float):  [Read-Write] 为false表示坐标为世界坐标，ture表示物体坐标

<a id="unreal.ColumnarHeatMapEntity.auto_cycle_time"></a>

#### auto\_cycle\_time

```python
@auto_cycle_time.setter
def auto_cycle_time(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.open_stroke"></a>

#### open\_stroke

```python
@property
def open_stroke() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ColumnarHeatMapEntity.open_stroke"></a>

#### open\_stroke

```python
@open_stroke.setter
def open_stroke(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntity.stroke_visibility_distance"></a>

#### stroke\_visibility\_distance

```python
@property
def stroke_visibility_distance() -> float
```

(float):  [Read-Write] 开启描边

<a id="unreal.ColumnarHeatMapEntity.stroke_visibility_distance"></a>

#### stroke\_visibility\_distance

```python
@stroke_visibility_distance.setter
def stroke_visibility_distance(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.open_mask"></a>

#### open\_mask

```python
@property
def open_mask() -> bool
```

(bool):  [Read-Write] 描边最大可视距离，过大会出现闪烁

<a id="unreal.ColumnarHeatMapEntity.open_mask"></a>

#### open\_mask

```python
@open_mask.setter
def open_mask(value: bool) -> None
```

<a id="unreal.ColumnarHeatMapEntity.brightness"></a>

#### brightness

```python
@property
def brightness() -> float
```

(float):  [Read-Write] 开启蒙板

<a id="unreal.ColumnarHeatMapEntity.brightness"></a>

#### brightness

```python
@brightness.setter
def brightness(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.metallic"></a>

#### metallic

```python
@property
def metallic() -> float
```

(float):  [Read-Write] 自发光亮度

<a id="unreal.ColumnarHeatMapEntity.metallic"></a>

#### metallic

```python
@metallic.setter
def metallic(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.specular"></a>

#### specular

```python
@property
def specular() -> float
```

(float):  [Read-Write] 金属属性

<a id="unreal.ColumnarHeatMapEntity.specular"></a>

#### specular

```python
@specular.setter
def specular(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.roughness"></a>

#### roughness

```python
@property
def roughness() -> float
```

(float):  [Read-Write] 高光

<a id="unreal.ColumnarHeatMapEntity.roughness"></a>

#### roughness

```python
@roughness.setter
def roughness(value: float) -> None
```

<a id="unreal.ColumnarHeatMapEntity.pixels_data_array"></a>

#### pixels\_data\_array

```python
@property
def pixels_data_array() -> Array[Color]
```

(Array[Color]):  [Read-Only] 粗糙度

<a id="unreal.ColumnarHeatMapEntity.auto_update_data"></a>

#### auto\_update\_data

```python
@property
def auto_update_data() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ColumnarHeatMapEntity.auto_update_data_open"></a>

#### auto\_update\_data\_open

```python
@property
def auto_update_data_open() -> bool
```

(bool):  [Read-Only]

<a id="unreal.ColumnarHeatMapEntity.pixels_block_white_data_array"></a>

#### pixels\_block\_white\_data\_array

```python
@property
def pixels_block_white_data_array() -> Array[Color]
```

(Array[Color]):  [Read-Only]

<a id="unreal.ColumnarHeatMapEntity.black_white_width"></a>

#### black\_white\_width

```python
@property
def black_white_width() -> int
```

(int32):  [Read-Only]

<a id="unreal.ColumnarHeatMapEntity.black_white_length"></a>

#### black\_white\_length

```python
@property
def black_white_length() -> int
```

(int32):  [Read-Only]

<a id="unreal.ColumnarHeatMapEntity.un_filter_columnar_heat_map_entity"></a>

#### un\_filter\_columnar\_heat\_map\_entity

```python
def un_filter_columnar_heat_map_entity() -> bool
```

x.un_filter_columnar_heat_map_entity() -> bool
Un Filter Columnar Heat Map Entity

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.spawn_instance"></a>

#### spawn\_instance

```python
def spawn_instance(clip_points: Array[Vector],
                   filter_value_range: Vector2D = [0.000000, 0.000000],
                   is_clip: bool = False,
                   is_filter: bool = False) -> None
```

x.spawn_instance(clip_points, filter_value_range=[0.000000, 0.000000], is_clip=False, is_filter=False) -> None
Spawn Instance

Args:
    clip_points (Array[Vector]): 
    filter_value_range (Vector2D): 
    is_clip (bool): 
    is_filter (bool):

<a id="unreal.ColumnarHeatMapEntity.spawn_data_array_form_heat_point"></a>

#### spawn\_data\_array\_form\_heat\_point

```python
def spawn_data_array_form_heat_point(
        heat_density_data: Array[API_HeatPointData]) -> Array[float]
```

x.spawn_data_array_form_heat_point(heat_density_data) -> Array[float]
Spawn Data Array Form Heat Point

Args:
    heat_density_data (Array[API_HeatPointData]): 

Returns:
    Array[float]:

<a id="unreal.ColumnarHeatMapEntity.set_width"></a>

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

<a id="unreal.ColumnarHeatMapEntity.set_polygon"></a>

#### set\_polygon

```python
def set_polygon(polygon: Array[Vector]) -> bool
```

x.set_polygon(polygon) -> bool
UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category = CoveringApi, meta = (DisplayName = "SetData"))
       bool SetColumnarData(const TArray<FColumnarData>& InData);
       virtual bool SetColumnarData_Implementation(const TArray<FColumnarData>& InData);

Args:
    polygon (Array[Vector]): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_min_height"></a>

#### set\_min\_height

```python
def set_min_height(min_height: float) -> bool
```

x.set_min_height(min_height) -> bool
Set Min Height

Args:
    min_height (float): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_max_height"></a>

#### set\_max\_height

```python
def set_max_height(max_height: float) -> bool
```

x.set_max_height(max_height) -> bool
Set Max Height

Args:
    max_height (float): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_garadient_setting"></a>

#### set\_garadient\_setting

```python
def set_garadient_setting(settings: Array[str]) -> bool
```

x.set_garadient_setting(settings) -> bool
Set Garadient Setting

Args:
    settings (Array[str]): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_enable_gap"></a>

#### set\_enable\_gap

```python
def set_enable_gap(gap: bool) -> bool
```

x.set_enable_gap(gap) -> bool
Set Enable Gap

Args:
    gap (bool): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_coord_z"></a>

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

<a id="unreal.ColumnarHeatMapEntity.set_brush_diameter"></a>

#### set\_brush\_diameter

```python
def set_brush_diameter(brush_diameter: float) -> bool
```

x.set_brush_diameter(brush_diameter) -> bool
Set Brush Diameter

Args:
    brush_diameter (float): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.set_type"></a>

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

<a id="unreal.ColumnarHeatMapEntity.set_clip_columnar_heat_map"></a>

#### set\_clip\_columnar\_heat\_map

```python
def set_clip_columnar_heat_map(polygon: Array[Vector],
                               fill_color: str) -> bool
```

x.set_clip_columnar_heat_map(polygon, fill_color) -> bool
Set Clip Columnar Heat Map

Args:
    polygon (Array[Vector]): 
    fill_color (str): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.remove_data"></a>

#### remove\_data

```python
def remove_data(heat_point_list: API_HeatPointList) -> None
```

x.remove_data(heat_point_list) -> None
Remove Data

Args:
    heat_point_list (API_HeatPointList):

<a id="unreal.ColumnarHeatMapEntity.push_all_data"></a>

#### push\_all\_data

```python
def push_all_data() -> None
```

x.push_all_data() -> None
Push All Data

<a id="unreal.ColumnarHeatMapEntity.init_base_data"></a>

#### init\_base\_data

```python
def init_base_data() -> None
```

x.init_base_data() -> None
Init Base Data

<a id="unreal.ColumnarHeatMapEntity.get_columnar_heat_map_points"></a>

#### get\_columnar\_heat\_map\_points

```python
def get_columnar_heat_map_points() -> Optional[Array[Vector]]
```

x.get_columnar_heat_map_points() -> Array[Vector] or None
Get Columnar Heat Map Points

Returns:
    Array[Vector] or None: 

    out_points (Array[Vector]):

<a id="unreal.ColumnarHeatMapEntity.get_columnar_heat_map_entity"></a>

#### get\_columnar\_heat\_map\_entity

```python
def get_columnar_heat_map_entity(location: Vector) -> float
```

x.get_columnar_heat_map_entity(location) -> float
Get Columnar Heat Map Entity

Args:
    location (Vector): 

Returns:
    float:

<a id="unreal.ColumnarHeatMapEntity.finish_create"></a>

#### finish\_create

```python
def finish_create() -> None
```

x.finish_create() -> None
Finish Create

<a id="unreal.ColumnarHeatMapEntity.filter_columnar_heat_map_entity"></a>

#### filter\_columnar\_heat\_map\_entity

```python
def filter_columnar_heat_map_entity(filter_value_range: Vector2D) -> bool
```

x.filter_columnar_heat_map_entity(filter_value_range) -> bool
Filter Columnar Heat Map Entity

Args:
    filter_value_range (Vector2D): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.create_columnar_heat_map"></a>

#### create\_columnar\_heat\_map

```python
def create_columnar_heat_map(points: Array[Vector],
                             heat_map_entity_atom: ColumnarHeatMapEntityAtom,
                             point_value_atom: PointValueAtom) -> bool
```

x.create_columnar_heat_map(points, heat_map_entity_atom, point_value_atom) -> bool
Create Columnar Heat Map

Args:
    points (Array[Vector]): 
    heat_map_entity_atom (ColumnarHeatMapEntityAtom): 
    point_value_atom (PointValueAtom): 

Returns:
    bool:

<a id="unreal.ColumnarHeatMapEntity.clear_heat"></a>

#### clear\_heat

```python
def clear_heat() -> None
```

x.clear_heat() -> None
Clear Heat

<a id="unreal.ColumnarHeatMapEntity.append_data"></a>

#### append\_data

```python
def append_data(heat_point_list: API_HeatPointList) -> None
```

x.append_data(heat_point_list) -> None
Append Data

Args:
    heat_point_list (API_HeatPointList):

<a id="unreal.CompassEntity"></a>