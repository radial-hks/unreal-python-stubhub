## WdpGetCurrentActionResult Objects

```python
class WdpGetCurrentActionResult(ResultBase)
```

Wdp Get Current Action Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionManagerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_name`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGetCurrentActionResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             action_name: str = "") -> None
```

<a id="unreal.WdpGetCurrentActionResult.action_name"></a>

#### action\_name

```python
@property
def action_name() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpGetCurrentActionResult.action_name"></a>

#### action\_name

```python
@action_name.setter
def action_name(value: str) -> None
```

<a id="unreal.WdpSetDefaultActionSettingParams"></a>