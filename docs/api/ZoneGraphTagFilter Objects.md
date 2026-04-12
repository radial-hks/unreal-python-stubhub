## ZoneGraphTagFilter Objects

```python
class ZoneGraphTagFilter(StructBase)
```

Filter passes if any of the 'AnyTags', and all of the 'AllTags', and none of the 'NotTags' are present.
Setting include or exclude tags to None, will skip that particular check.

**C++ Source:**

- **Plugin**: ZoneGraph
- **Module**: ZoneGraph
- **File**: ZoneGraphTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_tags`` (ZoneGraphTagMask):  [Read-Write]
- ``any_tags`` (ZoneGraphTagMask):  [Read-Write]
- ``not_tags`` (ZoneGraphTagMask):  [Read-Write]

<a id="unreal.ZoneGraphTagFilter.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MovieSceneBaseCacheParams"></a>