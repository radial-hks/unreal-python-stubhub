## EntityUpdatedEventArgs Objects

```python
class EntityUpdatedEventArgs(EventArgsBase)
```

Entity Updated Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type_to_eids`` (Map[Name, EidArrayParams]):  [Read-Write]

<a id="unreal.EntityUpdatedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type_to_eids: Map[Name, EidArrayParams] = {}) -> None
```

<a id="unreal.EntityUpdatedEventArgs.type_to_eids"></a>

#### type\_to\_eids

```python
@property
def type_to_eids() -> Map[Name, EidArrayParams]
```

(Map[Name, EidArrayParams]):  [Read-Write]

<a id="unreal.EntityUpdatedEventArgs.type_to_eids"></a>

#### type\_to\_eids

```python
@type_to_eids.setter
def type_to_eids(value: Map[Name, EidArrayParams]) -> None
```

<a id="unreal.WdpRuntimeVersionEventArgs"></a>