## MovieSceneGeometryCacheParams Objects

```python
class MovieSceneGeometryCacheParams(StructBase)
```

Movie Scene Geometry Cache Params

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCacheTracks
- **File**: MovieSceneGeometryCacheSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_frame_offset`` (FrameNumber):  [Read-Write] The offset into the end of the animation clip
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] The offset for the first loop of the animation clip
- ``geometry_cache_asset`` (GeometryCache):  [Read-Write] The animation this section plays
- ``play_rate`` (float):  [Read-Write] The playback rate of the animation clip
- ``reverse`` (bool):  [Read-Write] Reverse the playback of the animation clip
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.__init__"></a>

#### __init__

```python
def __init__(geometry_cache_asset: GeometryCache = None,
             first_loop_start_frame_offset: FrameNumber = [0],
             start_frame_offset: FrameNumber = [0],
             end_frame_offset: FrameNumber = [0],
             play_rate: float = 0.000000,
             reverse: bool = False) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.geometry_cache_asset"></a>

#### geometry_cache_asset

```python
@property
def geometry_cache_asset() -> GeometryCache
```

(GeometryCache):  [Read-Write] The animation this section plays

<a id="unreal.MovieSceneGeometryCacheParams.geometry_cache_asset"></a>

#### geometry_cache_asset

```python
@geometry_cache_asset.setter
def geometry_cache_asset(value: GeometryCache) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@property
def first_loop_start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset for the first loop of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@first_loop_start_frame_offset.setter
def first_loop_start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.start_frame_offset"></a>

#### start_frame_offset

```python
@property
def start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.start_frame_offset"></a>

#### start_frame_offset

```python
@start_frame_offset.setter
def start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.end_frame_offset"></a>

#### end_frame_offset

```python
@property
def end_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset into the end of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.end_frame_offset"></a>

#### end_frame_offset

```python
@end_frame_offset.setter
def end_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> float
```

(float):  [Read-Write] The playback rate of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.play_rate"></a>

#### play_rate

```python
@play_rate.setter
def play_rate(value: float) -> None
```

<a id="unreal.MovieSceneGeometryCacheParams.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] Reverse the playback of the animation clip

<a id="unreal.MovieSceneGeometryCacheParams.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.MovieSceneGeometryCacheSectionTemplateParameters"></a>