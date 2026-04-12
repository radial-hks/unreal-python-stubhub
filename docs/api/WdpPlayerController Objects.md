## WdpPlayerController Objects

```python
class WdpPlayerController(PlayerController)
```

Wdp Player Controller

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpPlayerController.h

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
- ``attach_to_pawn`` (bool):  [Read-Write] If true, the controller location will match the possessed Pawn's location. If false, it will not be updated. Rotation will match ControlRotation in either case.
  Since a Controller's location is normally inaccessible, this is intended mainly for purposes of being able to attach
  an Actor that follows the possessed Pawn location, but that still has the full aim rotation (since a Pawn might
  update only some components of the rotation).
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_manage_active_camera_target`` (bool):  [Read-Write] True to allow this player controller to manage the camera target for you,
  typically by using the possessed pawn as the camera target. Set to false
  if you want to manually control the camera target.
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_touch_input_sensitivity`` (float):  [Read-Write] 如果不使用Enhach Input中的数值，而是改用鼠标或触屏在平面上的位置去计算旋转，灵敏度是多少
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``cheat_class`` (type(Class)):  [Read-Write] Class of my CheatManager.
  see: CheatManager for more information about when it will be instantiated.
- ``cheat_manager`` (CheatManager):  [Read-Write] Object that manages "cheat" commands.

  By default:
        - In Shipping configurations, the manager is always disabled because UE_WITH_CHEAT_MANAGER is 0
    - When playing in the editor, cheats are always enabled
    - In other cases, cheats are enabled by default in single player games but can be forced on with the EnableCheats console command

  This behavior can be changed either by overriding APlayerController::EnableCheats or AGameModeBase::AllowCheats.
