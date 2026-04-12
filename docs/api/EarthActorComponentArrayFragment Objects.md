## EarthActorComponentArrayFragment Objects

```python
class EarthActorComponentArrayFragment(EarthOutputFragment)
```

ActorComponent数组数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthActorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_fragments`` (Array[EarthActorComponentFragment]):  [Read-Write]
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthActorComponentArrayFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        owned_object: Object = None,
        component_fragments: Array[EarthActorComponentFragment] = []) -> None
```

<a id="unreal.EarthActorComponentArrayFragment.component_fragments"></a>

#### component\_fragments

```python
@property
def component_fragments() -> Array[EarthActorComponentFragment]
```

(Array[EarthActorComponentFragment]):  [Read-Write]

<a id="unreal.EarthActorComponentArrayFragment.component_fragments"></a>

#### component\_fragments

```python
@component_fragments.setter
def component_fragments(value: Array[EarthActorComponentFragment]) -> None
```

<a id="unreal.EarthActorFragment"></a>