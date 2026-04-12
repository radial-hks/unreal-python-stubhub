## EarthBuildingSubAssetsFragment Objects

```python
class EarthBuildingSubAssetsFragment(EarthPropertyFragment)
```

定义建筑子资产信息列表的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthBuildingFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sub_assets`` (Array[EarthBuildingSubAsset]):  [Read-Write] 建筑子资产列表
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthBuildingSubAssetsFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             sub_assets: Array[EarthBuildingSubAsset] = []) -> None
```

<a id="unreal.EarthBuildingSubAssetsFragment.sub_assets"></a>

#### sub\_assets

```python
@property
def sub_assets() -> Array[EarthBuildingSubAsset]
```

(Array[EarthBuildingSubAsset]):  [Read-Write] 建筑子资产列表

<a id="unreal.EarthBuildingSubAssetsFragment.sub_assets"></a>

#### sub\_assets

```python
@sub_assets.setter
def sub_assets(value: Array[EarthBuildingSubAsset]) -> None
```

<a id="unreal.EarthEntityFragment"></a>