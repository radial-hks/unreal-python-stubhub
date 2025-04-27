## RigUnit_FindItemsWithMetadata Objects

```python
class RigUnit_FindItemsWithMetadata(RigUnit)
```

Returns all items containing a specific set of metadata

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write] The items containing the metadata
- ``name`` (Name):  [Read-Write] The name of the metadata to find
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``type`` (RigMetadataType):  [Read-Write] The type of metadata to find

<a id="unreal.RigUnit_FindItemsWithMetadata.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             type: RigMetadataType = RigMetadataType.BOOL,
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadata.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The name of the metadata to find

<a id="unreal.RigUnit_FindItemsWithMetadata.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadata.type"></a>

#### type

```python
@property
def type() -> RigMetadataType
```

(RigMetadataType):  [Read-Write] The type of metadata to find

<a id="unreal.RigUnit_FindItemsWithMetadata.type"></a>

#### type

```python
@type.setter
def type(value: RigMetadataType) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadata.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_FindItemsWithMetadata.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadata.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The items containing the metadata

<a id="unreal.RigUnit_GetMetadataTags"></a>