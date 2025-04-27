## MovieScenePropertyTrack Objects

```python
class MovieScenePropertyTrack(MovieSceneNameableTrack)
```

Base class for tracks that animate an object property

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScenePropertyTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieScenePropertyTrack.set_property_name_and_path"></a>

#### set_property_name_and_path

```python
def set_property_name_and_path(property_name: Name,
                               property_path: str) -> None
```

x.set_property_name_and_path(property_name, property_path) -> None
Set this track's property name and path

Args:
    property_name (Name): The property name
    property_path (str): The property path

<a id="unreal.MovieScenePropertyTrack.get_unique_track_name"></a>

#### get_unique_track_name

```python
def get_unique_track_name() -> Name
```

x.get_unique_track_name() -> Name
Get this track's unique name

Returns:
    Name: This track's unique name

<a id="unreal.MovieScenePropertyTrack.get_property_path"></a>

#### get_property_path

```python
def get_property_path() -> str
```

x.get_property_path() -> str
Get this track's property path

Returns:
    str: This track's property path

<a id="unreal.MovieScenePropertyTrack.get_property_name"></a>

#### get_property_name

```python
def get_property_name() -> Name
```

x.get_property_name() -> Name
Get this track's property name

Returns:
    Name: This track's property name

<a id="unreal.MovieScene2DTransformTrack"></a>