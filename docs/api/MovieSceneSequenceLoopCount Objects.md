## MovieSceneSequenceLoopCount Objects

```python
class MovieSceneSequenceLoopCount(StructBase)
```

POD struct that represents a number of loops where -1 signifies infinite looping, 0 means no loops, etc
Defined as a struct rather than an int so a property type customization can be bound to it

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequencePlaybackSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (int32):  [Read-Write] Whether or not to loop playback. If Loop Exactly is chosen, you can specify the number of times to loop

<a id="unreal.MovieSceneSequenceLoopCount.__init__"></a>

#### __init__

```python
def __init__(value: int = 0) -> None
```

<a id="unreal.MovieSceneSequenceLoopCount.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write] Whether or not to loop playback. If Loop Exactly is chosen, you can specify the number of times to loop

<a id="unreal.MovieSceneSequenceLoopCount.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.MovieSceneSequencePlaybackSettings"></a>