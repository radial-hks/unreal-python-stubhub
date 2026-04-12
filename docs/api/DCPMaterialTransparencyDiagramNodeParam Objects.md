## DCPMaterialTransparencyDiagramNodeParam Objects

```python
class DCPMaterialTransparencyDiagramNodeParam(ParamsBase)
```

DCPMaterial Transparency Diagram Node Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``use_wire_frame`` (bool):  [Read-Write]

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = [], use_wire_frame: bool = False) -> None
```

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam.use_wire_frame"></a>

#### use\_wire\_frame

```python
@property
def use_wire_frame() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam.use_wire_frame"></a>

#### use\_wire\_frame

```python
@use_wire_frame.setter
def use_wire_frame(value: bool) -> None
```

<a id="unreal.DCPMaterialTransparencyDiagramPercentParam"></a>