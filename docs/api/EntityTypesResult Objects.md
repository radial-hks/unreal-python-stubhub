## EntityTypesResult Objects

```python
class EntityTypesResult(ResultBase)
```

Entity Types Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_types`` (Array[str]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.EntityTypesResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             entity_types: Array[str] = []) -> None
```

<a id="unreal.EntityTypesResult.entity_types"></a>

#### entity\_types

```python
@property
def entity_types() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.EntityTypesResult.entity_types"></a>

#### entity\_types

```python
@entity_types.setter
def entity_types(value: Array[str]) -> None
```

<a id="unreal.SaveSceneParams"></a>