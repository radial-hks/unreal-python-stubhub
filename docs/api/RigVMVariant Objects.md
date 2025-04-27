## RigVMVariant Objects

```python
class RigVMVariant(StructBase)
```

Rig VMVariant

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMVariant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (Guid):  [Read-Only] Guid which is shared by all variants of the same element
- ``tags`` (Array[RigVMTag]):  [Read-Only] Tags applied to this variant

<a id="unreal.RigVMVariant.__init__"></a>

#### __init__

```python
def __init__(guid: Guid = [], tags: Array[RigVMTag] = []) -> None
```

<a id="unreal.RigVMVariant.guid"></a>

#### guid

```python
@property
def guid() -> Guid
```

(Guid):  [Read-Only] Guid which is shared by all variants of the same element

<a id="unreal.RigVMVariant.tags"></a>

#### tags

```python
@property
def tags() -> Array[RigVMTag]
```

(Array[RigVMTag]):  [Read-Only] Tags applied to this variant

<a id="unreal.RigVMTag"></a>