## MovieSceneDoubleVectorTrackExtensions Objects

```python
class MovieSceneDoubleVectorTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneDoubleVectorTrack for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneVectorTrackExtensions.h

<a id="unreal.MovieSceneDoubleVectorTrackExtensions.set_num_channels_used"></a>

#### set_num_channels_used

```python
@classmethod
def set_num_channels_used(cls, track: MovieSceneDoubleVectorTrack,
                          num_channels_used: int) -> None
```

X.set_num_channels_used(track, num_channels_used) -> None
Set the number of channels used for this track

Args:
    track (MovieSceneDoubleVectorTrack): The track to set
    num_channels_used (int32): The number of channels to use for this track

<a id="unreal.MovieSceneDoubleVectorTrackExtensions.get_num_channels_used"></a>

#### get_num_channels_used

```python
@classmethod
def get_num_channels_used(cls, track: MovieSceneDoubleVectorTrack) -> int
```

X.get_num_channels_used(track) -> int32
Get the number of channels used for this track

Args:
    track (MovieSceneDoubleVectorTrack): The track to query for the number of channels used

Returns:
    int32: The number of channels used for this track

<a id="unreal.SequencerScriptingRangeExtensions"></a>