## DCPMaterialEditorNameResult Objects

```python
class DCPMaterialEditorNameResult(ResultBase)
```

DCPMaterial Editor Name Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_lable`` (str):  [Read-Write]
- ``material_name`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialEditorNameResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             material_name: str = "",
             material_lable: str = "") -> None
```

<a id="unreal.DCPMaterialEditorNameResult.material_name"></a>

#### material\_name

```python
@property
def material_name() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorNameResult.material_name"></a>

#### material\_name

```python
@material_name.setter
def material_name(value: str) -> None
```

<a id="unreal.DCPMaterialEditorNameResult.material_lable"></a>

#### material\_lable

```python
@property
def material_lable() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorNameResult.material_lable"></a>

#### material\_lable

```python
@material_lable.setter
def material_lable(value: str) -> None
```

<a id="unreal.DCPMaterialEntityResult"></a>