## AesAssetActorBase Objects

```python
class AesAssetActorBase(Actor)
```

资产创作工具基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetActorBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_guid`` (Guid):  [Read-Write] The GUID for this actor; this guid will be the same for actors from instanced streaming levels.
  see: ActorInstanceGuid, FActorInstanceGuidMapper
  note: Don't use VisibleAnywhere here to avoid getting the CPF_Edit flag and get this property reset when resetting to defaults. See FActorDetails::AddActorCategory and EditorUtilities::CopySingleProperty for details.
- ``actor_instance_guid`` (Guid):  [Read-Write] The instance GUID for this actor; this guid will be unique for actors from instanced streaming levels.
  see: ActorGuid
  note: This is not guaranteed to be valid during PostLoad, but safe to access from RegisterAllComponents.
- ``all_child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 所有子资产引用列表
- ``allow_tick_before_begin_play`` (bool):  [Read-Write] Whether we allow this Actor to tick before it receives the BeginPlay event.
  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.
  This Actor must be able to tick for this setting to be relevant.
- ``always_relevant`` (bool):  [Read-Write] Always relevant for network (overrides bOnlyRelevantToOwner).
- ``asset_library`` (DataTable):  [Read-Write] 填写需要预览的资产在库中的序号
- ``async_physics_tick_enabled`` (bool):  [Read-Write] Whether to use use the async physics tick with this actor.
- ``auto_correct_curve`` (bool):  [Read-Write] 是否自动纠正样条线的错误，并在严重错误时停止生成
- ``auto_destroy_when_finished`` (bool):  [Read-Write] If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight.
- ``auto_preview`` (bool):  [Read-Write] 是否自动预览生成结果
- ``auto_receive_input`` (AutoReceiveInput):  [Read-Write] Automatically registers this actor to receive input from a player.
- ``block_input`` (bool):  [Read-Write] If true, all input on the stack below this actor will not be considered
- ``build_in_game_thread`` (bool):  [Read-Write] 是否在游戏线程执行生成
- ``call_pre_replication`` (bool):  [Read-Write]
- ``call_pre_replication_for_replay`` (bool):  [Read-Write]
- ``can_be_damaged`` (bool):  [Read-Write] Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.
  see: https://www.unrealengine.com/blog/damage-in-ue4
  see: TakeDamage(), ReceiveDamage()
- ``can_be_in_cluster`` (bool):  [Read-Write] If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance
- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``child_index_color`` (Color):  [Read-Write] 子资产索引值的颜色
- ``child_index_world_size`` (float):  [Read-Write] 子资产索引值的尺寸
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``content_bundle_guid`` (Guid):  [Read-Write] The GUID for this actor's content bundle.
- ``convert_dynamic_mesh_to_static_mesh`` (bool):  [Read-Write] 是否合并生成物
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
- ``has_per_instance_hit_proxies`` (bool):  [Read-Write] 是否能选中每个实例化静态网格体
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
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
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
- ``preview_index`` (int32):  [Read-Write] 填写需要预览的资产在库中的序号
- ``preview_lod`` (int32):  [Read-Write] 资产当前LOD级别
- ``preview_lod_max`` (int32):  [Read-Write] 资产最大LOD级别
- ``preview_name`` (Name):  [Read-Only] 需要预览的资产在库中的名字
- ``primary_actor_tick`` (ActorTickFunction):  [Read-Write] Primary Actor tick function, which calls TickActor().
  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.
  see: https://docs.unrealengine.com/API/Runtime/Engine/Engine/FTickFunction
  see: AddTickPrerequisiteActor(), AddTickPrerequisiteComponent()
- ``primitive_components`` (Array[PrimitiveComponent]):  [Read-Write] 资产生成物
- ``random_seed`` (int32):  [Read-Write] 随机种子
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
- ``save_child_assets`` (bool):  [Read-Write] 是否将子资产引用列表保存到库中
- ``show_child_index`` (bool):  [Read-Write] 是否可视化子资产的索引值
- ``show_registered_components`` (bool):  [Read-Write] 是否显示注册的生成物
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据
- ``spawn_collision_handling_method`` (SpawnActorCollisionHandlingMethod):  [Read-Write] Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here.
- ``spline_component`` (SplineComponent):  [Read-Write]
- ``sprite_scale`` (float):  [Read-Write] The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing.
- ``text_render_components`` (Array[TextRenderComponent]):  [Read-Write] 资产索引值
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

<a id="unreal.AesAssetActorBase.spline_component"></a>

#### spline\_component

```python
@property
def spline_component() -> SplineComponent
```

(SplineComponent):  [Read-Write]

<a id="unreal.AesAssetActorBase.spline_component"></a>

#### spline\_component

```python
@spline_component.setter
def spline_component(value: SplineComponent) -> None
```

<a id="unreal.AesAssetActorBase.random_seed"></a>

#### random\_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] 随机种子

<a id="unreal.AesAssetActorBase.random_seed"></a>

#### random\_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.AesAssetActorBase.meta_data"></a>

#### meta\_data

