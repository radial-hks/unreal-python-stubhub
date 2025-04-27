## MovieSceneMediaPlayerPropertySection Objects

```python
class MovieSceneMediaPlayerPropertySection(MovieSceneSection)
```

Implements a movie scene section for media playback on a UMediaPlayer.

**C++ Source:**

- **Plugin**: MediaCompositing
- **Module**: MediaCompositing
- **File**: MovieSceneMediaPlayerPropertySection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``loop`` (bool):  [Read-Write] Whether to loop this video.
- ``media_source`` (MediaSource):  [Read-Write] The source to play with this video track.
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneMediaPlayerPropertySection.media_source"></a>

#### media_source

```python
@property
def media_source() -> MediaSource
```

(MediaSource):  [Read-Write] The source to play with this video track.

<a id="unreal.MovieSceneMediaPlayerPropertySection.media_source"></a>

#### media_source

```python
@media_source.setter
def media_source(value: MediaSource) -> None
```

<a id="unreal.MovieSceneMediaPlayerPropertySection.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write] Whether to loop this video.

<a id="unreal.MovieSceneMediaPlayerPropertySection.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.MovieSceneMediaPlayerPropertyTrack"></a>