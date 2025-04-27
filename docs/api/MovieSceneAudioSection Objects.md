## MovieSceneAudioSection Objects

```python
class MovieSceneAudioSection(MovieSceneSection)
```

Audio section, for use in the audio track, or by attached audio objects

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneAudioSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attenuation_settings`` (SoundAttenuation):  [Read-Write] The attenuation settings to use.
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``looping`` (bool):  [Read-Write] Allow looping if the section length is greater than the sound duration
- ``override_attenuation`` (bool):  [Read-Write] Should the attenuation settings on this section be used.
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``sound`` (SoundBase):  [Read-Write] The sound cue or wave that this section plays
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the audio clip
- ``suppress_subtitles`` (bool):  [Read-Write]
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneAudioSection.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Write] The sound cue or wave that this section plays

<a id="unreal.MovieSceneAudioSection.sound"></a>

#### sound

```python
@sound.setter
def sound(value: SoundBase) -> None
```

<a id="unreal.MovieSceneAudioSection.set_suppress_subtitles"></a>

#### set_suppress_subtitles

```python
def set_suppress_subtitles(suppress_subtitles: bool) -> None
```

x.set_suppress_subtitles(suppress_subtitles) -> None
Set whether subtitles should be suppressed

Args:
    suppress_subtitles (bool):

<a id="unreal.MovieSceneAudioSection.set_start_offset"></a>

#### set_start_offset

```python
def set_start_offset(start_offset: FrameNumber) -> None
```

x.set_start_offset(start_offset) -> None
Set the offset into the beginning of the audio clip

Args:
    start_offset (FrameNumber):

<a id="unreal.MovieSceneAudioSection.set_sound"></a>

#### set_sound

```python
def set_sound(sound: SoundBase) -> None
```

x.set_sound(sound) -> None
Sets this section's sound

Args:
    sound (SoundBase):

<a id="unreal.MovieSceneAudioSection.set_override_attenuation"></a>

#### set_override_attenuation

```python
def set_override_attenuation(override_attenuation: bool) -> None
```

x.set_override_attenuation(override_attenuation) -> None
Set whether the attentuation should be overriden

Args:
    override_attenuation (bool):

<a id="unreal.MovieSceneAudioSection.set_looping"></a>

#### set_looping

```python
def set_looping(looping: bool) -> None
```

x.set_looping(looping) -> None
Set whether the sound should be looped

Args:
    looping (bool):

<a id="unreal.MovieSceneAudioSection.set_attenuation_settings"></a>

#### set_attenuation_settings

```python
def set_attenuation_settings(attenuation_settings: SoundAttenuation) -> None
```

x.set_attenuation_settings(attenuation_settings) -> None
Set the attenuation settings for this audio section

Args:
    attenuation_settings (SoundAttenuation):

<a id="unreal.MovieSceneAudioSection.get_suppress_subtitles"></a>

#### get_suppress_subtitles

```python
def get_suppress_subtitles() -> bool
```

x.get_suppress_subtitles() -> bool


Returns:
    bool: Whether subtitles should be suppressed

<a id="unreal.MovieSceneAudioSection.get_start_offset"></a>

#### get_start_offset

```python
def get_start_offset() -> FrameNumber
```

x.get_start_offset() -> FrameNumber
Get the offset into the beginning of the audio clip

Returns:
    FrameNumber:

<a id="unreal.MovieSceneAudioSection.get_sound"></a>

#### get_sound

```python
def get_sound() -> SoundBase
```

x.get_sound() -> SoundBase
Gets the sound for this section

Returns:
    SoundBase:

<a id="unreal.MovieSceneAudioSection.get_override_attenuation"></a>

#### get_override_attenuation

```python
def get_override_attenuation() -> bool
```

x.get_override_attenuation() -> bool


Returns:
    bool: Whether override settings on this section should be used

<a id="unreal.MovieSceneAudioSection.get_looping"></a>

#### get_looping

```python
def get_looping() -> bool
```

x.get_looping() -> bool


Returns:
    bool: Whether to allow looping if the section length is greater than the sound duration

<a id="unreal.MovieSceneAudioSection.get_attenuation_settings"></a>

#### get_attenuation_settings

```python
def get_attenuation_settings() -> SoundAttenuation
```

x.get_attenuation_settings() -> SoundAttenuation


Returns:
    SoundAttenuation: The attenuation settings

<a id="unreal.MovieSceneBaseCacheSection"></a>