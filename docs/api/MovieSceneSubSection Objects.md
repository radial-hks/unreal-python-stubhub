## MovieSceneSubSection Objects

```python
class MovieSceneSubSection(MovieSceneSection)
```

Implements a section in sub-sequence tracks.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSubSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``network_mask`` (uint8):  [Read-Write]
- ``parameters`` (MovieSceneSectionParameters):  [Read-Write]
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``sub_sequence`` (MovieSceneSequence):  [Read-Write] Movie scene being played by this section
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneSubSection.parameters"></a>

#### parameters

```python
@property
def parameters() -> MovieSceneSectionParameters
```

(MovieSceneSectionParameters):  [Read-Write]

<a id="unreal.MovieSceneSubSection.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: MovieSceneSectionParameters) -> None
```

<a id="unreal.MovieSceneSubSection.set_sequence"></a>

#### set_sequence

```python
def set_sequence(sequence: MovieSceneSequence) -> None
```

x.set_sequence(sequence) -> None
Sets the sequence played by this section.
see: GetSequence

Args:
    sequence (MovieSceneSequence): The sequence to play.

<a id="unreal.MovieSceneSubSection.get_sequence"></a>

#### get_sequence

```python
def get_sequence() -> MovieSceneSequence
```

x.get_sequence() -> MovieSceneSequence
Get the sequence that is assigned to this section.
see: SetSequence

Returns:
    MovieSceneSequence: The sequence.

<a id="unreal.MovieSceneSubSection.get_parent_sequence_frame"></a>

#### get_parent_sequence_frame

```python
def get_parent_sequence_frame(frame: int,
                              parent_sequence: MovieSceneSequence) -> int
```

x.get_parent_sequence_frame(frame, parent_sequence) -> int32
Get the frame in the space of its parent sequence

Args:
    frame (int32): The desired local frame
    parent_sequence (MovieSceneSequence): The parent sequence to traverse from

Returns:
    int32: The frame at the parent sequence

<a id="unreal.MovieSceneCinematicShotSection"></a>