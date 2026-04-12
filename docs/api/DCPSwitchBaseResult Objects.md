## DCPSwitchBaseResult Objects

```python
class DCPSwitchBaseResult(ResultBase)
```

DCPSwitch Base Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPSwitchAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_open`` (bool):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPSwitchBaseResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             is_open: bool = False) -> None
```

<a id="unreal.DCPSwitchBaseResult.is_open"></a>

#### is\_open

```python
@property
def is_open() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPSwitchBaseResult.is_open"></a>

#### is\_open

```python
@is_open.setter
def is_open(value: bool) -> None
```

<a id="unreal.DCPClickSinglePointResult"></a>