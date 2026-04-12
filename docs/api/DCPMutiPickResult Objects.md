## DCPMutiPickResult Objects

```python
class DCPMutiPickResult(ResultBase)
```

DCPMuti Pick Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPCommonAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``pick_infos`` (Array[DCPMutiPickInfo]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMutiPickResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             pick_infos: Array[DCPMutiPickInfo] = []) -> None
```

<a id="unreal.DCPMutiPickResult.pick_infos"></a>

#### pick\_infos

```python
@property
def pick_infos() -> Array[DCPMutiPickInfo]
```

(Array[DCPMutiPickInfo]):  [Read-Write]

<a id="unreal.DCPMutiPickResult.pick_infos"></a>

#### pick\_infos

```python
@pick_infos.setter
def pick_infos(value: Array[DCPMutiPickInfo]) -> None
```

<a id="unreal.DCPEffectSelectParam"></a>