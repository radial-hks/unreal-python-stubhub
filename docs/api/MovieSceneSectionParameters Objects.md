## MovieSceneSectionParameters Objects

```python
class MovieSceneSectionParameters(StructBase)
```

namespace UE::MovieScene

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSectionParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_loop`` (bool):  [Read-Write] Whether this section supports looping the sub-sequence.
- ``end_frame_offset`` (FrameNumber):  [Read-Write] Number of frames (in display rate) to skip at the beginning of the sub-sequence.
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] Number of frames (in display rate) to offset the first loop of the sub-sequence.
- ``flags`` (MovieSceneSubSectionFlags):  [Read-Write] Sub-section flags defining how to deal with this sub-sequence
- ``hierarchical_bias`` (int32):  [Read-Write] Hierachical bias. Higher bias will take precedence.
- ``start_frame_offset`` (FrameNumber):  [Read-Write] Number of frames (in display rate) to skip at the beginning of the sub-sequence.
- ``time_scale`` (MovieSceneTimeWarpVariant):  [Read-Write] Playback time scaling factor.

<a id="unreal.MovieSceneSectionParameters.__init__"></a>

#### __init__

```python
def __init__(
        start_frame_offset: FrameNumber = [0],
        can_loop: bool = False,
        end_frame_offset: FrameNumber = [0],
        first_loop_start_frame_offset: FrameNumber = [0],
        time_scale: MovieSceneTimeWarpVariant = [1.000000],
        hierarchical_bias: int = 0,
        flags: MovieSceneSubSectionFlags = MovieSceneSubSectionFlags.NONE
) -> None
```

<a id="unreal.MovieSceneSectionParameters.start_frame_offset"></a>

#### start_frame_offset

```python
@property
def start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of frames (in display rate) to skip at the beginning of the sub-sequence.

<a id="unreal.MovieSceneSectionParameters.start_frame_offset"></a>

#### start_frame_offset

```python
@start_frame_offset.setter
def start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionParameters.can_loop"></a>

#### can_loop

```python
@property
def can_loop() -> bool
```

(bool):  [Read-Write] Whether this section supports looping the sub-sequence.

<a id="unreal.MovieSceneSectionParameters.can_loop"></a>

#### can_loop

```python
@can_loop.setter
def can_loop(value: bool) -> None
```

<a id="unreal.MovieSceneSectionParameters.end_frame_offset"></a>

#### end_frame_offset

```python
@property
def end_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of frames (in display rate) to skip at the beginning of the sub-sequence.

<a id="unreal.MovieSceneSectionParameters.end_frame_offset"></a>

#### end_frame_offset

```python
@end_frame_offset.setter
def end_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionParameters.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@property
def first_loop_start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of frames (in display rate) to offset the first loop of the sub-sequence.

<a id="unreal.MovieSceneSectionParameters.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@first_loop_start_frame_offset.setter
def first_loop_start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionParameters.time_scale"></a>

#### time_scale

```python
@property
def time_scale() -> MovieSceneTimeWarpVariant
```

(MovieSceneTimeWarpVariant):  [Read-Write] Playback time scaling factor.

<a id="unreal.MovieSceneSectionParameters.time_scale"></a>

#### time_scale

```python
@time_scale.setter
def time_scale(value: MovieSceneTimeWarpVariant) -> None
```

<a id="unreal.MovieSceneSectionParameters.hierarchical_bias"></a>

#### hierarchical_bias

```python
@property
def hierarchical_bias() -> int
```

(int32):  [Read-Write] Hierachical bias. Higher bias will take precedence.

<a id="unreal.MovieSceneSectionParameters.hierarchical_bias"></a>

#### hierarchical_bias

```python
@hierarchical_bias.setter
def hierarchical_bias(value: int) -> None
```

<a id="unreal.MovieSceneSectionParameters.flags"></a>

#### flags

```python
@property
def flags() -> MovieSceneSubSectionFlags
```

(MovieSceneSubSectionFlags):  [Read-Write] Sub-section flags defining how to deal with this sub-sequence

<a id="unreal.MovieSceneSectionParameters.flags"></a>

#### flags

```python
@flags.setter
def flags(value: MovieSceneSubSectionFlags) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersSeconds"></a>