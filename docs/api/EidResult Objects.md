## EidResult Objects

```python
class EidResult(ResultBase)
```

Eid Result

**C++ Source:**

- **Plugin**: WdpAPIFrame
- **Module**: WdpAPIFramework
- **File**: ApiResultBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.EidResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False) -> None
```

<a id="unreal.EidArrayResult"></a>