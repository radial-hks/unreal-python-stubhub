## RigUnit_SetMetadataTag Objects

```python
class RigUnit_SetMetadataTag(RigUnitMutable)
```

Sets a single tag on an item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to set the metadata for
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``tag`` (Name):  [Read-Write] The name of the tag to set

<a id="unreal.RigUnit_SetMetadataTag.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        item: RigElementKey = [RigElementType.NONE, "None"],
        tag: Name = "None",
        name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE) -> None
```

<a id="unreal.RigUnit_SetMetadataTag.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to set the metadata for

<a id="unreal.RigUnit_SetMetadataTag.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_SetMetadataTag.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write] The name of the tag to set

<a id="unreal.RigUnit_SetMetadataTag.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.RigUnit_SetMetadataTag.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_SetMetadataTag.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_SetMetadataTagArray"></a>