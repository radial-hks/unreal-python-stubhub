## EarthSubAssetsFragment Objects

```python
class EarthSubAssetsFragment(EarthPropertyFragment)
```

定义预制体子资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sub_assets`` (Array[EarthSubAssetInfo]):  [Read-Write] 子资产信息列表
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthSubAssetsFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             sub_assets: Array[EarthSubAssetInfo] = []) -> None
```

<a id="unreal.EarthSubAssetsFragment.sub_assets"></a>

#### sub\_assets

```python
@property
def sub_assets() -> Array[EarthSubAssetInfo]
```

(Array[EarthSubAssetInfo]):  [Read-Write] 子资产信息列表

<a id="unreal.EarthSubAssetsFragment.sub_assets"></a>

#### sub\_assets

```python
@sub_assets.setter
def sub_assets(value: Array[EarthSubAssetInfo]) -> None
```

<a id="unreal.EarthFeatureIDFragment"></a>