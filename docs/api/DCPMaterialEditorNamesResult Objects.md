## DCPMaterialEditorNamesResult Objects

```python
class DCPMaterialEditorNamesResult(ResultBase)
```

DCPMaterial Editor Names Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_infos`` (Array[DCPMaterialEditorNameResult]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialEditorNamesResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             material_infos: Array[DCPMaterialEditorNameResult] = []) -> None
```

<a id="unreal.DCPMaterialEditorNamesResult.material_infos"></a>

#### material\_infos

```python
@property
def material_infos() -> Array[DCPMaterialEditorNameResult]
```

(Array[DCPMaterialEditorNameResult]):  [Read-Write]

<a id="unreal.DCPMaterialEditorNamesResult.material_infos"></a>

#### material\_infos

```python
@material_infos.setter
def material_infos(value: Array[DCPMaterialEditorNameResult]) -> None
```

<a id="unreal.DCPMaterialEditorAssetNameResult"></a>