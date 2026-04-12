## WdpGlobalGetVersionParams Objects

```python
class WdpGlobalGetVersionParams(ResultBase)
```

Wdp Global Get Version Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``version`` (str):  [Read-Write]

<a id="unreal.WdpGlobalGetVersionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             version: str = "") -> None
```

<a id="unreal.WdpGlobalGetVersionParams.version"></a>

#### version

```python
@property
def version() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpGlobalGetVersionParams.version"></a>

#### version

```python
@version.setter
def version(value: str) -> None
```

<a id="unreal.WdpGlobalSetCoordZTypeParams"></a>