## RigUnit_HasMetadata Objects

```python
class RigUnit_HasMetadata(RigUnit)
```

Returns true if a given item in the hierarchy has a specific set of metadata

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``found`` (bool):  [Read-Write] True if the item has the metadata
- ``item`` (RigElementKey):  [Read-Write] The item to check the metadata for
- ``name`` (Name):  [Read-Write] The name of the metadata to check
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``type`` (RigMetadataType):  [Read-Write] The type of metadata to check for

<a id="unreal.RigUnit_HasMetadata.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             name: Name = "None",
             type: RigMetadataType = RigMetadataType.BOOL,
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             found: bool = False) -> None
```

<a id="unreal.RigUnit_HasMetadata.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to check the metadata for

<a id="unreal.RigUnit_HasMetadata.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HasMetadata.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The name of the metadata to check

<a id="unreal.RigUnit_HasMetadata.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_HasMetadata.type"></a>

#### type

```python
@property
def type() -> RigMetadataType
```

(RigMetadataType):  [Read-Write] The type of metadata to check for

<a id="unreal.RigUnit_HasMetadata.type"></a>

#### type

```python
@type.setter
def type(value: RigMetadataType) -> None
```

<a id="unreal.RigUnit_HasMetadata.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_HasMetadata.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_HasMetadata.found"></a>

#### found

```python
@property
def found() -> bool
```

(bool):  [Read-Only] True if the item has the metadata

<a id="unreal.RigUnit_FindItemsWithMetadata"></a>