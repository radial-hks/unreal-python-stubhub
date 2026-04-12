## EarthOutputFragments Objects

```python
class EarthOutputFragments(StructBase)
```

输出片段数组

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthOutputTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instanced_fragments`` (Array[InstancedStruct]):  [Read-Write] 实例化结构体类型的输出片段数据，给当前结构体作为UObject的成员时序列化所用

<a id="unreal.EarthOutputFragments.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instanced_fragments: Array[InstancedStruct] = []) -> None
```

<a id="unreal.EarthOutputFragments.instanced_fragments"></a>

#### instanced\_fragments

```python
@property
def instanced_fragments() -> Array[InstancedStruct]
```

(Array[InstancedStruct]):  [Read-Write] 实例化结构体类型的输出片段数据，给当前结构体作为UObject的成员时序列化所用

<a id="unreal.EarthOutputFragments.instanced_fragments"></a>

#### instanced\_fragments

```python
@instanced_fragments.setter
def instanced_fragments(value: Array[InstancedStruct]) -> None
```

<a id="unreal.EarthOutputCollection"></a>