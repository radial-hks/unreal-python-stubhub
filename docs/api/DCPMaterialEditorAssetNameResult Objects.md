## DCPMaterialEditorAssetNameResult Objects

```python
class DCPMaterialEditorAssetNameResult(ResultBase)
```

DCPMaterial Editor Asset Name Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``mid`` (str):  [Read-Write]
- ``picture`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialEditorAssetNameResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             mid: str = "",
             picture: str = "") -> None
```

<a id="unreal.DCPMaterialEditorAssetNameResult.mid"></a>

#### mid

```python
@property
def mid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorAssetNameResult.mid"></a>

#### mid

```python
@mid.setter
def mid(value: str) -> None
```

<a id="unreal.DCPMaterialEditorAssetNameResult.picture"></a>

#### picture

```python
@property
def picture() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorAssetNameResult.picture"></a>

#### picture

```python
@picture.setter
def picture(value: str) -> None
```

<a id="unreal.DCPMaterialEditorAssetNamesResult"></a>