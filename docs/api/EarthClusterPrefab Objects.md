## EarthClusterPrefab Objects

```python
class EarthClusterPrefab(EarthPrefabBase)
```

集群预制体数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthClusterPrefab.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fragments`` (Array[InstancedStruct]):  [Read-Write] 片段数据，结构相同的片段有且仅有一份，不建议在非游戏线程中使用

<a id="unreal.EarthClusterPrefab.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fragments: Array[InstancedStruct] = []) -> None
```

<a id="unreal.EarthCollisionFragment"></a>