```python
@property
def meta_data() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write] 资产元数据

<a id="unreal.AesAssetActorBase.meta_data"></a>

#### meta\_data

```python
@meta_data.setter
def meta_data(value: AesAssetMetaData) -> None
```

<a id="unreal.AesAssetActorBase.size_data"></a>

#### size\_data

```python
@property
def size_data() -> AesAssetSizeData
```

(AesAssetSizeData):  [Read-Write] 资产尺寸数据

<a id="unreal.AesAssetActorBase.size_data"></a>

#### size\_data

```python
@size_data.setter
def size_data(value: AesAssetSizeData) -> None
```

<a id="unreal.AesAssetActorBase.collision_data"></a>

#### collision\_data

```python
@property
def collision_data() -> AesAssetCollisionData
```

(AesAssetCollisionData):  [Read-Write] 资产碰撞数据

<a id="unreal.AesAssetActorBase.collision_data"></a>

#### collision\_data

```python
@collision_data.setter
def collision_data(value: AesAssetCollisionData) -> None
```

<a id="unreal.AesAssetActorBase.child_assets"></a>

#### child\_assets

```python
@property
def child_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表

<a id="unreal.AesAssetActorBase.child_assets"></a>

#### child\_assets

```python
@child_assets.setter
def child_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesAssetActorBase.all_child_assets"></a>

#### all\_child\_assets

```python
@property
def all_child_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 所有子资产引用列表

<a id="unreal.AesAssetActorBase.all_child_assets"></a>

#### all\_child\_assets

