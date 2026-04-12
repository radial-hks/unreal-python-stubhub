## GetLogCachesResp Objects

```python
class GetLogCachesResp(ResultBase)
```

Get Log Caches Resp

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpLogAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``log_caches`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetLogCachesResp.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False) -> None
```

<a id="unreal.LogCachesEventArgs"></a>