## EarthInstancedStaticMeshPrefab Objects

```python
class EarthInstancedStaticMeshPrefab(EarthStaticMeshPrefab)
```

实例化静态网格预制体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthStaticMeshPrefab.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fragments`` (Array[InstancedStruct]):  [Read-Write] 片段数据，结构相同的片段有且仅有一份，不建议在非游戏线程中使用

<a id="unreal.EarthInstancedStaticMeshPrefab.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fragments: Array[InstancedStruct] = []) -> None
```

<a id="unreal.EarthSubdivideSegmentHelpers"></a>