## AesRenderResourceSettings Objects

```python
class AesRenderResourceSettings(DeveloperSettings)
```

Aes Render Resource Settings

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesRenderResource
- **File**: AesRenderResourceSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acc_pool_initial_size`` (int32):  [Read-Write]
- ``batch_counter_type`` (AesRenderResourceBatchCounterType):  [Read-Write]
- ``batch_instance_size`` (int32):  [Read-Write]
- ``cache_level_range`` (IntPoint):  [Read-Write] 控制缓存哪些级别的生成物
- ``cache_root_path`` (str):  [Read-Write] 缓存的保存路径
- ``cache_size`` (int32):  [Read-Write]
- ``combine_render_resource`` (bool):  [Read-Write] 是否合并生成物
- ``combine_to_dynamic_mesh`` (bool):  [Read-Write] 是否合并为动态网格体
- ``component_max_idle_frames`` (int32):  [Read-Write]
- ``component_mobility`` (ComponentMobility):  [Read-Write] 组件移动性
- ``convert_dynamic_mesh_to_static_mesh`` (bool):  [Read-Write] 是否将动态网格体转为静态网格体
- ``convert_nanite_static_mesh`` (bool):  [Read-Write] 是否生成Nanite静态网格体
- ``counter_factors`` (AesRenderResourceBatchCounterFactors):  [Read-Write]
- ``dmc_pool_initial_size`` (int32):  [Read-Write]
- ``force_no_collision`` (bool):  [Read-Write] 强制不使用碰撞
- ``ismc_pool_initial_size`` (int32):  [Read-Write]
- ``load_cache`` (bool):  [Read-Write] 控制是否加载缓存到本地的生成物
- ``mass_intersection_spawner`` (SoftClassPath):  [Read-Write]
- ``mass_vehicle_spawner`` (SoftClassPath):  [Read-Write]
- ``max_batch_amount`` (int32):  [Read-Write]
- ``max_batch_execution_time_in_seconds`` (double):  [Read-Write]
- ``max_collision_vertices`` (int32):  [Read-Write] 单体碰撞组件中的最大顶点数量
- ``max_combine_vertices`` (int32):  [Read-Write]
- ``max_instance_amount`` (int32):  [Read-Write]
- ``save_cache`` (bool):  [Read-Write] 控制是否缓存生成物到本地
- ``show_registered_components`` (bool):  [Read-Write] 显示注册的组件,仅非UE_BUILD_SHIPPING有效
- ``smc_pool_initial_size`` (int32):  [Read-Write]
- ``transient_render_resource_actor`` (bool):  [Read-Write] 是否生成临时的生成物
- ``use_async_cook_collision`` (bool):  [Read-Write] 是否异步生成碰撞
- ``use_component_pool`` (bool):  [Read-Write]
- ``use_distance_priority`` (bool):  [Read-Write]
- ``use_framing_register`` (bool):  [Read-Write]

<a id="unreal.AesRenderResourceSettings.component_mobility"></a>

#### component\_mobility

```python
@property
def component_mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] 组件移动性

<a id="unreal.AesStaticMeshComponent"></a>