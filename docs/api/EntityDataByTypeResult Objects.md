## EntityDataByTypeResult Objects

```python
class EntityDataByTypeResult(ResultBase)
```

Entity Data by Type Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entities_data`` (Map[str, EntityDataArr]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.EntityDataByTypeResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             entities_data: Map[str, EntityDataArr] = {}) -> None
```

<a id="unreal.EntityDataByTypeResult.entities_data"></a>

#### entities\_data

```python
@property
def entities_data() -> Map[str, EntityDataArr]
```

(Map[str, EntityDataArr]):  [Read-Write]

<a id="unreal.EntityDataByTypeResult.entities_data"></a>

#### entities\_data

```python
@entities_data.setter
def entities_data(value: Map[str, EntityDataArr]) -> None
```

<a id="unreal.EntityDataResult"></a>