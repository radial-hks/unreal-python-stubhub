## RigUnit_SetMetadataTagArray Objects

```python
class RigUnit_SetMetadataTagArray(RigUnitMutable)
```

Sets multiple tags on an item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to set the metadata for
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``tags`` (Array[Name]):  [Read-Write] The tags to set for the item

<a id="unreal.RigUnit_SetMetadataTagArray.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        item: RigElementKey = [RigElementType.NONE, "None"],
        tags: Array[Name] = [],
        name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE) -> None
```

<a id="unreal.RigUnit_SetMetadataTagArray.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to set the metadata for

<a id="unreal.RigUnit_SetMetadataTagArray.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetMetadataTagArray.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] The tags to set for the item

<a id="unreal.RigUnit_SetMetadataTagArray.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.RigUnit_SetMetadataTagArray.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_SetMetadataTagArray.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_RemoveMetadataTag"></a>