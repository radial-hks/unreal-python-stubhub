## WdpLoadAssetByIdResult Objects

```python
class WdpLoadAssetByIdResult(EidResult)
```

Wdp Load Asset by Id Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: WdpAssetAPI
- **File**: WdpAssetAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.WdpLoadAssetByIdResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             type: str = "") -> None
```

<a id="unreal.WdpLoadAssetByIdResult.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpLoadAssetByIdResult.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.WdpReplaceAssetParams"></a>