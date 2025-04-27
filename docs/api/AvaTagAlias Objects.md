## AvaTagAlias Objects

```python
class AvaTagAlias(StructBase)
```

An alias represents multiple other Tag Ids.

Unlike Tag Containers which would need to be updated in every place it's used when the set of tags it needs to manipulate is added to or removed from,
Aliases are a layer of abstraction that allows the set of tags to be added to or removed from without affecting the places where the alias is used.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTag
- **File**: AvaTagAlias.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alias_name`` (Name):  [Read-Write]
- ``tag_ids`` (Array[AvaTagId]):  [Read-Write]

<a id="unreal.AvaTagAlias.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AvaTagHandle"></a>