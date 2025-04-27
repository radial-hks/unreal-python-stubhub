## DynamicMeshChangeInfo Objects

```python
class DynamicMeshChangeInfo(StructBase)
```

FDynamicMeshChangeInfo stores information about a change to a UDynamicMesh.
This struct is emitted by the UDynamicMesh OnPreMeshChanged() and OnMeshChanged() delegates.

**C++ Source:**

- **Module**: GeometryFramework
- **File**: UDynamicMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flags`` (DynamicMeshAttributeChangeFlags):  [Read-Write]
- ``is_revert_change`` (bool):  [Read-Write] for changes that are an FChange, indicates whether this is an 'Apply' or 'Revert' of the FChange
- ``type`` (DynamicMeshChangeType):  [Read-Write]

<a id="unreal.DynamicMeshChangeInfo.__init__"></a>

#### __init__

```python
def __init__(
        type: DynamicMeshChangeType = DynamicMeshChangeType.GENERAL_EDIT,
        flags: DynamicMeshAttributeChangeFlags = DynamicMeshAttributeChangeFlags
    .UNKNOWN,
        is_revert_change: bool = False) -> None
```

<a id="unreal.DynamicMeshChangeInfo.type"></a>

#### type

```python
@property
def type() -> DynamicMeshChangeType
```

(DynamicMeshChangeType):  [Read-Only]

<a id="unreal.DynamicMeshChangeInfo.flags"></a>

#### flags

```python
@property
def flags() -> DynamicMeshAttributeChangeFlags
```

(DynamicMeshAttributeChangeFlags):  [Read-Only]

<a id="unreal.DynamicMeshChangeInfo.is_revert_change"></a>

#### is_revert_change

```python
@property
def is_revert_change() -> bool
```

(bool):  [Read-Only] for changes that are an FChange, indicates whether this is an 'Apply' or 'Revert' of the FChange

<a id="unreal.AvaMark"></a>