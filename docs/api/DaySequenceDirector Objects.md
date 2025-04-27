## DaySequenceDirector Objects

```python
class DaySequenceDirector(Object)
```

Day Sequence Director

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceDirector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``player`` (DaySequencePlayer):  [Read-Write] Pointer to the player that's playing back this director's sequence. Only valid in game or in PIE/Simulate.

<a id="unreal.DaySequenceDirector.player"></a>

#### player

```python
@property
def player() -> DaySequencePlayer
```

(DaySequencePlayer):  [Read-Only] Pointer to the player that's playing back this director's sequence. Only valid in game or in PIE/Simulate.

<a id="unreal.DaySequenceDirector.on_created"></a>

#### on_created

```python
def on_created() -> None
```

x.on_created() -> None
Called when this director is created

<a id="unreal.DaySequenceDirector.get_sequence"></a>

#### get_sequence

```python
def get_sequence() -> MovieSceneSequence
```

x.get_sequence() -> MovieSceneSequence
* Get the current sequence that this director is playing back within

Returns:
    MovieSceneSequence:

<a id="unreal.DaySequenceDirector.get_root_sequence_time"></a>

#### get_root_sequence_time

```python
def get_root_sequence_time() -> QualifiedTime
```

x.get_root_sequence_time() -> QualifiedTime
Get the current time for the outermost (root) sequence

Returns:
    QualifiedTime: The current playback position of the root sequence

<a id="unreal.DaySequenceDirector.get_current_time"></a>

#### get_current_time

```python
def get_current_time() -> QualifiedTime
```

x.get_current_time() -> QualifiedTime
Get the current time for this director's sub-sequence (or the root sequence, if this is a root sequence director)

Returns:
    QualifiedTime: The current playback position of this director's sequence

<a id="unreal.DaySequenceDirector.get_bound_objects"></a>

#### get_bound_objects

```python
def get_bound_objects(
        object_binding: MovieSceneObjectBindingID) -> Array[Object]
```

x.get_bound_objects(object_binding) -> Array[Object]
Resolve the bindings inside this sub-sequence that relate to the specified ID
note:: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

Args:
    object_binding (MovieSceneObjectBindingID): The ID for the object binding inside this sub-sequence or one of its children to resolve

Returns:
    Array[Object]:

<a id="unreal.DaySequenceDirector.get_bound_object"></a>

#### get_bound_object

```python
def get_bound_object(object_binding: MovieSceneObjectBindingID) -> Object
```

x.get_bound_object(object_binding) -> Object
Resolve the first valid binding inside this sub-sequence that relates to the specified ID
note:: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

Args:
    object_binding (MovieSceneObjectBindingID): The ID for the object binding inside this sub-sequence or one of its children to resolve

Returns:
    Object:

<a id="unreal.DaySequenceDirector.get_bound_actors"></a>

#### get_bound_actors

```python
def get_bound_actors(
        object_binding: MovieSceneObjectBindingID) -> Array[Actor]
```

x.get_bound_actors(object_binding) -> Array[Actor]
Resolve the actor bindings inside this sub-sequence that relate to the specified ID
note:: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

Args:
    object_binding (MovieSceneObjectBindingID): The ID for the object binding inside this sub-sequence or one of its children to resolve

Returns:
    Array[Actor]:

<a id="unreal.DaySequenceDirector.get_bound_actor"></a>

#### get_bound_actor

```python
def get_bound_actor(object_binding: MovieSceneObjectBindingID) -> Actor
```

x.get_bound_actor(object_binding) -> Actor
Resolve the first valid Actor binding inside this sub-sequence that relates to the specified ID
note:: ObjectBinding should be constructed from the same sequence as this Sequence Director's owning Sequence (see the GetSequenceBinding node)

Args:
    object_binding (MovieSceneObjectBindingID): The ID for the object binding inside this sub-sequence or one of its children to resolve

Returns:
    Actor:

<a id="unreal.TimeOfDaySequenceDirector"></a>