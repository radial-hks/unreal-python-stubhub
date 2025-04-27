## TakeRecorderCameraCutSource Objects

```python
class TakeRecorderCameraCutSource(TakeRecorderSource)
```

A recording source that detects camera switching and creates a camera cut track

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderCameraCutSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderLevelSequenceSource"></a>