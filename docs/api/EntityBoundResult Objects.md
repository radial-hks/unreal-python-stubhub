## EntityBoundResult Objects

```python
class EntityBoundResult(ResultBase)
```

Entity Bound Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entities_bound`` (Box):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.EntityBoundResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    message: str = "",
    scene_change_info: WdpSceneChangeInfo = [[], [], []],
    success: bool = False,
    entities_bound: Box = [[0.000000, 0.000000, 0.000000],
                           [0.000000, 0.000000, 0.000000], False]
) -> None
```

<a id="unreal.EntityBoundResult.entities_bound"></a>

#### entities\_bound

```python
@property
def entities_bound() -> Box
```

(Box):  [Read-Write]

<a id="unreal.EntityBoundResult.entities_bound"></a>

#### entities\_bound

```python
@entities_bound.setter
def entities_bound(value: Box) -> None
```

<a id="unreal.EntityTypesResult"></a>