## MovieScenePropertyTrackExtensions Objects

```python
class MovieScenePropertyTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieScenePropertyTrack for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieScenePropertyTrackExtensions.h

<a id="unreal.MovieScenePropertyTrackExtensions.set_property_name_and_path"></a>

#### set_property_name_and_path

```python
@classmethod
def set_property_name_and_path(cls, track: MovieScenePropertyTrack,
                               property_name: Name,
                               property_path: str) -> None
```

X.set_property_name_and_path(track, property_name, property_path) -> None
Set this track's property name and path

Args:
    track (MovieScenePropertyTrack): The track to use
    property_name (Name): The property name
    property_path (str): The property path

<a id="unreal.MovieScenePropertyTrackExtensions.set_object_property_class"></a>

#### set_object_property_class

```python
@classmethod
def set_object_property_class(cls, track: MovieSceneObjectPropertyTrack,
                              property_class: Class) -> None
```

X.set_object_property_class(track, property_class) -> None
Set this object property track's property class

Args:
    track (MovieSceneObjectPropertyTrack): The track to use
    property_class (type(Class)): The property class to set

<a id="unreal.MovieScenePropertyTrackExtensions.set_byte_track_enum"></a>

#### set_byte_track_enum

```python
@classmethod
def set_byte_track_enum(cls, track: MovieSceneByteTrack, enum: Enum) -> None
```

X.set_byte_track_enum(track, enum) -> None
Set this byte track's enum

Args:
    track (MovieSceneByteTrack): The track to use
    enum (Enum): The enum to set

<a id="unreal.MovieScenePropertyTrackExtensions.get_unique_track_name"></a>

#### get_unique_track_name

```python
@classmethod
def get_unique_track_name(cls, track: MovieScenePropertyTrack) -> Name
```

X.get_unique_track_name(track) -> Name
Get this track's unique name

Args:
    track (MovieScenePropertyTrack): The track to use

Returns:
    Name: This track's unique name

<a id="unreal.MovieScenePropertyTrackExtensions.get_property_path"></a>

#### get_property_path

```python
@classmethod
def get_property_path(cls, track: MovieScenePropertyTrack) -> str
```

X.get_property_path(track) -> str
Get this track's property path

Args:
    track (MovieScenePropertyTrack): The track to use

Returns:
    str: This track's property path

<a id="unreal.MovieScenePropertyTrackExtensions.get_property_name"></a>

#### get_property_name

```python
@classmethod
def get_property_name(cls, track: MovieScenePropertyTrack) -> Name
```

X.get_property_name(track) -> Name
Get this track's property name

Args:
    track (MovieScenePropertyTrack): The track to use

Returns:
    Name: This track's property name

<a id="unreal.MovieScenePropertyTrackExtensions.get_object_property_class"></a>

#### get_object_property_class

```python
@classmethod
def get_object_property_class(cls,
                              track: MovieSceneObjectPropertyTrack) -> Class
```

X.get_object_property_class(track) -> type(Class)
Get this object property track's property class

Args:
    track (MovieSceneObjectPropertyTrack): The track to use

Returns:
    type(Class): The property class for this object property track

<a id="unreal.MovieScenePropertyTrackExtensions.get_byte_track_enum"></a>

#### get_byte_track_enum

```python
@classmethod
def get_byte_track_enum(cls, track: MovieSceneByteTrack) -> Enum
```

X.get_byte_track_enum(track) -> Enum
Get this byte track's enum

Args:
    track (MovieSceneByteTrack): The track to use

Returns:
    Enum: The enum for this byte track

<a id="unreal.MovieSceneSectionExtensions"></a>