- ``click_event_keys`` (Array[Key]):  [Read-Write] List of keys that will cause click events to be forwarded, default to left click
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``control_mode`` (ControlMode):  [Read-Write] 控制模式 鼠标 触屏 控制器
- ``current_click_trace_channel`` (CollisionChannel):  [Read-Write] Trace channel currently being used for determining what world object was clicked on.
- ``current_mouse_cursor`` (MouseCursor):  [Read-Write] Currently visible mouse cursor
- ``cursor_style`` (MouseCursorStyle):  [Read-Write] 鼠标指针的样式
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_capture_mode`` (MouseCaptureMode):  [Read-Write] 默认的CaptureMode
- ``default_click_trace_channel`` (CollisionChannel):  [Read-Write] Default trace channel used for determining what world object was clicked on.
- ``default_mouse_cursor`` (MouseCursor):  [Read-Write] Type of mouse cursor to show by default
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
- ``enable_click_events`` (bool):  [Read-Write] Whether actor/component click events should be generated.
- ``enable_motion_controls`` (bool):  [Read-Write] Whether or not to consider input from motion sources (tilt, acceleration, etc)
- ``enable_mouse_over_events`` (bool):  [Read-Write] Whether actor/component mouse over events should be generated.
- ``enable_streaming_source`` (bool):  [Read-Write] Whether the PlayerController should be used as a World Partiton streaming source.
- ``enable_touch_events`` (bool):  [Read-Write] Whether actor/component touch events should be generated.
- ``enable_touch_over_events`` (bool):  [Read-Write] Whether actor/component touch over events should be generated.
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``force_feedback_enabled`` (bool):  [Read-Write]
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hit_result_trace_distance`` (float):  [Read-Write] Distance to trace when computing click events
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_pitch_scale`` (float):  [Read-Write] Pitch input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``input_roll_scale`` (float):  [Read-Write] Roll input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``input_yaw_scale`` (float):  [Read-Write] Yaw input speed scaling
  deprecated: Use the Enhanced Input plugin Scalar Modifier instead. See UInputSettings::bEnableLegacyInputScales to enable legacy behavior
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_pointer_key_down`` (bool):  [Read-Write] Pointer 是否激活状态
- ``is_possess_blending_camera`` (bool):  [Read-Write] 是否正在Possess过度相机动画的过程
- ``is_rotate_key_down`` (bool):  [Read-Write] Rotate 是否激活状态
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``is_zoom_key_down`` (bool):  [Read-Write] Zoom 是否激活状态
- ``is_zoom_touch_down`` (bool):  [Read-Write] Zoom 是否被触屏激活中
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
- ``on_any_key_rotate_value_updated`` (OnAnyKeyRotateValueUpdated):  [Read-Write]
- ``on_begin_cursor_over`` (ActorBeginCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.
- ``on_clicked`` (ActorOnClickedSignature):  [Read-Write] Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.
- ``on_control_mode_changed`` (InputChangedNotifyEvent):  [Read-Write]
- ``on_destroyed`` (ActorDestroyedSignature):  [Read-Write] Event triggered when the actor has been explicitly destroyed.
- ``on_end_cursor_over`` (ActorEndCursorOverSignature):  [Read-Write] Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.
- ``on_end_play`` (ActorEndPlaySignature):  [Read-Write] Event triggered when the actor is being deleted or removed from a level.
- ``on_input_touch_begin`` (ActorOnInputTouchBeginSignature):  [Read-Write] Called when a touch input is received over this actor when touch events are enabled in the player controller.
- ``on_input_touch_end`` (ActorOnInputTouchEndSignature):  [Read-Write] Called when a touch input is received over this component when touch events are enabled in the player controller.
- ``on_input_touch_enter`` (ActorBeginTouchOverSignature):  [Read-Write] Called when a finger is moved over this actor when touch over events are enabled in the player controller.
- ``on_input_touch_leave`` (ActorEndTouchOverSignature):  [Read-Write] Called when a finger is moved off this actor when touch over events are enabled in the player controller.
- ``on_instigated_any_damage`` (InstigatedAnyDamageSignature):  [Read-Write] Called when the controller has instigated damage in any way
- ``on_move_key_triggered`` (OnMoveKeyTriggered):  [Read-Write]
- ``on_pointer_key_double_clicked`` (OnPointerKeyDoubleClicked):  [Read-Write]
- ``on_pointer_key_pressed`` (OnPointerKeyPressed):  [Read-Write]
- ``on_pointer_key_released`` (OnPointerKeyReleased):  [Read-Write]
- ``on_pointer_key_rotate_value_updated`` (OnPointerKeyRotateValueUpdated):  [Read-Write]
- ``on_pointer_key_triggered`` (OnPointerKeyTriggered):  [Read-Write]
- ``on_possessed_pawn_changed`` (OnPossessedPawnChanged):  [Read-Write] Called on both authorities and clients when the possessed pawn changes (either OldPawn or NewPawn might be nullptr)
- ``on_released`` (ActorOnReleasedSignature):  [Read-Write] Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.
- ``on_rotate_key_pressed`` (OnRotateKeyPressed):  [Read-Write]
- ``on_rotate_key_released`` (OnRotateKeyReleased):  [Read-Write]
- ``on_rotate_key_triggered`` (OnRotateKeyTriggered):  [Read-Write]
- ``on_rotate_key_value_updated`` (OnRotateKeyValueUpdated):  [Read-Write]
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``on_zoom_key_pressed`` (OnZoomKeyPressed):  [Read-Write]
- ``on_zoom_key_released`` (OnZoomKeyReleased):  [Read-Write]
- ``on_zoom_key_triggered`` (OnZoomKeyTriggered):  [Read-Write]
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``override_player_input_class`` (type(Class)):  [Read-Write] If set, then this UPlayerInput class will be used instead of the Input Settings' DefaultPlayerInputClass
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_camera_manager`` (PlayerCameraManager):  [Read-Write] Camera manager associated with this Player Controller.
- ``player_camera_manager_class`` (type(Class)):  [Read-Write] PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used
- ``player_is_waiting`` (bool):  [Read-Only] True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state.
- ``player_state`` (PlayerState):  [Read-Write] PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs).
- ``pointer_action`` (InputAction):  [Read-Write] Left Click Action 左键或触屏点击(Pointer)事件
- ``pointer_key_screen_position`` (Vector2D):  [Read-Write] **************** 输入操作相关变量 *****************************************************//Pointer 的屏幕坐标
- ``possess_pawn_settings`` (PossessPawnSettings):  [Read-Write] Possess Pawn 的设置参数
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
- ``rotate_action`` (InputAction):  [Read-Write] Rotate Input Action 旋转事件 右键或滚轮
- ``rotate_key_screen_position`` (Vector2D):  [Read-Write] Rotate 的屏幕坐标
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``screen_mapping_context`` (InputMappingContext):  [Read-Write] MappingContext 当前的按键输入Mapping
- ``should_perform_full_tick_when_paused`` (bool):  [Read-Write] Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick.
- ``show_mouse_cursor`` (bool):  [Read-Write] Whether the mouse cursor should be displayed.
- ``smooth_target_view_rotation_speed`` (float):  [Read-Write] Interp speed for blending remote view rotation for smoother client updates
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``streaming_source_debug_color`` (Color):  [Read-Write] Color used for debugging.
- ``streaming_source_priority`` (StreamingSourcePriority):  [Read-Write] PlayerController streaming source priority.
- ``streaming_source_shapes`` (Array[StreamingSourceShape]):  [Read-Write] Optional aggregated shape list used to build a custom shape for the streaming source. When empty, fallbacks sphere shape with a radius equal to grid's loading range.
- ``streaming_source_should_activate`` (bool):  [Read-Write] Whether the PlayerController streaming source should activate cells after loading.
- ``streaming_source_should_block_on_slow_streaming`` (bool):  [Read-Write] Whether the PlayerController streaming source should block on slow streaming.
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
- ``wdp_base_pawn`` (WdpBasePawn):  [Read-Write] 用于管理多个pawn的情况，WdpPawn固定在场景中存在一个
  可以操作其他Pawn但是借用WdpPawn的相机，如果没有BPI也可以独立工作
