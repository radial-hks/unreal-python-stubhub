## MovieSceneGeometryCacheSection Objects

```python
class MovieSceneGeometryCacheSection(MovieSceneSection)
```

Movie scene section that control geometry cache playback

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCacheTracks
- **File**: MovieSceneGeometryCacheSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``params`` (MovieSceneGeometryCacheParams):  [Read-Write]
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneGeometryCacheSection.params"></a>

#### params

```python
@property
def params() -> MovieSceneGeometryCacheParams
```

(MovieSceneGeometryCacheParams):  [Read-Write]

<a id="unreal.MovieSceneGeometryCacheSection.params"></a>

#### params

```python
@params.setter
def params(value: MovieSceneGeometryCacheParams) -> None
```

<a id="unreal.MovieSceneGeometryCacheTrack"></a>