## TOD\_Base Objects

```python
class TOD_Base(Actor)
```

TOD Base

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

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
- ``blend_radius`` (float):  [Read-Write]
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
- ``earth_center`` (Vector):  [Read-Write]
- ``earth_radius`` (float):  [Read-Write]
- ``earth_skylight_attenuation`` (Vector2D):  [Read-Write]
- ``enable_auto_lod_generation`` (bool):  [Read-Write] Whether this actor should be considered or not during HLOD generation.
- ``enable_high_post`` (bool):  [Read-Write]
- ``external_data_layer_asset`` (ExternalDataLayerAsset):  [Read-Only]
- ``find_camera_component_when_view_target`` (bool):  [Read-Write] If true, this actor should search for an owned camera component to view through when used as a view target.
- ``fx_style`` (FXStyle):  [Read-Write] 开启此选项时间会自动流逝
- ``generate_overlap_events_during_level_streaming`` (bool):  [Read-Write] If true, this actor will generate overlap Begin/End events when spawned as part of level streaming, which includes initial level load.
  You might enable this is in the case where a streaming level loads around an actor and you want Begin/End overlap events to trigger.
  see: UpdateOverlapsMethodDuringLevelStreaming
- ``height_fog_magnification_curve_fog_density`` (CurveFloat):  [Read-Write] 在鸟瞰视角下，如果相机高度超过一定阈值则会导致渲染错误
  添加曲线后通过 相机高度->高度雾密度倍率 曲线来控制高度雾跟随相机高度进行高度雾密度的变化
  相较于高度雾阈值，使用曲线能够更精细的控制高度雾的变化
  运行时才有效果
- ``height_fog_magnification_curve_start_distance`` (CurveFloat):  [Read-Write] 在鸟瞰视角下，如果相机高度超过一定阈值则会导致渲染错误
  添加曲线后通过 相机高度->高度雾起始距离倍率 曲线来控制高度雾跟随相机高度进行高度雾起始距离的变化
  相较于高度雾阈值，使用曲线能够更精细的控制高度雾的变化
  运行时才有效果
- ``height_fog_threshold`` (float):  [Read-Write] 高度雾高度阈值，相机高度超过此值会关闭高度雾
- ``hidden`` (bool):  [Read-Write] Allows us to only see this Actor in the Editor, and not in the actual game.
  see: SetActorHiddenInGame()
- ``hide_sky_mesh`` (float):  [Read-Write] 当相机世界坐标Z值超过此数值便隐藏skycreator的天空球静态网格模型
- ``high_post`` (PostProcessVolume):  [Read-Write]
- ``high_range`` (Vector2D):  [Read-Write]
- ``hlod_layer`` (HLODLayer):  [Read-Write] The UHLODLayer in which this actor should be included.
- ``ignores_origin_shifting`` (bool):  [Read-Write] Whether this actor should not be affected by world origin shifting.
- ``initial_life_span`` (float):  [Read-Write] How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun.
- ``input_priority`` (int32):  [Read-Write] The priority of this input component when pushed in to the stack.
- ``instigator`` (Pawn):  [Read-Write] Pawn responsible for damage and other gameplay events caused by this actor.
- ``is_earth`` (bool):  [Read-Write]
- ``is_editor_only_actor`` (bool):  [Read-Write] Whether this actor is editor-only. Use with care, as if this actor is referenced by anything else that reference will be NULL in cooked builds
- ``is_main_world_only`` (bool):  [Read-Write] If checked, this Actor will only get loaded in a main world (persistent level), it will not be loaded through Level Instances.
- ``is_spatially_loaded`` (bool):  [Read-Write] Determine if this actor is spatially loaded when placed in a partitioned world.
       If true, this actor will be loaded when in the range of any streaming sources and if (1) in no data layers, or (2) one or more of its data layers are enabled.
       If false, this actor will be loaded if (1) in no data layers, or (2) one or more of its data layers are enabled.
