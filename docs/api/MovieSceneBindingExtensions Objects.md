## MovieSceneBindingExtensions Objects

```python
class MovieSceneBindingExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto FMovieSceneBindingProxies for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneBindingExtensions.h

<a id="unreal.MovieSceneBindingExtensions.set_spawnable_binding_id"></a>

#### set_spawnable_binding_id

```python
@classmethod
def set_spawnable_binding_id(
        cls, binding: MovieSceneBindingProxy,
        spawnable_binding_id: MovieSceneObjectBindingID) -> None
```

X.set_spawnable_binding_id(binding, spawnable_binding_id) -> None
Set the spawnable id that the possessable binding should possess

Args:
    binding (MovieSceneBindingProxy): The binding to set
    spawnable_binding_id (MovieSceneObjectBindingID): The spawnable's binding id

<a id="unreal.MovieSceneBindingExtensions.set_sorting_order"></a>

#### set_sorting_order

```python
@classmethod
def set_sorting_order(cls, binding: MovieSceneBindingProxy,
                      sorting_order: int) -> None
```

X.set_sorting_order(binding, sorting_order) -> None
Set the sorting order for this binding

Args:
    binding (MovieSceneBindingProxy): The binding to get the sorting order from
    sorting_order (int32): The sorting order to set

<a id="unreal.MovieSceneBindingExtensions.set_parent"></a>

#### set_parent

```python
@classmethod
def set_parent(cls, binding: MovieSceneBindingProxy,
               parent_binding: MovieSceneBindingProxy) -> None
```

X.set_parent(binding, parent_binding) -> None
Set the parent to this binding

Args:
    binding (MovieSceneBindingProxy): The binding to set
    parent_binding (MovieSceneBindingProxy): The parent to set the InBinding to

<a id="unreal.MovieSceneBindingExtensions.set_name"></a>

#### set_name

```python
@classmethod
def set_name(cls, binding: MovieSceneBindingProxy, name: str) -> None
```

X.set_name(binding, name) -> None
Set this binding's object non-display name

Args:
    binding (MovieSceneBindingProxy): The binding to get the name of
    name (str): The name of the binding

<a id="unreal.MovieSceneBindingExtensions.set_display_name"></a>

#### set_display_name

```python
@classmethod
def set_display_name(cls, binding: MovieSceneBindingProxy,
                     display_name: Text) -> None
```

X.set_display_name(binding, display_name) -> None
Set this binding's name

Args:
    binding (MovieSceneBindingProxy): The binding to get the name of
    display_name (Text):

<a id="unreal.MovieSceneBindingExtensions.remove_track"></a>

#### remove_track

```python
@classmethod
def remove_track(cls, binding: MovieSceneBindingProxy,
                 track_to_remove: MovieSceneTrack) -> None
```

X.remove_track(binding, track_to_remove) -> None
Remove the specified track from this binding

Args:
    binding (MovieSceneBindingProxy): The binding to remove the track from
    track_to_remove (MovieSceneTrack): The track to remove

<a id="unreal.MovieSceneBindingExtensions.remove"></a>

#### remove

```python
@classmethod
def remove(cls, binding: MovieSceneBindingProxy) -> None
```

X.remove(binding) -> None
Remove the specified binding

Args:
    binding (MovieSceneBindingProxy): The binding to remove the track from

<a id="unreal.MovieSceneBindingExtensions.move_binding_contents"></a>

#### move_binding_contents

```python
@classmethod
def move_binding_contents(
        cls, source_binding_id: MovieSceneBindingProxy,
        destination_binding_id: MovieSceneBindingProxy) -> None
```

X.move_binding_contents(source_binding_id, destination_binding_id) -> None
Move all the contents (tracks, child bindings) of the specified binding ID onto another

Args:
    source_binding_id (MovieSceneBindingProxy): The identifier of the binding ID to move all tracks and children from
    destination_binding_id (MovieSceneBindingProxy): The identifier of the binding ID to move the contents to

<a id="unreal.MovieSceneBindingExtensions.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(cls, binding: MovieSceneBindingProxy) -> bool
```

X.is_valid(binding) -> bool
Check whether the specified binding is valid

Args:
    binding (MovieSceneBindingProxy): 

Returns:
    bool:

<a id="unreal.MovieSceneBindingExtensions.get_tracks"></a>

#### get_tracks

```python
@classmethod
def get_tracks(cls, binding: MovieSceneBindingProxy) -> Array[MovieSceneTrack]
```

X.get_tracks(binding) -> Array[MovieSceneTrack]
Get all the tracks stored within this binding

Args:
    binding (MovieSceneBindingProxy): The binding to find tracks in

Returns:
    Array[MovieSceneTrack]: An array containing all the binding's tracks

<a id="unreal.MovieSceneBindingExtensions.get_sorting_order"></a>

#### get_sorting_order

```python
@classmethod
def get_sorting_order(cls, binding: MovieSceneBindingProxy) -> int
```

X.get_sorting_order(binding) -> int32
Get the sorting order for this binding

