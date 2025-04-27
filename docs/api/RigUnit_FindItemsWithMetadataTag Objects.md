## RigUnit_FindItemsWithMetadataTag Objects

```python
class RigUnit_FindItemsWithMetadataTag(RigUnit)
```

Returns all items with a specific tag

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write] The items containing the metadata
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``tag`` (Name):  [Read-Write] The name of the tag to find

<a id="unreal.RigUnit_FindItemsWithMetadataTag.__init__"></a>

#### __init__

```python
def __init__(tag: Name = "None",
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTag.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write] The name of the tag to find

<a id="unreal.RigUnit_FindItemsWithMetadataTag.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTag.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_FindItemsWithMetadataTag.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTag.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The items containing the metadata

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray"></a>