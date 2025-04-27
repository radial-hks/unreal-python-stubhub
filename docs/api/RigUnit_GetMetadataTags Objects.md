## RigUnit_GetMetadataTags Objects

```python
class RigUnit_GetMetadataTags(RigUnit)
```

Returns the metadata tags on an item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Metadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The item to check the metadata for
- ``tags`` (Array[Name]):  [Read-Write] The name of the tag to check

<a id="unreal.RigUnit_GetMetadataTags.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             tags: Array[Name] = []) -> None
```

<a id="unreal.RigUnit_GetMetadataTags.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to check the metadata for

<a id="unreal.RigUnit_GetMetadataTags.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetMetadataTags.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Only] The name of the tag to check

<a id="unreal.RigUnit_SetMetadataTag"></a>