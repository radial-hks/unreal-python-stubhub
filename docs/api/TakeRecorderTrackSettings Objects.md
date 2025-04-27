## TakeRecorderTrackSettings Objects

```python
class TakeRecorderTrackSettings(StructBase)
```

Take Recorder Track Settings

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeTrackRecorders
- **File**: IMovieSceneTrackRecorderHost.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_property_tracks`` (Array[TakeRecorderPropertyTrackSettings]):  [Read-Write] List of property names for which movie scene tracks will be created automatically.
- ``exclude_property_tracks`` (Array[TakeRecorderPropertyTrackSettings]):  [Read-Write] List of property names for which movie scene tracks will NOT be created automatically.
- ``matching_actor_class`` (SoftClassPath):  [Read-Write] The Actor class to create movie scene tracks for.

<a id="unreal.TakeRecorderTrackSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FBIKBoneLimit"></a>