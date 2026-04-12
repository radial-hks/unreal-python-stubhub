## EarthTerraformingPrefab Objects

```python
class EarthTerraformingPrefab(EarthPrefabBase)
```

地形改造预制体
轮廓线需要顺时针点序

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthTerraformingPrefab.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fragments`` (Array[InstancedStruct]):  [Read-Write] 片段数据，结构相同的片段有且仅有一份，不建议在非游戏线程中使用

<a id="unreal.EarthTerraformingPrefab.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fragments: Array[InstancedStruct] = []) -> None
```

<a id="unreal.EarthTerraformingMeshVertex"></a>