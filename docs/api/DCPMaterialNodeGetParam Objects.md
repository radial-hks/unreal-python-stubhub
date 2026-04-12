## DCPMaterialNodeGetParam Objects

```python
class DCPMaterialNodeGetParam(StructBase)
```

DCPMaterial Node Get Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_sphere_eid`` (str):  [Read-Write]
- ``mid`` (str):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_ids: Array[int] = [],
             mid: str = "",
             material_sphere_eid: str = "") -> None
```

<a id="unreal.DCPMaterialNodeGetParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPMaterialNodeGetParam.mid"></a>

#### mid

```python
@property
def mid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParam.mid"></a>

#### mid

```python
@mid.setter
def mid(value: str) -> None
```

<a id="unreal.DCPMaterialNodeGetParam.material_sphere_eid"></a>

#### material\_sphere\_eid

```python
@property
def material_sphere_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialNodeGetParam.material_sphere_eid"></a>

#### material\_sphere\_eid

```python
@material_sphere_eid.setter
def material_sphere_eid(value: str) -> None
```

<a id="unreal.DCPMaterialNodeGetParams"></a>