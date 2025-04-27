## MovieSceneSequencePlayToParams Objects

```python
class MovieSceneSequencePlayToParams(StructBase)
```

Movie Scene Sequence Play to Params

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exclusive`` (bool):  [Read-Write] Should the PlayTo time be considered exclusive? Defaults to true as end frames in Sequencer are exclusive by default.

<a id="unreal.MovieSceneSequencePlayToParams.__init__"></a>

#### __init__

```python
def __init__(exclusive: bool = False) -> None
```

<a id="unreal.MovieSceneSequencePlayToParams.exclusive"></a>

#### exclusive

```python
@property
def exclusive() -> bool
```

(bool):  [Read-Write] Should the PlayTo time be considered exclusive? Defaults to true as end frames in Sequencer are exclusive by default.

<a id="unreal.MovieSceneSequencePlayToParams.exclusive"></a>

#### exclusive

```python
@exclusive.setter
def exclusive(value: bool) -> None
```

<a id="unreal.MediaPlayerTrackOptions"></a>