Args:
    binding (MovieSceneBindingProxy): The binding to get the sorting order from

Returns:
    int32: The sorting order of the requested binding

<a id="unreal.MovieSceneBindingExtensions.get_possessed_object_class"></a>

#### get_possessed_object_class

```python
@classmethod
def get_possessed_object_class(cls, binding: MovieSceneBindingProxy) -> Class
```

X.get_possessed_object_class(binding) -> type(Class)
Get this binding's possessed object class

Args:
    binding (MovieSceneBindingProxy): The binding to get the possessed object class of

Returns:
    type(Class): The possessed object class of the binding

<a id="unreal.MovieSceneBindingExtensions.get_parent"></a>

#### get_parent

```python
@classmethod
def get_parent(cls, binding: MovieSceneBindingProxy) -> MovieSceneBindingProxy
```

X.get_parent(binding) -> MovieSceneBindingProxy
Get the parent of this binding

Args:
    binding (MovieSceneBindingProxy): The binding to get the parent of

Returns:
    MovieSceneBindingProxy: The binding's parent

<a id="unreal.MovieSceneBindingExtensions.get_object_template"></a>

#### get_object_template

```python
@classmethod
def get_object_template(cls, binding: MovieSceneBindingProxy) -> Object
```

X.get_object_template(binding) -> Object
Get this binding's object template

Args:
    binding (MovieSceneBindingProxy): The binding to get the object template of

Returns:
    Object: The object template of the binding

<a id="unreal.MovieSceneBindingExtensions.get_name"></a>

#### get_name

```python
@classmethod
def get_name(cls, binding: MovieSceneBindingProxy) -> str
```

X.get_name(binding) -> str
Get this binding's object non-display name

Args:
    binding (MovieSceneBindingProxy): The binding to get the name of

Returns:
    str: The name of the binding

<a id="unreal.MovieSceneBindingExtensions.get_id"></a>

#### get_id

```python
@classmethod
def get_id(cls, binding: MovieSceneBindingProxy) -> Guid
```

X.get_id(binding) -> Guid
Get this binding's ID

Args:
    binding (MovieSceneBindingProxy): The binding to get the ID of

Returns:
    Guid: The guid that uniquely represents this binding

<a id="unreal.MovieSceneBindingExtensions.get_display_name"></a>

#### get_display_name

```python
@classmethod
def get_display_name(cls, binding: MovieSceneBindingProxy) -> Text
```

X.get_display_name(binding) -> Text
Get this binding's name

Args:
    binding (MovieSceneBindingProxy): The binding to get the name of

Returns:
    Text: The display name of the binding

<a id="unreal.MovieSceneBindingExtensions.get_child_possessables"></a>

#### get_child_possessables

```python
@classmethod
def get_child_possessables(
        cls, binding: MovieSceneBindingProxy) -> Array[MovieSceneBindingProxy]
```

X.get_child_possessables(binding) -> Array[MovieSceneBindingProxy]
Get all the children of this binding

Args:
    binding (MovieSceneBindingProxy): The binding to to get children of

Returns:
    Array[MovieSceneBindingProxy]: An array containing all the binding's children

<a id="unreal.MovieSceneBindingExtensions.find_tracks_by_type"></a>

#### find_tracks_by_type

```python
@classmethod
def find_tracks_by_type(cls, binding: MovieSceneBindingProxy,
                        track_type: Class) -> Array[MovieSceneTrack]
```

X.find_tracks_by_type(binding, track_type) -> Array[MovieSceneTrack]
Find all tracks within a given binding of the specified type

Args:
    binding (MovieSceneBindingProxy): The binding to find tracks in
    track_type (type(Class)): A UMovieSceneTrack class type specifying which types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that match the type specified

<a id="unreal.MovieSceneBindingExtensions.find_tracks_by_exact_type"></a>

#### find_tracks_by_exact_type

```python
@classmethod
def find_tracks_by_exact_type(cls, binding: MovieSceneBindingProxy,
                              track_type: Class) -> Array[MovieSceneTrack]
```

X.find_tracks_by_exact_type(binding, track_type) -> Array[MovieSceneTrack]
Find all tracks within a given binding of the specified type, not allowing sub-classed types

Args:
    binding (MovieSceneBindingProxy): The binding to find tracks in
    track_type (type(Class)): A UMovieSceneTrack class type specifying the exact types of track to return

Returns:
    Array[MovieSceneTrack]: An array containing any tracks that are exactly the same as the type specified

<a id="unreal.MovieSceneBindingExtensions.add_track"></a>

#### add_track

```python
@classmethod
def add_track(cls, binding: MovieSceneBindingProxy,
              track_type: Class) -> MovieSceneTrack
```

X.add_track(binding, track_type) -> MovieSceneTrack
Add a new track to the specified binding

Args:
    binding (MovieSceneBindingProxy): The binding to add tracks to
    track_type (type(Class)): A UMovieSceneTrack class type specifying the type of track to create

Returns:
    MovieSceneTrack: The newly created track, if successful

<a id="unreal.MovieSceneEventTrackExtensions"></a>