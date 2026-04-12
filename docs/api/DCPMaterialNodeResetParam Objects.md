## DCPMaterialNodeResetParam Objects

```python
class DCPMaterialNodeResetParam(ParamsBase)
```

DCPMaterial Node Reset Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``model_eid`` (str):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPMaterialNodeResetParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(model_eid: str = "", node_ids: Array[int] = []) -> None
```

<a id="unreal.DCPMaterialNodeResetParam.model_eid"></a>

#### model\_eid

```python
@property
def model_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialNodeResetParam.model_eid"></a>

#### model\_eid

```python
@model_eid.setter
def model_eid(value: str) -> None
```

<a id="unreal.DCPMaterialNodeResetParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPMaterialNodeResetParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPMaterialTransparencyDiagramNodeParam"></a>