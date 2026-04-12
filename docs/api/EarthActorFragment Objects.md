## EarthActorFragment Objects

```python
class EarthActorFragment(EarthOutputFragment)
```

Actor数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthActorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor`` (Actor):  [Read-Write] 引用的Actor
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthActorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             actor: Actor = None) -> None
```

<a id="unreal.EarthActorFragment.actor"></a>

#### actor

```python
@property
def actor() -> Actor
```

(Actor):  [Read-Write] 引用的Actor

<a id="unreal.EarthActorFragment.actor"></a>

#### actor

```python
@actor.setter
def actor(value: Actor) -> None
```

<a id="unreal.EarthSubAssetInfo"></a>