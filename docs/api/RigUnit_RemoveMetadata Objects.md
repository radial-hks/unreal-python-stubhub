## RigUnit_RemoveMetadata Objects

```python
class RigUnit_RemoveMetadata(RigUnitMutable)
```

Removes an existing metadata filed from an item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``item`` (RigElementKey):  [Read-Write] The item to remove the metadata from
- ``name`` (Name):  [Read-Write] The name of the metadata to remove
- ``name_space`` (RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up
- ``removed`` (bool):  [Read-Write] True if the metadata has been removed

<a id="unreal.RigUnit_RemoveMetadata.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             name: Name = "None",
             name_space: RigMetaDataNameSpace = RigMetaDataNameSpace.NONE,
             removed: bool = False) -> None
```

<a id="unreal.RigUnit_RemoveMetadata.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to remove the metadata from

<a id="unreal.RigUnit_RemoveMetadata.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_RemoveMetadata.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The name of the metadata to remove

<a id="unreal.RigUnit_RemoveMetadata.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.RigUnit_RemoveMetadata.name_space"></a>

#### name_space

```python
@property
def name_space() -> RigMetaDataNameSpace
```

(RigMetaDataNameSpace):  [Read-Write] Defines in which namespace the metadata will be looked up

<a id="unreal.RigUnit_RemoveMetadata.name_space"></a>

#### name_space

```python
@name_space.setter
def name_space(value: RigMetaDataNameSpace) -> None
```

<a id="unreal.RigUnit_RemoveMetadata.removed"></a>

#### removed

```python
@property
def removed() -> bool
```

(bool):  [Read-Only] True if the metadata has been removed

<a id="unreal.RigUnit_RemoveAllMetadata"></a>