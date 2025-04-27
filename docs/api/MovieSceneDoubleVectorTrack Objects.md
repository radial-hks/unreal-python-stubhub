## MovieSceneDoubleVectorTrack Objects

```python
class MovieSceneDoubleVectorTrack(MovieScenePropertyTrack)
```

Handles manipulation of double vectors in a movie scene

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneVectorTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneDoubleVectorTrack.set_num_channels_used"></a>

#### set_num_channels_used

```python
def set_num_channels_used(num_channels_used: int) -> None
```

x.set_num_channels_used(num_channels_used) -> None
Set the number of channels used for this track

Args:
    num_channels_used (int32): The number of channels to use for this track

<a id="unreal.MovieSceneDoubleVectorTrack.get_num_channels_used"></a>

#### get_num_channels_used

```python
def get_num_channels_used() -> int
```

x.get_num_channels_used() -> int32
Get the number of channels used for this track

Returns:
    int32: The number of channels used for this track

<a id="unreal.MovieSceneVisibilityTrack"></a>