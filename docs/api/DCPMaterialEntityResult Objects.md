## DCPMaterialEntityResult Objects

```python
class DCPMaterialEntityResult(ResultBase)
```

DCPMaterial Entity Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_sphere_eid`` (str):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialEntityResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             material_sphere_eid: str = "") -> None
```

<a id="unreal.DCPMaterialEntityResult.material_sphere_eid"></a>

#### material\_sphere\_eid

```python
@property
def material_sphere_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEntityResult.material_sphere_eid"></a>

#### material\_sphere\_eid

```python
@material_sphere_eid.setter
def material_sphere_eid(value: str) -> None
```

<a id="unreal.DCPMaterialEditorNamesResult"></a>