- ``world_origin_anchor`` (WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor
- ``zoom_action`` (InputAction):  [Read-Write] Zoom Input Action 鼠标缩放
- ``zoom_key_screen_position`` (Vector2D):  [Read-Write] Zoom 的屏幕坐标

<a id="unreal.WdpPlayerController.world_origin_anchor"></a>

#### world\_origin\_anchor

```python
@property
def world_origin_anchor() -> WorldOriginAnchor
```

(WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor

<a id="unreal.WdpPlayerController.screen_mapping_context"></a>

#### screen\_mapping\_context

```python
@property
def screen_mapping_context() -> InputMappingContext
```

(InputMappingContext):  [Read-Only] MappingContext 当前的按键输入Mapping

<a id="unreal.WdpPlayerController.pointer_action"></a>

#### pointer\_action

```python
@property
def pointer_action() -> InputAction
```

(InputAction):  [Read-Only] Left Click Action 左键或触屏点击(Pointer)事件

<a id="unreal.WdpPlayerController.rotate_action"></a>

#### rotate\_action

```python
@property
def rotate_action() -> InputAction
```

(InputAction):  [Read-Only] Rotate Input Action 旋转事件 右键或滚轮

<a id="unreal.WdpPlayerController.zoom_action"></a>

#### zoom\_action

```python
@property
def zoom_action() -> InputAction
```

(InputAction):  [Read-Only] Zoom Input Action 鼠标缩放

<a id="unreal.WdpPlayerController.on_pointer_key_pressed"></a>

#### on\_pointer\_key\_pressed

```python
@property
def on_pointer_key_pressed() -> OnPointerKeyPressed
```

(OnPointerKeyPressed):  [Read-Write]

<a id="unreal.WdpPlayerController.on_pointer_key_pressed"></a>

#### on\_pointer\_key\_pressed

```python
@on_pointer_key_pressed.setter
def on_pointer_key_pressed(value: OnPointerKeyPressed) -> None
```

<a id="unreal.WdpPlayerController.on_pointer_key_triggered"></a>

#### on\_pointer\_key\_triggered

```python
@property
def on_pointer_key_triggered() -> OnPointerKeyTriggered
```

(OnPointerKeyTriggered):  [Read-Write]

<a id="unreal.WdpPlayerController.on_pointer_key_triggered"></a>

#### on\_pointer\_key\_triggered

```python
@on_pointer_key_triggered.setter
def on_pointer_key_triggered(value: OnPointerKeyTriggered) -> None
```

<a id="unreal.WdpPlayerController.on_pointer_key_released"></a>

#### on\_pointer\_key\_released

```python
@property
def on_pointer_key_released() -> OnPointerKeyReleased
```

(OnPointerKeyReleased):  [Read-Write]

<a id="unreal.WdpPlayerController.on_pointer_key_released"></a>

#### on\_pointer\_key\_released

```python
@on_pointer_key_released.setter
def on_pointer_key_released(value: OnPointerKeyReleased) -> None
```

<a id="unreal.WdpPlayerController.on_pointer_key_double_clicked"></a>

#### on\_pointer\_key\_double\_clicked

```python
@property
def on_pointer_key_double_clicked() -> OnPointerKeyDoubleClicked
```

(OnPointerKeyDoubleClicked):  [Read-Write]

<a id="unreal.WdpPlayerController.on_pointer_key_double_clicked"></a>

#### on\_pointer\_key\_double\_clicked

```python
@on_pointer_key_double_clicked.setter
def on_pointer_key_double_clicked(value: OnPointerKeyDoubleClicked) -> None
```

<a id="unreal.WdpPlayerController.on_pointer_key_rotate_value_updated"></a>

#### on\_pointer\_key\_rotate\_value\_updated

```python
@property
def on_pointer_key_rotate_value_updated() -> OnPointerKeyRotateValueUpdated
```

(OnPointerKeyRotateValueUpdated):  [Read-Write]

<a id="unreal.WdpPlayerController.on_pointer_key_rotate_value_updated"></a>

#### on\_pointer\_key\_rotate\_value\_updated

```python
@on_pointer_key_rotate_value_updated.setter
def on_pointer_key_rotate_value_updated(
        value: OnPointerKeyRotateValueUpdated) -> None
```

<a id="unreal.WdpPlayerController.on_rotate_key_pressed"></a>

#### on\_rotate\_key\_pressed

```python
@property
def on_rotate_key_pressed() -> OnRotateKeyPressed
```

(OnRotateKeyPressed):  [Read-Write]

<a id="unreal.WdpPlayerController.on_rotate_key_pressed"></a>

#### on\_rotate\_key\_pressed

```python
@on_rotate_key_pressed.setter
def on_rotate_key_pressed(value: OnRotateKeyPressed) -> None
```

<a id="unreal.WdpPlayerController.on_rotate_key_triggered"></a>

#### on\_rotate\_key\_triggered

```python
@property
def on_rotate_key_triggered() -> OnRotateKeyTriggered
```

(OnRotateKeyTriggered):  [Read-Write]

<a id="unreal.WdpPlayerController.on_rotate_key_triggered"></a>

#### on\_rotate\_key\_triggered

```python
@on_rotate_key_triggered.setter
def on_rotate_key_triggered(value: OnRotateKeyTriggered) -> None
```

<a id="unreal.WdpPlayerController.on_rotate_key_released"></a>

#### on\_rotate\_key\_released

```python
@property
def on_rotate_key_released() -> OnRotateKeyReleased
```

(OnRotateKeyReleased):  [Read-Write]

<a id="unreal.WdpPlayerController.on_rotate_key_released"></a>

#### on\_rotate\_key\_released

```python
@on_rotate_key_released.setter
def on_rotate_key_released(value: OnRotateKeyReleased) -> None
```

<a id="unreal.WdpPlayerController.on_rotate_key_value_updated"></a>

#### on\_rotate\_key\_value\_updated

```python
@property
def on_rotate_key_value_updated() -> OnRotateKeyValueUpdated
```

(OnRotateKeyValueUpdated):  [Read-Write]

<a id="unreal.WdpPlayerController.on_rotate_key_value_updated"></a>

#### on\_rotate\_key\_value\_updated

```python
@on_rotate_key_value_updated.setter
def on_rotate_key_value_updated(value: OnRotateKeyValueUpdated) -> None
```

<a id="unreal.WdpPlayerController.on_any_key_rotate_value_updated"></a>

#### on\_any\_key\_rotate\_value\_updated

```python
@property
def on_any_key_rotate_value_updated() -> OnAnyKeyRotateValueUpdated
```

(OnAnyKeyRotateValueUpdated):  [Read-Write]

<a id="unreal.WdpPlayerController.on_any_key_rotate_value_updated"></a>

#### on\_any\_key\_rotate\_value\_updated

```python
@on_any_key_rotate_value_updated.setter
def on_any_key_rotate_value_updated(value: OnAnyKeyRotateValueUpdated) -> None
```

<a id="unreal.WdpPlayerController.on_zoom_key_pressed"></a>

#### on\_zoom\_key\_pressed

```python
@property
def on_zoom_key_pressed() -> OnZoomKeyPressed
```

(OnZoomKeyPressed):  [Read-Write]

<a id="unreal.WdpPlayerController.on_zoom_key_pressed"></a>

#### on\_zoom\_key\_pressed

```python
@on_zoom_key_pressed.setter
def on_zoom_key_pressed(value: OnZoomKeyPressed) -> None
```

<a id="unreal.WdpPlayerController.on_zoom_key_triggered"></a>

#### on\_zoom\_key\_triggered

```python
@property
def on_zoom_key_triggered() -> OnZoomKeyTriggered
```

(OnZoomKeyTriggered):  [Read-Write]

<a id="unreal.WdpPlayerController.on_zoom_key_triggered"></a>

#### on\_zoom\_key\_triggered

```python
@on_zoom_key_triggered.setter
def on_zoom_key_triggered(value: OnZoomKeyTriggered) -> None
```

<a id="unreal.WdpPlayerController.on_zoom_key_released"></a>

#### on\_zoom\_key\_released

```python
@property
def on_zoom_key_released() -> OnZoomKeyReleased
```

(OnZoomKeyReleased):  [Read-Write]

<a id="unreal.WdpPlayerController.on_zoom_key_released"></a>

#### on\_zoom\_key\_released

```python
@on_zoom_key_released.setter
def on_zoom_key_released(value: OnZoomKeyReleased) -> None
```

<a id="unreal.WdpPlayerController.on_move_key_triggered"></a>

#### on\_move\_key\_triggered

```python
@property
def on_move_key_triggered() -> OnMoveKeyTriggered
```

(OnMoveKeyTriggered):  [Read-Write]

<a id="unreal.WdpPlayerController.on_move_key_triggered"></a>

#### on\_move\_key\_triggered

```python
@on_move_key_triggered.setter
def on_move_key_triggered(value: OnMoveKeyTriggered) -> None
```

<a id="unreal.WdpPlayerController.pointer_key_screen_position"></a>

#### pointer\_key\_screen\_position

```python
@property
def pointer_key_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] **************** 输入操作相关变量 *****************************************************//Pointer 的屏幕坐标

<a id="unreal.WdpPlayerController.pointer_key_screen_position"></a>

#### pointer\_key\_screen\_position

```python
@pointer_key_screen_position.setter
def pointer_key_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpPlayerController.rotate_key_screen_position"></a>

#### rotate\_key\_screen\_position

```python
@property
def rotate_key_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] Rotate 的屏幕坐标

<a id="unreal.WdpPlayerController.rotate_key_screen_position"></a>

#### rotate\_key\_screen\_position

```python
@rotate_key_screen_position.setter
def rotate_key_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpPlayerController.zoom_key_screen_position"></a>

#### zoom\_key\_screen\_position

```python
@property
def zoom_key_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] Zoom 的屏幕坐标

<a id="unreal.WdpPlayerController.zoom_key_screen_position"></a>

#### zoom\_key\_screen\_position

```python
@zoom_key_screen_position.setter
def zoom_key_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpPlayerController.is_pointer_key_down"></a>

#### is\_pointer\_key\_down

```python
@property
def is_pointer_key_down() -> bool
```

(bool):  [Read-Write] Pointer 是否激活状态

<a id="unreal.WdpPlayerController.is_pointer_key_down"></a>

#### is\_pointer\_key\_down

```python
@is_pointer_key_down.setter
def is_pointer_key_down(value: bool) -> None
```

<a id="unreal.WdpPlayerController.is_rotate_key_down"></a>

#### is\_rotate\_key\_down

```python
@property
def is_rotate_key_down() -> bool
```

(bool):  [Read-Write] Rotate 是否激活状态

<a id="unreal.WdpPlayerController.is_rotate_key_down"></a>

#### is\_rotate\_key\_down

```python
@is_rotate_key_down.setter
def is_rotate_key_down(value: bool) -> None
```

<a id="unreal.WdpPlayerController.is_zoom_key_down"></a>

#### is\_zoom\_key\_down

```python
@property
def is_zoom_key_down() -> bool
```

(bool):  [Read-Write] Zoom 是否激活状态

<a id="unreal.WdpPlayerController.is_zoom_key_down"></a>

#### is\_zoom\_key\_down

```python
@is_zoom_key_down.setter
def is_zoom_key_down(value: bool) -> None
```

<a id="unreal.WdpPlayerController.is_zoom_touch_down"></a>

#### is\_zoom\_touch\_down

```python
@property
def is_zoom_touch_down() -> bool
```

(bool):  [Read-Write] Zoom 是否被触屏激活中

<a id="unreal.WdpPlayerController.is_zoom_touch_down"></a>

#### is\_zoom\_touch\_down

```python
@is_zoom_touch_down.setter
def is_zoom_touch_down(value: bool) -> None
```

<a id="unreal.WdpPlayerController.control_mode"></a>

#### control\_mode

```python
@property
def control_mode() -> ControlMode
```

(ControlMode):  [Read-Write] 控制模式 鼠标 触屏 控制器

<a id="unreal.WdpPlayerController.control_mode"></a>

#### control\_mode

```python
@control_mode.setter
def control_mode(value: ControlMode) -> None
```

<a id="unreal.WdpPlayerController.on_control_mode_changed"></a>

#### on\_control\_mode\_changed

```python
@property
def on_control_mode_changed() -> InputChangedNotifyEvent
```

(InputChangedNotifyEvent):  [Read-Write]

<a id="unreal.WdpPlayerController.on_control_mode_changed"></a>

#### on\_control\_mode\_changed

```python
@on_control_mode_changed.setter
def on_control_mode_changed(value: InputChangedNotifyEvent) -> None
```

<a id="unreal.WdpPlayerController.cursor_style"></a>

#### cursor\_style

```python
@property
def cursor_style() -> MouseCursorStyle
```

(MouseCursorStyle):  [Read-Write] 鼠标指针的样式

<a id="unreal.WdpPlayerController.cursor_style"></a>

#### cursor\_style

```python
@cursor_style.setter
def cursor_style(value: MouseCursorStyle) -> None
```

<a id="unreal.WdpPlayerController.default_capture_mode"></a>

#### default\_capture\_mode

```python
@property
def default_capture_mode() -> MouseCaptureMode
```

(MouseCaptureMode):  [Read-Write] 默认的CaptureMode

<a id="unreal.WdpPlayerController.default_capture_mode"></a>

#### default\_capture\_mode

```python
@default_capture_mode.setter
def default_capture_mode(value: MouseCaptureMode) -> None
```

<a id="unreal.WdpPlayerController.wdp_base_pawn"></a>

#### wdp\_base\_pawn

```python
@property
def wdp_base_pawn() -> WdpBasePawn
```

(WdpBasePawn):  [Read-Write] 用于管理多个pawn的情况，WdpPawn固定在场景中存在一个
可以操作其他Pawn但是借用WdpPawn的相机，如果没有BPI也可以独立工作

<a id="unreal.WdpPlayerController.wdp_base_pawn"></a>

#### wdp\_base\_pawn

```python
@wdp_base_pawn.setter
def wdp_base_pawn(value: WdpBasePawn) -> None
```

<a id="unreal.WdpPlayerController.is_possess_blending_camera"></a>

#### is\_possess\_blending\_camera

```python
@property
def is_possess_blending_camera() -> bool
```

(bool):  [Read-Write] 是否正在Possess过度相机动画的过程

<a id="unreal.WdpPlayerController.is_possess_blending_camera"></a>

#### is\_possess\_blending\_camera

```python
@is_possess_blending_camera.setter
def is_possess_blending_camera(value: bool) -> None
```

<a id="unreal.WdpPlayerController.possess_pawn_settings"></a>

#### possess\_pawn\_settings

```python
@property
def possess_pawn_settings() -> PossessPawnSettings
```

(PossessPawnSettings):  [Read-Write] Possess Pawn 的设置参数

<a id="unreal.WdpPlayerController.possess_pawn_settings"></a>

#### possess\_pawn\_settings

```python
@possess_pawn_settings.setter
def possess_pawn_settings(value: PossessPawnSettings) -> None
```

<a id="unreal.WdpPlayerController.camera_touch_input_sensitivity"></a>

#### camera\_touch\_input\_sensitivity

```python
@property
def camera_touch_input_sensitivity() -> float
```

(float):  [Read-Write] 如果不使用Enhach Input中的数值，而是改用鼠标或触屏在平面上的位置去计算旋转，灵敏度是多少

<a id="unreal.WdpPlayerController.camera_touch_input_sensitivity"></a>

#### camera\_touch\_input\_sensitivity

```python
@camera_touch_input_sensitivity.setter
def camera_touch_input_sensitivity(value: float) -> None
```

<a id="unreal.WdpPlayerController.update_possess_pawn_settings"></a>

#### update\_possess\_pawn\_settings

```python
def update_possess_pawn_settings(settings: PossessPawnSettings) -> None
```

x.update_possess_pawn_settings(settings) -> None
更新Possess Pawn 的设置

Args:
    settings (PossessPawnSettings):

<a id="unreal.WdpPlayerController.un_possess_and_return"></a>

#### un\_possess\_and\_return

```python
def un_possess_and_return(duration: float = 0.000000) -> None
```

x.un_possess_and_return(duration=0.000000) -> None
结束possess，回到WdpPawn

Args:
    duration (float):

<a id="unreal.WdpPlayerController.switch_control_mode_by_key"></a>

#### switch\_control\_mode\_by\_key

```python
def switch_control_mode_by_key(key: Key) -> ControlMode
```

x.switch_control_mode_by_key(key) -> ControlMode
根据按键判断ControlMode

Args:
    key (Key): 

Returns:
    ControlMode:

<a id="unreal.WdpPlayerController.switch_control_mode"></a>

#### switch\_control\_mode

```python
def switch_control_mode(new_control_mode: ControlMode) -> None
```

x.switch_control_mode(new_control_mode) -> None
切换ControlMode

Args:
    new_control_mode (ControlMode):

<a id="unreal.WdpPlayerController.remote_zoom_value_update"></a>

#### remote\_zoom\_value\_update

```python
def remote_zoom_value_update(value: float) -> None
```

x.remote_zoom_value_update(value) -> None
API 缩放更新接口 Value > 0 = ZoomOut, < 0 = ZoomIn

Args:
    value (float):

<a id="unreal.WdpPlayerController.remote_zoom_key_released"></a>

#### remote\_zoom\_key\_released

```python
def remote_zoom_key_released() -> None
```

x.remote_zoom_key_released() -> None
API 缩放结束

<a id="unreal.WdpPlayerController.remote_zoom_key_pressed"></a>

#### remote\_zoom\_key\_pressed

```python
def remote_zoom_key_pressed() -> None
```

x.remote_zoom_key_pressed() -> None
API 缩放开始 自动输入屏幕中心点的坐标

<a id="unreal.WdpPlayerController.remote_rotate_key_value_update"></a>

#### remote\_rotate\_key\_value\_update

```python
def remote_rotate_key_value_update(value: Vector2D) -> None
```

x.remote_rotate_key_value_update(value) -> None
API 旋转输入值更新 X=Yaw Y=Pitch

Args:
    value (Vector2D):

<a id="unreal.WdpPlayerController.remote_rotate_key_released"></a>

#### remote\_rotate\_key\_released

```python
def remote_rotate_key_released() -> None
```

x.remote_rotate_key_released() -> None
API 旋转输入结束

<a id="unreal.WdpPlayerController.remote_rotate_key_pressed"></a>

#### remote\_rotate\_key\_pressed

```python
def remote_rotate_key_pressed() -> None
```

x.remote_rotate_key_pressed() -> None
API 旋转输入开始 自动输入屏幕中心点坐标

<a id="unreal.WdpPlayerController.remote_move_key_triggered"></a>

#### remote\_move\_key\_triggered

```python
def remote_move_key_triggered(value: Vector) -> None
```

x.remote_move_key_triggered(value) -> None
API 移动操作输入接口 X = Forward Y = Right Z = Up(注意XY方向和WdpPawn的2D移动不同)

Args:
    value (Vector):

<a id="unreal.WdpPlayerController.possess_to_new_pawn"></a>

#### possess\_to\_new\_pawn

```python
def possess_to_new_pawn(new_pawn: Pawn, duration: float = 0.000000) -> None
```

x.possess_to_new_pawn(new_pawn, duration=0.000000) -> None
切换到新的pawn，AutoFollow：WdpPawn是否跟着新pawn运动

Args:
    new_pawn (Pawn): 
    duration (float):

<a id="unreal.WdpPlayerController.init_world_origin_anchor"></a>

#### init\_world\_origin\_anchor

```python
def init_world_origin_anchor() -> None
```

x.init_world_origin_anchor() -> None
查找世界坐标锚点，用于支持球面操作

<a id="unreal.WdpPlayerController.init_input_mode"></a>

#### init\_input\_mode

```python
def init_input_mode() -> None
```

x.init_input_mode() -> None
初始化输入模式 显示鼠标

<a id="unreal.WdpPlayerController.init_input_mapping"></a>

#### init\_input\_mapping

```python
def init_input_mapping() -> None
```

x.init_input_mapping() -> None
初始化输入Mapping

<a id="unreal.WdpPlayerController.get_wdp_base_pawn"></a>

#### get\_wdp\_base\_pawn

```python
def get_wdp_base_pawn() -> WdpBasePawn
```

x.get_wdp_base_pawn() -> WdpBasePawn
获取WdpPawn的引用

Returns:
    WdpBasePawn:

<a id="unreal.WdpPlayerController.get_screen_center_position"></a>

#### get\_screen\_center\_position

```python
def get_screen_center_position() -> Vector2D
```

x.get_screen_center_position() -> Vector2D
获取屏幕中心的屏幕坐标

Returns:
    Vector2D:

<a id="unreal.WdpPlayerController.get_pointer_screen_position_dpi"></a>

#### get\_pointer\_screen\_position\_dpi

```python
def get_pointer_screen_position_dpi() -> Optional[Vector2D]
```

x.get_pointer_screen_position_dpi() -> Vector2D or None
根据当前的Input Mode 获取指针的DPI修正后的位置

Returns:
    Vector2D or None: 

    screen_position_dpi (Vector2D):

<a id="unreal.WdpPlayerController.get_pointer_screen_position"></a>

#### get\_pointer\_screen\_position

```python
def get_pointer_screen_position() -> Optional[Vector2D]
```

x.get_pointer_screen_position() -> Vector2D or None
根据当前的Input Mode 获取指针的原始位置

Returns:
    Vector2D or None: 

    screen_position_no_dpi (Vector2D):

<a id="unreal.WdpPlayerController.get_default_touch_index"></a>

#### get\_default\_touch\_index

```python
def get_default_touch_index() -> TouchIndex
```

x.get_default_touch_index() -> TouchIndex
默认的TouchIndex 可能是1或者2，从TouchComponent中获取

Returns:
    TouchIndex:

<a id="unreal.WdpPlayerController.calc_rotate_value_by_screen_pos"></a>

#### calc\_rotate\_value\_by\_screen\_pos

```python
def calc_rotate_value_by_screen_pos(current_pos: Vector2D,
                                    last_pos: Vector2D) -> Vector2D
```

x.calc_rotate_value_by_screen_pos(current_pos, last_pos) -> Vector2D
根据屏幕坐标插值计算旋转值 X=Yaw Y=Pitch

Args:
    current_pos (Vector2D): 
    last_pos (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.WdpPlayerController.auto_fix_capture_mode"></a>

#### auto\_fix\_capture\_mode

```python
def auto_fix_capture_mode() -> None
```

x.auto_fix_capture_mode() -> None
自动修复CaptureMode被引擎更改的问题

<a id="unreal.WdpSpringArmComponent"></a>