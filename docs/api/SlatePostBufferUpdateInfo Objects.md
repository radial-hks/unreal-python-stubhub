## SlatePostBufferUpdateInfo Objects

```python
class SlatePostBufferUpdateInfo(StructBase)
```

Struct containing info needed to update a particular buffer

**C++ Source:**

- **Module**: UMG
- **File**: PostBufferUpdate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_to_update`` (SlatePostRT):  [Read-Write] Buffers that we should update, all of these buffers will be affected by 'bPerformDefaultPostBufferUpdate' if disabled
- ``post_param_updater`` (SlatePostBufferProcessorUpdater):  [Read-Write] Optional processor updater for buffer, used to update a processor within a frame

<a id="unreal.SlatePostBufferUpdateInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AssetImportInfo"></a>