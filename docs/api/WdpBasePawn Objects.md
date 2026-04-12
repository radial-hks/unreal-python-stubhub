## WdpBasePawn Objects

```python
class WdpBasePawn(Pawn)
```

Wdp Base Pawn

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpBasePawn.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``ai_controller_class`` (type(Class)):  [Read-Write] Default class to use when pawn is controlled by AI.
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``anim_start_camera_data`` (CoreCameraData):  [Read-Write] 动画过度用，记录动画开始时的相机数据和目标要达到的相机数据
- ``anim_target_camera_data`` (CoreCameraData):  [Read-Write]
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_camera_self_rotation_settings`` (AutoSelfRotationSettings):  [Read-Write] 相机自身旋转的速度，单位度每秒，X为Pitch方向的旋转，Y为Yaw方向的旋转，正负决定方向
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_follow_when_not_being_view_target`` (bool):  [Read-Write] 是否在View Target不是自身的时候将镜头与当前Controller的View Target 同步
- ``auto_follow_when_un_possessed`` (bool):  [Read-Write] 当pawn不被控制时是否自动跟随CameraManger移动
- ``auto_movement_settings`` (AutoMovementSettings):  [Read-Write] 自动位移的速度 单位：m/s
- ``auto_possess_ai`` (AutoPossessAI):  [Read-Write] Determines when the Pawn creates and is possessed by an AI Controller (on level start, when spawned, etc).
  Only possible if AIControllerClassRef is set, and ignored if AutoPossessPlayer is enabled.
  see: AutoPossessPlayer
- ``auto_possess_player`` (AutoReceiveInput):  [Read-Write] Determines which PlayerController, if any, should automatically possess the pawn when the level starts or when the pawn is spawned.
  see: AutoPossessAI
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``auto_rotate_direction`` (int32):  [Read-Write] 自动旋转的方向，自动计算，只能等于-1或1，1为顺时针，-1为逆时针
- ``auto_rotation_duration_range`` (Vector2D):  [Read-Write] 通过Travel产生的自动旋转动画的速度范围，X为最快速度，Y为最慢速度
- ``auto_rotation_settings`` (AutoRotationSettings):  [Read-Write] 自动旋转的配置参数
- ``auto_rotation_start_min_threshold`` (float):  [Read-Write] 开始自动旋转的最小Yaw角度值，当动画开始时，只有超过这角度的变化才会自动开启旋转
- ``auto_travel_duration_range`` (Vector2D):  [Read-Write] 自动计算时长的时间范围限制，避免计算出的时间过长或过短
- ``base_eye_height`` (float):  [Read-Write] Base eye height above collision center.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``boost_movement_scale`` (float):  [Read-Write] 用于进阶按键移动速度倍率（如按下shift时的速度倍速）
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``camera_additional_rotate_scale`` (float):  [Read-Write] 相机旋转速度，在不修改用户配置和输入配置的情况下再进一步独立调整相机的旋转速度//相机最终的旋转速度为Input中的Scale * 用户设置的Scale * CameraAdditionalRotateScale
- ``camera_around_pivot_remain_rotation`` (Rotator):  [Read-Write] 缓动用，绕点旋转剩余没完成的角度 roll 无效
- ``camera_follow_actor_remain_location`` (Vector):  [Read-Write] 缓动用，用于在FollowActor时制造缓动跟踪效果
- ``camera_free_movement_remain_location`` (Vector):  [Read-Write] 相机自由运动的目标位置，不受球面运动影响的缓动距离，主要用于动画
- ``camera_height_movement_remain_distance`` (double):  [Read-Write] 缓动用，相机高度变化的剩余变化值，相机自身位置单纯的Z变化
- ``camera_height_to_virtual_plane`` (double):  [Read-Write] 相机距离虚拟平面的高度差
- ``camera_roll`` (double):  [Read-Write] 当前相机的Roll 单独设置
- ``camera_root`` (SceneComponent):  [Read-Only] 相机Root
- ``camera_rotate_mode`` (CameraRotateMode):  [Read-Write] 旋转的方式
- ``camera_self_remain_rotation`` (Rotator):  [Read-Write] 缓动用，相机自身旋转的剩余角度
- ``camera_surface_movement_remain_location`` (Vector):  [Read-Write] 表面运动缓动变量，指以相机自身为中心的平面上运动的方向，用于球面运动等
- ``camera_touch_input_sensitivity`` (float):  [Read-Write] 如果不使用Enhach Input中的数值，而是改用鼠标或触屏在平面上的位置去计算旋转，灵敏度是多少
- ``camera_travel_base_curve`` (CurveFloat):  [Read-Write] 相机动画单位圆弧曲线
- ``camera_travel_curve_sample_count`` (int32):  [Read-Write] 相机动画曲线的分段数量
- ``camera_travel_max_height_difference_scale`` (float):  [Read-Write] 相机Travel时如果有高度差，最大应用曲线和距离的倍数
- ``camera_zoom_remain_distance`` (double):  [Read-Write] /缓动用，缩放操作剩余的相机缩放
- ``can_affect_navigation_generation`` (bool):  [Read-Write] If set to false (default) given pawn instance will never affect navigation generation (but components could).
  Setting it to true will result in using regular AActor's navigation relevancy
  calculation to check if this pawn instance should affect navigation generation.
  note: Use SetCanAffectNavigationGeneration() to change this value at runtime.
  note: Modifying this value at runtime will result in any navigation change only if runtime navigation generation is enabled.
  note: Override UpdateNavigationRelevance() to propagate the flag to the desired components.
  see: SetCanAffectNavigationGeneration(), UpdateNavigationRelevance()
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``click_begin_camera_location`` (Vector):  [Read-Write] 左键(Pointer)点击开始时自身的世界坐标
- ``click_begin_pointer_location`` (Vector):  [Read-Write] 左键(Pointer)点击开始时的鼠标位置世界坐标
- ``click_begin_screen_position`` (Vector2D):  [Read-Write] 左键点击开始时的屏幕坐标
- ``click_pointer_current_screen_position`` (Vector2D):  [Read-Write] 当前的Pointer坐标
- ``click_pointer_last_screen_position`` (Vector2D):  [Read-Write] 上一帧左键移动(Pointer)的屏幕坐标位置
- ``click_pointer_screen_delta_position`` (Vector2D):  [Read-Write] 左键点击(Pointer)时的每帧移动delta距离
- ``collision_ignore_actors`` (Array[Actor]):  [Read-Write] 要忽略的碰撞对象，影响包括射线检测和碰撞检测
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``current_camera_data`` (AllCameraData):  [Read-Write] 完整的相机数据结构体 包含缩放 角度限制 碰撞设置等，都在这里扩展
- ``current_camera_fov`` (float):  [Read-Write] 当前的FOV
- ``custom_time_dilation`` (float):  [Read-Write] Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick.
- ``data_layer_assets`` (Array[DataLayerAsset]):  [Read-Write] There is currently an issue where if we allow property override of DataLayerAssets and it contains Private datalayers
  then it will always serialize a diff since those are outered to the instanced level and will get remapped differently between the Override instance and Archetype instance we are comparing against
