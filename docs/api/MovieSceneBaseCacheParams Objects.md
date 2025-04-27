## MovieSceneBaseCacheParams Objects

```python
class MovieSceneBaseCacheParams(StructBase)
```

Base class for the cache parameters that will be used in all the cache sections

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneBaseCacheSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_frame_offset`` (FrameNumber):  [Read-Write] The offset into the end of the animation clip
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] The offset for the first loop of the animation clip
- ``play_rate`` (float):  [Read-Write] The playback rate of the animation clip
- ``reverse`` (bool):  [Read-Write] Reverse the playback of the animation clip
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneBaseCacheParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneChaosCacheParams"></a>