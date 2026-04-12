## AesAssetSettings Objects

```python
class AesAssetSettings(DeveloperSettings)
```

Aes Asset Settings

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_parallel`` (bool):  [Read-Write] 是否使用并行计算
- ``building_batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``modular_building_guesser_max_iteration`` (int32):  [Read-Write] 模块化建筑猜测器最大迭代次数，次数越大，尝试匹配出来的模块化建筑风格表的次数越多，但是速度会变慢
- ``mono_building_guesser_max_iteration`` (int32):  [Read-Write] 单体建筑猜测器最大迭代次数，次数越大，尝试匹配出来的单体建筑风格表的次数越多，但是速度会变慢
- ``mono_building_guesser_precision`` (int32):  [Read-Write] 单体建筑猜测器精确度，值越大，猜测出来的单体建筑的匹配度越高，但可能导致单体建筑出现的数量变少
- ``region_libraries`` (Array[AesAssetRegionLibrary]):  [Read-Write] 区域列表
- ``road_batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``road_junction_batch_entity_size`` (int32):  [Read-Write] 并行计算时，每批计算的实体数量
- ``summary_library`` (SoftObjectPath):  [Read-Write] 资产表总表

<a id="unreal.AesAssetSettings.summary_library"></a>

#### summary\_library

```python
@property
def summary_library() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 资产表总表

<a id="unreal.AesAssetSettings.summary_library"></a>

#### summary\_library

```python
@summary_library.setter
def summary_library(value: SoftObjectPath) -> None
```

<a id="unreal.AesAssetSettings.region_libraries"></a>

#### region\_libraries

```python
@property
def region_libraries() -> Array[AesAssetRegionLibrary]
```

(Array[AesAssetRegionLibrary]):  [Read-Write] 区域列表

<a id="unreal.AesAssetSettings.region_libraries"></a>

#### region\_libraries

```python
@region_libraries.setter
def region_libraries(value: Array[AesAssetRegionLibrary]) -> None
```

<a id="unreal.AesClusterAssetActor"></a>