- ``data_layers`` (Array[ActorDataLayer]):  [Read-Only] DataLayers the actor belongs to.
- ``default_mapping_context`` (InputMappingContext):  [Read-Write] MappingContext 当前的按键输入Mapping
- ``default_trace_channel`` (TraceTypeQuery):  [Read-Write] 默认的点击操作检测通道
- ``default_update_overlaps_method_during_level_streaming`` (ActorUpdateOverlapsMethod):  [Read-Only] Default value taken from config file for this class when 'UseConfigDefault' is chosen for
  'UpdateOverlapsMethodDuringLevelStreaming'. This allows a default to be chosen per class in the matching config.
  For example, for Actor it could be specified in DefaultEngine.ini as:

  [/Script/Engine.Actor]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = OnlyUpdateMovable

  Another subclass could set their default to something different, such as:

  [/Script/Engine.BlockingVolume]
  DefaultUpdateOverlapsMethodDuringLevelStreaming = NeverUpdate
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``default_world_plane_height`` (double):  [Read-Write] 当射线检测失败时，点击操作使用的默认的世界位置水平面高度。只要点击成功过一次就会使用LastWorldHeight
- ``desired_camera_fov`` (float):  [Read-Write] 目标相机的FOV
- ``desired_camera_rotation`` (Rotator):  [Read-Write] 目标的相机旋转位置
- ``distance_to_move_angle_curve`` (CurveFloat):  [Read-Write] 相机动画距离对应自动曲线弧度的曲线
- ``distance_zoom_speed`` (float):  [Read-Write] 距离缩放的速度值
- ``double_click_zoom_scale`` (float):  [Read-Write] 双击移动时缩放的前进倍数
- ``drag_last_screen_position`` (Vector2D):  [Read-Write] 上一帧拖动时的屏幕坐标
- ``drag_start_screen_position`` (Vector2D):  [Read-Write] 拖动开始时的屏幕坐标
- ``drag_threshold_pitch_angle`` (float):  [Read-Write] 拖动角度的限制，当鼠标射线角度小于这个角度时停止拖动
- ``draw_debug_shapes`` (bool):  [Read-Write] 是否绘制点位和Lag的debug图案
- ``e_animation_blend_features`` (int32):  [Read-Write] 启用的动画过度功能
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_auto_rotation_after_travel`` (bool):  [Read-Write] 当Travel动画结束后是否自动开始相机旋转
- ``enable_camera_lag`` (bool):  [Read-Write] 是否启用相机lag
- ``enable_input_when_not_being_view_target`` (bool):  [Read-Write] 在自身不是View Target 的情况下是否允许输入操作
- ``enable_rotation_lag`` (bool):  [Read-Write] 是否启用旋转lag
- ``enable_user_input`` (bool):  [Read-Write] 全局启用禁用用户输入操作
- ``enabled_features`` (int32):  [Read-Write] 启用的功能，二进制bitmask//      1按键平面移动
  //     2按键上下移动
  //     3鼠标拖动移动
  //     4旋转镜头
  //     5滚轮缩放
  //     6地形高度自适应(TODO)
  //     7追踪Actor
  //     8自动移动
  //     9自动绕点旋转
  //     10相机自身旋转
  //     11双击操作
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``final_camera_data`` (AllCameraData):  [Read-Write] 最终Apply的动画数据，有需求时先对这个数据做修改，再传给Apply函数
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``follow_actor_lag_speed`` (float):  [Read-Write] FollowActor 的缓动速度*/
- ``following_actor`` (Actor):  [Read-Write] 被跟踪的对象Actor
- ``following_actor_last_location`` (Vector):  [Read-Write] 上一帧Follow对象的位置
- ``following_mode`` (FollowingMode):  [Read-Write] 跟踪的处理模式
- ``following_time`` (float):  [Read-Write] 跟踪持续的时长
- ``fov_lag_speed`` (float):  [Read-Write] FOV变化的缓动速度
- ``fov_zoom_speed`` (float):  [Read-Write] FOV缩放的速度值
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``ground_component_tag`` (Name):  [Read-Write] 碰撞检测地面时使用的tag
- ``ground_trace_channel`` (CollisionChannel):  [Read-Write] 定义"地面"的碰撞通道
- ``ground_trace_object_types`` (Array[ObjectTypeQuery]):  [Read-Write] 定义"地面"的碰撞通道
- ``height_to_move_speed_curve`` (CurveFloat):  [Read-Write] 相机高度对应的移动速度曲线 单位：米
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``idle_time`` (float):  [Read-Write] 闲置时间
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``inner_input_event_delegate`` (PawnInnerDelegate):  [Read-Write] 内部处理鼠标键盘操作事件 //TODO 删除
- ``input_event_delegate`` (PawnInnerDelegate):  [Read-Write] 对外鼠标键盘操作事件 //TODO 删除
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_auto_camera_self_rotation_active`` (bool):  [Read-Write] 是否开启相机自身自动旋转，和相机绕点旋转不同
- ``is_auto_movement_active`` (bool):  [Read-Write] 是否正在启用自动位移
- ``is_auto_rotation_active`` (bool):  [Read-Write] 当前是否正在自动绕点旋转
- ``is_camera_traveling`` (bool):  [Read-Write] 当前是否相机正在过渡动画中
- ``is_dragging_active`` (bool):  [Read-Write] 是否开启Drag计算
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_following_actor`` (bool):  [Read-Write] 是否在跟踪Actor
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_rotate_active`` (bool):  [Read-Write] 旋转是否是激活状态
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``key_move_forward_direction`` (MoveForwardDirection):  [Read-Write] 按前进按钮时，相机的移动方向
- ``key_movement_mode`` (KeyMovementMode):  [Read-Write] 按键移动的移动方式
- ``last_click_hit_result`` (HitResult):  [Read-Write] 上一次左键点击时有效的HitResult
- ``last_click_world_height`` (double):  [Read-Write] 最后一次点击时的地面世界位置高度 如果是球体，则表示和球心的距离
- ``last_conformed_zoom_location`` (Vector):  [Read-Write]
- ``last_delta_time`` (float):  [Read-Only] 上一帧的Tick时间
- ``last_hit_by`` (Controller):  [Read-Write] Controller of the last Actor that caused us damage.
- ``last_location`` (Vector):  [Read-Write] 上一帧的位置
- ``last_rotate_world_height`` (double):  [Read-Write] 最后一次旋转时的世界平面高度 注意旋转和平移可以有不同的WorldPlane 计划废弃
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``limit_zoom_direction`` (bool):  [Read-Write] 是否固定限制缩放方向，如果不限制缩放操作也会产生滑动效果
- ``main_camera`` (CameraComponent):  [Read-Only] 主相机
- ``min_fallback_zoom_distance`` (double):  [Read-Write] 最小的Zoom步长，如果目标碰撞不存在时，而且不存在和虚拟平面的焦点时，使用这个数值制造一个虚拟距离
- ``min_movement_speed`` (float):  [Read-Write] 最低的移动速度，单位: m/s
- ``min_net_update_frequency`` (float):  [Read-Write]
- ``min_up_down_movement_speed`` (float):  [Read-Write] 最低的上下移动速度，单位: m/s
- ``min_zoom_step`` (float):  [Read-Write] 最小的缩放步进，每次滚轮操作的最小缩放距离，防止Target和相机距离过近时无法操作的情况
- ``move_key_pressed`` (bool):  [Read-Write] 是否移动Key正在按下
- ``movement_lag_speed`` (float):  [Read-Write] 相机移动的缓动速度
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
- ``on_travel_animation_finished`` (OnTravelAnimationFinished):  [Read-Write]
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``override_input_component_class`` (type(Class)):  [Read-Write] If set, then this InputComponent class will be used instead of the Input Settings' DefaultInputComponentClass
- ``override_starting_location`` (bool):  [Read-Write] 设置初始位置
- ``override_starting_pitch`` (bool):  [Read-Write] 设置初始Pitch
- ``override_starting_yaw`` (bool):  [Read-Write] 设置初始Yaw
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``player_state`` (PlayerState):  [Read-Write] If Pawn is possessed by a player, points to its Player State.  Needed for network play as controllers are not replicated to clients.
- ``pointer_key_pressed`` (bool):  [Read-Write] 是否左键Pointer正在按下
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``receive_controller_changed_delegate`` (PawnControllerChangedSignature):  [Read-Write] Event called after a pawn's controller has changed, on the server and owning client. This will happen at the same time as the delegate on GameInstance
- ``receive_restarted_delegate`` (PawnRestartedSignature):  [Read-Write] Event called after a pawn has been restarted, usually by a possession change. This is called on the server for all pawns and the owning client for player pawns
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
- ``rotate_current_screen_position`` (Vector2D):  [Read-Write] 当前的旋转点屏幕坐标
- ``rotate_delta_screen_position`` (Vector2D):  [Read-Write] 旋转时每帧移动时的屏幕坐标delta
- ``rotate_key_pressed`` (bool):  [Read-Write] 是否旋转Key正在按下
- ``rotate_last_screen_position`` (Vector2D):  [Read-Write] 上一帧旋转时的鼠标屏幕坐标
- ``rotate_pivot_use_real_world_collision`` (bool):  [Read-Write] 旋转是否使用射线检测，如果没有则会回退到LastRotateHeight所在的虚拟平面上
- ``rotate_start_pivot_location`` (Vector):  [Read-Write] 右键旋转开始时的Pivot
- ``rotate_start_screen_position`` (Vector2D):  [Read-Write] 旋转开始时的指针屏幕位置
- ``rotate_start_zoom_distance`` (double):  [Read-Write] 开始绕点旋转时和Pivot的距离，用于碰撞后恢复原距离，会被Zoom行为更新
- ``rotate_threshold_pitch_angle`` (float):  [Read-Write] 旋转点角度限制，当鼠标射线角度小于这个角度时Clamp掉的点位
- ``rotation_lag_speed`` (float):  [Read-Write] 相机旋转缓动Lag的速度
- ``runtime_camera_data`` (RuntimeCameraData):  [Read-Write] 运行时的相机数据 高度检测等
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``scaling_distance_reference`` (double):  [Read-Write] 距离地面多高的时候使用默认速度移动
- ``self_rotate_key_pressed`` (bool):  [Read-Write] 是否自身旋转Key正在按下
- ``show_debug_log`` (bool):  [Read-Write] 是否显示事件log
- ``show_debug_status`` (bool):  [Read-Write] 是否显示屏幕状态
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sphere_component`` (SphereComponent):  [Read-Only] The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``starting_location`` (Vector):  [Read-Write]
- ``starting_pitch`` (float):  [Read-Write]
- ``starting_yaw`` (float):  [Read-Write]
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``tick_delta`` (float):  [Read-Only] Pawn每帧的Tick时间
- ``total_auto_rotate_angle`` (float):  [Read-Write] 当前累计的旋转角度
- ``travel_anim_duration`` (float):  [Read-Write] Travel 动画时长
- ``travel_animtion_settings`` (TravelAnimationSettings):  [Read-Write] 如何进行Travel动画的定义，包括是否使用曲线运动和路径的计算等
- ``travel_pivot_spline_component`` (SplineComponent):  [Read-Write] 相机运动动画Pivot的Spline Component
- ``travel_spline_component`` (SplineComponent):  [Read-Write] 相机运动动画的Spline Component
- ``up_down_movement_speed`` (double):  [Read-Write] 垂直移动时的速度，使用固定值而不用Scale
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
- ``use_clamped_target_when_dragging`` (bool):  [Read-Write] 当鼠标角度超出最大DragThreshold时，不去打断Drag操作，而是去把角度限制在一个范围内的点，如果为false则直接中断当前操作
- ``use_controller_rotation_pitch`` (bool):  [Read-Write] If true, this Pawn's pitch will be updated to match the Controller's ControlRotation pitch, if controlled by a PlayerController.
- ``use_controller_rotation_roll`` (bool):  [Read-Write] If true, this Pawn's roll will be updated to match the Controller's ControlRotation roll, if controlled by a PlayerController.
- ``use_controller_rotation_yaw`` (bool):  [Read-Write] If true, this Pawn's yaw will be updated to match the Controller's ControlRotation yaw, if controlled by a PlayerController.
- ``use_pivot_as_zoom_target_when_input`` (bool):  [Read-Write] 当鼠标点击或旋转时，是否使用点击按下时的位置而不是鼠标的位置，如果为否则一直使用鼠标指针位置//其中旋转点的位置优先级比左键高
- ``use_rotate_value_from_input`` (bool):  [Read-Write] 如果为True：直接使用来自Input中的Value，如果为False：使用鼠标位置去计算，使触屏和鼠标行为统一//Control Mode为Controller时不起作用
- ``use_screen_center_as_zoom_direction`` (bool):  [Read-Write] 不使用鼠标位置，而是使用屏幕中心位置去旋转相机
- ``use_tag_find_ground`` (bool):  [Read-Write] 碰撞检测是否使用Tag查找地面
- ``use_vertical_fov`` (bool):  [Read-Write] 是否使用垂直FOV，用于超宽屏适配
- ``user_camera_settings`` (UserCameraSettings):  [Read-Write] 交给用户设置的相机操作参数
- ``velocity`` (Vector):  [Read-Write] 相机运动速度Velocity
- ``virtual_camera_diatance`` (double):  [Read-Write] 虚拟的相机臂距离，相机距离Pivot的点位
- ``virtual_pivot_location`` (Vector):  [Read-Write] 虚拟Pivot点位，类似以前的中心点，当碰撞检测失败或启用虚拟平面时，自动回退的点位
- ``wdp_common_input`` (WdpCommonInput):  [Read-Only] 通用输入组件
- ``world_origin_anchor`` (WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor
- ``zoom_action_type`` (ZoomActionType):  [Read-Write] 使用滚轮缩放时，缩放的类型，距离或FOV
- ``zoom_key_pressed`` (bool):  [Read-Write] 是否缩放Key正在按下
- ``zoom_lag_speed`` (float):  [Read-Write] 相机缩放的缓动速度
- ``zoom_start_screen_position`` (Vector2D):  [Read-Write] 当缩放开始时的屏幕坐标位置
- ``zoom_target_location`` (Vector):  [Read-Write] 缩放的目标点位置

<a id="unreal.WdpBasePawn.sphere_component"></a>

#### sphere\_component

```python
@property
def sphere_component() -> SphereComponent
```

(SphereComponent):  [Read-Only] The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions.

<a id="unreal.WdpBasePawn.camera_root"></a>

#### camera\_root

```python
@property
def camera_root() -> SceneComponent
```

(SceneComponent):  [Read-Only] 相机Root

<a id="unreal.WdpBasePawn.main_camera"></a>

#### main\_camera

```python
@property
def main_camera() -> CameraComponent
```

(CameraComponent):  [Read-Only] 主相机

<a id="unreal.WdpBasePawn.wdp_common_input"></a>

#### wdp\_common\_input

```python
@property
def wdp_common_input() -> WdpCommonInput
```

(WdpCommonInput):  [Read-Only] 通用输入组件

<a id="unreal.WdpBasePawn.world_origin_anchor"></a>

#### world\_origin\_anchor

```python
@property
def world_origin_anchor() -> WorldOriginAnchor
```

(WorldOriginAnchor):  [Read-Only] 用于球面操作的坐标转换Actor

<a id="unreal.WdpBasePawn.input_event_delegate"></a>

#### input\_event\_delegate

```python
@property
def input_event_delegate() -> PawnInnerDelegate
```

(PawnInnerDelegate):  [Read-Write] 对外鼠标键盘操作事件 //TODO 删除

<a id="unreal.WdpBasePawn.input_event_delegate"></a>

#### input\_event\_delegate

```python
@input_event_delegate.setter
def input_event_delegate(value: PawnInnerDelegate) -> None
```

<a id="unreal.WdpBasePawn.inner_input_event_delegate"></a>

#### inner\_input\_event\_delegate

```python
@property
def inner_input_event_delegate() -> PawnInnerDelegate
```

(PawnInnerDelegate):  [Read-Write] 内部处理鼠标键盘操作事件 //TODO 删除

<a id="unreal.WdpBasePawn.inner_input_event_delegate"></a>

#### inner\_input\_event\_delegate

```python
@inner_input_event_delegate.setter
def inner_input_event_delegate(value: PawnInnerDelegate) -> None
```

<a id="unreal.WdpBasePawn.tick_delta"></a>

#### tick\_delta

```python
@property
def tick_delta() -> float
```

(float):  [Read-Only] Pawn每帧的Tick时间

<a id="unreal.WdpBasePawn.last_delta_time"></a>

#### last\_delta\_time

```python
@property
def last_delta_time() -> float
```

(float):  [Read-Only] 上一帧的Tick时间

<a id="unreal.WdpBasePawn.show_debug_log"></a>

#### show\_debug\_log

```python
@property
def show_debug_log() -> bool
```

(bool):  [Read-Write] 是否显示事件log

<a id="unreal.WdpBasePawn.show_debug_log"></a>

#### show\_debug\_log

```python
@show_debug_log.setter
def show_debug_log(value: bool) -> None
```

<a id="unreal.WdpBasePawn.show_debug_status"></a>

#### show\_debug\_status

```python
@property
def show_debug_status() -> bool
```

(bool):  [Read-Write] 是否显示屏幕状态

<a id="unreal.WdpBasePawn.show_debug_status"></a>

#### show\_debug\_status

```python
@show_debug_status.setter
def show_debug_status(value: bool) -> None
```

<a id="unreal.WdpBasePawn.draw_debug_shapes"></a>

#### draw\_debug\_shapes

```python
@property
def draw_debug_shapes() -> bool
```

(bool):  [Read-Write] 是否绘制点位和Lag的debug图案

<a id="unreal.WdpBasePawn.draw_debug_shapes"></a>

#### draw\_debug\_shapes

```python
@draw_debug_shapes.setter
def draw_debug_shapes(value: bool) -> None
```

<a id="unreal.WdpBasePawn.enabled_features"></a>

#### enabled\_features

```python
@property
def enabled_features() -> int
```

(int32):  [Read-Only] 启用的功能，二进制bitmask//      1按键平面移动
//     2按键上下移动
//     3鼠标拖动移动
//     4旋转镜头
//     5滚轮缩放
//     6地形高度自适应(TODO)
//     7追踪Actor
//     8自动移动
//     9自动绕点旋转
//     10相机自身旋转
//     11双击操作

<a id="unreal.WdpBasePawn.default_mapping_context"></a>

#### default\_mapping\_context

```python
@property
def default_mapping_context() -> InputMappingContext
```

(InputMappingContext):  [Read-Only] MappingContext 当前的按键输入Mapping

<a id="unreal.WdpBasePawn.override_starting_location"></a>

#### override\_starting\_location

```python
@property
def override_starting_location() -> bool
```

(bool):  [Read-Write] 设置初始位置

<a id="unreal.WdpBasePawn.override_starting_location"></a>

#### override\_starting\_location

```python
@override_starting_location.setter
def override_starting_location(value: bool) -> None
```

<a id="unreal.WdpBasePawn.starting_location"></a>

#### starting\_location

```python
@property
def starting_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpBasePawn.starting_location"></a>

#### starting\_location

```python
@starting_location.setter
def starting_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.override_starting_yaw"></a>

#### override\_starting\_yaw

```python
@property
def override_starting_yaw() -> bool
```

(bool):  [Read-Write] 设置初始Yaw

<a id="unreal.WdpBasePawn.override_starting_yaw"></a>

#### override\_starting\_yaw

```python
@override_starting_yaw.setter
def override_starting_yaw(value: bool) -> None
```

<a id="unreal.WdpBasePawn.starting_yaw"></a>

#### starting\_yaw

```python
@property
def starting_yaw() -> float
```

(float):  [Read-Write]

<a id="unreal.WdpBasePawn.starting_yaw"></a>

#### starting\_yaw

```python
@starting_yaw.setter
def starting_yaw(value: float) -> None
```

<a id="unreal.WdpBasePawn.override_starting_pitch"></a>

#### override\_starting\_pitch

```python
@property
def override_starting_pitch() -> bool
```

(bool):  [Read-Write] 设置初始Pitch

<a id="unreal.WdpBasePawn.override_starting_pitch"></a>

#### override\_starting\_pitch

```python
@override_starting_pitch.setter
def override_starting_pitch(value: bool) -> None
```

<a id="unreal.WdpBasePawn.starting_pitch"></a>

#### starting\_pitch

```python
@property
def starting_pitch() -> float
```

(float):  [Read-Write]

<a id="unreal.WdpBasePawn.starting_pitch"></a>

#### starting\_pitch

```python
@starting_pitch.setter
def starting_pitch(value: float) -> None
```

<a id="unreal.WdpBasePawn.idle_time"></a>

#### idle\_time

```python
@property
def idle_time() -> float
```

(float):  [Read-Only] 闲置时间

<a id="unreal.WdpBasePawn.enable_user_input"></a>

#### enable\_user\_input

```python
@property
def enable_user_input() -> bool
```

(bool):  [Read-Write] 全局启用禁用用户输入操作

<a id="unreal.WdpBasePawn.enable_user_input"></a>

#### enable\_user\_input

```python
@enable_user_input.setter
def enable_user_input(value: bool) -> None
```

<a id="unreal.WdpBasePawn.enable_input_when_not_being_view_target"></a>

#### enable\_input\_when\_not\_being\_view\_target

```python
@property
def enable_input_when_not_being_view_target() -> bool
```

(bool):  [Read-Write] 在自身不是View Target 的情况下是否允许输入操作

<a id="unreal.WdpBasePawn.enable_input_when_not_being_view_target"></a>

#### enable\_input\_when\_not\_being\_view\_target

```python
@enable_input_when_not_being_view_target.setter
def enable_input_when_not_being_view_target(value: bool) -> None
```

<a id="unreal.WdpBasePawn.pointer_key_pressed"></a>

#### pointer\_key\_pressed

```python
@property
def pointer_key_pressed() -> bool
```

(bool):  [Read-Write] 是否左键Pointer正在按下

<a id="unreal.WdpBasePawn.pointer_key_pressed"></a>

#### pointer\_key\_pressed

```python
@pointer_key_pressed.setter
def pointer_key_pressed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.rotate_key_pressed"></a>

#### rotate\_key\_pressed

```python
@property
def rotate_key_pressed() -> bool
```

(bool):  [Read-Write] 是否旋转Key正在按下

<a id="unreal.WdpBasePawn.rotate_key_pressed"></a>

#### rotate\_key\_pressed

```python
@rotate_key_pressed.setter
def rotate_key_pressed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.zoom_key_pressed"></a>

#### zoom\_key\_pressed

```python
@property
def zoom_key_pressed() -> bool
```

(bool):  [Read-Write] 是否缩放Key正在按下

<a id="unreal.WdpBasePawn.zoom_key_pressed"></a>

#### zoom\_key\_pressed

```python
@zoom_key_pressed.setter
def zoom_key_pressed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.move_key_pressed"></a>

#### move\_key\_pressed

```python
@property
def move_key_pressed() -> bool
```

(bool):  [Read-Write] 是否移动Key正在按下

<a id="unreal.WdpBasePawn.move_key_pressed"></a>

#### move\_key\_pressed

```python
@move_key_pressed.setter
def move_key_pressed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.self_rotate_key_pressed"></a>

#### self\_rotate\_key\_pressed

```python
@property
def self_rotate_key_pressed() -> bool
```

(bool):  [Read-Write] 是否自身旋转Key正在按下

<a id="unreal.WdpBasePawn.self_rotate_key_pressed"></a>

#### self\_rotate\_key\_pressed

```python
@self_rotate_key_pressed.setter
def self_rotate_key_pressed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.last_click_hit_result"></a>

#### last\_click\_hit\_result

```python
@property
def last_click_hit_result() -> HitResult
```

(HitResult):  [Read-Write] 上一次左键点击时有效的HitResult

<a id="unreal.WdpBasePawn.last_click_hit_result"></a>

#### last\_click\_hit\_result

```python
@last_click_hit_result.setter
def last_click_hit_result(value: HitResult) -> None
```

<a id="unreal.WdpBasePawn.click_begin_screen_position"></a>

#### click\_begin\_screen\_position

```python
@property
def click_begin_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 左键点击开始时的屏幕坐标

<a id="unreal.WdpBasePawn.click_begin_screen_position"></a>

#### click\_begin\_screen\_position

```python
@click_begin_screen_position.setter
def click_begin_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.click_begin_pointer_location"></a>

#### click\_begin\_pointer\_location

```python
@property
def click_begin_pointer_location() -> Vector
```

(Vector):  [Read-Write] 左键(Pointer)点击开始时的鼠标位置世界坐标

<a id="unreal.WdpBasePawn.click_begin_pointer_location"></a>

#### click\_begin\_pointer\_location

```python
@click_begin_pointer_location.setter
def click_begin_pointer_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.click_begin_camera_location"></a>

#### click\_begin\_camera\_location

```python
@property
def click_begin_camera_location() -> Vector
```

(Vector):  [Read-Write] 左键(Pointer)点击开始时自身的世界坐标

<a id="unreal.WdpBasePawn.click_begin_camera_location"></a>

#### click\_begin\_camera\_location

```python
@click_begin_camera_location.setter
def click_begin_camera_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.click_pointer_last_screen_position"></a>

#### click\_pointer\_last\_screen\_position

```python
@property
def click_pointer_last_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 上一帧左键移动(Pointer)的屏幕坐标位置

<a id="unreal.WdpBasePawn.click_pointer_last_screen_position"></a>

#### click\_pointer\_last\_screen\_position

```python
@click_pointer_last_screen_position.setter
def click_pointer_last_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.click_pointer_screen_delta_position"></a>

#### click\_pointer\_screen\_delta\_position

```python
@property
def click_pointer_screen_delta_position() -> Vector2D
```

(Vector2D):  [Read-Write] 左键点击(Pointer)时的每帧移动delta距离

<a id="unreal.WdpBasePawn.click_pointer_screen_delta_position"></a>

#### click\_pointer\_screen\_delta\_position

```python
@click_pointer_screen_delta_position.setter
def click_pointer_screen_delta_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.click_pointer_current_screen_position"></a>

#### click\_pointer\_current\_screen\_position

```python
@property
def click_pointer_current_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 当前的Pointer坐标

<a id="unreal.WdpBasePawn.click_pointer_current_screen_position"></a>

#### click\_pointer\_current\_screen\_position

```python
@click_pointer_current_screen_position.setter
def click_pointer_current_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.last_click_world_height"></a>

#### last\_click\_world\_height

```python
@property
def last_click_world_height() -> float
```

(double):  [Read-Write] 最后一次点击时的地面世界位置高度 如果是球体，则表示和球心的距离

<a id="unreal.WdpBasePawn.last_click_world_height"></a>

#### last\_click\_world\_height

```python
@last_click_world_height.setter
def last_click_world_height(value: float) -> None
```

<a id="unreal.WdpBasePawn.camera_rotate_mode"></a>

#### camera\_rotate\_mode

```python
@property
def camera_rotate_mode() -> CameraRotateMode
```

(CameraRotateMode):  [Read-Write] 旋转的方式

<a id="unreal.WdpBasePawn.camera_rotate_mode"></a>

#### camera\_rotate\_mode

```python
@camera_rotate_mode.setter
def camera_rotate_mode(value: CameraRotateMode) -> None
```

<a id="unreal.WdpBasePawn.rotate_start_screen_position"></a>

#### rotate\_start\_screen\_position

```python
@property
def rotate_start_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 旋转开始时的指针屏幕位置

<a id="unreal.WdpBasePawn.rotate_start_screen_position"></a>

#### rotate\_start\_screen\_position

```python
@rotate_start_screen_position.setter
def rotate_start_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.rotate_last_screen_position"></a>

#### rotate\_last\_screen\_position

```python
@property
def rotate_last_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 上一帧旋转时的鼠标屏幕坐标

<a id="unreal.WdpBasePawn.rotate_last_screen_position"></a>

#### rotate\_last\_screen\_position

```python
@rotate_last_screen_position.setter
def rotate_last_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.rotate_delta_screen_position"></a>

#### rotate\_delta\_screen\_position

```python
@property
def rotate_delta_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 旋转时每帧移动时的屏幕坐标delta

<a id="unreal.WdpBasePawn.rotate_delta_screen_position"></a>

#### rotate\_delta\_screen\_position

```python
@rotate_delta_screen_position.setter
def rotate_delta_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.rotate_current_screen_position"></a>

#### rotate\_current\_screen\_position

```python
@property
def rotate_current_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 当前的旋转点屏幕坐标

<a id="unreal.WdpBasePawn.rotate_current_screen_position"></a>

#### rotate\_current\_screen\_position

```python
@rotate_current_screen_position.setter
def rotate_current_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.rotate_start_pivot_location"></a>

#### rotate\_start\_pivot\_location

```python
@property
def rotate_start_pivot_location() -> Vector
```

(Vector):  [Read-Write] 右键旋转开始时的Pivot

<a id="unreal.WdpBasePawn.rotate_start_pivot_location"></a>

#### rotate\_start\_pivot\_location

```python
@rotate_start_pivot_location.setter
def rotate_start_pivot_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.last_rotate_world_height"></a>

#### last\_rotate\_world\_height

```python
@property
def last_rotate_world_height() -> float
```

(double):  [Read-Write] 最后一次旋转时的世界平面高度 注意旋转和平移可以有不同的WorldPlane 计划废弃

<a id="unreal.WdpBasePawn.last_rotate_world_height"></a>

#### last\_rotate\_world\_height

```python
@last_rotate_world_height.setter
def last_rotate_world_height(value: float) -> None
```

<a id="unreal.WdpBasePawn.rotate_start_zoom_distance"></a>

#### rotate\_start\_zoom\_distance

```python
@property
def rotate_start_zoom_distance() -> float
```

(double):  [Read-Write] 开始绕点旋转时和Pivot的距离，用于碰撞后恢复原距离，会被Zoom行为更新

<a id="unreal.WdpBasePawn.rotate_start_zoom_distance"></a>

#### rotate\_start\_zoom\_distance

```python
@rotate_start_zoom_distance.setter
def rotate_start_zoom_distance(value: float) -> None
```

<a id="unreal.WdpBasePawn.camera_around_pivot_remain_rotation"></a>

#### camera\_around\_pivot\_remain\_rotation

```python
@property
def camera_around_pivot_remain_rotation() -> Rotator
```

(Rotator):  [Read-Write] 缓动用，绕点旋转剩余没完成的角度 roll 无效

<a id="unreal.WdpBasePawn.camera_around_pivot_remain_rotation"></a>

#### camera\_around\_pivot\_remain\_rotation

```python
@camera_around_pivot_remain_rotation.setter
def camera_around_pivot_remain_rotation(value: Rotator) -> None
```

<a id="unreal.WdpBasePawn.camera_self_remain_rotation"></a>

#### camera\_self\_remain\_rotation

```python
@property
def camera_self_remain_rotation() -> Rotator
```

(Rotator):  [Read-Write] 缓动用，相机自身旋转的剩余角度

<a id="unreal.WdpBasePawn.camera_self_remain_rotation"></a>

#### camera\_self\_remain\_rotation

```python
@camera_self_remain_rotation.setter
def camera_self_remain_rotation(value: Rotator) -> None
```

<a id="unreal.WdpBasePawn.camera_free_movement_remain_location"></a>

#### camera\_free\_movement\_remain\_location

```python
@property
def camera_free_movement_remain_location() -> Vector
```

(Vector):  [Read-Write] 相机自由运动的目标位置，不受球面运动影响的缓动距离，主要用于动画

<a id="unreal.WdpBasePawn.camera_free_movement_remain_location"></a>

#### camera\_free\_movement\_remain\_location

```python
@camera_free_movement_remain_location.setter
def camera_free_movement_remain_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.camera_surface_movement_remain_location"></a>

#### camera\_surface\_movement\_remain\_location

```python
@property
def camera_surface_movement_remain_location() -> Vector
```

(Vector):  [Read-Write] 表面运动缓动变量，指以相机自身为中心的平面上运动的方向，用于球面运动等

<a id="unreal.WdpBasePawn.camera_surface_movement_remain_location"></a>

#### camera\_surface\_movement\_remain\_location

```python
@camera_surface_movement_remain_location.setter
def camera_surface_movement_remain_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.camera_height_movement_remain_distance"></a>

#### camera\_height\_movement\_remain\_distance

```python
@property
def camera_height_movement_remain_distance() -> float
```

(double):  [Read-Write] 缓动用，相机高度变化的剩余变化值，相机自身位置单纯的Z变化

<a id="unreal.WdpBasePawn.camera_height_movement_remain_distance"></a>

#### camera\_height\_movement\_remain\_distance

```python
@camera_height_movement_remain_distance.setter
def camera_height_movement_remain_distance(value: float) -> None
```

<a id="unreal.WdpBasePawn.camera_follow_actor_remain_location"></a>

#### camera\_follow\_actor\_remain\_location

```python
@property
def camera_follow_actor_remain_location() -> Vector
```

(Vector):  [Read-Write] 缓动用，用于在FollowActor时制造缓动跟踪效果

<a id="unreal.WdpBasePawn.camera_follow_actor_remain_location"></a>

#### camera\_follow\_actor\_remain\_location

```python
@camera_follow_actor_remain_location.setter
def camera_follow_actor_remain_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.camera_zoom_remain_distance"></a>

#### camera\_zoom\_remain\_distance

```python
@property
def camera_zoom_remain_distance() -> float
```

(double):  [Read-Write] /缓动用，缩放操作剩余的相机缩放

<a id="unreal.WdpBasePawn.camera_zoom_remain_distance"></a>

#### camera\_zoom\_remain\_distance

```python
@camera_zoom_remain_distance.setter
def camera_zoom_remain_distance(value: float) -> None
```

<a id="unreal.WdpBasePawn.zoom_target_location"></a>

#### zoom\_target\_location

```python
@property
def zoom_target_location() -> Vector
```

(Vector):  [Read-Write] 缩放的目标点位置

<a id="unreal.WdpBasePawn.zoom_target_location"></a>

#### zoom\_target\_location

```python
@zoom_target_location.setter
def zoom_target_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.zoom_start_screen_position"></a>

#### zoom\_start\_screen\_position

```python
@property
def zoom_start_screen_position() -> Vector2D
```

(Vector2D):  [Read-Only] 当缩放开始时的屏幕坐标位置

<a id="unreal.WdpBasePawn.last_conformed_zoom_location"></a>

#### last\_conformed\_zoom\_location

```python
@property
def last_conformed_zoom_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpBasePawn.last_conformed_zoom_location"></a>

#### last\_conformed\_zoom\_location

```python
@last_conformed_zoom_location.setter
def last_conformed_zoom_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.min_zoom_step"></a>

#### min\_zoom\_step

```python
@property
def min_zoom_step() -> float
```

(float):  [Read-Write] 最小的缩放步进，每次滚轮操作的最小缩放距离，防止Target和相机距离过近时无法操作的情况

<a id="unreal.WdpBasePawn.min_zoom_step"></a>

#### min\_zoom\_step

```python
@min_zoom_step.setter
def min_zoom_step(value: float) -> None
```

<a id="unreal.WdpBasePawn.up_down_movement_speed"></a>

#### up\_down\_movement\_speed

```python
@property
def up_down_movement_speed() -> float
```

(double):  [Read-Write] 垂直移动时的速度，使用固定值而不用Scale

<a id="unreal.WdpBasePawn.up_down_movement_speed"></a>

#### up\_down\_movement\_speed

```python
@up_down_movement_speed.setter
def up_down_movement_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.scaling_distance_reference"></a>

#### scaling\_distance\_reference

```python
@property
def scaling_distance_reference() -> float
```

(double):  [Read-Write] 距离地面多高的时候使用默认速度移动

<a id="unreal.WdpBasePawn.scaling_distance_reference"></a>

#### scaling\_distance\_reference

```python
@scaling_distance_reference.setter
def scaling_distance_reference(value: float) -> None
```

<a id="unreal.WdpBasePawn.key_movement_mode"></a>

#### key\_movement\_mode

```python
@property
def key_movement_mode() -> KeyMovementMode
```

(KeyMovementMode):  [Read-Write] 按键移动的移动方式

<a id="unreal.WdpBasePawn.key_movement_mode"></a>

#### key\_movement\_mode

```python
@key_movement_mode.setter
def key_movement_mode(value: KeyMovementMode) -> None
```

<a id="unreal.WdpBasePawn.current_camera_data"></a>

#### current\_camera\_data

```python
@property
def current_camera_data() -> AllCameraData
```

(AllCameraData):  [Read-Write] 完整的相机数据结构体 包含缩放 角度限制 碰撞设置等，都在这里扩展

<a id="unreal.WdpBasePawn.current_camera_data"></a>

#### current\_camera\_data

```python
@current_camera_data.setter
def current_camera_data(value: AllCameraData) -> None
```

<a id="unreal.WdpBasePawn.runtime_camera_data"></a>

#### runtime\_camera\_data

```python
@property
def runtime_camera_data() -> RuntimeCameraData
```

(RuntimeCameraData):  [Read-Write] 运行时的相机数据 高度检测等

<a id="unreal.WdpBasePawn.runtime_camera_data"></a>

#### runtime\_camera\_data

```python
@runtime_camera_data.setter
def runtime_camera_data(value: RuntimeCameraData) -> None
```

<a id="unreal.WdpBasePawn.virtual_pivot_location"></a>

#### virtual\_pivot\_location

```python
@property
def virtual_pivot_location() -> Vector
```

(Vector):  [Read-Write] 虚拟Pivot点位，类似以前的中心点，当碰撞检测失败或启用虚拟平面时，自动回退的点位

<a id="unreal.WdpBasePawn.virtual_pivot_location"></a>

#### virtual\_pivot\_location

```python
@virtual_pivot_location.setter
def virtual_pivot_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.virtual_camera_diatance"></a>

#### virtual\_camera\_diatance

```python
@property
def virtual_camera_diatance() -> float
```

(double):  [Read-Write] 虚拟的相机臂距离，相机距离Pivot的点位

<a id="unreal.WdpBasePawn.virtual_camera_diatance"></a>

#### virtual\_camera\_diatance

```python
@virtual_camera_diatance.setter
def virtual_camera_diatance(value: float) -> None
```

<a id="unreal.WdpBasePawn.camera_height_to_virtual_plane"></a>

#### camera\_height\_to\_virtual\_plane

```python
@property
def camera_height_to_virtual_plane() -> float
```

(double):  [Read-Write] 相机距离虚拟平面的高度差

<a id="unreal.WdpBasePawn.camera_height_to_virtual_plane"></a>

#### camera\_height\_to\_virtual\_plane

```python
@camera_height_to_virtual_plane.setter
def camera_height_to_virtual_plane(value: float) -> None
```

<a id="unreal.WdpBasePawn.user_camera_settings"></a>

#### user\_camera\_settings

```python
@property
def user_camera_settings() -> UserCameraSettings
```

(UserCameraSettings):  [Read-Write] 交给用户设置的相机操作参数

<a id="unreal.WdpBasePawn.user_camera_settings"></a>

#### user\_camera\_settings

```python
@user_camera_settings.setter
def user_camera_settings(value: UserCameraSettings) -> None
```

<a id="unreal.WdpBasePawn.camera_additional_rotate_scale"></a>

#### camera\_additional\_rotate\_scale

```python
@property
def camera_additional_rotate_scale() -> float
```

(float):  [Read-Write] 相机旋转速度，在不修改用户配置和输入配置的情况下再进一步独立调整相机的旋转速度//相机最终的旋转速度为Input中的Scale * 用户设置的Scale * CameraAdditionalRotateScale

<a id="unreal.WdpBasePawn.camera_additional_rotate_scale"></a>

#### camera\_additional\_rotate\_scale

```python
@camera_additional_rotate_scale.setter
def camera_additional_rotate_scale(value: float) -> None
```

<a id="unreal.WdpBasePawn.camera_touch_input_sensitivity"></a>

#### camera\_touch\_input\_sensitivity

```python
@property
def camera_touch_input_sensitivity() -> float
```

(float):  [Read-Write] 如果不使用Enhach Input中的数值，而是改用鼠标或触屏在平面上的位置去计算旋转，灵敏度是多少

<a id="unreal.WdpBasePawn.camera_touch_input_sensitivity"></a>

#### camera\_touch\_input\_sensitivity

```python
@camera_touch_input_sensitivity.setter
def camera_touch_input_sensitivity(value: float) -> None
```

<a id="unreal.WdpBasePawn.use_rotate_value_from_input"></a>

#### use\_rotate\_value\_from\_input

```python
@property
def use_rotate_value_from_input() -> bool
```

(bool):  [Read-Write] 如果为True：直接使用来自Input中的Value，如果为False：使用鼠标位置去计算，使触屏和鼠标行为统一//Control Mode为Controller时不起作用

<a id="unreal.WdpBasePawn.use_rotate_value_from_input"></a>

#### use\_rotate\_value\_from\_input

```python
@use_rotate_value_from_input.setter
def use_rotate_value_from_input(value: bool) -> None
```

<a id="unreal.WdpBasePawn.use_pivot_as_zoom_target_when_input"></a>

#### use\_pivot\_as\_zoom\_target\_when\_input

```python
@property
def use_pivot_as_zoom_target_when_input() -> bool
```

(bool):  [Read-Write] 当鼠标点击或旋转时，是否使用点击按下时的位置而不是鼠标的位置，如果为否则一直使用鼠标指针位置//其中旋转点的位置优先级比左键高

<a id="unreal.WdpBasePawn.use_pivot_as_zoom_target_when_input"></a>

#### use\_pivot\_as\_zoom\_target\_when\_input

```python
@use_pivot_as_zoom_target_when_input.setter
def use_pivot_as_zoom_target_when_input(value: bool) -> None
```

<a id="unreal.WdpBasePawn.use_screen_center_as_zoom_direction"></a>

#### use\_screen\_center\_as\_zoom\_direction

```python
@property
def use_screen_center_as_zoom_direction() -> bool
```

(bool):  [Read-Write] 不使用鼠标位置，而是使用屏幕中心位置去旋转相机

<a id="unreal.WdpBasePawn.use_screen_center_as_zoom_direction"></a>

#### use\_screen\_center\_as\_zoom\_direction

```python
@use_screen_center_as_zoom_direction.setter
def use_screen_center_as_zoom_direction(value: bool) -> None
```

<a id="unreal.WdpBasePawn.default_world_plane_height"></a>

#### default\_world\_plane\_height

```python
@property
def default_world_plane_height() -> float
```

(double):  [Read-Write] 当射线检测失败时，点击操作使用的默认的世界位置水平面高度。只要点击成功过一次就会使用LastWorldHeight

<a id="unreal.WdpBasePawn.default_world_plane_height"></a>

#### default\_world\_plane\_height

```python
@default_world_plane_height.setter
def default_world_plane_height(value: float) -> None
```

<a id="unreal.WdpBasePawn.drag_threshold_pitch_angle"></a>

#### drag\_threshold\_pitch\_angle

```python
@property
def drag_threshold_pitch_angle() -> float
```

(float):  [Read-Write] 拖动角度的限制，当鼠标射线角度小于这个角度时停止拖动

<a id="unreal.WdpBasePawn.drag_threshold_pitch_angle"></a>

#### drag\_threshold\_pitch\_angle

```python
@drag_threshold_pitch_angle.setter
def drag_threshold_pitch_angle(value: float) -> None
```

<a id="unreal.WdpBasePawn.rotate_threshold_pitch_angle"></a>

#### rotate\_threshold\_pitch\_angle

```python
@property
def rotate_threshold_pitch_angle() -> float
```

(float):  [Read-Write] 旋转点角度限制，当鼠标射线角度小于这个角度时Clamp掉的点位

<a id="unreal.WdpBasePawn.rotate_threshold_pitch_angle"></a>

#### rotate\_threshold\_pitch\_angle

```python
@rotate_threshold_pitch_angle.setter
def rotate_threshold_pitch_angle(value: float) -> None
```

<a id="unreal.WdpBasePawn.rotate_pivot_use_real_world_collision"></a>

#### rotate\_pivot\_use\_real\_world\_collision

```python
@property
def rotate_pivot_use_real_world_collision() -> bool
```

(bool):  [Read-Write] 旋转是否使用射线检测，如果没有则会回退到LastRotateHeight所在的虚拟平面上

<a id="unreal.WdpBasePawn.rotate_pivot_use_real_world_collision"></a>

#### rotate\_pivot\_use\_real\_world\_collision

```python
@rotate_pivot_use_real_world_collision.setter
def rotate_pivot_use_real_world_collision(value: bool) -> None
```

<a id="unreal.WdpBasePawn.min_fallback_zoom_distance"></a>

#### min\_fallback\_zoom\_distance

```python
@property
def min_fallback_zoom_distance() -> float
```

(double):  [Read-Write] 最小的Zoom步长，如果目标碰撞不存在时，而且不存在和虚拟平面的焦点时，使用这个数值制造一个虚拟距离

<a id="unreal.WdpBasePawn.min_fallback_zoom_distance"></a>

#### min\_fallback\_zoom\_distance

```python
@min_fallback_zoom_distance.setter
def min_fallback_zoom_distance(value: float) -> None
```

<a id="unreal.WdpBasePawn.use_clamped_target_when_dragging"></a>

#### use\_clamped\_target\_when\_dragging

```python
@property
def use_clamped_target_when_dragging() -> bool
```

(bool):  [Read-Write] 当鼠标角度超出最大DragThreshold时，不去打断Drag操作，而是去把角度限制在一个范围内的点，如果为false则直接中断当前操作

<a id="unreal.WdpBasePawn.use_clamped_target_when_dragging"></a>

#### use\_clamped\_target\_when\_dragging

```python
@use_clamped_target_when_dragging.setter
def use_clamped_target_when_dragging(value: bool) -> None
```

<a id="unreal.WdpBasePawn.rotation_lag_speed"></a>

#### rotation\_lag\_speed

```python
@property
def rotation_lag_speed() -> float
```

(float):  [Read-Write] 相机旋转缓动Lag的速度

<a id="unreal.WdpBasePawn.rotation_lag_speed"></a>

#### rotation\_lag\_speed

```python
@rotation_lag_speed.setter
def rotation_lag_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.movement_lag_speed"></a>

#### movement\_lag\_speed

```python
@property
def movement_lag_speed() -> float
```

(float):  [Read-Write] 相机移动的缓动速度

<a id="unreal.WdpBasePawn.movement_lag_speed"></a>

#### movement\_lag\_speed

```python
@movement_lag_speed.setter
def movement_lag_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.zoom_lag_speed"></a>

#### zoom\_lag\_speed

```python
@property
def zoom_lag_speed() -> float
```

(float):  [Read-Write] 相机缩放的缓动速度

<a id="unreal.WdpBasePawn.zoom_lag_speed"></a>

#### zoom\_lag\_speed

```python
@zoom_lag_speed.setter
def zoom_lag_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.fov_lag_speed"></a>

#### fov\_lag\_speed

```python
@property
def fov_lag_speed() -> float
```

(float):  [Read-Write] FOV变化的缓动速度

<a id="unreal.WdpBasePawn.fov_lag_speed"></a>

#### fov\_lag\_speed

```python
@fov_lag_speed.setter
def fov_lag_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.follow_actor_lag_speed"></a>

#### follow\_actor\_lag\_speed

```python
@property
def follow_actor_lag_speed() -> float
```

(float):  [Read-Write] FollowActor 的缓动速度*/

<a id="unreal.WdpBasePawn.follow_actor_lag_speed"></a>

#### follow\_actor\_lag\_speed

```python
@follow_actor_lag_speed.setter
def follow_actor_lag_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.use_vertical_fov"></a>

#### use\_vertical\_fov

```python
@property
def use_vertical_fov() -> bool
```

(bool):  [Read-Write] 是否使用垂直FOV，用于超宽屏适配

<a id="unreal.WdpBasePawn.use_vertical_fov"></a>

#### use\_vertical\_fov

```python
@use_vertical_fov.setter
def use_vertical_fov(value: bool) -> None
```

<a id="unreal.WdpBasePawn.key_move_forward_direction"></a>

#### key\_move\_forward\_direction

```python
@property
def key_move_forward_direction() -> MoveForwardDirection
```

(MoveForwardDirection):  [Read-Write] 按前进按钮时，相机的移动方向

<a id="unreal.WdpBasePawn.key_move_forward_direction"></a>

#### key\_move\_forward\_direction

```python
@key_move_forward_direction.setter
def key_move_forward_direction(value: MoveForwardDirection) -> None
```

<a id="unreal.WdpBasePawn.zoom_action_type"></a>

#### zoom\_action\_type

```python
@property
def zoom_action_type() -> ZoomActionType
```

(ZoomActionType):  [Read-Write] 使用滚轮缩放时，缩放的类型，距离或FOV

<a id="unreal.WdpBasePawn.zoom_action_type"></a>

#### zoom\_action\_type

```python
@zoom_action_type.setter
def zoom_action_type(value: ZoomActionType) -> None
```

<a id="unreal.WdpBasePawn.distance_zoom_speed"></a>

#### distance\_zoom\_speed

```python
@property
def distance_zoom_speed() -> float
```

(float):  [Read-Write] 距离缩放的速度值

<a id="unreal.WdpBasePawn.distance_zoom_speed"></a>

#### distance\_zoom\_speed

```python
@distance_zoom_speed.setter
def distance_zoom_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.fov_zoom_speed"></a>

#### fov\_zoom\_speed

```python
@property
def fov_zoom_speed() -> float
```

(float):  [Read-Write] FOV缩放的速度值

<a id="unreal.WdpBasePawn.fov_zoom_speed"></a>

#### fov\_zoom\_speed

```python
@fov_zoom_speed.setter
def fov_zoom_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.boost_movement_scale"></a>

#### boost\_movement\_scale

```python
@property
def boost_movement_scale() -> float
```

(float):  [Read-Write] 用于进阶按键移动速度倍率（如按下shift时的速度倍速）

<a id="unreal.WdpBasePawn.boost_movement_scale"></a>

#### boost\_movement\_scale

```python
@boost_movement_scale.setter
def boost_movement_scale(value: float) -> None
```

<a id="unreal.WdpBasePawn.min_movement_speed"></a>

#### min\_movement\_speed

```python
@property
def min_movement_speed() -> float
```

(float):  [Read-Write] 最低的移动速度，单位: m/s

<a id="unreal.WdpBasePawn.min_movement_speed"></a>

#### min\_movement\_speed

```python
@min_movement_speed.setter
def min_movement_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.min_up_down_movement_speed"></a>

#### min\_up\_down\_movement\_speed

```python
@property
def min_up_down_movement_speed() -> float
```

(float):  [Read-Write] 最低的上下移动速度，单位: m/s

<a id="unreal.WdpBasePawn.min_up_down_movement_speed"></a>

#### min\_up\_down\_movement\_speed

```python
@min_up_down_movement_speed.setter
def min_up_down_movement_speed(value: float) -> None
```

<a id="unreal.WdpBasePawn.height_to_move_speed_curve"></a>

#### height\_to\_move\_speed\_curve

```python
@property
def height_to_move_speed_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 相机高度对应的移动速度曲线 单位：米

<a id="unreal.WdpBasePawn.height_to_move_speed_curve"></a>

#### height\_to\_move\_speed\_curve

```python
@height_to_move_speed_curve.setter
def height_to_move_speed_curve(value: CurveFloat) -> None
```

<a id="unreal.WdpBasePawn.camera_travel_base_curve"></a>

#### camera\_travel\_base\_curve

```python
@property
def camera_travel_base_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 相机动画单位圆弧曲线

<a id="unreal.WdpBasePawn.camera_travel_base_curve"></a>

#### camera\_travel\_base\_curve

```python
@camera_travel_base_curve.setter
def camera_travel_base_curve(value: CurveFloat) -> None
```

<a id="unreal.WdpBasePawn.camera_travel_curve_sample_count"></a>

#### camera\_travel\_curve\_sample\_count

```python
@property
def camera_travel_curve_sample_count() -> int
```

(int32):  [Read-Write] 相机动画曲线的分段数量

<a id="unreal.WdpBasePawn.camera_travel_curve_sample_count"></a>

#### camera\_travel\_curve\_sample\_count

```python
@camera_travel_curve_sample_count.setter
def camera_travel_curve_sample_count(value: int) -> None
```

<a id="unreal.WdpBasePawn.distance_to_move_angle_curve"></a>

#### distance\_to\_move\_angle\_curve

```python
@property
def distance_to_move_angle_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 相机动画距离对应自动曲线弧度的曲线

<a id="unreal.WdpBasePawn.distance_to_move_angle_curve"></a>

#### distance\_to\_move\_angle\_curve

```python
@distance_to_move_angle_curve.setter
def distance_to_move_angle_curve(value: CurveFloat) -> None
```

<a id="unreal.WdpBasePawn.camera_travel_max_height_difference_scale"></a>

#### camera\_travel\_max\_height\_difference\_scale

```python
@property
def camera_travel_max_height_difference_scale() -> float
```

(float):  [Read-Write] 相机Travel时如果有高度差，最大应用曲线和距离的倍数

<a id="unreal.WdpBasePawn.camera_travel_max_height_difference_scale"></a>

#### camera\_travel\_max\_height\_difference\_scale

```python
@camera_travel_max_height_difference_scale.setter
def camera_travel_max_height_difference_scale(value: float) -> None
```

<a id="unreal.WdpBasePawn.double_click_zoom_scale"></a>

#### double\_click\_zoom\_scale

```python
@property
def double_click_zoom_scale() -> float
```

(float):  [Read-Write] 双击移动时缩放的前进倍数

<a id="unreal.WdpBasePawn.double_click_zoom_scale"></a>

#### double\_click\_zoom\_scale

```python
@double_click_zoom_scale.setter
def double_click_zoom_scale(value: float) -> None
```

<a id="unreal.WdpBasePawn.enable_camera_lag"></a>

#### enable\_camera\_lag

```python
@property
def enable_camera_lag() -> bool
```

(bool):  [Read-Write] 是否启用相机lag

<a id="unreal.WdpBasePawn.enable_camera_lag"></a>

#### enable\_camera\_lag

```python
@enable_camera_lag.setter
def enable_camera_lag(value: bool) -> None
```

<a id="unreal.WdpBasePawn.enable_rotation_lag"></a>

#### enable\_rotation\_lag

```python
@property
def enable_rotation_lag() -> bool
```

(bool):  [Read-Write] 是否启用旋转lag

<a id="unreal.WdpBasePawn.enable_rotation_lag"></a>

#### enable\_rotation\_lag

```python
@enable_rotation_lag.setter
def enable_rotation_lag(value: bool) -> None
```

<a id="unreal.WdpBasePawn.last_location"></a>

#### last\_location

```python
@property
def last_location() -> Vector
```

(Vector):  [Read-Only] 上一帧的位置

<a id="unreal.WdpBasePawn.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only] 相机运动速度Velocity

<a id="unreal.WdpBasePawn.is_dragging_active"></a>

#### is\_dragging\_active

```python
@property
def is_dragging_active() -> bool
```

(bool):  [Read-Write] 是否开启Drag计算

<a id="unreal.WdpBasePawn.is_dragging_active"></a>

#### is\_dragging\_active

```python
@is_dragging_active.setter
def is_dragging_active(value: bool) -> None
```

<a id="unreal.WdpBasePawn.drag_start_screen_position"></a>

#### drag\_start\_screen\_position

```python
@property
def drag_start_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 拖动开始时的屏幕坐标

<a id="unreal.WdpBasePawn.drag_start_screen_position"></a>

#### drag\_start\_screen\_position

```python
@drag_start_screen_position.setter
def drag_start_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.drag_last_screen_position"></a>

#### drag\_last\_screen\_position

```python
@property
def drag_last_screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 上一帧拖动时的屏幕坐标

<a id="unreal.WdpBasePawn.drag_last_screen_position"></a>

#### drag\_last\_screen\_position

```python
@drag_last_screen_position.setter
def drag_last_screen_position(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.camera_roll"></a>

#### camera\_roll

```python
@property
def camera_roll() -> float
```

(double):  [Read-Write] 当前相机的Roll 单独设置

<a id="unreal.WdpBasePawn.camera_roll"></a>

#### camera\_roll

```python
@camera_roll.setter
def camera_roll(value: float) -> None
```

<a id="unreal.WdpBasePawn.desired_camera_rotation"></a>

#### desired\_camera\_rotation

```python
@property
def desired_camera_rotation() -> Rotator
```

(Rotator):  [Read-Write] 目标的相机旋转位置

<a id="unreal.WdpBasePawn.desired_camera_rotation"></a>

#### desired\_camera\_rotation

```python
@desired_camera_rotation.setter
def desired_camera_rotation(value: Rotator) -> None
```

<a id="unreal.WdpBasePawn.desired_camera_fov"></a>

#### desired\_camera\_fov

```python
@property
def desired_camera_fov() -> float
```

(float):  [Read-Write] 目标相机的FOV

<a id="unreal.WdpBasePawn.desired_camera_fov"></a>

#### desired\_camera\_fov

```python
@desired_camera_fov.setter
def desired_camera_fov(value: float) -> None
```

<a id="unreal.WdpBasePawn.current_camera_fov"></a>

#### current\_camera\_fov

```python
@property
def current_camera_fov() -> float
```

(float):  [Read-Write] 当前的FOV

<a id="unreal.WdpBasePawn.current_camera_fov"></a>

#### current\_camera\_fov

```python
@current_camera_fov.setter
def current_camera_fov(value: float) -> None
```

<a id="unreal.WdpBasePawn.is_rotate_active"></a>

#### is\_rotate\_active

```python
@property
def is_rotate_active() -> bool
```

(bool):  [Read-Write] 旋转是否是激活状态

<a id="unreal.WdpBasePawn.is_rotate_active"></a>

#### is\_rotate\_active

```python
@is_rotate_active.setter
def is_rotate_active(value: bool) -> None
```

<a id="unreal.WdpBasePawn.is_auto_movement_active"></a>

#### is\_auto\_movement\_active

```python
@property
def is_auto_movement_active() -> bool
```

(bool):  [Read-Write] 是否正在启用自动位移

<a id="unreal.WdpBasePawn.is_auto_movement_active"></a>

#### is\_auto\_movement\_active

```python
@is_auto_movement_active.setter
def is_auto_movement_active(value: bool) -> None
```

<a id="unreal.WdpBasePawn.auto_movement_settings"></a>

#### auto\_movement\_settings

```python
@property
def auto_movement_settings() -> AutoMovementSettings
```

(AutoMovementSettings):  [Read-Write] 自动位移的速度 单位：m/s

<a id="unreal.WdpBasePawn.auto_movement_settings"></a>

#### auto\_movement\_settings

```python
@auto_movement_settings.setter
def auto_movement_settings(value: AutoMovementSettings) -> None
```

<a id="unreal.WdpBasePawn.is_auto_rotation_active"></a>

#### is\_auto\_rotation\_active

```python
@property
def is_auto_rotation_active() -> bool
```

(bool):  [Read-Write] 当前是否正在自动绕点旋转

<a id="unreal.WdpBasePawn.is_auto_rotation_active"></a>

#### is\_auto\_rotation\_active

```python
@is_auto_rotation_active.setter
def is_auto_rotation_active(value: bool) -> None
```

<a id="unreal.WdpBasePawn.enable_auto_rotation_after_travel"></a>

#### enable\_auto\_rotation\_after\_travel

```python
@property
def enable_auto_rotation_after_travel() -> bool
```

(bool):  [Read-Write] 当Travel动画结束后是否自动开始相机旋转

<a id="unreal.WdpBasePawn.enable_auto_rotation_after_travel"></a>

#### enable\_auto\_rotation\_after\_travel

```python
@enable_auto_rotation_after_travel.setter
def enable_auto_rotation_after_travel(value: bool) -> None
```

<a id="unreal.WdpBasePawn.auto_rotation_start_min_threshold"></a>

#### auto\_rotation\_start\_min\_threshold

```python
@property
def auto_rotation_start_min_threshold() -> float
```

(float):  [Read-Write] 开始自动旋转的最小Yaw角度值，当动画开始时，只有超过这角度的变化才会自动开启旋转

<a id="unreal.WdpBasePawn.auto_rotation_start_min_threshold"></a>

#### auto\_rotation\_start\_min\_threshold

```python
@auto_rotation_start_min_threshold.setter
def auto_rotation_start_min_threshold(value: float) -> None
```

<a id="unreal.WdpBasePawn.auto_rotation_duration_range"></a>

#### auto\_rotation\_duration\_range

```python
@property
def auto_rotation_duration_range() -> Vector2D
```

(Vector2D):  [Read-Write] 通过Travel产生的自动旋转动画的速度范围，X为最快速度，Y为最慢速度

<a id="unreal.WdpBasePawn.auto_rotation_duration_range"></a>

#### auto\_rotation\_duration\_range

```python
@auto_rotation_duration_range.setter
def auto_rotation_duration_range(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.total_auto_rotate_angle"></a>

#### total\_auto\_rotate\_angle

```python
@property
def total_auto_rotate_angle() -> float
```

(float):  [Read-Only] 当前累计的旋转角度

<a id="unreal.WdpBasePawn.auto_rotate_direction"></a>

#### auto\_rotate\_direction

```python
@property
def auto_rotate_direction() -> int
```

(int32):  [Read-Only] 自动旋转的方向，自动计算，只能等于-1或1，1为顺时针，-1为逆时针

<a id="unreal.WdpBasePawn.auto_rotation_settings"></a>

#### auto\_rotation\_settings

```python
@property
def auto_rotation_settings() -> AutoRotationSettings
```

(AutoRotationSettings):  [Read-Write] 自动旋转的配置参数

<a id="unreal.WdpBasePawn.auto_rotation_settings"></a>

#### auto\_rotation\_settings

```python
@auto_rotation_settings.setter
def auto_rotation_settings(value: AutoRotationSettings) -> None
```

<a id="unreal.WdpBasePawn.is_auto_camera_self_rotation_active"></a>

#### is\_auto\_camera\_self\_rotation\_active

```python
@property
def is_auto_camera_self_rotation_active() -> bool
```

(bool):  [Read-Write] 是否开启相机自身自动旋转，和相机绕点旋转不同

<a id="unreal.WdpBasePawn.is_auto_camera_self_rotation_active"></a>

#### is\_auto\_camera\_self\_rotation\_active

```python
@is_auto_camera_self_rotation_active.setter
def is_auto_camera_self_rotation_active(value: bool) -> None
```

<a id="unreal.WdpBasePawn.auto_camera_self_rotation_settings"></a>

#### auto\_camera\_self\_rotation\_settings

```python
@property
def auto_camera_self_rotation_settings() -> AutoSelfRotationSettings
```

(AutoSelfRotationSettings):  [Read-Write] 相机自身旋转的速度，单位度每秒，X为Pitch方向的旋转，Y为Yaw方向的旋转，正负决定方向

<a id="unreal.WdpBasePawn.auto_camera_self_rotation_settings"></a>

#### auto\_camera\_self\_rotation\_settings

```python
@auto_camera_self_rotation_settings.setter
def auto_camera_self_rotation_settings(
        value: AutoSelfRotationSettings) -> None
```

<a id="unreal.WdpBasePawn.default_trace_channel"></a>

#### default\_trace\_channel

```python
@property
def default_trace_channel() -> TraceTypeQuery
```

(TraceTypeQuery):  [Read-Write] 默认的点击操作检测通道

<a id="unreal.WdpBasePawn.default_trace_channel"></a>

#### default\_trace\_channel

```python
@default_trace_channel.setter
def default_trace_channel(value: TraceTypeQuery) -> None
```

<a id="unreal.WdpBasePawn.ground_trace_channel"></a>

#### ground\_trace\_channel

```python
@property
def ground_trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] 定义"地面"的碰撞通道

<a id="unreal.WdpBasePawn.ground_trace_channel"></a>

#### ground\_trace\_channel

```python
@ground_trace_channel.setter
def ground_trace_channel(value: CollisionChannel) -> None
```

<a id="unreal.WdpBasePawn.ground_trace_object_types"></a>

#### ground\_trace\_object\_types

```python
@property
def ground_trace_object_types() -> Array[ObjectTypeQuery]
```

(Array[ObjectTypeQuery]):  [Read-Write] 定义"地面"的碰撞通道

<a id="unreal.WdpBasePawn.ground_trace_object_types"></a>

#### ground\_trace\_object\_types

```python
@ground_trace_object_types.setter
def ground_trace_object_types(value: Array[ObjectTypeQuery]) -> None
```

<a id="unreal.WdpBasePawn.use_tag_find_ground"></a>

#### use\_tag\_find\_ground

```python
@property
def use_tag_find_ground() -> bool
```

(bool):  [Read-Write] 碰撞检测是否使用Tag查找地面

<a id="unreal.WdpBasePawn.use_tag_find_ground"></a>

#### use\_tag\_find\_ground

```python
@use_tag_find_ground.setter
def use_tag_find_ground(value: bool) -> None
```

<a id="unreal.WdpBasePawn.ground_component_tag"></a>

#### ground\_component\_tag

```python
@property
def ground_component_tag() -> Name
```

(Name):  [Read-Write] 碰撞检测地面时使用的tag

<a id="unreal.WdpBasePawn.ground_component_tag"></a>

#### ground\_component\_tag

```python
@ground_component_tag.setter
def ground_component_tag(value: Name) -> None
```

<a id="unreal.WdpBasePawn.limit_zoom_direction"></a>

#### limit\_zoom\_direction

```python
@property
def limit_zoom_direction() -> bool
```

(bool):  [Read-Write] 是否固定限制缩放方向，如果不限制缩放操作也会产生滑动效果

<a id="unreal.WdpBasePawn.limit_zoom_direction"></a>

#### limit\_zoom\_direction

```python
@limit_zoom_direction.setter
def limit_zoom_direction(value: bool) -> None
```

<a id="unreal.WdpBasePawn.collision_ignore_actors"></a>

#### collision\_ignore\_actors

```python
@property
def collision_ignore_actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] 要忽略的碰撞对象，影响包括射线检测和碰撞检测

<a id="unreal.WdpBasePawn.collision_ignore_actors"></a>

#### collision\_ignore\_actors

```python
@collision_ignore_actors.setter
def collision_ignore_actors(value: Array[Actor]) -> None
```

<a id="unreal.WdpBasePawn.e_animation_blend_features"></a>

#### e\_animation\_blend\_features

```python
@property
def e_animation_blend_features() -> int
```

(int32):  [Read-Write] 启用的动画过度功能

<a id="unreal.WdpBasePawn.e_animation_blend_features"></a>

#### e\_animation\_blend\_features

```python
@e_animation_blend_features.setter
def e_animation_blend_features(value: int) -> None
```

<a id="unreal.WdpBasePawn.is_camera_traveling"></a>

#### is\_camera\_traveling

```python
@property
def is_camera_traveling() -> bool
```

(bool):  [Read-Write] 当前是否相机正在过渡动画中

<a id="unreal.WdpBasePawn.is_camera_traveling"></a>

#### is\_camera\_traveling

```python
@is_camera_traveling.setter
def is_camera_traveling(value: bool) -> None
```

<a id="unreal.WdpBasePawn.anim_start_camera_data"></a>

#### anim\_start\_camera\_data

```python
@property
def anim_start_camera_data() -> CoreCameraData
```

(CoreCameraData):  [Read-Write] 动画过度用，记录动画开始时的相机数据和目标要达到的相机数据

<a id="unreal.WdpBasePawn.anim_start_camera_data"></a>

#### anim\_start\_camera\_data

```python
@anim_start_camera_data.setter
def anim_start_camera_data(value: CoreCameraData) -> None
```

<a id="unreal.WdpBasePawn.anim_target_camera_data"></a>

#### anim\_target\_camera\_data

```python
@property
def anim_target_camera_data() -> CoreCameraData
```

(CoreCameraData):  [Read-Write]

<a id="unreal.WdpBasePawn.anim_target_camera_data"></a>

#### anim\_target\_camera\_data

```python
@anim_target_camera_data.setter
def anim_target_camera_data(value: CoreCameraData) -> None
```

<a id="unreal.WdpBasePawn.travel_animtion_settings"></a>

#### travel\_animtion\_settings

```python
@property
def travel_animtion_settings() -> TravelAnimationSettings
```

(TravelAnimationSettings):  [Read-Write] 如何进行Travel动画的定义，包括是否使用曲线运动和路径的计算等

<a id="unreal.WdpBasePawn.travel_animtion_settings"></a>

#### travel\_animtion\_settings

```python
@travel_animtion_settings.setter
def travel_animtion_settings(value: TravelAnimationSettings) -> None
```

<a id="unreal.WdpBasePawn.travel_spline_component"></a>

#### travel\_spline\_component

```python
@property
def travel_spline_component() -> SplineComponent
```

(SplineComponent):  [Read-Write] 相机运动动画的Spline Component

<a id="unreal.WdpBasePawn.travel_spline_component"></a>

#### travel\_spline\_component

```python
@travel_spline_component.setter
def travel_spline_component(value: SplineComponent) -> None
```

<a id="unreal.WdpBasePawn.travel_pivot_spline_component"></a>

#### travel\_pivot\_spline\_component

```python
@property
def travel_pivot_spline_component() -> SplineComponent
```

(SplineComponent):  [Read-Write] 相机运动动画Pivot的Spline Component

<a id="unreal.WdpBasePawn.travel_pivot_spline_component"></a>

#### travel\_pivot\_spline\_component

```python
@travel_pivot_spline_component.setter
def travel_pivot_spline_component(value: SplineComponent) -> None
```

<a id="unreal.WdpBasePawn.travel_anim_duration"></a>

#### travel\_anim\_duration

```python
@property
def travel_anim_duration() -> float
```

(float):  [Read-Write] Travel 动画时长

<a id="unreal.WdpBasePawn.travel_anim_duration"></a>

#### travel\_anim\_duration

```python
@travel_anim_duration.setter
def travel_anim_duration(value: float) -> None
```

<a id="unreal.WdpBasePawn.final_camera_data"></a>

#### final\_camera\_data

```python
@property
def final_camera_data() -> AllCameraData
```

(AllCameraData):  [Read-Write] 最终Apply的动画数据，有需求时先对这个数据做修改，再传给Apply函数

<a id="unreal.WdpBasePawn.final_camera_data"></a>

#### final\_camera\_data

```python
@final_camera_data.setter
def final_camera_data(value: AllCameraData) -> None
```

<a id="unreal.WdpBasePawn.auto_travel_duration_range"></a>

#### auto\_travel\_duration\_range

```python
@property
def auto_travel_duration_range() -> Vector2D
```

(Vector2D):  [Read-Write] 自动计算时长的时间范围限制，避免计算出的时间过长或过短

<a id="unreal.WdpBasePawn.auto_travel_duration_range"></a>

#### auto\_travel\_duration\_range

```python
@auto_travel_duration_range.setter
def auto_travel_duration_range(value: Vector2D) -> None
```

<a id="unreal.WdpBasePawn.on_travel_animation_finished"></a>

#### on\_travel\_animation\_finished

```python
@property
def on_travel_animation_finished() -> OnTravelAnimationFinished
```

(OnTravelAnimationFinished):  [Read-Write]

<a id="unreal.WdpBasePawn.on_travel_animation_finished"></a>

#### on\_travel\_animation\_finished

```python
@on_travel_animation_finished.setter
def on_travel_animation_finished(value: OnTravelAnimationFinished) -> None
```

<a id="unreal.WdpBasePawn.is_following_actor"></a>

#### is\_following\_actor

```python
@property
def is_following_actor() -> bool
```

(bool):  [Read-Write] 是否在跟踪Actor

<a id="unreal.WdpBasePawn.is_following_actor"></a>

#### is\_following\_actor

```python
@is_following_actor.setter
def is_following_actor(value: bool) -> None
```

<a id="unreal.WdpBasePawn.following_mode"></a>

#### following\_mode

```python
@property
def following_mode() -> FollowingMode
```

(FollowingMode):  [Read-Write] 跟踪的处理模式

<a id="unreal.WdpBasePawn.following_mode"></a>

#### following\_mode

```python
@following_mode.setter
def following_mode(value: FollowingMode) -> None
```

<a id="unreal.WdpBasePawn.following_actor"></a>

#### following\_actor

```python
@property
def following_actor() -> Actor
```

(Actor):  [Read-Write] 被跟踪的对象Actor

<a id="unreal.WdpBasePawn.following_actor"></a>

#### following\_actor

```python
@following_actor.setter
def following_actor(value: Actor) -> None
```

<a id="unreal.WdpBasePawn.following_time"></a>

#### following\_time

```python
@property
def following_time() -> float
```

(float):  [Read-Write] 跟踪持续的时长

<a id="unreal.WdpBasePawn.following_time"></a>

#### following\_time

```python
@following_time.setter
def following_time(value: float) -> None
```

<a id="unreal.WdpBasePawn.following_actor_last_location"></a>

#### following\_actor\_last\_location

```python
@property
def following_actor_last_location() -> Vector
```

(Vector):  [Read-Write] 上一帧Follow对象的位置

<a id="unreal.WdpBasePawn.following_actor_last_location"></a>

#### following\_actor\_last\_location

```python
@following_actor_last_location.setter
def following_actor_last_location(value: Vector) -> None
```

<a id="unreal.WdpBasePawn.auto_follow_when_un_possessed"></a>

#### auto\_follow\_when\_un\_possessed

```python
@property
def auto_follow_when_un_possessed() -> bool
```

(bool):  [Read-Write] 当pawn不被控制时是否自动跟随CameraManger移动

<a id="unreal.WdpBasePawn.auto_follow_when_un_possessed"></a>

#### auto\_follow\_when\_un\_possessed

```python
@auto_follow_when_un_possessed.setter
def auto_follow_when_un_possessed(value: bool) -> None
```

<a id="unreal.WdpBasePawn.auto_follow_when_not_being_view_target"></a>

#### auto\_follow\_when\_not\_being\_view\_target

```python
@property
def auto_follow_when_not_being_view_target() -> bool
```

(bool):  [Read-Write] 是否在View Target不是自身的时候将镜头与当前Controller的View Target 同步

<a id="unreal.WdpBasePawn.auto_follow_when_not_being_view_target"></a>

#### auto\_follow\_when\_not\_being\_view\_target

```python
@auto_follow_when_not_being_view_target.setter
def auto_follow_when_not_being_view_target(value: bool) -> None
```

<a id="unreal.WdpBasePawn.update_virtual_pivot"></a>

#### update\_virtual\_pivot

```python
def update_virtual_pivot() -> None
```

x.update_virtual_pivot() -> None
更新VirtualPivot

<a id="unreal.WdpBasePawn.update_travel_animation"></a>

#### update\_travel\_animation

```python
def update_travel_animation(alpha: float) -> None
```

x.update_travel_animation(alpha) -> None
更新动画逻辑 根据Feature过渡参数

Args:
    alpha (float):

<a id="unreal.WdpBasePawn.update_start_auto_rotation_after_travel"></a>

#### update\_start\_auto\_rotation\_after\_travel

```python
def update_start_auto_rotation_after_travel(target_rotation: Rotator,
                                            duration: float) -> None
```

x.update_start_auto_rotation_after_travel(target_rotation, duration) -> None
检测是否自动开启自动旋转动画

Args:
    target_rotation (Rotator): 
    duration (float):

<a id="unreal.WdpBasePawn.update_runtime_camera_data"></a>

#### update\_runtime\_camera\_data

```python
def update_runtime_camera_data() -> None
```

x.update_runtime_camera_data() -> None
更新运行时相机数据

<a id="unreal.WdpBasePawn.update_rotate_pivot_by_movement"></a>

#### update\_rotate\_pivot\_by\_movement

```python
def update_rotate_pivot_by_movement(start_camera_location: Vector,
                                    camera_surface_delta: Vector,
                                    camera_height_delta: Vector) -> None
```

x.update_rotate_pivot_by_movement(start_camera_location, camera_surface_delta, camera_height_delta) -> None
Pivot 坐标更新逻辑

Args:
    start_camera_location (Vector): 
    camera_surface_delta (Vector): 
    camera_height_delta (Vector):

<a id="unreal.WdpBasePawn.update_mouse_drag"></a>

#### update\_mouse\_drag

```python
def update_mouse_drag(screen_position: Vector2D) -> None
```

x.update_mouse_drag(screen_position) -> None
更新相机拖动计算

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.update_idle_time"></a>

#### update\_idle\_time

```python
def update_idle_time() -> None
```

x.update_idle_time() -> None
在Tick中更新闲置时间

<a id="unreal.WdpBasePawn.update_debug_status"></a>

#### update\_debug\_status

```python
def update_debug_status() -> None
```

x.update_debug_status() -> None
更新屏幕状态信息Log

<a id="unreal.WdpBasePawn.update_debug_shapes"></a>

#### update\_debug\_shapes

```python
def update_debug_shapes() -> None
```

x.update_debug_shapes() -> None
更新绘制的Debug图形

<a id="unreal.WdpBasePawn.update_camera_rotation"></a>

#### update\_camera\_rotation

```python
def update_camera_rotation(new_rotation: Rotator) -> None
```

x.update_camera_rotation(new_rotation) -> None
设置当前相机的角度，同时设置pawn的角度

Args:
    new_rotation (Rotator):

<a id="unreal.WdpBasePawn.update_camera_location"></a>

#### update\_camera\_location

```python
def update_camera_location(new_location: Vector) -> None
```

x.update_camera_location(new_location) -> None
设置当前相机的位置

Args:
    new_location (Vector):

<a id="unreal.WdpBasePawn.update_camera_instant"></a>

#### update\_camera\_instant

```python
def update_camera_instant(camera_data: CoreCameraData) -> bool
```

x.update_camera_instant(camera_data) -> bool
瞬时设置相机数据

Args:
    camera_data (CoreCameraData): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.update_camera_fov"></a>

#### update\_camera\_fov

```python
def update_camera_fov(desired_fov: float = 90.000000,
                      ignore_lag: bool = False) -> None
```

x.update_camera_fov(desired_fov=90.000000, ignore_lag=False) -> None
更新FOV函数

Args:
    desired_fov (float): 
    ignore_lag (bool):

<a id="unreal.WdpBasePawn.update_auto_rotation"></a>

#### update\_auto\_rotation

```python
def update_auto_rotation() -> None
```

x.update_auto_rotation() -> None
更新自动旋转逻辑

<a id="unreal.WdpBasePawn.update_auto_movement"></a>

#### update\_auto\_movement

```python
def update_auto_movement() -> None
```

x.update_auto_movement() -> None
更新自动位移

<a id="unreal.WdpBasePawn.update_auto_camera_self_rotation"></a>

#### update\_auto\_camera\_self\_rotation

```python
def update_auto_camera_self_rotation() -> None
```

x.update_auto_camera_self_rotation() -> None
更新相机自身旋转

<a id="unreal.WdpBasePawn.toggle_speed_up"></a>

#### toggle\_speed\_up

```python
def toggle_speed_up(boost: float) -> None
```

x.toggle_speed_up(boost) -> None
冲刺键切换

Args:
    boost (float):

<a id="unreal.WdpBasePawn.toggle_show_debug"></a>

#### toggle\_show\_debug

```python
def toggle_show_debug(show_log: bool, show_status: bool,
                      show_shapes: bool) -> None
```

x.toggle_show_debug(show_log, show_status, show_shapes) -> None
切换debug开关

Args:
    show_log (bool): 
    show_status (bool): 
    show_shapes (bool):

<a id="unreal.WdpBasePawn.toggle_self_rotate_key_pressed"></a>

#### toggle\_self\_rotate\_key\_pressed

```python
def toggle_self_rotate_key_pressed(pressed: bool) -> None
```

x.toggle_self_rotate_key_pressed(pressed) -> None
相机自身旋转按键切换开关

Args:
    pressed (bool):

<a id="unreal.WdpBasePawn.toggle_rotating_active"></a>

#### toggle\_rotating\_active

```python
def toggle_rotating_active(activate: bool) -> None
```

x.toggle_rotating_active(activate) -> None
是否切换旋转 右键按下时也可能不会开始旋转 所以单独分离

Args:
    activate (bool):

<a id="unreal.WdpBasePawn.toggle_mouse_drag"></a>

#### toggle\_mouse\_drag

```python
def toggle_mouse_drag(activate: bool) -> None
```

x.toggle_mouse_drag(activate) -> None
激活鼠标拖动移动

Args:
    activate (bool):

<a id="unreal.WdpBasePawn.toggle_following_actor"></a>

#### toggle\_following\_actor

```python
def toggle_following_actor(target_actor: Actor, follow: bool) -> None
```

x.toggle_following_actor(target_actor, follow) -> None
切换是否跟踪对象

Args:
    target_actor (Actor): 
    follow (bool):

<a id="unreal.WdpBasePawn.toggle_auto_rotation"></a>

#### toggle\_auto\_rotation

```python
def toggle_auto_rotation(active: bool, settings: AutoRotationSettings) -> bool
```

x.toggle_auto_rotation(active, settings) -> bool
切换自动旋转

Args:
    active (bool): 
    settings (AutoRotationSettings): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.toggle_auto_movement"></a>

#### toggle\_auto\_movement

```python
def toggle_auto_movement(active: bool, settings: AutoMovementSettings) -> bool
```

x.toggle_auto_movement(active, settings) -> bool
设置自动位移 速度单位：m/s

Args:
    active (bool): 
    settings (AutoMovementSettings): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.toggle_auto_camera_self_rotation"></a>

#### toggle\_auto\_camera\_self\_rotation

```python
def toggle_auto_camera_self_rotation(
        active: bool, settings: AutoSelfRotationSettings) -> None
```

x.toggle_auto_camera_self_rotation(active, settings) -> None
切换相机自身旋转 单位度每秒，X为Pitch方向的旋转，Y为Yaw方向的旋转

Args:
    active (bool): 
    settings (AutoSelfRotationSettings):

<a id="unreal.WdpBasePawn.tick_camera"></a>

#### tick\_camera

```python
def tick_camera() -> None
```

x.tick_camera() -> None
相机更新核心函数

<a id="unreal.WdpBasePawn.stop_mouse_drag"></a>

#### stop\_mouse\_drag

```python
def stop_mouse_drag() -> None
```

x.stop_mouse_drag() -> None
结束相机拖动计算

<a id="unreal.WdpBasePawn.stop_following_actor"></a>

#### stop\_following\_actor

```python
def stop_following_actor() -> None
```

x.stop_following_actor() -> None
停止跟踪

<a id="unreal.WdpBasePawn.stop_camera_auto_rotation"></a>

#### stop\_camera\_auto\_rotation

```python
def stop_camera_auto_rotation() -> None
```

x.stop_camera_auto_rotation() -> None
停止自动旋转函数

<a id="unreal.WdpBasePawn.stop_camera_auto_movement"></a>

#### stop\_camera\_auto\_movement

```python
def stop_camera_auto_movement() -> None
```

x.stop_camera_auto_movement() -> None
停止自动位移

<a id="unreal.WdpBasePawn.stop_auto_camera_self_rotation"></a>

#### stop\_auto\_camera\_self\_rotation

```python
def stop_auto_camera_self_rotation() -> None
```

x.stop_auto_camera_self_rotation() -> None
停止相机自身旋转

<a id="unreal.WdpBasePawn.stop_all_camera_movement"></a>

#### stop\_all\_camera\_movement

```python
def stop_all_camera_movement() -> None
```

x.stop_all_camera_movement() -> None
停止全部的相机运动，包括插值

<a id="unreal.WdpBasePawn.start_travel_animation"></a>

#### start\_travel\_animation

```python
def start_travel_animation(target_data: AllCameraData,
                           settings: TravelAnimationSettings,
                           duration: float = 1.200000) -> None
```

x.start_travel_animation(target_data, settings, duration=1.200000) -> None
需要传入目标的相机数据，动画时长，相机动画的运行方式 **//暂时在蓝图中实现

Args:
    target_data (AllCameraData): 
    settings (TravelAnimationSettings): 
    duration (float):

<a id="unreal.WdpBasePawn.start_mouse_drag"></a>

#### start\_mouse\_drag

```python
def start_mouse_drag(screen_position: Vector2D) -> None
```

x.start_mouse_drag(screen_position) -> None
开始相机拖动计算

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.start_following_actor"></a>

#### start\_following\_actor

```python
def start_following_actor(
        target_actor: Actor,
        follow_mode: FollowingMode = FollowingMode.FM_TRACKING_LIGHT,
        duration: float = 1.200000) -> None
```

x.start_following_actor(target_actor, follow_mode=FollowingMode.FM_TRACKING_LIGHT, duration=1.200000) -> None
进入以动画方式跟踪

Args:
    target_actor (Actor): 
    follow_mode (FollowingMode): 
    duration (float):

<a id="unreal.WdpBasePawn.sphere_trace_move_by_profile"></a>

#### sphere\_trace\_move\_by\_profile

```python
def sphere_trace_move_by_profile(start: Vector, end: Vector,
                                 profile_name: Name) -> Optional[HitResult]
```

x.sphere_trace_move_by_profile(start, end, profile_name) -> HitResult or None
使用Collision Profile 检测Pawn移动时的碰撞

Args:
    start (Vector): 
    end (Vector): 
    profile_name (Name): 

Returns:
    HitResult or None: 

    out_hit (HitResult):

<a id="unreal.WdpBasePawn.single_sphere_trace_ground"></a>

#### single\_sphere\_trace\_ground

```python
def single_sphere_trace_ground(start: Vector,
                               end: Vector) -> Optional[HitResult]
```

x.single_sphere_trace_ground(start, end) -> HitResult or None
针对地面碰撞的检测 Single

Args:
    start (Vector): 
    end (Vector): 

Returns:
    HitResult or None: 

    out_hit (HitResult):

<a id="unreal.WdpBasePawn.should_update_arm_collision"></a>

#### should\_update\_arm\_collision

```python
def should_update_arm_collision() -> bool
```

x.should_update_arm_collision() -> bool
判断是否要进行旋转碰撞检测

Returns:
    bool:

<a id="unreal.WdpBasePawn.should_enable_move_collision"></a>

#### should\_enable\_move\_collision

```python
def should_enable_move_collision() -> bool
```

x.should_enable_move_collision() -> bool
判断是否需要移动的碰撞更新

Returns:
    bool:

<a id="unreal.WdpBasePawn.should_auto_update_pivot"></a>

#### should\_auto\_update\_pivot

```python
def should_auto_update_pivot() -> bool
```

x.should_auto_update_pivot() -> bool
判断是否需要进行Pivot坐标动态更新

Returns:
    bool:

<a id="unreal.WdpBasePawn.set_world_plane_height"></a>

#### set\_world\_plane\_height

```python
def set_world_plane_height(new_height: float) -> None
```

x.set_world_plane_height(new_height) -> None
设置操作虚拟平面的高度

Args:
    new_height (double):

<a id="unreal.WdpBasePawn.set_virtual_pivot_location"></a>

#### set\_virtual\_pivot\_location

```python
def set_virtual_pivot_location(new_pivot: Vector) -> None
```

x.set_virtual_pivot_location(new_pivot) -> None
更新虚拟点位的位置

Args:
    new_pivot (Vector):

<a id="unreal.WdpBasePawn.set_rotate_pivot"></a>

#### set\_rotate\_pivot

```python
def set_rotate_pivot(new_pivot: Vector) -> None
```

x.set_rotate_pivot(new_pivot) -> None
设置旋转Pivot，储存在CoreCameraData中

Args:
    new_pivot (Vector):

<a id="unreal.WdpBasePawn.set_enabled_features"></a>

#### set\_enabled\_features

```python
def set_enabled_features(features_to_enable: int) -> None
```

x.set_enabled_features(features_to_enable) -> None
直接设置Feature内容

Args:
    features_to_enable (int32):

<a id="unreal.WdpBasePawn.set_desired_fov"></a>

#### set\_desired\_fov

```python
def set_desired_fov(new_fov: float = 90.000000,
                    ignore_lag: bool = False) -> None
```

x.set_desired_fov(new_fov=90.000000, ignore_lag=False) -> None
设置目标相机的FOV

Args:
    new_fov (float): 
    ignore_lag (bool):

<a id="unreal.WdpBasePawn.set_camera_rotate_mode"></a>

#### set\_camera\_rotate\_mode

```python
def set_camera_rotate_mode(new_mode: CameraRotateMode) -> None
```

x.set_camera_rotate_mode(new_mode) -> None
切换相机旋转的方式

Args:
    new_mode (CameraRotateMode):

<a id="unreal.WdpBasePawn.set_camera_free_movement_desired_location"></a>

#### set\_camera\_free\_movement\_desired\_location

```python
def set_camera_free_movement_desired_location(
        desired_location: Vector) -> None
```

x.set_camera_free_movement_desired_location(desired_location) -> None
缓动动画用，设置相机的自由移动的目标位置

Args:
    desired_location (Vector):

<a id="unreal.WdpBasePawn.set_camera_desired_self_rotation_surface_space"></a>

#### set\_camera\_desired\_self\_rotation\_surface\_space

```python
def set_camera_desired_self_rotation_surface_space(
        desired_location: Vector, desired_surface_rotation: Rotator) -> None
```

x.set_camera_desired_self_rotation_surface_space(desired_location, desired_surface_rotation) -> None
以球的表面空间旋转设置相机自身旋转的目标角度

Args:
    desired_location (Vector): 
    desired_surface_rotation (Rotator):

<a id="unreal.WdpBasePawn.set_camera_desired_self_rotation"></a>

#### set\_camera\_desired\_self\_rotation

```python
def set_camera_desired_self_rotation(desired_rotation: Rotator) -> None
```

x.set_camera_desired_self_rotation(desired_rotation) -> None
设置相机自身旋转的目标角度

Args:
    desired_rotation (Rotator):

<a id="unreal.WdpBasePawn.safe_move_pawn_by_collision"></a>

#### safe\_move\_pawn\_by\_collision

```python
def safe_move_pawn_by_collision(
        start: Vector,
        delta: Vector,
        profile_name: Name,
        sweep: bool,
        ground_only: bool = False) -> Tuple[Vector, HitResult]
```

x.safe_move_pawn_by_collision(start, delta, profile_name, sweep, ground_only=False) -> (Vector, out_hit=HitResult)
计算一次安全移动的碰撞检测结果 输出HitResult和实际移动了的Delta

Args:
    start (Vector): 
    delta (Vector): 
    profile_name (Name): 
    sweep (bool): 
    ground_only (bool): 

Returns:
    HitResult: 

    out_hit (HitResult):

<a id="unreal.WdpBasePawn.reset_idle_time"></a>

#### reset\_idle\_time

```python
def reset_idle_time() -> None
```

x.reset_idle_time() -> None
重置闲置时间

<a id="unreal.WdpBasePawn.remove_input_mapping"></a>

#### remove\_input\_mapping

```python
def remove_input_mapping() -> None
```

x.remove_input_mapping() -> None
移除输入Mapping的注册

<a id="unreal.WdpBasePawn.remove_collision_ignore_actor"></a>

#### remove\_collision\_ignore\_actor

```python
def remove_collision_ignore_actor(actor: Actor) -> None
```

x.remove_collision_ignore_actor(actor) -> None
移除要忽略碰撞的对象

Args:
    actor (Actor):

<a id="unreal.WdpBasePawn.print_debug_string"></a>

#### print\_debug\_string

```python
def print_debug_string(
    string: str = "Debug",
    duration: float = 2.000000,
    text_color: LinearColor = [0.000000, 0.660000, 1.000000,
                               1.000000]) -> None
```

x.print_debug_string(string="Debug", duration=2.000000, text_color=[0.000000, 0.660000, 1.000000, 1.000000]) -> None
打印log

Args:
    string (str): 
    duration (float): 
    text_color (LinearColor):

<a id="unreal.WdpBasePawn.on_zoom_key_released"></a>

#### on\_zoom\_key\_released

```python
def on_zoom_key_released() -> None
```

x.on_zoom_key_released() -> None
缩放事件开始

<a id="unreal.WdpBasePawn.on_zoom_key_pressed"></a>

#### on\_zoom\_key\_pressed

```python
def on_zoom_key_pressed(screen_position: Vector2D) -> None
```

x.on_zoom_key_pressed(screen_position) -> None
缩放事件开始

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.on_rotate_key_released"></a>

#### on\_rotate\_key\_released

```python
def on_rotate_key_released() -> None
```

x.on_rotate_key_released() -> None
旋转点击结束事件

<a id="unreal.WdpBasePawn.on_rotate_key_pressed"></a>

#### on\_rotate\_key\_pressed

```python
def on_rotate_key_pressed(screen_position: Vector2D) -> None
```

x.on_rotate_key_pressed(screen_position) -> None
旋转点击开始事件

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.on_pointer_key_released"></a>

#### on\_pointer\_key\_released

```python
def on_pointer_key_released() -> None
```

x.on_pointer_key_released() -> None
触屏左键松开事件

<a id="unreal.WdpBasePawn.on_pointer_key_pressed"></a>

#### on\_pointer\_key\_pressed

```python
def on_pointer_key_pressed(screen_position: Vector2D) -> None
```

x.on_pointer_key_pressed(screen_position) -> None
左键(Pointer)点击事件 所有事件的入口

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.on_pointer_key_move"></a>

#### on\_pointer\_key\_move

```python
def on_pointer_key_move(screen_position: Vector2D) -> None
```

x.on_pointer_key_move(screen_position) -> None
左键移动事件

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.on_double_click_triggered"></a>

#### on\_double\_click\_triggered

```python
def on_double_click_triggered(screen_position: Vector2D) -> None
```

x.on_double_click_triggered(screen_position) -> None
双击事件

Args:
    screen_position (Vector2D):

<a id="unreal.WdpBasePawn.limit_camera_yaw"></a>

#### limit\_camera\_yaw

```python
def limit_camera_yaw(view_rotation: Rotator,
                     view_yaw_min: float = -179.998993,
                     view_yaw_max: float = 179.998993) -> Rotator
```

x.limit_camera_yaw(view_rotation, view_yaw_min=-179.998993, view_yaw_max=179.998993) -> Rotator
限制相机Yaw

Args:
    view_rotation (Rotator): 
    view_yaw_min (float): 
    view_yaw_max (float): 

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.limit_camera_pitch"></a>

#### limit\_camera\_pitch

```python
def limit_camera_pitch(view_rotation: Rotator,
                       view_pitch_min: float = -89.000000,
                       view_pitch_max: float = 89.000000) -> Rotator
```

x.limit_camera_pitch(view_rotation, view_pitch_min=-89.000000, view_pitch_max=89.000000) -> Rotator
限制相机Pitch

Args:
    view_rotation (Rotator): 
    view_pitch_min (float): 
    view_pitch_max (float): 

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.is_self_rotate_key_pressed"></a>

#### is\_self\_rotate\_key\_pressed

```python
def is_self_rotate_key_pressed() -> bool
```

x.is_self_rotate_key_pressed() -> bool
获取当前是否按下了自身旋转按键

Returns:
    bool:

<a id="unreal.WdpBasePawn.is_point_in_custom_points_range"></a>

#### is\_point\_in\_custom\_points\_range

```python
def is_point_in_custom_points_range(point: Vector,
                                    custom_points: Array[Vector]) -> bool
```

x.is_point_in_custom_points_range(point, custom_points) -> bool
判断一个点是否在点的碰撞区域范围内部，按照边界判断规则

Args:
    point (Vector): 
    custom_points (Array[Vector]): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.is_pointer_in_valid_dragging_position"></a>

#### is\_pointer\_in\_valid\_dragging\_position

```python
def is_pointer_in_valid_dragging_position(direction: Vector) -> bool
```

x.is_pointer_in_valid_dragging_position(direction) -> bool
判断目前Pointer的位置是否允许进行Drag操作

Args:
    direction (Vector): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.is_following_any_actor"></a>

#### is\_following\_any\_actor

```python
def is_following_any_actor() -> bool
```

x.is_following_any_actor() -> bool
Is Following Any Actor

Returns:
    bool:

<a id="unreal.WdpBasePawn.init_world_origin_anchor"></a>

#### init\_world\_origin\_anchor

```python
def init_world_origin_anchor() -> None
```

x.init_world_origin_anchor() -> None
查找世界坐标锚点，用于支持球面操作

<a id="unreal.WdpBasePawn.init_virtual_pivot_location"></a>

#### init\_virtual\_pivot\_location

```python
def init_virtual_pivot_location() -> None
```

x.init_virtual_pivot_location() -> None
在初始化时寻找一个合适的Pivot点位，会首先检测地面，如果地面不存在会建立一个默认的虚拟平面

<a id="unreal.WdpBasePawn.init_travel_animation"></a>

#### init\_travel\_animation

```python
def init_travel_animation() -> None
```

x.init_travel_animation() -> None
初始化Travel动画数据，记录动画开始时的状态

<a id="unreal.WdpBasePawn.init_starting_position"></a>

#### init\_starting\_position

```python
def init_starting_position() -> None
```

x.init_starting_position() -> None
执行初始化设置

<a id="unreal.WdpBasePawn.init_pawn_settings"></a>

#### init\_pawn\_settings

```python
def init_pawn_settings() -> None
```

x.init_pawn_settings() -> None
初始化Pawn参数

<a id="unreal.WdpBasePawn.init_input_mapping"></a>

#### init\_input\_mapping

```python
def init_input_mapping() -> None
```

x.init_input_mapping() -> None
将输入事件Mapping注册到Controller，控制多个Pawn时需要

<a id="unreal.WdpBasePawn.get_zoom_limit"></a>

#### get\_zoom\_limit

```python
def get_zoom_limit() -> Vector2D
```

x.get_zoom_limit() -> Vector2D
获取缩放的最大最小值

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_zoom_direction"></a>

#### get\_zoom\_direction

```python
def get_zoom_direction() -> Vector
```

x.get_zoom_direction() -> Vector
获取目标的缩放方向 首先要拿到Desired的坐标

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_yaw_limit"></a>

#### get\_yaw\_limit

```python
def get_yaw_limit() -> Vector2D
```

x.get_yaw_limit() -> Vector2D
计算Yaw的角度限制 X为最小值，Y为最大值

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_world_rotation_on_surface"></a>

#### get\_world\_rotation\_on\_surface

```python
def get_world_rotation_on_surface(origin: Vector) -> Rotator
```

x.get_world_rotation_on_surface(origin) -> Rotator
根据一个点，获取这个点的世界平面旋转，也就是东北天坐标系

Args:
    origin (Vector): 

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.get_world_plane_normal_at_location"></a>

#### get\_world\_plane\_normal\_at\_location

```python
def get_world_plane_normal_at_location(location: Vector) -> Vector
```

x.get_world_plane_normal_at_location(location) -> Vector
获取世界某一位置上的平面方向

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_world_plane_normal"></a>

#### get\_world\_plane\_normal

```python
def get_world_plane_normal() -> Vector
```

x.get_world_plane_normal() -> Vector
获取世界平面的方向

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_true_desired_location"></a>

#### get\_true\_desired\_location

```python
def get_true_desired_location() -> Vector
```

x.get_true_desired_location() -> Vector
计算真正的DesiredLocation，包括缓动的变量+缩放的插值

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_start_rotate_pivot"></a>

#### get\_start\_rotate\_pivot

```python
def get_start_rotate_pivot(rotate_mode: CameraRotateMode) -> Optional[Vector]
```

x.get_start_rotate_pivot(rotate_mode) -> Vector or None
获取开始旋转时的旋转中心点

Args:
    rotate_mode (CameraRotateMode): 

Returns:
    Vector or None: 

    start_pivot_location (Vector):

<a id="unreal.WdpBasePawn.get_speed"></a>

#### get\_speed

```python
def get_speed() -> float
```

x.get_speed() -> double
获取当前相机的移动速度 单位: m/s

Returns:
    double:

<a id="unreal.WdpBasePawn.get_screen_position_hit_result"></a>

#### get\_screen\_position\_hit\_result

```python
def get_screen_position_hit_result(
        screen_position: Vector2D,
        trace_channel: TraceTypeQuery) -> Optional[HitResult]
```

x.get_screen_position_hit_result(screen_position, trace_channel) -> HitResult or None
获取屏幕坐标点的HitResult（基于TraceChannel）

Args:
    screen_position (Vector2D): 
    trace_channel (TraceTypeQuery): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_screen_center_position"></a>

#### get\_screen\_center\_position

```python
def get_screen_center_position() -> Vector2D
```

x.get_screen_center_position() -> Vector2D
获取屏幕正中间的像素位置

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_screen_center_object_hit_result"></a>

#### get\_screen\_center\_object\_hit\_result

```python
def get_screen_center_object_hit_result(
        object_types: Array[ObjectTypeQuery]) -> Optional[HitResult]
```

x.get_screen_center_object_hit_result(object_types) -> HitResult or None
获取屏幕中心点的HitResult（基于ObjectCollision）

Args:
    object_types (Array[ObjectTypeQuery]): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_screen_center_hit_result"></a>

#### get\_screen\_center\_hit\_result

```python
def get_screen_center_hit_result(
        trace_channel: TraceTypeQuery) -> Optional[HitResult]
```

x.get_screen_center_hit_result(trace_channel) -> HitResult or None
获取屏幕中心点的HitResult（基于TraceChannel）

Args:
    trace_channel (TraceTypeQuery): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_safe_click_location_on_plane"></a>

#### get\_safe\_click\_location\_on\_plane

```python
def get_safe_click_location_on_plane(fallback_height: float) -> Vector
```

x.get_safe_click_location_on_plane(fallback_height) -> Vector
获取安全的点击坐标，如果结果为False还会回退到Fallback的平面高度上

Args:
    fallback_height (double): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_rotate_pivot"></a>

#### get\_rotate\_pivot

```python
def get_rotate_pivot() -> Vector
```

x.get_rotate_pivot() -> Vector
使用函数替换变量，获取旋转时的Pivot，储存在CoreCameraData中

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_pitch_limit"></a>

#### get\_pitch\_limit

```python
def get_pitch_limit() -> Vector2D
```

x.get_pitch_limit() -> Vector2D
计算Pitch的角度限制 X为最小值，Y为最大值

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_movement_scale_factor"></a>

#### get\_movement\_scale\_factor

```python
def get_movement_scale_factor() -> float
```

x.get_movement_scale_factor() -> double
Movement 行为的速度放大倍率，

Returns:
    double:

<a id="unreal.WdpBasePawn.get_mouse_target_direction"></a>

#### get\_mouse\_target\_direction

```python
def get_mouse_target_direction(force_center: bool) -> Vector
```

x.get_mouse_target_direction(force_center) -> Vector
获取鼠标位置的法线方向//
Force: Center:强制使用屏幕中心方向

Args:
    force_center (bool): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_main_camera_rotation"></a>

#### get\_main\_camera\_rotation

```python
def get_main_camera_rotation() -> Rotator
```

x.get_main_camera_rotation() -> Rotator
获取主相机相机旋转

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.get_main_camera_location"></a>

#### get\_main\_camera\_location

```python
def get_main_camera_location() -> Vector
```

x.get_main_camera_location() -> Vector
获取主相机的位置

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_main_camera_fov"></a>

#### get\_main\_camera\_fov

```python
def get_main_camera_fov() -> float
```

x.get_main_camera_fov() -> float
获取主相机的FOV

Returns:
    float:

<a id="unreal.WdpBasePawn.get_main_camera_forward_vector"></a>

#### get\_main\_camera\_forward\_vector

```python
def get_main_camera_forward_vector() -> Vector
```

x.get_main_camera_forward_vector() -> Vector
获取主相机的朝向

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_last_conformed_zoom_location"></a>

#### get\_last\_conformed\_zoom\_location

```python
def get_last_conformed_zoom_location() -> Vector
```

x.get_last_conformed_zoom_location() -> Vector
获取最后一次确认的目标的缩放点位

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_is_view_target"></a>

#### get\_is\_view\_target

```python
def get_is_view_target() -> bool
```

x.get_is_view_target() -> bool
当前的ViewTarget是否是自身

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_is_pointer_on_valid_dragging_position"></a>

#### get\_is\_pointer\_on\_valid\_dragging\_position

```python
def get_is_pointer_on_valid_dragging_position() -> bool
```

x.get_is_pointer_on_valid_dragging_position() -> bool
检测当前的鼠标Pointer位置是否在安全范围内并决定是否开启Dragging

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_is_earth_mode"></a>

#### get\_is\_earth\_mode

```python
def get_is_earth_mode() -> bool
```

x.get_is_earth_mode() -> bool
是否为地球操作模式

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_is_active_dargging"></a>

#### get\_is\_active\_dargging

```python
def get_is_active_dargging() -> bool
```

x.get_is_active_dargging() -> bool
是否开启鼠标拖动判断 可以添加更复杂的逻辑

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_fov_limit"></a>

#### get\_fov\_limit

```python
def get_fov_limit() -> Vector2D
```

x.get_fov_limit() -> Vector2D
获取相机的FOV变化最大最小值

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_following_zoom_limit"></a>

#### get\_following\_zoom\_limit

```python
def get_following_zoom_limit() -> Vector2D
```

x.get_following_zoom_limit() -> Vector2D
获取跟踪时的相机距离限制范围

Returns:
    Vector2D:

<a id="unreal.WdpBasePawn.get_following_target_location"></a>

#### get\_following\_target\_location

```python
def get_following_target_location() -> Vector
```

x.get_following_target_location() -> Vector
获取被跟踪对象的坐标，因为对象不一定等于物体本身

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_enable_user_input"></a>

#### get\_enable\_user\_input

```python
def get_enable_user_input() -> bool
```

x.get_enable_user_input() -> bool
是否允许用户输入

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_enable_touch_effect"></a>

#### get\_enable\_touch\_effect

```python
def get_enable_touch_effect() -> bool
```

x.get_enable_touch_effect() -> bool
是否启用点击特效

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_enable_target_effect"></a>

#### get\_enable\_target\_effect

```python
def get_enable_target_effect() -> bool
```

x.get_enable_target_effect() -> bool
是否启用旋转ICON

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_enabled_features"></a>

#### get\_enabled\_features

```python
def get_enabled_features() -> int
```

x.get_enabled_features() -> int32
获取已启用的功能

Returns:
    int32:

<a id="unreal.WdpBasePawn.get_enable_camera_collision"></a>

#### get\_enable\_camera\_collision

```python
def get_enable_camera_collision() -> bool
```

x.get_enable_camera_collision() -> bool
获取是否启用相机的碰撞，用于在过场动画时禁用碰撞

Returns:
    bool:

<a id="unreal.WdpBasePawn.get_direction_object_hit_result"></a>

#### get\_direction\_object\_hit\_result

```python
def get_direction_object_hit_result(
        start: Vector, direction: Vector,
        trace_channel: CollisionChannel) -> Optional[HitResult]
```

x.get_direction_object_hit_result(start, direction, trace_channel) -> HitResult or None
获取Object射线方向

Args:
    start (Vector): 
    direction (Vector): 
    trace_channel (CollisionChannel): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_direction_hit_result"></a>

#### get\_direction\_hit\_result

```python
def get_direction_hit_result(
        start: Vector, direction: Vector,
        trace_channel: TraceTypeQuery) -> Optional[HitResult]
```

x.get_direction_hit_result(start, direction, trace_channel) -> HitResult or None
获取Trace射线方向

Args:
    start (Vector): 
    direction (Vector): 
    trace_channel (TraceTypeQuery): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_desired_zoom_target_location"></a>

#### get\_desired\_zoom\_target\_location

```python
def get_desired_zoom_target_location() -> Optional[Tuple[Vector, Vector]]
```

x.get_desired_zoom_target_location() -> (target=Vector, direction=Vector) or None
获取目标的缩放点位 新

Returns:
    tuple or None: 

    target (Vector): 

    direction (Vector):

<a id="unreal.WdpBasePawn.get_desired_zoom_location"></a>

#### get\_desired\_zoom\_location

```python
def get_desired_zoom_location() -> Vector
```

x.get_desired_zoom_location() -> Vector
获取目标的缩放点位

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_desired_zoom_distance"></a>

#### get\_desired\_zoom\_distance

```python
def get_desired_zoom_distance() -> float
```

x.get_desired_zoom_distance() -> double
获取和目标的Zoom距离（加上插值的）

Returns:
    double:

<a id="unreal.WdpBasePawn.get_desired_rotate_pivot"></a>

#### get\_desired\_rotate\_pivot

```python
def get_desired_rotate_pivot() -> Vector
```

x.get_desired_rotate_pivot() -> Vector
获取目标的旋转中心点

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_default_touch_index"></a>

#### get\_default\_touch\_index

```python
def get_default_touch_index() -> TouchIndex
```

x.get_default_touch_index() -> TouchIndex
默认的TouchIndex 可能是1或者2，从TouchComponent中获取

Returns:
    TouchIndex:

<a id="unreal.WdpBasePawn.get_current_zoom_distance"></a>

#### get\_current\_zoom\_distance

```python
def get_current_zoom_distance() -> float
```

x.get_current_zoom_distance() -> double
获取当前的Zoom距离

Returns:
    double:

<a id="unreal.WdpBasePawn.get_current_camera_data"></a>

#### get\_current\_camera\_data

```python
def get_current_camera_data() -> AllCameraData
```

x.get_current_camera_data() -> AllCameraData
获取当前的CameraData，每次重新计算

Returns:
    AllCameraData:

<a id="unreal.WdpBasePawn.get_core_camera_data"></a>

#### get\_core\_camera\_data

```python
def get_core_camera_data() -> CoreCameraData
```

x.get_core_camera_data() -> CoreCameraData
获取当前的核心相机数据

Returns:
    CoreCameraData:

<a id="unreal.WdpBasePawn.get_control_mode"></a>

#### get\_control\_mode

```python
def get_control_mode() -> ControlMode
```

x.get_control_mode() -> ControlMode
获取当前的控制模式 鼠标 触屏 控制器

Returns:
    ControlMode:

<a id="unreal.WdpBasePawn.get_collision_ignore_actors"></a>

#### get\_collision\_ignore\_actors

```python
def get_collision_ignore_actors() -> Array[Actor]
```

x.get_collision_ignore_actors() -> Array[Actor]
获取碰撞检测时要忽略的对象

Returns:
    Array[Actor]:

<a id="unreal.WdpBasePawn.get_click_screen_position"></a>

#### get\_click\_screen\_position

```python
def get_click_screen_position() -> Optional[Tuple[Vector2D, Vector2D]]
```

x.get_click_screen_position() -> (screen_position=Vector2D, screen_position_without_dpi=Vector2D) or None
获取当前鼠标的屏幕位置

Returns:
    tuple or None: 

    screen_position (Vector2D): 

    screen_position_without_dpi (Vector2D):

<a id="unreal.WdpBasePawn.get_click_object_hit_result"></a>

#### get\_click\_object\_hit\_result

```python
def get_click_object_hit_result(
        object_types: Array[ObjectTypeQuery]) -> Optional[HitResult]
```

x.get_click_object_hit_result(object_types) -> HitResult or None
获取鼠标或触屏点击的碰撞结果（Object碰撞）

Args:
    object_types (Array[ObjectTypeQuery]): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_click_hit_result"></a>

#### get\_click\_hit\_result

```python
def get_click_hit_result(trace_channel: TraceTypeQuery) -> Optional[HitResult]
```

x.get_click_hit_result(trace_channel) -> HitResult or None
获取鼠标或触屏点击的碰撞结果

Args:
    trace_channel (TraceTypeQuery): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpBasePawn.get_camera_pitch_from_rotate_pivot"></a>

#### get\_camera\_pitch\_from\_rotate\_pivot

```python
def get_camera_pitch_from_rotate_pivot() -> float
```

x.get_camera_pitch_from_rotate_pivot() -> float
计算当前相机位置和Pivot坐标产生的Pitch角度，相机和旋转点构成的坐标系

Returns:
    float:

<a id="unreal.WdpBasePawn.get_camera_height_to_ground_at_location"></a>

#### get\_camera\_height\_to\_ground\_at\_location

```python
def get_camera_height_to_ground_at_location(location: Vector) -> float
```

x.get_camera_height_to_ground_at_location(location) -> double
根据输入的坐标，返回该坐标相对与地面的高度

Args:
    location (Vector): 

Returns:
    double:

<a id="unreal.WdpBasePawn.get_camera_height_to_ground"></a>

#### get\_camera\_height\_to\_ground

```python
def get_camera_height_to_ground() -> float
```

x.get_camera_height_to_ground() -> double
获取相机距离地面的高度，只检查Ground通道，如果不存在会返回虚拟平面高度

Returns:
    double:

<a id="unreal.WdpBasePawn.get_camera_collision_data"></a>

#### get\_camera\_collision\_data

```python
def get_camera_collision_data() -> CameraCollisionData
```

x.get_camera_collision_data() -> CameraCollisionData
获取当前的碰撞相机数据

Returns:
    CameraCollisionData:

<a id="unreal.WdpBasePawn.get_alternative_up_vector"></a>

#### get\_alternative\_up\_vector

```python
def get_alternative_up_vector(rotation: Rotator, pivot: Vector) -> Vector
```

x.get_alternative_up_vector(rotation, pivot) -> Vector
Get Alternative Up Vector

Args:
    rotation (Rotator): 
    pivot (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_alternative_right_vector"></a>

#### get\_alternative\_right\_vector

```python
def get_alternative_right_vector(rotation: Rotator, pivot: Vector) -> Vector
```

x.get_alternative_right_vector(rotation, pivot) -> Vector
Get Alternative Right Vector

Args:
    rotation (Rotator): 
    pivot (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.get_alternative_forward_vector"></a>

#### get\_alternative\_forward\_vector

```python
def get_alternative_forward_vector(rotation: Rotator, pivot: Vector) -> Vector
```

x.get_alternative_forward_vector(rotation, pivot) -> Vector
根据Rotation获取移动角度

Args:
    rotation (Rotator): 
    pivot (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.follow_traget_tick"></a>

#### follow\_traget\_tick

```python
def follow_traget_tick() -> None
```

x.follow_traget_tick() -> None
跟踪Actor的更新函数

<a id="unreal.WdpBasePawn.fix_rotate_around_collision_angle"></a>

#### fix\_rotate\_around\_collision\_angle

```python
def fix_rotate_around_collision_angle(pivot: Vector, start_location: Vector,
                                      target_location: Vector,
                                      collide_location: Vector,
                                      start_rotation: Rotator,
                                      delta_rotation: Rotator) -> Rotator
```

x.fix_rotate_around_collision_angle(pivot, start_location, target_location, collide_location, start_rotation, delta_rotation) -> Rotator
将绕点旋转后的碰撞修正回去

Args:
    pivot (Vector): 
    start_location (Vector): 
    target_location (Vector): 
    collide_location (Vector): 
    start_rotation (Rotator): 
    delta_rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.fix_pawn_movement_by_collision"></a>

#### fix\_pawn\_movement\_by\_collision

```python
def fix_pawn_movement_by_collision(start: Vector,
                                   target: Vector,
                                   profile_name: Name,
                                   ground_only: bool = False) -> Vector
```

x.fix_pawn_movement_by_collision(start, target, profile_name, ground_only=False) -> Vector
根据相机碰撞设置修正Pawn的移动目标位置点//Start: 开始时的Pawn的位置， Target: 要运动到目标的位置
//碰撞半径根据Pawn的半径决定 参考FloatingPawnMovement的Tick

Args:
    start (Vector): 
    target (Vector): 
    profile_name (Name): 
    ground_only (bool): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.fix_core_camera_data"></a>

#### fix\_core\_camera\_data

```python
def fix_core_camera_data(
        core_camera_data_in: CoreCameraData) -> CoreCameraData
```

x.fix_core_camera_data(core_camera_data_in) -> CoreCameraData
修正Core的相机数据，将目标的角度和旋转限制在指定Limit数据范围内

Args:
    core_camera_data_in (CoreCameraData): 

Returns:
    CoreCameraData:

<a id="unreal.WdpBasePawn.enable_features"></a>

#### enable\_features

```python
def enable_features(features_to_enable: int) -> None
```

x.enable_features(features_to_enable) -> None
启用功能

Args:
    features_to_enable (int32):

<a id="unreal.WdpBasePawn.disable_features"></a>

#### disable\_features

```python
def disable_features(features_to_disable: int) -> None
```

x.disable_features(features_to_disable) -> None
禁用功能

Args:
    features_to_disable (int32):

<a id="unreal.WdpBasePawn.convert_surface_rotation_to_world"></a>

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

<a id="unreal.WdpBasePawn.convert_rotation_to_surface_space"></a>

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

<a id="unreal.WdpBasePawn.conver_transform_to_surface_space"></a>

#### conver\_transform\_to\_surface\_space

```python
def conver_transform_to_surface_space(origin: Vector,
                                      transform: Transform) -> Transform
```

x.conver_transform_to_surface_space(origin, transform) -> Transform
计算一个点的世界空间，用于将球面操作转换成平面操作

Args:
    origin (Vector): 
    transform (Transform): 

Returns:
    Transform:

<a id="unreal.WdpBasePawn.clear_collision_ignore_actors"></a>

#### clear\_collision\_ignore\_actors

```python
def clear_collision_ignore_actors() -> None
```

x.clear_collision_ignore_actors() -> None
清空要忽略碰撞的对象

<a id="unreal.WdpBasePawn.clear_all_remain_movement"></a>

#### clear\_all\_remain\_movement

```python
def clear_all_remain_movement() -> None
```

x.clear_all_remain_movement() -> None
清空全部缓动插值 包括旋转 缩放 移动等，用于动画问题

<a id="unreal.WdpBasePawn.clamp_target_point_in_zoom_distance_limit"></a>

#### clamp\_target\_point\_in\_zoom\_distance\_limit

```python
def clamp_target_point_in_zoom_distance_limit(target_point: Vector) -> Vector
```

x.clamp_target_point_in_zoom_distance_limit(target_point) -> Vector
限制点击点位的距离，用于旋转和缩放防止超过距离上限

Args:
    target_point (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.clamp_fixed_collision_custom_points"></a>

#### clamp\_fixed\_collision\_custom\_points

```python
def clamp_fixed_collision_custom_points(
        start: Vector,
        target: Vector,
        custom_points: Array[Vector],
        limit_direction: bool = False) -> Vector
```

x.clamp_fixed_collision_custom_points(start, target, custom_points, limit_direction=False) -> Vector
使用点位修正碰撞边界//如果只有两个点，作为Box区域的碰撞处理，如果有三个点以上，作为多边形限制处理，点会被Clamp到多边形范围内，不会改变Z
//
LimitDirection:: 是否将点限制在Start到Target的连线上

Args:
    start (Vector): 
    target (Vector): 
    custom_points (Array[Vector]): 
    limit_direction (bool): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.check_should_break_following"></a>

#### check\_should\_break\_following

```python
def check_should_break_following(auto_break: bool) -> bool
```

x.check_should_break_following(auto_break) -> bool
是否打断跟踪对象

Args:
    auto_break (bool): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.check_auto_break_movement"></a>

#### check\_auto\_break\_movement

```python
def check_auto_break_movement(input_type: UserInputActionType) -> None
```

x.check_auto_break_movement(input_type) -> None
自动判断是否打断自动旋转/移动/跟踪逻辑

Args:
    input_type (UserInputActionType):

<a id="unreal.WdpBasePawn.can_keep_zooming_input"></a>

#### can\_keep\_zooming\_input

```python
def can_keep_zooming_input(target: Vector, action_value: float) -> bool
```

x.can_keep_zooming_input(target, action_value) -> bool
是否允许缩放操作，基于目标点和Zoom限制参数做判断

Args:
    target (Vector): 
    action_value (float): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.calc_zoom_tick_delta_value"></a>

#### calc\_zoom\_tick\_delta\_value

```python
def calc_zoom_tick_delta_value(
        current: Vector, zoom_target: Vector,
        remain_distance: float) -> Tuple[Vector, Vector, float, float]
```

x.calc_zoom_tick_delta_value(current, zoom_target, remain_distance) -> (out_location=Vector, delta_movement=Vector, new_remain_distance=double, delta_distance=double)
计算缩放要变化的数值 输入：剩余的缩放量，输出：要变化的delta vector

Args:
    current (Vector): 
    zoom_target (Vector): 
    remain_distance (double): 

Returns:
    tuple: 

    out_location (Vector): 

    delta_movement (Vector): 

    new_remain_distance (double): 

    delta_distance (double):

<a id="unreal.WdpBasePawn.calc_zoom_collision_block_value"></a>

#### calc\_zoom\_collision\_block\_value

```python
def calc_zoom_collision_block_value(
        start: Vector, target: Vector,
        collision_data: CameraCollisionData) -> Optional[Tuple[Vector, float]]
```

x.calc_zoom_collision_block_value(start, target, collision_data) -> (out_location=Vector, delta_distance=double) or None
阻挡缩放操作的碰撞检测，用于鼠标滚轮检测
返回值：是否发生了阻挡: 

Args:
    start (Vector): 
    target (Vector): 
    collision_data (CameraCollisionData): 

Returns:
    tuple or None: 

    out_location (Vector): 

    delta_distance (double):

<a id="unreal.WdpBasePawn.calc_surface_movement_delta_value"></a>

#### calc\_surface\_movement\_delta\_value

```python
def calc_surface_movement_delta_value(
        current: Vector) -> Tuple[Vector, Vector]
```

x.calc_surface_movement_delta_value(current) -> (delta_movement=Vector, new_remain=Vector)
计算平面运动的插值//
Current：当前剩余的平面运动值，@DeltaMovement：这一帧要变化的平面运动插值，@NewRemain：插值后剩余的数值，后面需要Rotate: 

Args:
    current (Vector): 

Returns:
    tuple: 

    delta_movement (Vector): 

    new_remain (Vector):

<a id="unreal.WdpBasePawn.calc_split_movement_to_surface_and_height"></a>

#### calc\_split\_movement\_to\_surface\_and\_height

```python
def calc_split_movement_to_surface_and_height(
        move_direction: Vector, move_distance: float) -> Tuple[Vector, float]
```

x.calc_split_movement_to_surface_and_height(move_direction, move_distance) -> (out_surface_delta=Vector, out_height_delta=double)
将移动速度和方向分解成平面移动和垂直移动

Args:
    move_direction (Vector): 
    move_distance (double): 

Returns:
    tuple: 

    out_surface_delta (Vector): 

    out_height_delta (double):

<a id="unreal.WdpBasePawn.calc_rotate_pivot_surface_move"></a>

#### calc\_rotate\_pivot\_surface\_move

```python
def calc_rotate_pivot_surface_move(start_camera_location: Vector,
                                   pivot: Vector, camera_surface_delta: Vector,
                                   camera_height_delta: Vector) -> Vector
```

x.calc_rotate_pivot_surface_move(start_camera_location, pivot, camera_surface_delta, camera_height_delta) -> Vector
计算RotatePivot，按键移动会让Pivot同步进行更新，eg.按住右键的同时按WASD操作//
StartCameraLocation：当前相机位置，@Pivot：当前Pivot位置，@CameraSurfaceDelta：相机在表面移动的直线距离和方向: 
CameraHeightDelta: 相机高度移动的变化量 //输出新Pivot坐标

Args:
    start_camera_location (Vector): 
    pivot (Vector): 
    camera_surface_delta (Vector): 
    camera_height_delta (Vector): 

Returns:
    Vector:

<a id="unreal.WdpBasePawn.calc_rotate_around_pivot_value"></a>

#### calc\_rotate\_around\_pivot\_value

```python
def calc_rotate_around_pivot_value(start_loc: Vector, start_rot: Rotator,
                                   pivot: Vector, pitch: float,
                                   yaw: float) -> Tuple[Vector, Rotator]
```

x.calc_rotate_around_pivot_value(start_loc, start_rot, pivot, pitch, yaw) -> (out_location=Vector, out_delta_rotation=Rotator)
计算相机绕点旋转后的角度和位置//Current：起始位置，Pivot：旋转点，Pitch：大于零为抬头，Yaw：大于零为向右

Args:
    start_loc (Vector): 
    start_rot (Rotator): 
    pivot (Vector): 
    pitch (float): 
    yaw (float): 

Returns:
    tuple: 

    out_location (Vector): 

    out_delta_rotation (Rotator):

<a id="unreal.WdpBasePawn.calc_rotate_around_collision_value"></a>

#### calc\_rotate\_around\_collision\_value

```python
def calc_rotate_around_collision_value(
        pivot: Vector, start_location: Vector, target_location: Vector,
        collision_data: CameraCollisionData) -> Optional[Tuple[Vector, float]]
```

x.calc_rotate_around_collision_value(pivot, start_location, target_location, collision_data) -> (out_location=Vector, distance=double) or None
计算绕点旋转的碰撞参数//
Pivot：旋转中心，@StartLocation: 开始旋转前的坐标
TargetLocation：旋转后的目标点，@CollisionData：碰撞设置，@TraceStartPercent（0-1）：从哪里开始计算射线，碰撞检测不是从头发出的: //
ReturnValue: 是否发生了碰撞
OutLocation: 输出的位置，
Distance：最终的新Distance: 

Args:
    pivot (Vector): 
    start_location (Vector): 
    target_location (Vector): 
    collision_data (CameraCollisionData): 

Returns:
    tuple or None: 

    out_location (Vector): 

    distance (double):

<a id="unreal.WdpBasePawn.calc_rotate_around_camera_data"></a>

#### calc\_rotate\_around\_camera\_data

```python
def calc_rotate_around_camera_data(
        start_rotation: Rotator, start_location: Vector,
        remain_rotation: Rotator, pivot: Vector, pitch_limit: Vector2D,
        yaw_limit: Vector2D) -> Tuple[Vector, Rotator, Rotator, Vector]
```

x.calc_rotate_around_camera_data(start_rotation, start_location, remain_rotation, pivot, pitch_limit, yaw_limit) -> (out_location=Vector, out_delta_rotation=Rotator, new_remain_rotation=Rotator, new_direction=Vector)
完整的Camera Rotate Around 计算角度逻辑//
StartRotation: 开始时相机的角度
RemainRotation: 剩余缓动角度
Pivot: 旋转点
PitchLimit: 俯仰角限制
YawLimit: 水平旋转限制 //
OutLocation: 旋转后的相机位置
OutDeltaRotation: 实际产生的角度变化量
NewRemainRotation: 旋转后的剩余缓动角度
NewDirection: 旋转后的新方向，Pivot指向相机的方向

Args:
    start_rotation (Rotator): 
    start_location (Vector): 
    remain_rotation (Rotator): 
    pivot (Vector): 
    pitch_limit (Vector2D): 
    yaw_limit (Vector2D): 

Returns:
    tuple: 

    out_location (Vector): 

    out_delta_rotation (Rotator): 

    new_remain_rotation (Rotator): 

    new_direction (Vector):

<a id="unreal.WdpBasePawn.calc_pitch_from_rotate_pivot_local"></a>

#### calc\_pitch\_from\_rotate\_pivot\_local

```python
def calc_pitch_from_rotate_pivot_local(camera_loc: Vector,
                                       pivot: Vector) -> float
```

x.calc_pitch_from_rotate_pivot_local(camera_loc, pivot) -> double
计算目标Pivot位置和当前相机距离产生的Pitch角度 球表面坐标

Args:
    camera_loc (Vector): 
    pivot (Vector): 

Returns:
    double:

<a id="unreal.WdpBasePawn.calc_pitch_from_pivot_camera_dir_local"></a>

#### calc\_pitch\_from\_pivot\_camera\_dir\_local

```python
def calc_pitch_from_pivot_camera_dir_local(camera_loc: Vector,
                                           camera_rot: Rotator,
                                           pivot: Vector) -> float
```

x.calc_pitch_from_pivot_camera_dir_local(camera_loc, camera_rot, pivot) -> double
计算沿着相机方向的角度与Pivot产生的Pitch角度，只计算垂直方向

Args:
    camera_loc (Vector): 
    camera_rot (Rotator): 
    pivot (Vector): 

Returns:
    double:

<a id="unreal.WdpBasePawn.calc_move_value_along_surface"></a>

#### calc\_move\_value\_along\_surface

```python
def calc_move_value_along_surface(
        start: Vector, surface_dir: Vector) -> Tuple[Vector, Vector]
```

x.calc_move_value_along_surface(start, surface_dir) -> (Vector, move_delta=Vector)
计算在平面上运动的相机实际运动方向//
Start：开始时的位置，@SurfaceDir：移动的方向和距离，@MoveDelta：表面移动后的实际变化量: 

Args:
    start (Vector): 
    surface_dir (Vector): 

Returns:
    Vector: 

    move_delta (Vector):

<a id="unreal.WdpBasePawn.calc_height_movement_delta_value"></a>

#### calc\_height\_movement\_delta\_value

```python
def calc_height_movement_delta_value(
        current_location: Vector, up_direction: Vector,
        remain_height: float) -> Tuple[Vector, Vector, float]
```

x.calc_height_movement_delta_value(current_location, up_direction, remain_height) -> (out_location=Vector, delta_movement=Vector, new_remain_height=double)
计算垂直运动的插值//
CurrentLocation：当前位置，@UpDirection：向上的方向，@RemainHeight：剩余垂直移动的数值，@OutLocation：垂直移动后的新位置，@DeltaMovement：移动了多少，: 
NewRemainHeight: 插值后的新剩余数值

Args:
    current_location (Vector): 
    up_direction (Vector): 
    remain_height (double): 

Returns:
    tuple: 

    out_location (Vector): 

    delta_movement (Vector): 

    new_remain_height (double):

<a id="unreal.WdpBasePawn.calc_free_movement_delta_value"></a>

#### calc\_free\_movement\_delta\_value

```python
def calc_free_movement_delta_value(
        current_location: Vector,
        free_move_remain: Vector) -> Tuple[Vector, Vector]
```

x.calc_free_movement_delta_value(current_location, free_move_remain) -> (out_location=Vector, new_free_move_remain=Vector)
计算自由运动的插值 自由运动是值不受球面影响 引擎空间的运动值//
CurrentLocation：当前位置，@FreeMoveRemain：剩余移动向量，@OutLocation：自由移动后的新位置: 
NewFreeMoveRemain: 插值后的新剩余数值

Args:
    current_location (Vector): 
    free_move_remain (Vector): 

Returns:
    tuple: 

    out_location (Vector): 

    new_free_move_remain (Vector):

<a id="unreal.WdpBasePawn.calc_follow_actor_movement_delta_value"></a>

#### calc\_follow\_actor\_movement\_delta\_value

```python
def calc_follow_actor_movement_delta_value(
        current_location: Vector,
        follow_move_remain: Vector) -> Tuple[Vector, Vector]
```

x.calc_follow_actor_movement_delta_value(current_location, follow_move_remain) -> (out_location=Vector, new_follow_move_remain=Vector)
计算FollowActor运动的插值 只受FollowActor的坐标变化影响 引擎空间的运动值//
CurrentLocation：当前位置，@FollowMoveRemain：剩余移动向量，@OutLocation：跟随移动后的新位置: 
NewFollowMoveRemain: 插值后的新剩余数值

Args:
    current_location (Vector): 
    follow_move_remain (Vector): 

Returns:
    tuple: 

    out_location (Vector): 

    new_follow_move_remain (Vector):

<a id="unreal.WdpBasePawn.calc_fix_rotate_around_pitch_delta"></a>

#### calc\_fix\_rotate\_around\_pitch\_delta

```python
def calc_fix_rotate_around_pitch_delta(pitch_delta: float, camera_loc: Vector,
                                       camera_rot: Rotator, pivot: Vector,
                                       pitch_limit: Vector2D) -> float
```

x.calc_fix_rotate_around_pitch_delta(pitch_delta, camera_loc, camera_rot, pivot, pitch_limit) -> double
修正Rotate Around的Pitch Delta，Rotate Around 使用的是旋转点和相机的夹角，所以不能和旋转的Limit通用

Args:
    pitch_delta (double): 
    camera_loc (Vector): 
    camera_rot (Rotator): 
    pivot (Vector): 
    pitch_limit (Vector2D): 

Returns:
    double:

<a id="unreal.WdpBasePawn.calc_fixed_ground_position"></a>

#### calc\_fixed\_ground\_position

```python
def calc_fixed_ground_position(
    start: Vector,
    target: Vector,
    ground_position_mode: GroundPositionMode = GroundPositionMode.
    GPM_AVOID_ONLY
) -> Tuple[Vector, Vector]
```

x.calc_fixed_ground_position(start, target, ground_position_mode=GroundPositionMode.GPM_AVOID_ONLY) -> (Vector, out_delta=Vector)
修正地面检测碰撞 输出被修正的地面位置数值

Args:
    start (Vector): 
    target (Vector): 
    ground_position_mode (GroundPositionMode): 

Returns:
    Vector: 

    out_delta (Vector):

<a id="unreal.WdpBasePawn.calc_fixed_collision_profile"></a>

#### calc\_fixed\_collision\_profile

```python
def calc_fixed_collision_profile(
        start: Vector, target: Vector,
        collision_profile: Name) -> Tuple[Vector, Vector]
```

x.calc_fixed_collision_profile(start, target, collision_profile) -> (Vector, out_delta=Vector)
根据CollisionMode和Profile计算碰撞后的新位置

Args:
    start (Vector): 
    target (Vector): 
    collision_profile (Name): 

Returns:
    Vector: 

    out_delta (Vector):

<a id="unreal.WdpBasePawn.calc_double_click_core_data"></a>

#### calc\_double\_click\_core\_data

```python
def calc_double_click_core_data(current_data: AllCameraData, target: Vector,
                                scale: float) -> CoreCameraData
```

x.calc_double_click_core_data(current_data, target, scale) -> CoreCameraData
计算双击操作的目标CoreData

Args:
    current_data (AllCameraData): 
    target (Vector): 
    scale (float): 

Returns:
    CoreCameraData:

<a id="unreal.WdpBasePawn.calc_delta_camera_rotation_data"></a>

#### calc\_delta\_camera\_rotation\_data

```python
def calc_delta_camera_rotation_data(
        current_location: Vector, rotate_pivot: Vector,
        delta_rotation_in: Rotator) -> Tuple[Vector, Rotator]
```

x.calc_delta_camera_rotation_data(current_location, rotate_pivot, delta_rotation_in) -> (out_location=Vector, out_delta_rotation=Rotator)
计算相机的旋转插值，DeltaRotationIn是这一帧里旋转的插值，对相机位置进行修正

Args:
    current_location (Vector): 
    rotate_pivot (Vector): 
    delta_rotation_in (Rotator): 

Returns:
    tuple: 

    out_location (Vector): 

    out_delta_rotation (Rotator):

<a id="unreal.WdpBasePawn.calc_camera_surface_height_movement_data"></a>

#### calc\_camera\_surface\_height\_movement\_data

```python
def calc_camera_surface_height_movement_data(
        start_location: Vector, surface_remain: Vector,
        height_remain: float) -> Tuple[Vector, Vector, float, Vector, Vector]
```

x.calc_camera_surface_height_movement_data(start_location, surface_remain, height_remain) -> (out_location=Vector, new_surface_remain=Vector, new_height_remain=double, surface_delta=Vector, height_delta=Vector)
完整的表面运动+垂直运动逻辑//
StartLocation: 开始时的相机坐标
SurfaceRemain: 剩余表面距离
HeightRemain: 剩余高度距离 //
OutLocation: 移动后的位置
NewSurfaceRemain: 更新后的剩余表面距离
NewHeightRemain: 更新后的剩余高度
SurfaceDelta: 表面移动的变化量
HeightDelta: 高度移动的变化量

Args:
    start_location (Vector): 
    surface_remain (Vector): 
    height_remain (double): 

Returns:
    tuple: 

    out_location (Vector): 

    new_surface_remain (Vector): 

    new_height_remain (double): 

    surface_delta (Vector): 

    height_delta (Vector):

<a id="unreal.WdpBasePawn.calc_camera_self_rotate_data"></a>

#### calc\_camera\_self\_rotate\_data

```python
def calc_camera_self_rotate_data(start_rotation: Rotator,
                                 start_location: Vector,
                                 remain_rotation: Rotator,
                                 pitch_limit: Vector2D, yaw_limit: Vector2D,
                                 roll: float) -> Tuple[Rotator, Rotator]
```

x.calc_camera_self_rotate_data(start_rotation, start_location, remain_rotation, pitch_limit, yaw_limit, roll) -> (out_rotation=Rotator, new_remain_rotation=Rotator)
完整的Camera Self Rotate 角度计算逻辑//
StartRotation: 开始时相机的角度
RemainRotation: 剩余缓动角度
PitchLimit: 俯仰角限制
YawLimit: 水平旋转限制
Roll: 相机自身的roll旋转 //
OutRotation: 旋转后角度
NewRemainRotation: 旋转后的剩余缓动角度

Args:
    start_rotation (Rotator): 
    start_location (Vector): 
    remain_rotation (Rotator): 
    pitch_limit (Vector2D): 
    yaw_limit (Vector2D): 
    roll (double): 

Returns:
    tuple: 

    out_rotation (Rotator): 

    new_remain_rotation (Rotator):

<a id="unreal.WdpBasePawn.calc_camera_collision_result"></a>

#### calc\_camera\_collision\_result

```python
def calc_camera_collision_result(
        start_location: Vector, target_location: Vector,
        collision_data: CameraCollisionData,
        limit_direction: bool) -> Optional[Tuple[Vector, Vector]]
```

x.calc_camera_collision_result(start_location, target_location, collision_data, limit_direction) -> (out_location=Vector, delta=Vector) or None
完整的相机碰撞计算逻辑//
StartLocation: 开始时的相机坐标
TargetLocation: 目标要前往位置
CollisionData: 碰撞设置
LimitDirection: 是否将点限制在Start到Target的连线上，避免角度改变 //
OutLocation: 碰撞后的位置
Delta: 实际移动的距离
ReturnValue：是否发生了碰撞: 

Args:
    start_location (Vector): 
    target_location (Vector): 
    collision_data (CameraCollisionData): 
    limit_direction (bool): 

Returns:
    tuple or None: 

    out_location (Vector): 

    delta (Vector):

<a id="unreal.WdpBasePawn.calc_auto_travel_duration"></a>

#### calc\_auto\_travel\_duration

```python
def calc_auto_travel_duration(duration: float,
                              target_location: Vector) -> float
```

x.calc_auto_travel_duration(duration, target_location) -> float
计算Duration，如果<0则使用自动计算逻辑

Args:
    duration (float): 
    target_location (Vector): 

Returns:
    float:

<a id="unreal.WdpBasePawn.calc_anim_cam_rotation"></a>

#### calc\_anim\_cam\_rotation

```python
def calc_anim_cam_rotation(start_rotation: Rotator, target_rotation: Rotator,
                           alpha: float) -> Rotator
```

x.calc_anim_cam_rotation(start_rotation, target_rotation, alpha) -> Rotator
计算动画插值旋转结果

Args:
    start_rotation (Rotator): 
    target_rotation (Rotator): 
    alpha (float): 

Returns:
    Rotator:

<a id="unreal.WdpBasePawn.are_features_enabled"></a>

#### are\_features\_enabled

```python
def are_features_enabled(features_to_test: int) -> bool
```

x.are_features_enabled(features_to_test) -> bool
是否开启功能

Args:
    features_to_test (int32): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.are_anim_blend_feature_enabled"></a>

#### are\_anim\_blend\_feature\_enabled

```python
def are_anim_blend_feature_enabled(features_to_test: int) -> bool
```

x.are_anim_blend_feature_enabled(features_to_test) -> bool
查询是否开启了部分动画功能

Args:
    features_to_test (int32): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.apply_zoom_limit"></a>

#### apply\_zoom\_limit

```python
def apply_zoom_limit(new_zoom_limit: CameraZoomLimitationData) -> None
```

x.apply_zoom_limit(new_zoom_limit) -> None
设置缩放限制参数

Args:
    new_zoom_limit (CameraZoomLimitationData):

<a id="unreal.WdpBasePawn.apply_yaw_limit"></a>

#### apply\_yaw\_limit

```python
def apply_yaw_limit(min_yaw: float = -179.998993,
                    max_yaw: float = 179.998993) -> None
```

x.apply_yaw_limit(min_yaw=-179.998993, max_yaw=179.998993) -> None
赋值Yaw限制，自动修正不能等于0和360的问题

Args:
    min_yaw (float): 
    max_yaw (float):

<a id="unreal.WdpBasePawn.apply_rotate_limit"></a>

#### apply\_rotate\_limit

```python
def apply_rotate_limit(new_rotate_limit: CameraRotationLimitationData) -> None
```

x.apply_rotate_limit(new_rotate_limit) -> None
设置旋转限制参数

Args:
    new_rotate_limit (CameraRotationLimitationData):

<a id="unreal.WdpBasePawn.apply_pitch_limit"></a>

#### apply\_pitch\_limit

```python
def apply_pitch_limit(min_pitch: float = -89.000000,
                      max_pitch: float = 89.000000) -> None
```

x.apply_pitch_limit(min_pitch=-89.000000, max_pitch=89.000000) -> None
设置Pitch限制，自动检查大小问题

Args:
    min_pitch (float): 
    max_pitch (float):

<a id="unreal.WdpBasePawn.apply_camera_data"></a>

#### apply\_camera\_data

```python
def apply_camera_data(new_camera_data: AllCameraData) -> None
```

x.apply_camera_data(new_camera_data) -> None
设置新的CameraData，在动画设置时使用

Args:
    new_camera_data (AllCameraData):

<a id="unreal.WdpBasePawn.apply_camera_collision_data"></a>

#### apply\_camera\_collision\_data

```python
def apply_camera_collision_data(collision_data: CameraCollisionData) -> bool
```

x.apply_camera_collision_data(collision_data) -> bool
应用相机碰撞参数

Args:
    collision_data (CameraCollisionData): 

Returns:
    bool:

<a id="unreal.WdpBasePawn.add_collision_ignore_actor"></a>

#### add\_collision\_ignore\_actor

```python
def add_collision_ignore_actor(actor: Actor) -> None
```

x.add_collision_ignore_actor(actor) -> None
添加要忽略碰撞的对象

Args:
    actor (Actor):

<a id="unreal.WdpBasePawn.add_camera_zoom_input"></a>

#### add\_camera\_zoom\_input

```python
def add_camera_zoom_input(value: float) -> None
```

x.add_camera_zoom_input(value) -> None
单独的ZoomInput控制逻辑，整合FOV和Distance，使用枚举做判断

Args:
    value (float):

<a id="unreal.WdpBasePawn.add_camera_surface_movement_value"></a>

#### add\_camera\_surface\_movement\_value

```python
def add_camera_surface_movement_value(delta_movement: Vector) -> None
```

x.add_camera_surface_movement_value(delta_movement) -> None
缓动用，增加相机的平面移动，方向是相机在平面上的投影，距离是向量长度，如果是球面那就是弧长

Args:
    delta_movement (Vector):

<a id="unreal.WdpBasePawn.add_camera_self_rotation"></a>

#### add\_camera\_self\_rotation

```python
def add_camera_self_rotation(delta_rotation: Rotator) -> None
```

x.add_camera_self_rotation(delta_rotation) -> None
增加相机自身的旋转变化

Args:
    delta_rotation (Rotator):

<a id="unreal.WdpBasePawn.add_camera_rotate_self_input"></a>

#### add\_camera\_rotate\_self\_input

```python
def add_camera_rotate_self_input(value: Vector2D) -> None
```

x.add_camera_rotate_self_input(value) -> None
自身旋转相机的输入 X=Yaw Y=Pitch

Args:
    value (Vector2D):

<a id="unreal.WdpBasePawn.add_camera_rotate_around_input"></a>

#### add\_camera\_rotate\_around\_input

```python
def add_camera_rotate_around_input(value: Vector2D) -> None
```

x.add_camera_rotate_around_input(value) -> None
绕点旋转相机的输入 X=Yaw Y=Pitch

Args:
    value (Vector2D):

<a id="unreal.WdpBasePawn.add_camera_movement_input_up_down"></a>

#### add\_camera\_movement\_input\_up\_down

```python
def add_camera_movement_input_up_down(value: float) -> None
```

x.add_camera_movement_input_up_down(value) -> None
垂直方向移动相机的按键

Args:
    value (float):

<a id="unreal.WdpBasePawn.add_camera_movement_input"></a>

#### add\_camera\_movement\_input

```python
def add_camera_movement_input(axis_value: Vector2D) -> None
```

x.add_camera_movement_input(axis_value) -> None
水平方向移动相机的按键 X = Right Y = Forward

Args:
    axis_value (Vector2D):

<a id="unreal.WdpBasePawn.add_camera_height_movement_value"></a>

#### add\_camera\_height\_movement\_value

```python
def add_camera_height_movement_value(height: float) -> None
```

x.add_camera_height_movement_value(height) -> None
缓动用，增加相机的高度变化

Args:
    height (double):

<a id="unreal.WdpBasePawn.add_camera_free_movement_value"></a>

#### add\_camera\_free\_movement\_value

```python
def add_camera_free_movement_value(delta_movement: Vector) -> None
```

x.add_camera_free_movement_value(delta_movement) -> None
缓动动画用，增加相机的自由移动

Args:
    delta_movement (Vector):

<a id="unreal.WdpBasePawn.add_camera_fov_zoom_input"></a>

#### add\_camera\_fov\_zoom\_input

```python
def add_camera_fov_zoom_input(value: float) -> None
```

x.add_camera_fov_zoom_input(value) -> None
缩放相机的按键输入，FOV

Args:
    value (float):

<a id="unreal.WdpBasePawn.add_camera_follow_actor_movement_value"></a>

#### add\_camera\_follow\_actor\_movement\_value

```python
def add_camera_follow_actor_movement_value(delta_movement: Vector) -> None
```

x.add_camera_follow_actor_movement_value(delta_movement) -> None
缓动动画用，增加相机的自由移动

Args:
    delta_movement (Vector):

<a id="unreal.WdpBasePawn.add_camera_distance_zoom_value"></a>

#### add\_camera\_distance\_zoom\_value

```python
def add_camera_distance_zoom_value(delta_zoom: float) -> None
```

x.add_camera_distance_zoom_value(delta_zoom) -> None
缓动用，增加相机的缩放

Args:
    delta_zoom (float):

<a id="unreal.WdpBasePawn.add_camera_distance_zoom_input"></a>

#### add\_camera\_distance\_zoom\_input

```python
def add_camera_distance_zoom_input(value: float) -> None
```

x.add_camera_distance_zoom_input(value) -> None
缩放相机的按键输入，相机距离

Args:
    value (float):

<a id="unreal.WdpBasePawn.add_camera_around_pivot_rotation"></a>

#### add\_camera\_around\_pivot\_rotation

```python
def add_camera_around_pivot_rotation(delta_rotation: Rotator) -> None
```

x.add_camera_around_pivot_rotation(delta_rotation) -> None
增加绕点旋转的坐标变化

Args:
    delta_rotation (Rotator):

<a id="unreal.WdpCameraBPLibrary"></a>