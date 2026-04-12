## WdpCameraPresetActor Objects

```python
class WdpCameraPresetActor(Actor)
```

Wdp Camera Preset Actor

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpCameraPresetActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``all_camera_data_preview`` (AllCameraData):  [Read-Write] 最后要发送的相机数据预览
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
- ``camera_fov`` (float):  [Read-Write] 相机FOV
- ``camera_index`` (int32):  [Read-Write] 相机编号
- ``camera_location`` (Vector):  [Read-Write] 相机位置
- ``camera_pivot`` (Vector):  [Read-Write] 相机轴点
- ``camera_rotation`` (Rotator):  [Read-Write] 相机旋转
- ``camera_tag`` (GameplayTagContainer):  [Read-Write] 相机标签
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``collision_mode`` (CameraCollisionMode):  [Read-Write] 碰撞模式
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``custom_points`` (Array[Vector]):  [Read-Write] 碰撞的边界点 如果是两个点，表示矩形的两个对角，如果是三个或以上，表示按顺序的多边形 只有2D限制//注意这里的本地空间的点，传数据时会自动转换
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
- ``enabled_features`` (int32):  [Read-Write] 目标要开启的Features
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``forward_direction`` (MoveForwardDirection):  [Read-Write] 按下W时的前进方向
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``ground_position_mode`` (GroundPositionMode):  [Read-Write] 地面碰撞模式
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
- ``max_zoom_distance`` (double):  [Read-Write] 最大缩放距离
- ``max_zoom_fov`` (float):  [Read-Write] 最大缩放FOV
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``min_zoom_distance`` (double):  [Read-Write] 最小缩放距离
- ``min_zoom_fov`` (float):  [Read-Write] 最小缩放FOV
- ``net_cull_distance_squared`` (float):  [Read-Write]
- ``net_dormancy`` (NetDormancy):  [Read-Write] Dormancy setting for actor to take itself off of the replication list without being destroyed on clients.
- ``net_load_on_client`` (bool):  [Read-Write] This actor will be loaded on network clients during map load
- ``net_priority`` (float):  [Read-Write] Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate
- ``net_update_frequency`` (float):  [Read-Write]
- ``net_use_owner_relevancy`` (bool):  [Read-Write] If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority
- ``note`` (str):  [Read-Write] 相机注释
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
- ``override_collision`` (bool):  [Read-Write] 是否改变碰撞限制
- ``override_core_data`` (bool):  [Read-Write] 是否启用相机的核心数据变更，如果不勾选，则只改变相机功能参数，不改变位置
- ``override_features`` (bool):  [Read-Write] 是否改变Feature功能
- ``override_forward_direction`` (bool):  [Read-Write] 是否改前进的方向
- ``override_rotate_limit`` (bool):  [Read-Write] 是否改变旋转限制
- ``override_rotate_mode`` (bool):  [Read-Write] 是否改变旋转的操作模式
- ``override_zoom_limit`` (bool):  [Read-Write] 是否改变缩放限制
- ``override_zoom_mode`` (bool):  [Read-Write] 是否改变缩放的操作模式
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pitch_limit`` (Vector2D):  [Read-Write] Pitch 的限制角度
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``possess_pawn_ref`` (Pawn):  [Read-Write] 需要Possess的Pawn的引用
- ``possess_use_auto_spawn`` (bool):  [Read-Write] 是否使用Spawn模式，如果是将在切换相机后自动创建一个Pawn
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``profile_name`` (CollisionProfileName):  [Read-Write] 碰撞的ProfileName
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
- ``roll_limit`` (Vector2D):  [Read-Write] Roll 的限制角度
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``rotate_mode`` (CameraRotateMode):  [Read-Write] 操作的旋转模式
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``spawn_pawn_class`` (type(Class)):  [Read-Write] 需要被Spawn的Pawn的Class
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
- ``use_as_default_camera`` (bool):  [Read-Write] 作为默认相机使用，场景中只应该存在一个默认相机
- ``use_pivot_location_as_spawn_location`` (bool):  [Read-Write] 是否使用Pivot坐标Spawn，如果不是则使用相机坐标
- ``use_possess_mode`` (bool):  [Read-Write] 是否使用Possess模式
- ``use_wdp_pawn_as_default`` (bool):  [Read-Write] 在当前Pawn不是WdpPawn的时候是否自动切换回WdpPawn
- ``yaw_limit`` (Vector2D):  [Read-Write] Yaw 的限制角度
- ``zoom_mode`` (ZoomActionType):  [Read-Write] 操作的旋转模式

