## MovieSceneSectionTimingParametersFrames Objects

```python
class MovieSceneSectionTimingParametersFrames(StructBase)
```

Parameter utility that converts section timing parameters to a transform using inner frame values.

Transformation happens in the following order:

InputTime (relative to section start)
    >> Play Rate / Time Warp
    >> FrameRate conversion
    >> +StartTimeOffset
    >> Loop (% duration)
    >> Reverse

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSectionTimingParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp`` (bool):  [Read-Write] When true, apply clamping to the inner range. Mutually exclusive with bLoop.
- ``first_loop_start_offset`` (FrameNumber):  [Read-Write] Start offset to apply only to the first loop
- ``inner_end_offset`` (FrameNumber):  [Read-Write] End offset (in inner framerate frames) to apply to all loops ie, loop_range=[0 + InnerStartOffset, End- InnerEndOffset)
- ``inner_start_offset`` (FrameNumber):  [Read-Write] Start offset (in inner framerate frames) to apply to all loops
- ``loop`` (bool):  [Read-Write] When true, apply looping to the inner range. Mutually exclusive with bClamp.
- ``play_rate`` (MovieSceneTimeWarpVariant):  [Read-Write] Playrate optionally implemented as time-warp
- ``reverse`` (bool):  [Read-Write] When true, reverses the play direction. Applied after all other transformations

<a id="unreal.MovieSceneSectionTimingParametersFrames.__init__"></a>

#### __init__

```python
def __init__(play_rate: MovieSceneTimeWarpVariant = [1.000000],
             inner_start_offset: FrameNumber = [0],
             inner_end_offset: FrameNumber = [0],
             first_loop_start_offset: FrameNumber = [0],
             loop: bool = False,
             clamp: bool = False,
             reverse: bool = False) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> MovieSceneTimeWarpVariant
```

(MovieSceneTimeWarpVariant):  [Read-Write] Playrate optionally implemented as time-warp

<a id="unreal.MovieSceneSectionTimingParametersFrames.play_rate"></a>

#### play_rate

```python
@play_rate.setter
def play_rate(value: MovieSceneTimeWarpVariant) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.inner_start_offset"></a>

#### inner_start_offset

```python
@property
def inner_start_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Start offset (in inner framerate frames) to apply to all loops

<a id="unreal.MovieSceneSectionTimingParametersFrames.inner_start_offset"></a>

#### inner_start_offset

```python
@inner_start_offset.setter
def inner_start_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.inner_end_offset"></a>

#### inner_end_offset

```python
@property
def inner_end_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] End offset (in inner framerate frames) to apply to all loops ie, loop_range=[0 + InnerStartOffset, End- InnerEndOffset)

<a id="unreal.MovieSceneSectionTimingParametersFrames.inner_end_offset"></a>

#### inner_end_offset

```python
@inner_end_offset.setter
def inner_end_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.first_loop_start_offset"></a>

#### first_loop_start_offset

```python
@property
def first_loop_start_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] Start offset to apply only to the first loop

<a id="unreal.MovieSceneSectionTimingParametersFrames.first_loop_start_offset"></a>

#### first_loop_start_offset

```python
@first_loop_start_offset.setter
def first_loop_start_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write] When true, apply looping to the inner range. Mutually exclusive with bClamp.

<a id="unreal.MovieSceneSectionTimingParametersFrames.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.clamp"></a>

#### clamp

```python
@property
def clamp() -> bool
```

(bool):  [Read-Write] When true, apply clamping to the inner range. Mutually exclusive with bLoop.

<a id="unreal.MovieSceneSectionTimingParametersFrames.clamp"></a>

#### clamp

```python
@clamp.setter
def clamp(value: bool) -> None
```

<a id="unreal.MovieSceneSectionTimingParametersFrames.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] When true, reverses the play direction. Applied after all other transformations

<a id="unreal.MovieSceneSectionTimingParametersFrames.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.MovieSceneSequenceLoopCount"></a>