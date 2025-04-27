## AvaTagHandleContainer Objects

```python
class AvaTagHandleContainer(StructBase)
```

Handle to a multiple tags in a particular Source.
This should be used by the UStructs/UObjects to properly reference a multiple FAvaTags.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheTag
- **File**: AvaTagHandleContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source`` (AvaTagCollection):  [Read-Write]
- ``tag_ids`` (Array[AvaTagId]):  [Read-Write]

<a id="unreal.AvaTagHandleContainer.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AvaTagSoftHandle"></a>