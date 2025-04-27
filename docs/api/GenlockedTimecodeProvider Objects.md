## GenlockedTimecodeProvider Objects

```python
class GenlockedTimecodeProvider(TimecodeProvider)
```

This timecode provider base class will try to use the engine genlock sync to adjust its count.

**C++ Source:**

- **Module**: TimeManagement
- **File**: GenlockedTimecodeProvider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_delay`` (float):  [Read-Write] Number of frames to subtract from the qualified frame time when GetDelayedQualifiedFrameTime or GetDelayedTimecode is called.
  see: GetDelayedQualifiedFrameTime, GetDelayedTimecode
- ``use_genlock_to_count`` (bool):  [Read-Write] Use Genlock Sync to update Timecode count

<a id="unreal.TimeManagementLibrary"></a>