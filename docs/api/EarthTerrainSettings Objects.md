## EarthTerrainSettings Objects

```python
class EarthTerrainSettings(EarthLayerSettingsBase)
```

地球地形设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthTerrainSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_collision`` (bool):  [Read-Write] 是否生成地形碰撞
- ``collision_color`` (Color):  [Read-Write] 碰撞颜色
- ``collision_vertex_num`` (int32):  [Read-Write] 地形碰撞的顶点数
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``dom_process_settings`` (EarthDomProcessSettings):  [Read-Write]
- ``dom_use_full_mip`` (bool):  [Read-Write] Dom是否生成全量的Mipmap，默认是1
- ``enable_max_update_speed`` (bool):  [Read-Write]
- ``flow_map_level_config`` (Array[uint8]):  [Read-Write] FlowMap所在级别
- ``is_visible`` (bool):  [Read-Write] 是否显示要素
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``max_level`` (int32):  [Read-Write] 控制地形图层生成的最大等级
- ``max_update_speed`` (float):  [Read-Write] 仅在相机移动速度小于该值时，LOD系统才会进行实时更新，单位为m/s
- ``mesh_batch_element_size`` (int32):  [Read-Write] 当需要频繁修改地形材质时，建议将值尽量调小，而不需要修改材质时，将值改为1000
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``receives_decals`` (bool):  [Read-Write] 是否接收贴花
- ``register_hole_mask`` (bool):  [Read-Write] 默认为False，因为Normal已在VertexFactory中实时计算
- ``register_land_classification`` (bool):  [Read-Write]
- ``register_lcg`` (bool):  [Read-Write]
- ``register_vgm`` (bool):  [Read-Write]
- ``sampler_type`` (EarthSamplerType):  [Read-Write] 控制数字高程图的采样类型
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``show_mesh`` (bool):  [Read-Write]
- ``splat_map_color_index_mappings`` (Array[EarthSplatMapColorIndexMapping]):  [Read-Write] SplatMap颜色到索引的映射配置
- ``splat_map_level_config`` (Array[uint8]):  [Read-Write] SplatMap所在级别
- ``terrain_precision_mode`` (EarthTerrainPrecisionMode):  [Read-Write] 地形精度
- ``use_bake_board`` (bool):  [Read-Write]
- ``use_collision`` (bool):  [Read-Write]

<a id="unreal.EarthTerrainSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False, is_visible: bool = False) -> None
```

<a id="unreal.EarthTerrainSettings.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write] 是否显示要素

<a id="unreal.EarthTerrainSettings.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.EarthSplatMapColorIndexMapping"></a>