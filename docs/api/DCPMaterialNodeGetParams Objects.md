## DCPMaterialNodeGetParams Objects

```python
class DCPMaterialNodeGetParams(ResultBase)
```

DCPMaterial Node Get Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``node_materials`` (Array[DCPMaterialNodeGetParam]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             node_materials: Array[DCPMaterialNodeGetParam] = []) -> None
```

<a id="unreal.DCPMaterialNodeGetParams.node_materials"></a>

#### node\_materials

```python
@property
def node_materials() -> Array[DCPMaterialNodeGetParam]
```

(Array[DCPMaterialNodeGetParam]):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParams.node_materials"></a>

#### node\_materials

```python
@node_materials.setter
def node_materials(value: Array[DCPMaterialNodeGetParam]) -> None
```

<a id="unreal.DCPMaterialNodeResetParam"></a>