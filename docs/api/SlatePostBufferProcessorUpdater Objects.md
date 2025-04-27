## SlatePostBufferProcessorUpdater Objects

```python
class SlatePostBufferProcessorUpdater(Object)
```

Class that can create a FPostParamUpdaterProxy whose lifetime
will be managed by the renderthread. This proxy will be given a
Post buffer processor to update mid-frame.

**C++ Source:**

- **Module**: UMG
- **File**: PostBufferUpdate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``skip_buffer_update`` (bool):  [Read-Write] True implies we will skip the buffer update & only update the processor.
  Useful to reset params for processor runs next frame

<a id="unreal.PostBufferBlurUpdater"></a>