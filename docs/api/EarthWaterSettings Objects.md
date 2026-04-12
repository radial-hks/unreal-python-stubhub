## EarthWaterSettings Objects

```python
class EarthWaterSettings(EarthLayerSettingsBase)
```

地球全局控制参数

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthWaterSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_terrain`` (bool):  [Read-Write] 水域是否影响地形高程，开启后，水域可通过矢量上的Depth属性对地形高程进行下压
- ``build_collision`` (bool):  [Read-Write] 是否生成水域碰撞
- ``collision_color`` (Color):  [Read-Write] 碰撞颜色
- ``collision_enabled`` (CollisionEnabled):  [Read-Write] 碰撞启用类型
- ``collision_object_type`` (CollisionChannel):  [Read-Write] 碰撞对象类型
- ``collision_profile_name`` (Name):  [Read-Write] 碰撞预设名称，该名称需要在ProjectSettings->Engine->Collision->Preset中定义
- ``collision_vertex_num`` (int32):  [Read-Write] 水域碰撞的顶点数
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``fetch_multi_tiles`` (bool):  [Read-Write] 是否从周围地块中获取数据，开启后，会多读取周围8个地块的水域数据，以解决开启bUseInnerExpand参数后可能导致的地块边界处的衔接问题
- ``is_visible`` (bool):  [Read-Write] 控制水域模型显隐
- ``limit_under_water_dem`` (bool):  [Read-Write] 是否限制水下地形的最大高度，防止其超过水域深度Depth属性的设定值
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``mesh_batch_element_size`` (int32):  [Read-Write] 当需要频繁修改水域材质时，建议将值尽量调小，而不需要修改材质时，将值改为1000
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``show_mesh`` (bool):  [Read-Write] 是否渲染水域模型
- ``show_tile_hem`` (bool):  [Read-Write] 是否在水域地块拼接处生成包边
- ``show_under_water`` (bool):  [Read-Write] 是否渲染水下效果
- ``tile_hem_level_range`` (IntPoint):  [Read-Write] 生成水域地块包边的级别，X为生成的最低级别，Y为生成的最高级别
- ``under_water_start_level`` (int32):  [Read-Write] 水下效果从哪一级开始出现
- ``use_bake_board`` (bool):  [Read-Write]
- ``use_collision`` (bool):  [Read-Write]
- ``use_inner_expand`` (bool):  [Read-Write] 开启后，水域蒙版和水域裙边会向轮廓内生成；关闭后，水域蒙版和水域裙边会向轮廓外生成
- ``water_outline_data_level`` (int32):  [Read-Write] 水域描边效果所用的数据级别，仅供API使用

<a id="unreal.EarthWaterSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False) -> None
```

<a id="unreal.EarthRoadSettings"></a>