## EarthBuildingSettings Objects

```python
class EarthBuildingSettings(EarthLayerSettingsBase)
```

地球建筑设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthBuildingSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_terrain`` (bool):  [Read-Write] 建筑是否影响地形高程
- ``batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``build_level_config`` (Map[int32, EntityBuildLevelLimits]):  [Read-Write] 哪些级别会产生生成物
- ``build_parallel`` (bool):  [Read-Write] 是否执行并行计算
- ``cache_levels`` (Array[int32]):  [Read-Write] 缓存的级别
- ``debug_mode`` (bool):  [Read-Write] 是否为调试模式
- ``default_regional_prefab_asset_library`` (SoftObjectPath):  [Read-Write] 默认的区域资产库
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``is_visible`` (bool):  [Read-Write] 是否显示要素
- ``mask_levels`` (Array[uint8]):  [Read-Write] 建筑蒙版所在级别
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``max_instance_count_per_ism`` (int32):  [Read-Write] ISM 输出片段合并的最大实例数上限
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``receives_decals`` (bool):  [Read-Write] 是否接收贴花
- ``regional_prefab_asset_libraries`` (Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``use_bake_board`` (bool):  [Read-Write]
- ``use_collision`` (bool):  [Read-Write] 是否使用碰撞
- ``use_color_data`` (bool):  [Read-Write] 是否使用数据源提供的color字段作为建筑立面颜色
- ``use_earth_prefab`` (bool):  [Read-Write] 是否使用预制体建筑系统
- ``use_roof_color_data`` (bool):  [Read-Write] 是否使用数据源提供的roof_color字段作为建筑屋顶颜色

<a id="unreal.EarthBuildingSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False,
             use_earth_prefab: bool = False,
             build_parallel: bool = False,
             batch_entity_size: int = 0,
             debug_mode: bool = False,
             max_instance_count_per_ism: int = 0,
             default_regional_prefab_asset_library: SoftObjectPath = [""],
             regional_prefab_asset_libraries: Array[SoftObjectPath] = [],
             is_visible: bool = False,
             use_collision: bool = False) -> None
```

<a id="unreal.EarthBuildingSettings.use_earth_prefab"></a>

#### use\_earth\_prefab

```python
@property
def use_earth_prefab() -> bool
```

(bool):  [Read-Write] 是否使用预制体建筑系统

<a id="unreal.EarthBuildingSettings.use_earth_prefab"></a>

#### use\_earth\_prefab

```python
@use_earth_prefab.setter
def use_earth_prefab(value: bool) -> None
```

<a id="unreal.EarthBuildingSettings.build_parallel"></a>

#### build\_parallel

```python
@property
def build_parallel() -> bool
```

(bool):  [Read-Write] 是否执行并行计算

<a id="unreal.EarthBuildingSettings.build_parallel"></a>

#### build\_parallel

```python
@build_parallel.setter
def build_parallel(value: bool) -> None
```

<a id="unreal.EarthBuildingSettings.batch_entity_size"></a>

#### batch\_entity\_size

```python
@property
def batch_entity_size() -> int
```

(int32):  [Read-Write] 并行计算时，每批计算的实体数量

<a id="unreal.EarthBuildingSettings.batch_entity_size"></a>

#### batch\_entity\_size

```python
@batch_entity_size.setter
def batch_entity_size(value: int) -> None
```

<a id="unreal.EarthBuildingSettings.debug_mode"></a>

#### debug\_mode

```python
@property
def debug_mode() -> bool
```

(bool):  [Read-Write] 是否为调试模式

<a id="unreal.EarthBuildingSettings.debug_mode"></a>

#### debug\_mode

```python
@debug_mode.setter
def debug_mode(value: bool) -> None
```

<a id="unreal.EarthBuildingSettings.max_instance_count_per_ism"></a>

#### max\_instance\_count\_per\_ism

```python
@property
def max_instance_count_per_ism() -> int
```

(int32):  [Read-Write] ISM 输出片段合并的最大实例数上限

<a id="unreal.EarthBuildingSettings.max_instance_count_per_ism"></a>

#### max\_instance\_count\_per\_ism

```python
@max_instance_count_per_ism.setter
def max_instance_count_per_ism(value: int) -> None
```

<a id="unreal.EarthBuildingSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@property
def default_regional_prefab_asset_library() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 默认的区域资产库

<a id="unreal.EarthBuildingSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@default_regional_prefab_asset_library.setter
def default_regional_prefab_asset_library(value: SoftObjectPath) -> None
```

<a id="unreal.EarthBuildingSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@property
def regional_prefab_asset_libraries() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库

<a id="unreal.EarthBuildingSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@regional_prefab_asset_libraries.setter
def regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthBuildingSettings.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write] 是否显示要素

<a id="unreal.EarthBuildingSettings.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.EarthBuildingSettings.use_collision"></a>

#### use\_collision

```python
@property
def use_collision() -> bool
```

(bool):  [Read-Write] 是否使用碰撞

<a id="unreal.EarthBuildingSettings.use_collision"></a>

#### use\_collision

```python
@use_collision.setter
def use_collision(value: bool) -> None
```

<a id="unreal.EntityBuildLevelLimits"></a>