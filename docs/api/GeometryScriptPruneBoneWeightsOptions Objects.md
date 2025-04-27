## GeometryScriptPruneBoneWeightsOptions Objects

```python
class GeometryScriptPruneBoneWeightsOptions(StructBase)
```

Geometry Script Prune Bone Weights Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ignored_invalid_bones`` (bool):  [Read-Write] Ignore invalid bones. Otherwise, if invalid bones are given, the operation terminates with an error
- ``reassignment_type`` (GeometryScriptPruneBoneWeightsAssignmentType):  [Read-Write] Specifies how the weight of the removed bone from a vertex's bone weights list gets reassigned.

<a id="unreal.GeometryScriptPruneBoneWeightsOptions.__init__"></a>

#### __init__

```python
def __init__(
        reassignment_type:
    GeometryScriptPruneBoneWeightsAssignmentType = GeometryScriptPruneBoneWeightsAssignmentType
    .RENORMALIZE_REMAINING,
        ignored_invalid_bones: bool = False) -> None
```

<a id="unreal.GeometryScriptPruneBoneWeightsOptions.reassignment_type"></a>

#### reassignment_type

```python
@property
def reassignment_type() -> GeometryScriptPruneBoneWeightsAssignmentType
```

(GeometryScriptPruneBoneWeightsAssignmentType):  [Read-Write] Specifies how the weight of the removed bone from a vertex's bone weights list gets reassigned.

<a id="unreal.GeometryScriptPruneBoneWeightsOptions.reassignment_type"></a>

#### reassignment_type

```python
@reassignment_type.setter
def reassignment_type(
        value: GeometryScriptPruneBoneWeightsAssignmentType) -> None
```

<a id="unreal.GeometryScriptPruneBoneWeightsOptions.ignored_invalid_bones"></a>

#### ignored_invalid_bones

```python
@property
def ignored_invalid_bones() -> bool
```

(bool):  [Read-Write] Ignore invalid bones. Otherwise, if invalid bones are given, the operation terminates with an error

<a id="unreal.GeometryScriptPruneBoneWeightsOptions.ignored_invalid_bones"></a>

#### ignored_invalid_bones

```python
@ignored_invalid_bones.setter
def ignored_invalid_bones(value: bool) -> None
```

<a id="unreal.GeometryScriptSmoothBoneWeightsOptions"></a>