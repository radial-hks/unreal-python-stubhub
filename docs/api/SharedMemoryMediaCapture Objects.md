## SharedMemoryMediaCapture Objects

```python
class SharedMemoryMediaCapture(MediaCapture)
```

Output Media for SharedMemory.

The pixels are captured into shared cross gpu textures, that a player can read.
Inter-process communication happens via shared system memory. The metadata exchanged is documented
in the FSharedMemoryMediaFrameMetadata structure. The shared memory can be located via a UniqueName
that must match in the Media Output and corresponding Media Source settings.

It is mostly intended for use in nDisplay render nodes, which are designed to be frame-locked.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: SharedMemoryMedia
- **File**: SharedMemoryMediaCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_state_changed`` (MediaCaptureStateChangedSignature):  [Read-Write] Called when the state of the capture changed.

<a id="unreal.SharedMemoryMediaOutput"></a>