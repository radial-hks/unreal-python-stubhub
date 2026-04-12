## AllEntitiesResult Objects

```python
class AllEntitiesResult(ResultBase)
```

All Entities Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_type_to_eids`` (Map[Name, EntityIds]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AllEntitiesResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             entity_type_to_eids: Map[Name, EntityIds] = {}) -> None
```

<a id="unreal.AllEntitiesResult.entity_type_to_eids"></a>

#### entity\_type\_to\_eids

```python
@property
def entity_type_to_eids() -> Map[Name, EntityIds]
```

(Map[Name, EntityIds]):  [Read-Write]

<a id="unreal.AllEntitiesResult.entity_type_to_eids"></a>

#### entity\_type\_to\_eids

```python
@entity_type_to_eids.setter
def entity_type_to_eids(value: Map[Name, EntityIds]) -> None
```

<a id="unreal.EntityDataArr"></a>