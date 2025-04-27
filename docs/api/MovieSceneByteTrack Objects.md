## MovieSceneByteTrack Objects

```python
class MovieSceneByteTrack(MovieScenePropertyTrack)
```

Handles manipulation of byte properties in a movie scene

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneByteTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneByteTrack.set_byte_track_enum"></a>

#### set_byte_track_enum

```python
def set_byte_track_enum(enum: Enum) -> None
```

x.set_byte_track_enum(enum) -> None
Set this byte track's enum

Args:
    enum (Enum): The enum to set

<a id="unreal.MovieSceneByteTrack.get_byte_track_enum"></a>

#### get_byte_track_enum

```python
def get_byte_track_enum() -> Enum
```

x.get_byte_track_enum() -> Enum
Get this byte track's enum

Returns:
    Enum: The enum for this byte track

<a id="unreal.MovieSceneCameraCutTrack"></a>