## EarthFeatureIdSettings Objects

```python
class EarthFeatureIdSettings(EarthLayerSettingsBase)
```

地球地形设置

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthFeatureIdSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_delta_level_bias`` (int32):  [Read-Write] 与ScreenSizeFactor叠加
- ``max_concurrent_requests`` (int32):  [Read-Write] 最多有多少个带图层的地块在并行生成，可根据机器性能微调
- ``need_register`` (bool):  [Read-Write] 是否开启图层生成
- ``screen_size_factor`` (Vector):  [Read-Write] 高级别的图层是否会更早的出现，数值越大，在高空时越能看到更精细的生成物
- ``use_bake_board`` (bool):  [Read-Write]

<a id="unreal.EarthFeatureIdSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_bake_board: bool = False) -> None
```

<a id="unreal.EarthGlobalSettings"></a>