## EarthScenerySettings Objects

```python
class EarthScenerySettings(EarthLayerSettingsBase)
```

地球布景设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthScenerySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_level_config`` (Map[int32, EntityBuildLevelLimits]):  [Read-Write] 哪些级别会产生生成物
- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``is_visible`` (bool):  [Read-Write] 是否显示要素
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``receives_decals`` (bool):  [Read-Write] 是否接收贴花
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``use_bake_board`` (bool):  [Read-Write]

<a id="unreal.EarthScenerySettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False, is_visible: bool = False) -> None
```

<a id="unreal.EarthScenerySettings.is_visible"></a>

#### is\_visible

```python
@property
def is_visible() -> bool
```

(bool):  [Read-Write] 是否显示要素

<a id="unreal.EarthScenerySettings.is_visible"></a>

#### is\_visible

```python
@is_visible.setter
def is_visible(value: bool) -> None
```

<a id="unreal.EarthVegetationSettings"></a>