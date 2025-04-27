## MovieSceneGeometryCacheSectionTemplateParameters Objects

```python
class MovieSceneGeometryCacheSectionTemplateParameters(
        MovieSceneGeometryCacheParams)
```

Movie Scene Geometry Cache Section Template Parameters

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCacheTracks
- **File**: MovieSceneGeometryCacheTemplate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_frame_offset`` (FrameNumber):  [Read-Write] The offset into the end of the animation clip
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] The offset for the first loop of the animation clip
- ``geometry_cache_asset`` (GeometryCache):  [Read-Write] The animation this section plays
- ``play_rate`` (float):  [Read-Write] The playback rate of the animation clip
- ``reverse`` (bool):  [Read-Write] Reverse the playback of the animation clip
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneGeometryCacheSectionTemplateParameters.__init__"></a>

#### __init__

```python
def __init__(geometry_cache_asset: GeometryCache = None,
             first_loop_start_frame_offset: FrameNumber = [0],
             start_frame_offset: FrameNumber = [0],
             end_frame_offset: FrameNumber = [0],
             play_rate: float = 0.000000,
             reverse: bool = False) -> None
```

<a id="unreal.Ellipsoid"></a>