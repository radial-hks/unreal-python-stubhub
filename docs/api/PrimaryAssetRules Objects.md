## PrimaryAssetRules Objects

```python
class PrimaryAssetRules(StructBase)
```

Structure defining rules for what to do with assets, this is defined per type and can be overridden per asset

**C++ Source:**

- **Module**: Engine
- **File**: AssetManagerTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_recursively`` (bool):  [Read-Write] If true, this rule will apply to all referenced Secondary Assets recursively, as long as they are not managed by a higher-priority Primary Asset.
- ``chunk_id`` (int32):  [Read-Write] Assets will be put into this Chunk ID specifically, if set to something other than -1. The default Chunk is Chunk 0.
- ``cook_rule`` (PrimaryAssetCookRule):  [Read-Write] Rule describing when this asset should be cooked.
- ``priority`` (int32):  [Read-Write] Primary Assets with a higher priority will take precedence over lower priorities when assigning management for referenced assets. If priorities match, both will manage the same Secondary Asset.

<a id="unreal.PrimaryAssetRules.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BoneMirrorInfo"></a>