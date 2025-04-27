## RigUnit_FindItemsWithMetadataTagArray Objects

```python
class RigUnit_FindItemsWithMetadataTagArray(RigUnit)
```

Returns all items with a specific tag

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``items`` (Array[RigElementKey]):  [Read-Write] The items containing the metadata
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``tags`` (Array[Name]):  [Read-Write] The tags to find

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.__init__"></a>

#### __init__

```python
def __init__(tags: Array[Name] = [],
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] The tags to find

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_FindItemsWithMetadataTagArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The items containing the metadata

<a id="unreal.RigUnit_FilterItemsByMetadataTags"></a>