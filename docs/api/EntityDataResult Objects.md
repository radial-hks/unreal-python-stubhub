## EntityDataResult Objects

```python
class EntityDataResult(ResultBase)
```

Entity Data Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entities_data`` (Array[WdpJsonObjectWrapper]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.EntityDataResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             entities_data: Array[WdpJsonObjectWrapper] = []) -> None
```

<a id="unreal.EntityDataResult.entities_data"></a>

#### entities\_data

```python
@property
def entities_data() -> Array[WdpJsonObjectWrapper]
```

(Array[WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.EntityDataResult.entities_data"></a>

#### entities\_data

```python
@entities_data.setter
def entities_data(value: Array[WdpJsonObjectWrapper]) -> None
```

<a id="unreal.EntityBoundResult"></a>