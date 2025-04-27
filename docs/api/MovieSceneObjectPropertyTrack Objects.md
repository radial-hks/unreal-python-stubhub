## MovieSceneObjectPropertyTrack Objects

```python
class MovieSceneObjectPropertyTrack(MovieScenePropertyTrack)
```

Movie Scene Object Property Track

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneObjectPropertyTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneObjectPropertyTrack.set_object_property_class"></a>

#### set_object_property_class

```python
def set_object_property_class(property_class: Class) -> None
```

x.set_object_property_class(property_class) -> None
Set this object property track's property class

Args:
    property_class (type(Class)): The property class to set

<a id="unreal.MovieSceneObjectPropertyTrack.get_object_property_class"></a>

#### get_object_property_class

```python
def get_object_property_class() -> Class
```

x.get_object_property_class() -> type(Class)
Get this object property track's property class

Returns:
    type(Class): The property class for this object property track

<a id="unreal.MovieSceneParticleParameterTrack"></a>