## MovieSceneSequencePlaybackParams Objects

```python
class MovieSceneSequencePlaybackParams(StructBase)
```

Movie Scene Sequence Playback Params

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame`` (FrameTime):  [Read-Write]
- ``has_jumped`` (bool):  [Read-Write]
- ``marked_frame`` (str):  [Read-Write]
- ``position_type`` (MovieScenePositionType):  [Read-Write]
- ``time`` (float):  [Read-Write]
- ``timecode`` (Timecode):  [Read-Write]
- ``update_method`` (UpdatePositionMethod):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.__init__"></a>

#### __init__

```python
def __init__(
        frame: FrameTime = [[0], 0.000000],
        time: float = 0.000000,
        marked_frame: str = "",
        timecode: Timecode = [0, 0, 0, 0, 0.000000, False],
        position_type: MovieScenePositionType = MovieScenePositionType.FRAME,
        update_method: UpdatePositionMethod = UpdatePositionMethod.PLAY,
        has_jumped: bool = False) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.frame"></a>

#### frame

```python
@property
def frame() -> FrameTime
```

(FrameTime):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.frame"></a>

#### frame

```python
@frame.setter
def frame(value: FrameTime) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.time"></a>

#### time

```python
@time.setter
def time(value: float) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.marked_frame"></a>

#### marked_frame

```python
@property
def marked_frame() -> str
```

(str):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.marked_frame"></a>

#### marked_frame

```python
@marked_frame.setter
def marked_frame(value: str) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.timecode"></a>

#### timecode

```python
@property
def timecode() -> Timecode
```

(Timecode):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.timecode"></a>

#### timecode

```python
@timecode.setter
def timecode(value: Timecode) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.position_type"></a>

#### position_type

```python
@property
def position_type() -> MovieScenePositionType
```

(MovieScenePositionType):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.position_type"></a>

#### position_type

```python
@position_type.setter
def position_type(value: MovieScenePositionType) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.update_method"></a>

#### update_method

```python
@property
def update_method() -> UpdatePositionMethod
```

(UpdatePositionMethod):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.update_method"></a>

#### update_method

```python
@update_method.setter
def update_method(value: UpdatePositionMethod) -> None
```

<a id="unreal.MovieSceneSequencePlaybackParams.has_jumped"></a>

#### has_jumped

```python
@property
def has_jumped() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieSceneSequencePlaybackParams.has_jumped"></a>

#### has_jumped

```python
@has_jumped.setter
def has_jumped(value: bool) -> None
```

<a id="unreal.MovieSceneSequencePlayToParams"></a>