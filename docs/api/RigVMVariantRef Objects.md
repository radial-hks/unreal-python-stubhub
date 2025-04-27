## RigVMVariantRef Objects

```python
class RigVMVariantRef(StructBase)
```

This struct should not be serialized.
It is generated on demand.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMVariant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object_path`` (SoftObjectPath):  [Read-Write]
- ``variant`` (RigVMVariant):  [Read-Write]

<a id="unreal.RigVMVariantRef.__init__"></a>

#### __init__

```python
def __init__(object_path: SoftObjectPath = [""],
             variant: RigVMVariant = [[], []]) -> None
```

<a id="unreal.RigVMVariantRef.object_path"></a>

#### object_path

```python
@property
def object_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only]

<a id="unreal.RigVMVariantRef.variant"></a>

#### variant

```python
@property
def variant() -> RigVMVariant
```

(RigVMVariant):  [Read-Only]

<a id="unreal.RigVMParameter"></a>