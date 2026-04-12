## EarthGlobalSettings Objects

```python
class EarthGlobalSettings(StructBase)
```

地球全局控制参数

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthGlobalSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``building_settings`` (EarthBuildingSettings):  [Read-Write] 地球地形设置
- ``custom_settings`` (EarthCustomSettings):  [Read-Write] 地球地形设置
- ``embankment_settings`` (EarthEmbankmentSettings):  [Read-Write] 路堤设置
- ``feature_id_settings`` (EarthFeatureIdSettings):  [Read-Write] 地球地形设置
- ``is_visible`` (bool):  [Read-Write] 控制全局模型显隐
- ``level_split_factors`` (Map[int32, float]):  [Read-Write] 控制不同Level是否分裂的系数
- ``receives_decals`` (bool):  [Read-Write] 控制全局接收贴花与否
- ``road_settings`` (EarthRoadSettings):  [Read-Write] 地球地形设置
- ``scenery_settings`` (EarthScenerySettings):  [Read-Write] 地球地形设置
- ``terrain_settings`` (EarthTerrainSettings):  [Read-Write] 地球地形设置
- ``use_collision`` (bool):  [Read-Write] 控制全局碰撞有无
- ``vegetation_settings`` (EarthVegetationSettings):  [Read-Write] 地球地形设置
- ``water_settings`` (EarthWaterSettings):  [Read-Write] 地球地形设置

<a id="unreal.EarthGlobalSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EarthScenerySettings"></a>