<a id="unreal.WdpCameraPresetActor.camera_tag"></a>

#### camera\_tag

```python
@property
def camera_tag() -> GameplayTagContainer
```

(GameplayTagContainer):  [Read-Write] 相机标签

<a id="unreal.WdpCameraPresetActor.camera_tag"></a>

#### camera\_tag

```python
@camera_tag.setter
def camera_tag(value: GameplayTagContainer) -> None
```

<a id="unreal.WdpCameraPresetActor.camera_index"></a>

#### camera\_index

```python
@property
def camera_index() -> int
```

(int32):  [Read-Write] 相机编号

<a id="unreal.WdpCameraPresetActor.camera_index"></a>

#### camera\_index

```python
@camera_index.setter
def camera_index(value: int) -> None
```

<a id="unreal.WdpCameraPresetActor.note"></a>

#### note

```python
@property
def note() -> str
```

(str):  [Read-Write] 相机注释

<a id="unreal.WdpCameraPresetActor.note"></a>

#### note

```python
@note.setter
def note(value: str) -> None
```

<a id="unreal.WdpCameraPresetActor.all_camera_data_preview"></a>

#### all\_camera\_data\_preview

```python
@property
def all_camera_data_preview() -> AllCameraData
```

(AllCameraData):  [Read-Write] 最后要发送的相机数据预览

<a id="unreal.WdpCameraPresetActor.all_camera_data_preview"></a>

#### all\_camera\_data\_preview

```python
@all_camera_data_preview.setter
def all_camera_data_preview(value: AllCameraData) -> None
```

<a id="unreal.WdpCameraPresetActor.use_as_default_camera"></a>

#### use\_as\_default\_camera

```python
@property
def use_as_default_camera() -> bool
```

(bool):  [Read-Write] 作为默认相机使用，场景中只应该存在一个默认相机

<a id="unreal.WdpCameraPresetActor.use_as_default_camera"></a>

#### use\_as\_default\_camera

