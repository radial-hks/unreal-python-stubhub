## GeometryScriptMeshDifferenceInfo Objects

```python
class GeometryScriptMeshDifferenceInfo(StructBase)
```

Geometry Script Mesh Difference Info

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshComparisonFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``detail`` (str):  [Read-Write] String that may contain additional detail on the difference
- ``element_id_type`` (GeometryScriptIndexType):  [Read-Write] Indicates the type of element that TargetMeshElementID and OtherMeshElementID reference
- ``other_mesh_element_id`` (int32):  [Read-Write]
- ``reason`` (GeometryScriptMeshDifferenceReason):  [Read-Write]
- ``target_mesh_element_id`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshDifferenceInfo.__init__"></a>

#### __init__

```python
def __init__(
    reason:
    GeometryScriptMeshDifferenceReason = GeometryScriptMeshDifferenceReason.
    UNKNOWN,
    detail: str = "",
    target_mesh_element_id: int = 0,
    other_mesh_element_id: int = 0,
    element_id_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY
) -> None
```

<a id="unreal.GeometryScriptMeshDifferenceInfo.reason"></a>

#### reason

```python
@property
def reason() -> GeometryScriptMeshDifferenceReason
```

(GeometryScriptMeshDifferenceReason):  [Read-Write]

<a id="unreal.GeometryScriptMeshDifferenceInfo.reason"></a>

#### reason

```python
@reason.setter
def reason(value: GeometryScriptMeshDifferenceReason) -> None
```

<a id="unreal.GeometryScriptMeshDifferenceInfo.detail"></a>

#### detail

```python
@property
def detail() -> str
```

(str):  [Read-Write] String that may contain additional detail on the difference

<a id="unreal.GeometryScriptMeshDifferenceInfo.detail"></a>

#### detail

```python
@detail.setter
def detail(value: str) -> None
```

<a id="unreal.GeometryScriptMeshDifferenceInfo.target_mesh_element_id"></a>

#### target_mesh_element_id

```python
@property
def target_mesh_element_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshDifferenceInfo.target_mesh_element_id"></a>

#### target_mesh_element_id

```python
@target_mesh_element_id.setter
def target_mesh_element_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshDifferenceInfo.other_mesh_element_id"></a>

#### other_mesh_element_id

```python
@property
def other_mesh_element_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptMeshDifferenceInfo.other_mesh_element_id"></a>

#### other_mesh_element_id

```python
@other_mesh_element_id.setter
def other_mesh_element_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshDifferenceInfo.element_id_type"></a>

#### element_id_type

```python
@property
def element_id_type() -> GeometryScriptIndexType
```

(GeometryScriptIndexType):  [Read-Write] Indicates the type of element that TargetMeshElementID and OtherMeshElementID reference

<a id="unreal.GeometryScriptMeshDifferenceInfo.element_id_type"></a>

#### element_id_type

```python
@element_id_type.setter
def element_id_type(value: GeometryScriptIndexType) -> None
```

<a id="unreal.GeometryScriptBendWarpOptions"></a>