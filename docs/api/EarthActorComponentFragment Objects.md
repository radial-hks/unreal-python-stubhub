## EarthActorComponentFragment Objects

```python
class EarthActorComponentFragment(EarthOutputFragment)
```

ActorComponent数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthActorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component`` (ActorComponent):  [Read-Write]
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthActorComponentFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             component: ActorComponent = None) -> None
```

<a id="unreal.EarthActorComponentFragment.component"></a>

#### component

```python
@property
def component() -> ActorComponent
```

(ActorComponent):  [Read-Write]

<a id="unreal.EarthActorComponentFragment.component"></a>

#### component

```python
@component.setter
def component(value: ActorComponent) -> None
```

<a id="unreal.EarthActorComponentArrayFragment"></a>