```python
@all_child_assets.setter
def all_child_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesAssetActorBase.auto_preview"></a>

#### auto\_preview

```python
@property
def auto_preview() -> bool
```

(bool):  [Read-Write] 是否自动预览生成结果

<a id="unreal.AesAssetActorBase.auto_preview"></a>

#### auto\_preview

```python
@auto_preview.setter
def auto_preview(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.preview_lod"></a>

#### preview\_lod

```python
@property
def preview_lod() -> int
```

(int32):  [Read-Write] 资产当前LOD级别

<a id="unreal.AesAssetActorBase.preview_lod"></a>

#### preview\_lod

```python
@preview_lod.setter
def preview_lod(value: int) -> None
```

<a id="unreal.AesAssetActorBase.preview_lod_max"></a>

#### preview\_lod\_max

```python
@property
def preview_lod_max() -> int
```

(int32):  [Read-Write] 资产最大LOD级别

<a id="unreal.AesAssetActorBase.preview_lod_max"></a>

#### preview\_lod\_max

```python
@preview_lod_max.setter
def preview_lod_max(value: int) -> None
```

<a id="unreal.AesAssetActorBase.show_registered_components"></a>

#### show\_registered\_components

```python
@property
def show_registered_components() -> bool
```

(bool):  [Read-Write] 是否显示注册的生成物

<a id="unreal.AesAssetActorBase.show_registered_components"></a>

#### show\_registered\_components

```python
@show_registered_components.setter
def show_registered_components(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.auto_correct_curve"></a>

#### auto\_correct\_curve

```python
@property
def auto_correct_curve() -> bool
```

(bool):  [Read-Write] 是否自动纠正样条线的错误，并在严重错误时停止生成

<a id="unreal.AesAssetActorBase.auto_correct_curve"></a>

#### auto\_correct\_curve

```python
@auto_correct_curve.setter
def auto_correct_curve(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.build_in_game_thread"></a>

#### build\_in\_game\_thread

```python
@property
def build_in_game_thread() -> bool
```

(bool):  [Read-Write] 是否在游戏线程执行生成

<a id="unreal.AesAssetActorBase.build_in_game_thread"></a>

#### build\_in\_game\_thread

```python
@build_in_game_thread.setter
def build_in_game_thread(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.convert_dynamic_mesh_to_static_mesh"></a>

#### convert\_dynamic\_mesh\_to\_static\_mesh

```python
@property
def convert_dynamic_mesh_to_static_mesh() -> bool
```

(bool):  [Read-Write] 是否合并生成物

<a id="unreal.AesAssetActorBase.convert_dynamic_mesh_to_static_mesh"></a>

#### convert\_dynamic\_mesh\_to\_static\_mesh

```python
@convert_dynamic_mesh_to_static_mesh.setter
def convert_dynamic_mesh_to_static_mesh(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.primitive_components"></a>

#### primitive\_components

```python
@property
def primitive_components() -> Array[PrimitiveComponent]
```

(Array[PrimitiveComponent]):  [Read-Write] 资产生成物

<a id="unreal.AesAssetActorBase.primitive_components"></a>

#### primitive\_components

```python
@primitive_components.setter
def primitive_components(value: Array[PrimitiveComponent]) -> None
```

<a id="unreal.AesAssetActorBase.has_per_instance_hit_proxies"></a>

#### has\_per\_instance\_hit\_proxies

```python
@property
def has_per_instance_hit_proxies() -> bool
```

(bool):  [Read-Write] 是否能选中每个实例化静态网格体

<a id="unreal.AesAssetActorBase.has_per_instance_hit_proxies"></a>

#### has\_per\_instance\_hit\_proxies

```python
@has_per_instance_hit_proxies.setter
def has_per_instance_hit_proxies(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.show_child_index"></a>

#### show\_child\_index

```python
@property
def show_child_index() -> bool
```

(bool):  [Read-Write] 是否可视化子资产的索引值

<a id="unreal.AesAssetActorBase.show_child_index"></a>

#### show\_child\_index

```python
@show_child_index.setter
def show_child_index(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.child_index_world_size"></a>

#### child\_index\_world\_size

```python
@property
def child_index_world_size() -> float
```

(float):  [Read-Write] 子资产索引值的尺寸

<a id="unreal.AesAssetActorBase.child_index_world_size"></a>

#### child\_index\_world\_size

```python
@child_index_world_size.setter
def child_index_world_size(value: float) -> None
```

<a id="unreal.AesAssetActorBase.child_index_color"></a>

#### child\_index\_color

```python
@property
def child_index_color() -> Color
```

(Color):  [Read-Write] 子资产索引值的颜色

<a id="unreal.AesAssetActorBase.child_index_color"></a>

#### child\_index\_color

```python
@child_index_color.setter
def child_index_color(value: Color) -> None
```

<a id="unreal.AesAssetActorBase.text_render_components"></a>

#### text\_render\_components

```python
@property
def text_render_components() -> Array[TextRenderComponent]
```

(Array[TextRenderComponent]):  [Read-Write] 资产索引值

<a id="unreal.AesAssetActorBase.text_render_components"></a>

#### text\_render\_components

```python
@text_render_components.setter
def text_render_components(value: Array[TextRenderComponent]) -> None
```

<a id="unreal.AesAssetActorBase.asset_library"></a>

#### asset\_library

```python
@property
def asset_library() -> DataTable
```

(DataTable):  [Read-Write] 填写需要预览的资产在库中的序号

<a id="unreal.AesAssetActorBase.asset_library"></a>

#### asset\_library

```python
@asset_library.setter
def asset_library(value: DataTable) -> None
```

<a id="unreal.AesAssetActorBase.preview_index"></a>

#### preview\_index

```python
@property
def preview_index() -> int
```

(int32):  [Read-Write] 填写需要预览的资产在库中的序号

<a id="unreal.AesAssetActorBase.preview_index"></a>

#### preview\_index

```python
@preview_index.setter
def preview_index(value: int) -> None
```

<a id="unreal.AesAssetActorBase.preview_name"></a>

#### preview\_name

```python
@property
def preview_name() -> Name
```

(Name):  [Read-Only] 需要预览的资产在库中的名字

<a id="unreal.AesAssetActorBase.save_child_assets"></a>

#### save\_child\_assets

```python
@property
def save_child_assets() -> bool
```

(bool):  [Read-Write] 是否将子资产引用列表保存到库中

<a id="unreal.AesAssetActorBase.save_child_assets"></a>

#### save\_child\_assets

```python
@save_child_assets.setter
def save_child_assets(value: bool) -> None
```

<a id="unreal.AesAssetActorBase.sync_asset_data"></a>

#### sync\_asset\_data

```python
def sync_asset_data(reverse: bool = False) -> None
```

x.sync_asset_data(reverse=False) -> None
更新资产参数

Args:
    reverse (bool):

<a id="unreal.AesAssetActorBase.set_spline_curves"></a>

#### set\_spline\_curves

```python
def set_spline_curves(spline_curves: AesSplineCurves) -> None
```

x.set_spline_curves(spline_curves) -> None
设置样条线

Args:
    spline_curves (AesSplineCurves):

<a id="unreal.AesAssetActorBase.save_to_library"></a>

#### save\_to\_library

```python
def save_to_library() -> None
```

x.save_to_library() -> None
保存资产数据到库中

<a id="unreal.AesAssetActorBase.register_asset"></a>

#### register\_asset

```python
def register_asset() -> None
```

x.register_asset() -> None
注册资产生成物

<a id="unreal.AesAssetActorBase.load_from_library"></a>

#### load\_from\_library

```python
def load_from_library() -> None
```

x.load_from_library() -> None
加载库中的资产数据

<a id="unreal.AesAssetActorBase.get_spline_curves"></a>

#### get\_spline\_curves

```python
def get_spline_curves() -> AesSplineCurves
```

x.get_spline_curves() -> AesSplineCurves
获取样条线

Returns:
    AesSplineCurves:

<a id="unreal.AesAssetActorBase.destroy_asset"></a>

#### destroy\_asset

```python
def destroy_asset() -> None
```

x.destroy_asset() -> None
销毁资产生成物

<a id="unreal.AesAssetActorBase.debug_asset"></a>

#### debug\_asset

```python
def debug_asset() -> None
```

x.debug_asset() -> None
生成资产调试数据

<a id="unreal.AesAssetActorBase.create_asset"></a>

#### create\_asset

```python
def create_asset() -> None
```

x.create_asset() -> None
执行创建资产

<a id="unreal.AesAssetActorBase.build_asset"></a>

#### build\_asset

```python
def build_asset() -> None
```

x.build_asset() -> None
创建资产生成物

<a id="unreal.AesAssetSettings"></a>