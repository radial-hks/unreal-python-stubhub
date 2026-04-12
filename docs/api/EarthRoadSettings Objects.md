## EarthRoadSettings Objects

```python
class EarthRoadSettings(EarthLayerSettingsBase)
```

地球道路设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthRoadSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_terrain`` (bool):  [Read-Write] 道路是否影响地形高程
- ``batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``build_parallel`` (bool):  [Read-Write] 是否执行并行计算
- ``build_underground_road`` (bool):  [Read-Write] 是否生成地下道路
- ``cache_levels`` (Array[int32]):  [Read-Write]
- ``debug_mode`` (bool):  [Read-Write] 是否为调试模式
- ``default_regional_prefab_asset_library`` (SoftObjectPath):  [Read-Write] 默认的区域资产库
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``is_visible`` (bool):  [Read-Write] 是否显示要素
- ``is_visible_traffic`` (bool):  [Read-Write] 是否生成车流
- ``level_terrain_buffers`` (Map[int32, EarthRoadTerrainBufferSettings]):  [Read-Write] 不同级别影响地形参数
- ``mask_extend_width`` (float):  [Read-Write] 道路蒙版和压地形最大增加宽度，单位cm
- ``mask_level_config`` (Array[uint8]):  [Read-Write] 道路蒙版所在级别
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``max_instance_count_per_ism`` (int32):  [Read-Write] ISM 输出片段合并的最大实例数上限
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``receives_decals`` (bool):  [Read-Write] 是否接收贴花
- ``regional_prefab_asset_libraries`` (Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库
- ``register_mask`` (bool):  [Read-Write]
- ``road_feature_level_config`` (Array[int32]):  [Read-Write] 道路要素分级生成级别
- ``road_level_config`` (Map[int32, EntityRoadLevelLimits]):  [Read-Write] 每个级别生成道路分类
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``use_bake_board`` (bool):  [Read-Write]
- ``use_collision`` (bool):  [Read-Write] 是否使用碰撞
- ``use_earth_prefab`` (bool):  [Read-Write] 是否使用预制体建筑系统
- ``use_road_feature_lod`` (bool):  [Read-Write] 是否使用预制体建筑系统

<a id="unreal.EarthRoadSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        use_bake_board: bool = False,
        use_road_feature_lod: bool = False,
        build_underground_road: bool = False,
        is_visible: bool = False,
        is_visible_traffic: bool = False,
        use_collision: bool = False,
        use_earth_prefab: bool = False,
        build_parallel: bool = False,
        batch_entity_size: int = 0,
        debug_mode: bool = False,
        max_instance_count_per_ism: int = 0,
        default_regional_prefab_asset_library: SoftObjectPath = [""],
        regional_prefab_asset_libraries: Array[SoftObjectPath] = []) -> None
```

<a id="unreal.EarthRoadSettings.use_road_feature_lod"></a>

#### use\_road\_feature\_lod

```python
@property
def use_road_feature_lod() -> bool
```

(bool):  [Read-Write] 是否使用预制体建筑系统

<a id="unreal.EarthRoadSettings.use_road_feature_lod"></a>

#### use\_road\_feature\_lod

```python
@use_road_feature_lod.setter
def use_road_feature_lod(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.build_underground_road"></a>

#### build\_underground\_road

```python
@property
def build_underground_road() -> bool
```

(bool):  [Read-Write] 是否生成地下道路

<a id="unreal.EarthRoadSettings.build_underground_road"></a>

#### build\_underground\_road

```python
@build_underground_road.setter
def build_underground_road(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write] 是否显示要素

<a id="unreal.EarthRoadSettings.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.is_visible_traffic"></a>

#### is\_visible\_traffic

```python
@property
def is_visible_traffic() -> bool
```

(bool):  [Read-Write] 是否生成车流

<a id="unreal.EarthRoadSettings.is_visible_traffic"></a>

#### is\_visible\_traffic

```python
@is_visible_traffic.setter
def is_visible_traffic(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.use_collision"></a>

#### use\_collision

```python
@property
def use_collision() -> bool
```

(bool):  [Read-Write] 是否使用碰撞

<a id="unreal.EarthRoadSettings.use_collision"></a>

#### use\_collision

```python
@use_collision.setter
def use_collision(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.use_earth_prefab"></a>

#### use\_earth\_prefab

```python
@property
def use_earth_prefab() -> bool
```

(bool):  [Read-Write] 是否使用预制体建筑系统

<a id="unreal.EarthRoadSettings.use_earth_prefab"></a>

#### use\_earth\_prefab

```python
@use_earth_prefab.setter
def use_earth_prefab(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.b_use_earth_prefab_road"></a>

#### b\_use\_earth\_prefab\_road

```python
@property
def b_use_earth_prefab_road() -> bool
```

deprecated: 'b_use_earth_prefab_road' was renamed to 'use_earth_prefab'.

<a id="unreal.EarthRoadSettings.b_use_earth_prefab_road"></a>

#### b\_use\_earth\_prefab\_road

```python
@b_use_earth_prefab_road.setter
def b_use_earth_prefab_road(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.build_parallel"></a>

#### build\_parallel

```python
@property
def build_parallel() -> bool
```

(bool):  [Read-Write] 是否执行并行计算

<a id="unreal.EarthRoadSettings.build_parallel"></a>

#### build\_parallel

```python
@build_parallel.setter
def build_parallel(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.batch_entity_size"></a>

#### batch\_entity\_size

```python
@property
def batch_entity_size() -> int
```

(int32):  [Read-Write] 并行计算时，每批计算的实体数量

<a id="unreal.EarthRoadSettings.batch_entity_size"></a>

#### batch\_entity\_size

```python
@batch_entity_size.setter
def batch_entity_size(value: int) -> None
```

<a id="unreal.EarthRoadSettings.debug_mode"></a>

#### debug\_mode

```python
@property
def debug_mode() -> bool
```

(bool):  [Read-Write] 是否为调试模式

<a id="unreal.EarthRoadSettings.debug_mode"></a>

#### debug\_mode

```python
@debug_mode.setter
def debug_mode(value: bool) -> None
```

<a id="unreal.EarthRoadSettings.max_instance_count_per_ism"></a>

#### max\_instance\_count\_per\_ism

```python
@property
def max_instance_count_per_ism() -> int
```

(int32):  [Read-Write] ISM 输出片段合并的最大实例数上限

<a id="unreal.EarthRoadSettings.max_instance_count_per_ism"></a>

#### max\_instance\_count\_per\_ism

```python
@max_instance_count_per_ism.setter
def max_instance_count_per_ism(value: int) -> None
```

<a id="unreal.EarthRoadSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@property
def default_regional_prefab_asset_library() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 默认的区域资产库

<a id="unreal.EarthRoadSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@default_regional_prefab_asset_library.setter
def default_regional_prefab_asset_library(value: SoftObjectPath) -> None
```

<a id="unreal.EarthRoadSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@property
def regional_prefab_asset_libraries() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库

<a id="unreal.EarthRoadSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@regional_prefab_asset_libraries.setter
def regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthRoadTerrainBufferSettings"></a>