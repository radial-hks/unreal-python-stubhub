## NiagaraTypeDefinition Objects

```python
class NiagaraTypeDefinition(StructBase)
```

Niagara Type Definition

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_struct_or_enum`` (Object):  [Read-Write] Underlying type for this variable, use FUnderlyingType to determine type without casting
  This can be a UClass, UStruct or UEnum.  Pointing to something like the struct for an FVector, etc.
  In occasional situations this may be a UClass when we're dealing with DataInterface etc.
- ``flags`` (uint8):  [Read-Write]
- ``underlying_type`` (uint16):  [Read-Write] See enumeration FUnderlyingType for possible values

<a id="unreal.NiagaraTypeDefinition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraPlatformSet"></a>