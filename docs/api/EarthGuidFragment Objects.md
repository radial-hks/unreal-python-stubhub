## EarthGuidFragment Objects

```python
class EarthGuidFragment(EarthOutputFragment)
```

全局唯一标识符数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthActorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (Guid):  [Read-Write] 全局唯一标识符
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthGuidFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             guid: Guid = []) -> None
```

<a id="unreal.EarthGuidFragment.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Write] 全局唯一标识符

<a id="unreal.EarthGuidFragment.guid"></a>

#### guid

```python
@guid.setter
def guid(value: Guid) -> None
```

<a id="unreal.EarthActorComponentFragment"></a>