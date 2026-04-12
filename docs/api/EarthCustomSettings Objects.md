## EarthCustomSettings Objects

```python
class EarthCustomSettings(EarthLayerSettingsBase)
```

Earth Custom Settings

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthCustomSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_regional_prefab_asset_library`` (SoftObjectPath):  [Read-Write] 默认的区域资产库
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``layer_configs`` (Array[EarthCustomLayerConfig]):  [Read-Write] 使用何种数据源
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``regional_prefab_asset_libraries`` (Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``use_bake_board`` (bool):  [Read-Write]

<a id="unreal.EarthCustomSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        use_bake_board: bool = False,
        layer_configs: Array[EarthCustomLayerConfig] = [],
        default_regional_prefab_asset_library: SoftObjectPath = [""],
        regional_prefab_asset_libraries: Array[SoftObjectPath] = []) -> None
```

<a id="unreal.EarthCustomSettings.layer_configs"></a>

#### layer\_configs

```python
@property
def layer_configs() -> Array[EarthCustomLayerConfig]
```

(Array[EarthCustomLayerConfig]):  [Read-Write] 使用何种数据源

<a id="unreal.EarthCustomSettings.layer_configs"></a>

#### layer\_configs

```python
@layer_configs.setter
def layer_configs(value: Array[EarthCustomLayerConfig]) -> None
```

<a id="unreal.EarthCustomSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@property
def default_regional_prefab_asset_library() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 默认的区域资产库

<a id="unreal.EarthCustomSettings.default_regional_prefab_asset_library"></a>

#### default\_regional\_prefab\_asset\_library

```python
@default_regional_prefab_asset_library.setter
def default_regional_prefab_asset_library(value: SoftObjectPath) -> None
```

<a id="unreal.EarthCustomSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@property
def regional_prefab_asset_libraries() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 额外的区域资产库

<a id="unreal.EarthCustomSettings.regional_prefab_asset_libraries"></a>

#### regional\_prefab\_asset\_libraries

```python
@regional_prefab_asset_libraries.setter
def regional_prefab_asset_libraries(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthEmbankmentSettings"></a>