## MovieScenePasteSectionsParams Objects

```python
class MovieScenePasteSectionsParams(StructBase)
```

Paste sections params

**C++ Source:**

- **Module**: Sequencer
- **File**: SequencerUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``time`` (FrameTime):  [Read-Write]
- ``track_row_indices`` (Array[int32]):  [Read-Write]
- ``tracks`` (Array[MovieSceneTrack]):  [Read-Write]

<a id="unreal.MovieScenePasteSectionsParams.__init__"></a>

#### __init__

```python
def __init__(tracks: Array[MovieSceneTrack] = [],
             track_row_indices: Array[int] = [],
             time: FrameTime = [[0], 0.000000]) -> None
```

<a id="unreal.MovieScenePasteSectionsParams.tracks"></a>

#### tracks

```python
@property
def tracks() -> Array[MovieSceneTrack]
```

(Array[MovieSceneTrack]):  [Read-Write]

<a id="unreal.MovieScenePasteSectionsParams.tracks"></a>

#### tracks

```python
@tracks.setter
def tracks(value: Array[MovieSceneTrack]) -> None
```

<a id="unreal.MovieScenePasteSectionsParams.track_row_indices"></a>

#### track_row_indices

```python
@property
def track_row_indices() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.MovieScenePasteSectionsParams.track_row_indices"></a>

#### track_row_indices

```python
@track_row_indices.setter
def track_row_indices(value: Array[int]) -> None
```

<a id="unreal.MovieScenePasteSectionsParams.time"></a>

#### time

```python
@property
def time() -> FrameTime
```

(FrameTime):  [Read-Write]

<a id="unreal.MovieScenePasteSectionsParams.time"></a>

#### time

```python
@time.setter
def time(value: FrameTime) -> None
```

<a id="unreal.MovieScenePasteTracksParams"></a>