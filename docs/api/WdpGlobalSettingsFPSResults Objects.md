## WdpGlobalSettingsFPSResults Objects

```python
class WdpGlobalSettingsFPSResults(ResultBase)
```

Wdp Global Settings FPSResults

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_fps`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGlobalSettingsFPSResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             max_fps: int = 0) -> None
```

<a id="unreal.WdpGlobalSettingsFPSResults.max_fps"></a>

#### max\_fps

```python
@property
def max_fps() -> int
```

(int32):  [Read-Write]

<a id="unreal.WdpGlobalSettingsFPSResults.max_fps"></a>

#### max\_fps

```python
@max_fps.setter
def max_fps(value: int) -> None
```

<a id="unreal.WdpGlobalSettingsSoundParams"></a>