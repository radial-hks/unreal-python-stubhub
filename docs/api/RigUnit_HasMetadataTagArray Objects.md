## RigUnit_HasMetadataTagArray Objects

```python
class RigUnit_HasMetadataTagArray(RigUnit)
```

Returns true if a given item in the hierarchy has all of the provided tags

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``found`` (bool):  [Read-Write] True if the item has the metadata
- ``item`` (RigElementKey):  [Read-Write] The item to check the metadata for
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``tags`` (Array[Name]):  [Read-Write] The name of the tag to check

<a id="unreal.RigUnit_HasMetadataTagArray.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             tags: Array[Name] = [],
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             found: bool = False) -> None
```

<a id="unreal.RigUnit_HasMetadataTagArray.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to check the metadata for

<a id="unreal.RigUnit_HasMetadataTagArray.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_HasMetadataTagArray.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] The name of the tag to check

<a id="unreal.RigUnit_HasMetadataTagArray.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.RigUnit_HasMetadataTagArray.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_HasMetadataTagArray.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_HasMetadataTagArray.found"></a>

#### found

```python
@property
def found() -> bool
```

(bool):  [Read-Only] True if the item has the metadata

<a id="unreal.RigUnit_FindItemsWithMetadataTag"></a>