```python
@use_as_default_camera.setter
def use_as_default_camera(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.override_core_data"></a>

#### override\_core\_data

```python
@property
def override_core_data() -> bool
```

(bool):  [Read-Write] 是否启用相机的核心数据变更，如果不勾选，则只改变相机功能参数，不改变位置

<a id="unreal.WdpCameraPresetActor.override_core_data"></a>

#### override\_core\_data

```python
@override_core_data.setter
def override_core_data(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.camera_location"></a>

#### camera\_location

```python
@property
def camera_location() -> Vector
```

(Vector):  [Read-Write] 相机位置

<a id="unreal.WdpCameraPresetActor.camera_location"></a>

#### camera\_location

```python
@camera_location.setter
def camera_location(value: Vector) -> None
```

<a id="unreal.WdpCameraPresetActor.camera_rotation"></a>

#### camera\_rotation

```python
@property
def camera_rotation() -> Rotator
```

(Rotator):  [Read-Write] 相机旋转

<a id="unreal.WdpCameraPresetActor.camera_rotation"></a>

#### camera\_rotation

```python
@camera_rotation.setter
def camera_rotation(value: Rotator) -> None
```

<a id="unreal.WdpCameraPresetActor.camera_fov"></a>

#### camera\_fov

```python
@property
def camera_fov() -> float
```

(float):  [Read-Write] 相机FOV

<a id="unreal.WdpCameraPresetActor.camera_fov"></a>

#### camera\_fov

```python
@camera_fov.setter
def camera_fov(value: float) -> None
```

<a id="unreal.WdpCameraPresetActor.camera_pivot"></a>

#### camera\_pivot

```python
@property
def camera_pivot() -> Vector
```

(Vector):  [Read-Write] 相机轴点

<a id="unreal.WdpCameraPresetActor.camera_pivot"></a>

#### camera\_pivot

```python
@camera_pivot.setter
def camera_pivot(value: Vector) -> None
```

<a id="unreal.WdpCameraPresetActor.override_features"></a>

#### override\_features

```python
@property
def override_features() -> bool
```

(bool):  [Read-Write] 是否改变Feature功能

<a id="unreal.WdpCameraPresetActor.override_features"></a>

#### override\_features

```python
@override_features.setter
def override_features(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.enabled_features"></a>

#### enabled\_features

```python
@property
def enabled_features() -> int
```

(int32):  [Read-Write] 目标要开启的Features

<a id="unreal.WdpCameraPresetActor.enabled_features"></a>

#### enabled\_features

```python
@enabled_features.setter
def enabled_features(value: int) -> None
```

<a id="unreal.WdpCameraPresetActor.override_rotate_mode"></a>

#### override\_rotate\_mode

```python
@property
def override_rotate_mode() -> bool
```

(bool):  [Read-Write] 是否改变旋转的操作模式

<a id="unreal.WdpCameraPresetActor.override_rotate_mode"></a>

#### override\_rotate\_mode

```python
@override_rotate_mode.setter
def override_rotate_mode(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.rotate_mode"></a>

#### rotate\_mode

```python
@property
def rotate_mode() -> CameraRotateMode
```

(CameraRotateMode):  [Read-Write] 操作的旋转模式

<a id="unreal.WdpCameraPresetActor.rotate_mode"></a>

#### rotate\_mode

```python
@rotate_mode.setter
def rotate_mode(value: CameraRotateMode) -> None
```

<a id="unreal.WdpCameraPresetActor.override_zoom_mode"></a>

#### override\_zoom\_mode

```python
@property
def override_zoom_mode() -> bool
```

(bool):  [Read-Write] 是否改变缩放的操作模式

<a id="unreal.WdpCameraPresetActor.override_zoom_mode"></a>

#### override\_zoom\_mode

```python
@override_zoom_mode.setter
def override_zoom_mode(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.zoom_mode"></a>

#### zoom\_mode

```python
@property
def zoom_mode() -> ZoomActionType
```

(ZoomActionType):  [Read-Write] 操作的旋转模式

<a id="unreal.WdpCameraPresetActor.zoom_mode"></a>

#### zoom\_mode

```python
@zoom_mode.setter
def zoom_mode(value: ZoomActionType) -> None
```

<a id="unreal.WdpCameraPresetActor.override_forward_direction"></a>

#### override\_forward\_direction

```python
@property
def override_forward_direction() -> bool
```

(bool):  [Read-Write] 是否改前进的方向

<a id="unreal.WdpCameraPresetActor.override_forward_direction"></a>

#### override\_forward\_direction

```python
@override_forward_direction.setter
def override_forward_direction(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.forward_direction"></a>

#### forward\_direction

```python
@property
def forward_direction() -> MoveForwardDirection
```

(MoveForwardDirection):  [Read-Write] 按下W时的前进方向

<a id="unreal.WdpCameraPresetActor.forward_direction"></a>

#### forward\_direction

```python
@forward_direction.setter
def forward_direction(value: MoveForwardDirection) -> None
```

<a id="unreal.WdpCameraPresetActor.override_rotate_limit"></a>

#### override\_rotate\_limit

```python
@property
def override_rotate_limit() -> bool
```

(bool):  [Read-Write] 是否改变旋转限制

<a id="unreal.WdpCameraPresetActor.override_rotate_limit"></a>

#### override\_rotate\_limit

```python
@override_rotate_limit.setter
def override_rotate_limit(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.pitch_limit"></a>

#### pitch\_limit

```python
@property
def pitch_limit() -> Vector2D
```

(Vector2D):  [Read-Write] Pitch 的限制角度

<a id="unreal.WdpCameraPresetActor.pitch_limit"></a>

#### pitch\_limit

```python
@pitch_limit.setter
def pitch_limit(value: Vector2D) -> None
```

<a id="unreal.WdpCameraPresetActor.yaw_limit"></a>

#### yaw\_limit

```python
@property
def yaw_limit() -> Vector2D
```

(Vector2D):  [Read-Write] Yaw 的限制角度

<a id="unreal.WdpCameraPresetActor.yaw_limit"></a>

#### yaw\_limit

```python
@yaw_limit.setter
def yaw_limit(value: Vector2D) -> None
```

<a id="unreal.WdpCameraPresetActor.roll_limit"></a>

#### roll\_limit

```python
@property
def roll_limit() -> Vector2D
```

(Vector2D):  [Read-Write] Roll 的限制角度

<a id="unreal.WdpCameraPresetActor.roll_limit"></a>

#### roll\_limit

```python
@roll_limit.setter
def roll_limit(value: Vector2D) -> None
```

<a id="unreal.WdpCameraPresetActor.override_zoom_limit"></a>

#### override\_zoom\_limit

```python
@property
def override_zoom_limit() -> bool
```

(bool):  [Read-Write] 是否改变缩放限制

<a id="unreal.WdpCameraPresetActor.override_zoom_limit"></a>

#### override\_zoom\_limit

```python
@override_zoom_limit.setter
def override_zoom_limit(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.min_zoom_distance"></a>

#### min\_zoom\_distance

```python
@property
def min_zoom_distance() -> float
```

(double):  [Read-Write] 最小缩放距离

<a id="unreal.WdpCameraPresetActor.min_zoom_distance"></a>

#### min\_zoom\_distance

```python
@min_zoom_distance.setter
def min_zoom_distance(value: float) -> None
```

<a id="unreal.WdpCameraPresetActor.max_zoom_distance"></a>

#### max\_zoom\_distance

```python
@property
def max_zoom_distance() -> float
```

(double):  [Read-Write] 最大缩放距离

<a id="unreal.WdpCameraPresetActor.max_zoom_distance"></a>

#### max\_zoom\_distance

```python
@max_zoom_distance.setter
def max_zoom_distance(value: float) -> None
```

<a id="unreal.WdpCameraPresetActor.min_zoom_fov"></a>

#### min\_zoom\_fov

```python
@property
def min_zoom_fov() -> float
```

(float):  [Read-Write] 最小缩放FOV

<a id="unreal.WdpCameraPresetActor.min_zoom_fov"></a>

#### min\_zoom\_fov

```python
@min_zoom_fov.setter
def min_zoom_fov(value: float) -> None
```

<a id="unreal.WdpCameraPresetActor.max_zoom_fov"></a>

#### max\_zoom\_fov

```python
@property
def max_zoom_fov() -> float
```

(float):  [Read-Write] 最大缩放FOV

<a id="unreal.WdpCameraPresetActor.max_zoom_fov"></a>

#### max\_zoom\_fov

```python
@max_zoom_fov.setter
def max_zoom_fov(value: float) -> None
```

<a id="unreal.WdpCameraPresetActor.override_collision"></a>

#### override\_collision

```python
@property
def override_collision() -> bool
```

(bool):  [Read-Write] 是否改变碰撞限制

<a id="unreal.WdpCameraPresetActor.override_collision"></a>

#### override\_collision

```python
@override_collision.setter
def override_collision(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.collision_mode"></a>

#### collision\_mode

```python
@property
def collision_mode() -> CameraCollisionMode
```

(CameraCollisionMode):  [Read-Write] 碰撞模式

<a id="unreal.WdpCameraPresetActor.collision_mode"></a>

#### collision\_mode

```python
@collision_mode.setter
def collision_mode(value: CameraCollisionMode) -> None
```

<a id="unreal.WdpCameraPresetActor.profile_name"></a>

#### profile\_name

```python
@property
def profile_name() -> CollisionProfileName
```

(CollisionProfileName):  [Read-Write] 碰撞的ProfileName

<a id="unreal.WdpCameraPresetActor.profile_name"></a>

#### profile\_name

```python
@profile_name.setter
def profile_name(value: CollisionProfileName) -> None
```

<a id="unreal.WdpCameraPresetActor.custom_points"></a>

#### custom\_points

```python
@property
def custom_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] 碰撞的边界点 如果是两个点，表示矩形的两个对角，如果是三个或以上，表示按顺序的多边形 只有2D限制//注意这里的本地空间的点，传数据时会自动转换

<a id="unreal.WdpCameraPresetActor.custom_points"></a>

#### custom\_points

```python
@custom_points.setter
def custom_points(value: Array[Vector]) -> None
```

<a id="unreal.WdpCameraPresetActor.ground_position_mode"></a>

#### ground\_position\_mode

```python
@property
def ground_position_mode() -> GroundPositionMode
```

(GroundPositionMode):  [Read-Write] 地面碰撞模式

<a id="unreal.WdpCameraPresetActor.ground_position_mode"></a>

#### ground\_position\_mode

```python
@ground_position_mode.setter
def ground_position_mode(value: GroundPositionMode) -> None
```

<a id="unreal.WdpCameraPresetActor.use_wdp_pawn_as_default"></a>

#### use\_wdp\_pawn\_as\_default

```python
@property
def use_wdp_pawn_as_default() -> bool
```

(bool):  [Read-Write] 在当前Pawn不是WdpPawn的时候是否自动切换回WdpPawn

<a id="unreal.WdpCameraPresetActor.use_wdp_pawn_as_default"></a>

#### use\_wdp\_pawn\_as\_default

```python
@use_wdp_pawn_as_default.setter
def use_wdp_pawn_as_default(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.use_possess_mode"></a>

#### use\_possess\_mode

```python
@property
def use_possess_mode() -> bool
```

(bool):  [Read-Write] 是否使用Possess模式

<a id="unreal.WdpCameraPresetActor.use_possess_mode"></a>

#### use\_possess\_mode

```python
@use_possess_mode.setter
def use_possess_mode(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.possess_pawn_ref"></a>

#### possess\_pawn\_ref

```python
@property
def possess_pawn_ref() -> Pawn
```

(Pawn):  [Read-Write] 需要Possess的Pawn的引用

<a id="unreal.WdpCameraPresetActor.possess_pawn_ref"></a>

#### possess\_pawn\_ref

```python
@possess_pawn_ref.setter
def possess_pawn_ref(value: Pawn) -> None
```

<a id="unreal.WdpCameraPresetActor.possess_use_auto_spawn"></a>

#### possess\_use\_auto\_spawn

```python
@property
def possess_use_auto_spawn() -> bool
```

(bool):  [Read-Write] 是否使用Spawn模式，如果是将在切换相机后自动创建一个Pawn

<a id="unreal.WdpCameraPresetActor.possess_use_auto_spawn"></a>

#### possess\_use\_auto\_spawn

```python
@possess_use_auto_spawn.setter
def possess_use_auto_spawn(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.spawn_pawn_class"></a>

#### spawn\_pawn\_class

```python
@property
def spawn_pawn_class() -> Class
```

(type(Class)):  [Read-Write] 需要被Spawn的Pawn的Class

<a id="unreal.WdpCameraPresetActor.spawn_pawn_class"></a>

#### spawn\_pawn\_class

```python
@spawn_pawn_class.setter
def spawn_pawn_class(value: Class) -> None
```

<a id="unreal.WdpCameraPresetActor.use_pivot_location_as_spawn_location"></a>

#### use\_pivot\_location\_as\_spawn\_location

```python
@property
def use_pivot_location_as_spawn_location() -> bool
```

(bool):  [Read-Write] 是否使用Pivot坐标Spawn，如果不是则使用相机坐标

<a id="unreal.WdpCameraPresetActor.use_pivot_location_as_spawn_location"></a>

#### use\_pivot\_location\_as\_spawn\_location

```python
@use_pivot_location_as_spawn_location.setter
def use_pivot_location_as_spawn_location(value: bool) -> None
```

<a id="unreal.WdpCameraPresetActor.set_preset_with_camera_data"></a>

#### set\_preset\_with\_camera\_data

```python
def set_preset_with_camera_data(all_camera_data: AllCameraData) -> None
```

x.set_preset_with_camera_data(all_camera_data) -> None
将外部相机参数设置到Preset里

Args:
    all_camera_data (AllCameraData):

<a id="unreal.WdpCameraPresetActor.does_match_camera"></a>

#### does\_match\_camera

```python
def does_match_camera(tag: GameplayTag, index: int) -> bool
```

x.does_match_camera(tag, index) -> bool
是否匹配参数

Args:
    tag (GameplayTag): 
    index (int32): 

Returns:
    bool:

<a id="unreal.WdpCameraPresetActor.change_camera"></a>

#### change\_camera

```python
def change_camera(settings: TravelAnimationSettings, duration: float) -> bool
```

x.change_camera(settings, duration) -> bool
调用当前的相机预设

Args:
    settings (TravelAnimationSettings): 
    duration (float): 

Returns:
    bool:

<a id="unreal.WdpCameraUtilityLibrary"></a>