- ``is_sunrise`` (bool):  [Read-Write]
- ``is_sunset`` (bool):  [Read-Write]
- ``layers`` (Array[Name]):  [Read-Write] Layers the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling.
- ``light_array`` (Array[LightArray]):  [Read-Only] 搜集的灯光Actor
- ``light_oc`` (Array[LightOC]):  [Read-Write] 灯光数据
- ``light_oc_mpc`` (Array[LightOC_MPC]):  [Read-Write] 受日出日落影响的参数集
- ``lightning_light`` (DirectionalLightComponent):  [Read-Write]
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
- ``on_sunrise`` (OnSunrise):  [Read-Write]
- ``on_sunset`` (OnSunset):  [Read-Write]
- ``on_take_any_damage`` (TakeAnyDamageSignature):  [Read-Write] Called when the actor is damaged in any way.
- ``on_take_point_damage`` (TakePointDamageSignature):  [Read-Write] Called when the actor is damaged by point damage.
- ``on_take_radial_damage`` (TakeRadialDamageSignature):  [Read-Write] Called when the actor is damaged by radial damage.
- ``only_relevant_to_owner`` (bool):  [Read-Write] If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed.
- ``optimize_bp_component_data`` (bool):  [Read-Write] Whether to cook additional data to speed up spawn events at runtime for any Blueprint classes based on this Actor. This option may slightly increase memory usage in a cooked build.
- ``physics_replication_mode`` (PhysicsReplicationMode):  [Read-Write] Which mode to replicate physics through for this actor. Only relevant if the actor replicates movement and has a component that simulate physics.
- ``pivot_offset`` (Vector):  [Read-Write] Local space pivot offset for the actor, only used in the editor
- ``post`` (PostProcessVolume):  [Read-Write] 场景中的后期盒子对象
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``rain_sound`` (AudioComponent):  [Read-Write]
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
- ``root`` (SceneComponent):  [Read-Write]
- ``root_component`` (SceneComponent):  [Read-Write] The component that defines the transform (location, rotation, scale) of this Actor in the world, all other components must be attached to this one somehow
- ``runtime_grid`` (Name):  [Read-Write] Determine in which partition grid this actor will be placed in the partition (if the world is partitioned).
  If None, the decision will be left to the partition.
- ``shadow_contrast_scale`` (float):  [Read-Write]
- ``sky_creator`` (SkyCreator):  [Read-Write] 场景中的Skycreator对象
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``time_of_day`` (float):  [Read-Write]
- ``time_speed_up_scale`` (float):  [Read-Write] 时间加速流逝倍率，过大会导致错误
- ``tod_control_height_fog_density`` (bool):  [Read-Write] 由TOD来控制高度雾密度值，反之则由天气预设表来控制高度雾密度值
- ``tod_height_fog_density`` (float):  [Read-Write]
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
- ``use_compunter_time`` (bool):  [Read-Write] 使用电脑时间
- ``use_height_fog_threshold`` (bool):  [Read-Write] 在鸟瞰视角下，如果高度超过一定阈值则在高度雾作用下会导致渲染错误
  开启此值，超过阈值时将关闭高度雾
  运行时才有效果
- ``use_time_speed_up`` (bool):  [Read-Write] 开启此选项时间会自动流逝
- ``weather_fx`` (NiagaraComponent):  [Read-Write] 4时间段后期框废弃
        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
        UPostProcessComponent* Post_Morning;

        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
        UPostProcessComponent* Post_Noon;

        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
        UPostProcessComponent* Post_Dusk;

        UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
        UPostProcessComponent* Post_Night;
- ``weather_preset_51`` (SkyCreatorWeatherPreset_51):  [Read-Write] 天气预设文件

<a id="unreal.TOD_Base.time_of_day"></a>

#### time\_of\_day

```python
@property
def time_of_day() -> float
```

(float):  [Read-Write]

<a id="unreal.TOD_Base.time_of_day"></a>

#### time\_of\_day

```python
@time_of_day.setter
def time_of_day(value: float) -> None
```

<a id="unreal.TOD_Base.is_sunrise"></a>

#### is\_sunrise

```python
@property
def is_sunrise() -> bool
```

(bool):  [Read-Only]

<a id="unreal.TOD_Base.is_sunset"></a>

#### is\_sunset

```python
@property
def is_sunset() -> bool
```

(bool):  [Read-Only]

<a id="unreal.TOD_Base.weather_preset_51"></a>

#### weather\_preset\_51

```python
@property
def weather_preset_51() -> SkyCreatorWeatherPreset_51
```

(SkyCreatorWeatherPreset_51):  [Read-Write] 天气预设文件

<a id="unreal.TOD_Base.weather_preset_51"></a>

#### weather\_preset\_51

```python
@weather_preset_51.setter
def weather_preset_51(value: SkyCreatorWeatherPreset_51) -> None
```

<a id="unreal.TOD_Base.sky_creator"></a>

#### sky\_creator

```python
@property
def sky_creator() -> SkyCreator
```

(SkyCreator):  [Read-Only] 场景中的Skycreator对象

<a id="unreal.TOD_Base.use_compunter_time"></a>

#### use\_compunter\_time

```python
@property
def use_compunter_time() -> bool
```

(bool):  [Read-Write] 使用电脑时间

<a id="unreal.TOD_Base.use_compunter_time"></a>

#### use\_compunter\_time

```python
@use_compunter_time.setter
def use_compunter_time(value: bool) -> None
```

<a id="unreal.TOD_Base.use_time_speed_up"></a>

#### use\_time\_speed\_up

