## DCPAPIVersionParam Objects

```python
class DCPAPIVersionParam(ResultBase)
```

DCPAPIVersion Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPInitAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``already`` (bool):  [Read-Write]
- ``api_version`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPAPIVersionParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             already: bool = False,
             api_version: str = "") -> None
```

<a id="unreal.DCPAPIVersionParam.already"></a>

#### already

```python
@property
def already() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPAPIVersionParam.already"></a>

#### already

```python
@already.setter
def already(value: bool) -> None
```

<a id="unreal.DCPAPIVersionParam.api_version"></a>

#### api\_version

```python
@property
def api_version() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPAPIVersionParam.api_version"></a>

#### api\_version

```python
@api_version.setter
def api_version(value: str) -> None
```

<a id="unreal.DCPMaterialEditorNameResult"></a>