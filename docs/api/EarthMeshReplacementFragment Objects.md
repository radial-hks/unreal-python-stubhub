## EarthMeshReplacementFragment Objects

```python
class EarthMeshReplacementFragment(EarthPropertyFragment)
```

网格替换片段 - 用于替换静态网格体实例的网格并按包围盒匹配尺寸

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``replacement_map`` (Map[StaticMesh, EarthStaticMeshAssetFragment]):  [Read-Write] 网格替换映射表：源网格 → 目标网格资产片段
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthMeshReplacementFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    replacement_map: Map[StaticMesh,
                         EarthStaticMeshAssetFragment] = {}) -> None
```

<a id="unreal.EarthMeshReplacementFragment.replacement_map"></a>

#### replacement\_map

```python
@property
def replacement_map() -> Map[StaticMesh, EarthStaticMeshAssetFragment]
```

(Map[StaticMesh, EarthStaticMeshAssetFragment]):  [Read-Write] 网格替换映射表：源网格 → 目标网格资产片段

<a id="unreal.EarthMeshReplacementFragment.replacement_map"></a>

#### replacement\_map

```python
@replacement_map.setter
def replacement_map(
        value: Map[StaticMesh, EarthStaticMeshAssetFragment]) -> None
```

<a id="unreal.EarthOutputMergeConfigFragment"></a>