```python
@property
def use_time_speed_up() -> bool
```

(bool):  [Read-Write] 开启此选项时间会自动流逝

<a id="unreal.TOD_Base.use_time_speed_up"></a>

#### use\_time\_speed\_up

```python
@use_time_speed_up.setter
def use_time_speed_up(value: bool) -> None
```

<a id="unreal.TOD_Base.time_speed_up_scale"></a>

#### time\_speed\_up\_scale

```python
@property
def time_speed_up_scale() -> float
```

(float):  [Read-Write] 时间加速流逝倍率，过大会导致错误

<a id="unreal.TOD_Base.time_speed_up_scale"></a>

#### time\_speed\_up\_scale

```python
@time_speed_up_scale.setter
def time_speed_up_scale(value: float) -> None
```

<a id="unreal.TOD_Base.fx_style"></a>

#### fx\_style

```python
@property
def fx_style() -> FXStyle
```

(FXStyle):  [Read-Write] 开启此选项时间会自动流逝

<a id="unreal.TOD_Base.fx_style"></a>

#### fx\_style

```python
@fx_style.setter
def fx_style(value: FXStyle) -> None
```

<a id="unreal.TOD_Base.hide_sky_mesh"></a>

#### hide\_sky\_mesh

```python
@property
def hide_sky_mesh() -> float
```

(float):  [Read-Write] 当相机世界坐标Z值超过此数值便隐藏skycreator的天空球静态网格模型

<a id="unreal.TOD_Base.hide_sky_mesh"></a>

#### hide\_sky\_mesh

```python
@hide_sky_mesh.setter
def hide_sky_mesh(value: float) -> None
```

<a id="unreal.TOD_Base.use_height_fog_threshold"></a>

#### use\_height\_fog\_threshold

```python
@property
def use_height_fog_threshold() -> bool
```

(bool):  [Read-Only] 在鸟瞰视角下，如果高度超过一定阈值则在高度雾作用下会导致渲染错误
开启此值，超过阈值时将关闭高度雾
运行时才有效果

<a id="unreal.TOD_Base.height_fog_threshold"></a>

#### height\_fog\_threshold

```python
@property
def height_fog_threshold() -> float
```

(float):  [Read-Only] 高度雾高度阈值，相机高度超过此值会关闭高度雾

<a id="unreal.TOD_Base.is_earth"></a>

#### is\_earth

```python
@property
def is_earth() -> bool
```

(bool):  [Read-Only]

<a id="unreal.TOD_Base.earth_center"></a>

#### earth\_center

