## MovieSceneTimecodeSource Objects

```python
class MovieSceneTimecodeSource(StructBase)
```

Movie Scene Timecode Source

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``timecode`` (Timecode):  [Read-Write] The global timecode at which this target is based (ie. the timecode at the beginning of the movie scene section when it was recorded)

<a id="unreal.MovieSceneTimecodeSource.__init__"></a>

#### __init__

```python
def __init__(timecode: Timecode = [0, 0, 0, 0, 0.000000, False]) -> None
```

<a id="unreal.MovieSceneTimecodeSource.timecode"></a>

#### timecode

```python
@property
def timecode() -> Timecode
```

(Timecode):  [Read-Only] The global timecode at which this target is based (ie. the timecode at the beginning of the movie scene section when it was recorded)

<a id="unreal.MovieSceneSequencePlaybackParams"></a>