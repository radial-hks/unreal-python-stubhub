## EarthDataBase Objects

```python
class EarthDataBase(StructBase)
```

所有运行时可修改数据的基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fragments`` (Array[InstancedStruct]):  [Read-Write] 片段数据，结构相同的片段有且仅有一份，不建议在非游戏线程中使用

<a id="unreal.EarthDataBase.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fragments: Array[InstancedStruct] = []) -> None
```

<a id="unreal.EarthDataBase.fragments"></a>

#### fragments

```python
@property
def fragments() -> Array[InstancedStruct]
```

(Array[InstancedStruct]):  [Read-Write] 片段数据，结构相同的片段有且仅有一份，不建议在非游戏线程中使用

<a id="unreal.EarthDataBase.fragments"></a>

#### fragments

```python
@fragments.setter
def fragments(value: Array[InstancedStruct]) -> None
```

<a id="unreal.EarthPrefabBase"></a>