## PostBufferBlurUpdater Objects

```python
class PostBufferBlurUpdater(SlatePostBufferProcessorUpdater)
```

Processor updater that sets the blur strength for a blur processor intra-frame on the renderthread

**C++ Source:**

- **Module**: UMG
- **File**: PostBufferBlurUpdater.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gaussian_blur_strength`` (float):  [Read-Write]
- ``skip_buffer_update`` (bool):  [Read-Write] True implies we will skip the buffer update & only update the processor.
  Useful to reset params for processor runs next frame

<a id="unreal.PostBufferUpdate"></a>