```python
@property
def earth_center() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TOD_Base.earth_radius"></a>

#### earth\_radius

```python
@property
def earth_radius() -> float
```

(float):  [Read-Only]

<a id="unreal.TOD_Base.earth_skylight_attenuation"></a>

#### earth\_skylight\_attenuation

```python
@property
def earth_skylight_attenuation() -> Vector2D
```

(Vector2D):  [Read-Only]

<a id="unreal.TOD_Base.height_fog_magnification_curve_fog_density"></a>

#### height\_fog\_magnification\_curve\_fog\_density

```python
@property
def height_fog_magnification_curve_fog_density() -> CurveFloat
```

(CurveFloat):  [Read-Only] 在鸟瞰视角下，如果相机高度超过一定阈值则会导致渲染错误
添加曲线后通过 相机高度->高度雾密度倍率 曲线来控制高度雾跟随相机高度进行高度雾密度的变化
相较于高度雾阈值，使用曲线能够更精细的控制高度雾的变化
运行时才有效果

<a id="unreal.TOD_Base.height_fog_magnification_curve_start_distance"></a>

#### height\_fog\_magnification\_curve\_start\_distance

```python
@property
def height_fog_magnification_curve_start_distance() -> CurveFloat
```

(CurveFloat):  [Read-Only] 在鸟瞰视角下，如果相机高度超过一定阈值则会导致渲染错误
添加曲线后通过 相机高度->高度雾起始距离倍率 曲线来控制高度雾跟随相机高度进行高度雾起始距离的变化
相较于高度雾阈值，使用曲线能够更精细的控制高度雾的变化
运行时才有效果

<a id="unreal.TOD_Base.tod_control_height_fog_density"></a>

#### tod\_control\_height\_fog\_density

```python
@property
def tod_control_height_fog_density() -> bool
```

(bool):  [Read-Write] 由TOD来控制高度雾密度值，反之则由天气预设表来控制高度雾密度值

<a id="unreal.TOD_Base.tod_control_height_fog_density"></a>

#### tod\_control\_height\_fog\_density

```python
@tod_control_height_fog_density.setter
def tod_control_height_fog_density(value: bool) -> None
```

<a id="unreal.TOD_Base.tod_height_fog_density"></a>

#### tod\_height\_fog\_density

```python
@property
def tod_height_fog_density() -> float
```

(float):  [Read-Write]

<a id="unreal.TOD_Base.tod_height_fog_density"></a>

#### tod\_height\_fog\_density

```python
@tod_height_fog_density.setter
def tod_height_fog_density(value: float) -> None
```

<a id="unreal.TOD_Base.root"></a>

#### root

```python
@property
def root() -> SceneComponent
```

(SceneComponent):  [Read-Only]

<a id="unreal.TOD_Base.weather_fx"></a>

#### weather\_fx

```python
@property
def weather_fx() -> NiagaraComponent
```

(NiagaraComponent):  [Read-Only] 4时间段后期框废弃
      UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
      UPostProcessComponent* Post_Morning;

      UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
      UPostProcessComponent* Post_Noon;

      UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
      UPostProcessComponent* Post_Dusk;

      UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Tod|Post")
      UPostProcessComponent* Post_Night;

<a id="unreal.TOD_Base.lightning_light"></a>

#### lightning\_light

```python
@property
def lightning_light() -> DirectionalLightComponent
```

(DirectionalLightComponent):  [Read-Only]

<a id="unreal.TOD_Base.rain_sound"></a>

#### rain\_sound

```python
@property
def rain_sound() -> AudioComponent
```

(AudioComponent):  [Read-Only]

<a id="unreal.TOD_Base.on_sunrise"></a>

#### on\_sunrise

```python
@property
def on_sunrise() -> OnSunrise
```

(OnSunrise):  [Read-Write]

<a id="unreal.TOD_Base.on_sunrise"></a>

#### on\_sunrise

```python
@on_sunrise.setter
def on_sunrise(value: OnSunrise) -> None
```

<a id="unreal.TOD_Base.on_sunset"></a>

#### on\_sunset

```python
@property
def on_sunset() -> OnSunset
```

(OnSunset):  [Read-Write]

<a id="unreal.TOD_Base.on_sunset"></a>

#### on\_sunset

```python
@on_sunset.setter
def on_sunset(value: OnSunset) -> None
```

<a id="unreal.TOD_Base.set_time_section_hdr"></a>

#### set\_time\_section\_hdr

```python
def set_time_section_hdr(time_section_hdr: Map[Vector2D, TextureCube]) -> None
```

x.set_time_section_hdr(time_section_hdr) -> None
Set Time Section HDR

Args:
    time_section_hdr (Map[Vector2D, TextureCube]):

<a id="unreal.TOD_Base.set_skycreator_hdr_texture"></a>

#### set\_skycreator\_hdr\_texture

```python
def set_skycreator_hdr_texture() -> None
```

x.set_skycreator_hdr_texture() -> None
Set Skycreator HDRTexture

<a id="unreal.TOD_Base.refresh_post"></a>

#### refresh\_post

```python
def refresh_post() -> None
```

x.refresh_post() -> None
Refresh Post

<a id="unreal.TOD_Base.refresh"></a>

#### refresh

```python
def refresh() -> None
```

x.refresh() -> None
调节曲线数值后需手动刷新场景

<a id="unreal.TOD_Base.on_change_main_camera"></a>

#### on\_change\_main\_camera

```python
def on_change_main_camera(cam_comp: CameraComponent) -> None
```

x.on_change_main_camera(cam_comp) -> None
当主视口摄像机变动时需把摄像机的UCameraComponnt传进来用以把粒子组件附加在相机下面

Args:
    cam_comp (CameraComponent):

<a id="unreal.TOD_Base.collection_light_actors"></a>

#### collection\_light\_actors

```python
def collection_light_actors() -> None
```

x.collection_light_actors() -> None
搜集场景中所有带标签的灯光Actor，场景中有灯光Actor增减时需要刷新一次

<a id="unreal.TOD_Base.change_weather"></a>

#### change\_weather

```python
def change_weather(new_weather_set: SkyCreatorWeatherPreset_51,
                   lerp_speed: float = 0.500000) -> None
```

x.change_weather(new_weather_set, lerp_speed=0.500000) -> None
变化天气
LerpSpeed：过渡时间（秒）

Args:
    new_weather_set (SkyCreatorWeatherPreset_51): 
    lerp_speed (float):

<a id="unreal.TOD_Base.change_time"></a>

#### change\_time

```python
def change_time(new_time: float,
                is_lerp: bool = True,
                lerp_speed: float = 1.000000) -> None
```

x.change_time(new_time, is_lerp=True, lerp_speed=1.000000) -> None
变化时间
LerpSpeed：过渡时间（秒）

Args:
    new_time (float): 
    is_lerp (bool): 
    lerp_speed (float):

<a id="unreal.EnvironmentUtilManager"></a>