## MovieSceneBindingProxy Objects

```python
class MovieSceneBindingProxy(StructBase)
```

Movie Scene Binding Proxy represents the binding ID (an FGuid) and the corresponding sequence that it relates to.
This is primarily used for scripting where there is no support for FMovieSceneSequenceID and use cases where
managing multiple bindings with their corresponding sequences is necessary.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBindingProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding_id`` (Guid):  [Read-Write]
- ``sequence`` (MovieSceneSequence):  [Read-Write]

<a id="unreal.MovieSceneBindingProxy.__init__"></a>

#### __init__

```python
def __init__(binding_id: Guid = [],
             sequence: MovieSceneSequence = None) -> None
```

<a id="unreal.MovieSceneBindingProxy.binding_id"></a>

#### binding_id

```python
@property
def binding_id() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.MovieSceneBindingProxy.sequence"></a>

#### sequence

```python
@property
def sequence() -> MovieSceneSequence
```

(MovieSceneSequence):  [Read-Only]

<a id="unreal.MovieSceneBindingProxy.set_spawnable_binding_id"></a>

#### set_spawnable_binding_id

```python
def set_spawnable_binding_id(
        spawnable_binding_id: MovieSceneObjectBindingID) -> None
```

x.set_spawnable_binding_id(spawnable_binding_id) -> None
Set the spawnable id that the possessable binding should possess

Args:
    spawnable_binding_id (MovieSceneObjectBindingID): The spawnable's binding id

<a id="unreal.MovieSceneBindingProxy.set_sorting_order"></a>

#### set_sorting_order

```python
def set_sorting_order(sorting_order: int) -> None
```

x.set_sorting_order(sorting_order) -> None
Set the sorting order for this binding

Args:
    sorting_order (int32): The sorting order to set

<a id="unreal.MovieSceneBindingProxy.set_parent"></a>

#### set_parent

```python
def set_parent(parent_binding: MovieSceneBindingProxy) -> None
```

x.set_parent(parent_binding) -> None
Set the parent to this binding

Args:
    parent_binding (MovieSceneBindingProxy): The parent to set the InBinding to

<a id="unreal.MovieSceneBindingProxy.set_name"></a>

#### set_name

```python
def set_name(name: str) -> None
```

x.set_name(name) -> None
Set this binding's object non-display name

Args:
    name (str): The name of the binding

<a id="unreal.MovieSceneBindingProxy.set_display_name"></a>

#### set_display_name

```python
def set_display_name(display_name: Text) -> None
```

x.set_display_name(display_name) -> None
Set this binding's name

Args:
    display_name (Text):

<a id="unreal.MovieSceneBindingProxy.remove_track"></a>

#### remove_track

```python
def remove_track(track_to_remove: MovieSceneTrack) -> None
```

x.remove_track(track_to_remove) -> None
Remove the specified track from this binding

Args:
    track_to_remove (MovieSceneTrack): The track to remove

<a id="unreal.MovieSceneBindingProxy.remove"></a>

#### remove

```python
def remove() -> None
```

x.remove() -> None
Remove the specified binding

<a id="unreal.MovieSceneBindingProxy.move_binding_contents"></a>

#### move_binding_contents

```python
def move_binding_contents(
        destination_binding_id: MovieSceneBindingProxy) -> None
```

x.move_binding_contents(destination_binding_id) -> None
Move all the contents (tracks, child bindings) of the specified binding ID onto another

Args:
    destination_binding_id (MovieSceneBindingProxy): The identifier of the binding ID to move the contents to

<a id="unreal.MovieSceneBindingProxy.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Check whether the specified binding is valid

Returns:
    bool:

<a id="unreal.MovieSceneBindingProxy.get_tracks"></a>

#### get_tracks

```python
def get_tracks() -> Array[MovieSceneTrack]
```

x.get_tracks() -> Array[MovieSceneTrack]
Get all the tracks stored within this binding

Returns:
    Array[MovieSceneTrack]: An array containing all the binding's tracks

<a id="unreal.MovieSceneBindingProxy.get_sorting_order"></a>

#### get_sorting_order

```python
def get_sorting_order() -> int
```

x.get_sorting_order() -> int32
Get the sorting order for this binding

Returns:
    int32: The sorting order of the requested binding

<a id="unreal.MovieSceneBindingProxy.get_possessed_object_class"></a>

#### get_possessed_object_class

```python
def get_possessed_object_class() -> Class
```

x.get_possessed_object_class() -> type(Class)
Get this binding's possessed object class

Returns:
    type(Class): The possessed object class of the binding

<a id="unreal.MovieSceneBindingProxy.get_parent"></a>

#### get_parent

```python
def get_parent() -> MovieSceneBindingProxy
```

x.get_parent() -> MovieSceneBindingProxy
Get the parent of this binding

Returns:
    MovieSceneBindingProxy: The binding's parent

<a id="unreal.MovieSceneBindingProxy.get_object_template"></a>

#### get_object_template

```python
def get_object_template() -> Object
```

x.get_object_template() -> Object
Get this binding's object template

Returns:
    Object: The object template of the binding

<a id="unreal.MovieSceneBindingProxy.get_name"></a>

#### get_name

```python
def get_name() -> str
```

x.get_name() -> str
Get this binding's object non-display name

Returns:
    str: The name of the binding

<a id="unreal.MovieSceneBindingProxy.get_id"></a>

#### get_id

```python
def get_id() -> Guid
```

x.get_id() -> Guid
Get this binding's ID

Returns:
    Guid: The guid that uniquely represents this binding

<a id="unreal.MovieSceneBindingProxy.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

x.get_display_name() -> Text
Get this binding's name

Returns:
    Text: The display name of the binding

<a id="unreal.MovieSceneBindingProxy.get_child_possessables"></a>

#### get_child_possessables

```python
def get_child_possessables() -> Array[MovieSceneBindingProxy]
```

x.get_child_possessables() -> Array[MovieSceneBindingProxy]
Get all the children of this binding

Returns:
    Array[MovieSceneBindingProxy]: An array containing all the binding's children

<a id="unreal.MovieSceneBindingProxy.find_tracks_by_type"></a>

#### find_tracks_by_type

```python
def find_tracks_by_type(track_type: Class) -> Array[MovieSceneTrack]
```

x.find_tracks_by_type(track_type) -> Array[MovieSceneTrack]
Find all tracks within a given binding of the specified type

Args:
    track_type (type(Class)): A UMovieSceneTrack class type specifying which types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that match the type specified

<a id="unreal.MovieSceneBindingProxy.find_tracks_by_exact_type"></a>

#### find_tracks_by_exact_type

```python
def find_tracks_by_exact_type(track_type: Class) -> Array[MovieSceneTrack]
```

x.find_tracks_by_exact_type(track_type) -> Array[MovieSceneTrack]
Find all tracks within a given binding of the specified type, not allowing sub-classed types

Args:
    track_type (type(Class)): A UMovieSceneTrack class type specifying the exact types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that are exactly the same as the type specified

<a id="unreal.MovieSceneBindingProxy.add_track"></a>

#### add_track

```python
def add_track(track_type: Class) -> MovieSceneTrack
```

x.add_track(track_type) -> MovieSceneTrack
Add a new track to the specified binding

Args:
    track_type (type(Class)): A UMovieSceneTrack class type specifying the type of track to create

Returns:
    MovieSceneTrack: The newly created track, if successful

<a id="unreal.SequencerBindingProxy"></a>