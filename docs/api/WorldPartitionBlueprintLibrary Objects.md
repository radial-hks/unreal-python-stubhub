## WorldPartitionBlueprintLibrary Objects

```python
class WorldPartitionBlueprintLibrary(BlueprintFunctionLibrary)
```

World Partition Blueprint Library

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionBlueprintLibrary.h

<a id="unreal.WorldPartitionBlueprintLibrary.unpin_actors"></a>

#### unpin_actors

```python
@classmethod
def unpin_actors(cls, actors_to_unpin: Array[Guid]) -> None
```

X.unpin_actors(actors_to_unpin) -> None
Unpin actors

Args:
    actors_to_unpin (Array[Guid]):

<a id="unreal.WorldPartitionBlueprintLibrary.unload_actors"></a>

#### unload_actors

```python
@classmethod
def unload_actors(cls, actors_to_unload: Array[Guid]) -> None
```

X.unload_actors(actors_to_unload) -> None
Unload actors

Args:
    actors_to_unload (Array[Guid]):

<a id="unreal.WorldPartitionBlueprintLibrary.pin_actors"></a>

#### pin_actors

```python
@classmethod
def pin_actors(cls, actors_to_pin: Array[Guid]) -> None
```

X.pin_actors(actors_to_pin) -> None
Pin actors

Args:
    actors_to_pin (Array[Guid]):

<a id="unreal.WorldPartitionBlueprintLibrary.load_actors"></a>

#### load_actors

```python
@classmethod
def load_actors(cls, actors_to_load: Array[Guid]) -> None
```

X.load_actors(actors_to_load) -> None
Load actors

Args:
    actors_to_load (Array[Guid]):

<a id="unreal.WorldPartitionBlueprintLibrary.get_runtime_world_bounds"></a>

#### get_runtime_world_bounds

```python
@classmethod
def get_runtime_world_bounds(cls) -> Box
```

X.get_runtime_world_bounds() -> Box
Gets the runtime world bounds, which only includes actor descriptors that aren't editor only.

Returns:
    Box: The runtime world bounds.

<a id="unreal.WorldPartitionBlueprintLibrary.get_intersecting_actor_descs"></a>

#### get_intersecting_actor_descs

```python
@classmethod
def get_intersecting_actor_descs(cls, box: Box) -> Optional[Array[ActorDesc]]
```

X.get_intersecting_actor_descs(box) -> Array[ActorDesc] or None
Gets all the actor descriptors intersecting the provided box into the provided array, recursing into actor containers.

Args:
    box (Box): 

Returns:
    Array[ActorDesc] or None: True if the operation was successful.

    out_actor_descs (Array[ActorDesc]):

<a id="unreal.WorldPartitionBlueprintLibrary.get_editor_world_bounds"></a>

#### get_editor_world_bounds

```python
@classmethod
def get_editor_world_bounds(cls) -> Box
```

X.get_editor_world_bounds() -> Box
Gets the editor world bounds, which includes all actor descriptors.

Returns:
    Box: The editor world bounds.

<a id="unreal.WorldPartitionBlueprintLibrary.get_data_layer_manager"></a>

#### get_data_layer_manager

```python
@classmethod
def get_data_layer_manager(cls,
                           world_context_object: Object) -> DataLayerManager
```

X.get_data_layer_manager(world_context_object) -> DataLayerManager
Returns the Data Layer Manager for this object.

Args:
    world_context_object (Object): 

Returns:
    DataLayerManager:

<a id="unreal.WorldPartitionBlueprintLibrary.get_actor_descs_for_actors"></a>

#### get_actor_descs_for_actors

```python
@classmethod
def get_actor_descs_for_actors(
        cls, actors: Array[Actor]) -> Optional[Array[ActorDesc]]
```

X.get_actor_descs_for_actors(actors) -> Array[ActorDesc] or None
Gets all the actor descriptors from the provided actor pointers, which represents descriptors on disk, e.g. will not
reflect properties of unsaved actors.

Args:
    actors (Array[Actor]): 

Returns:
    Array[ActorDesc] or None: True if the operation was successful.

    out_actor_descs (Array[ActorDesc]):

<a id="unreal.WorldPartitionBlueprintLibrary.get_actor_descs"></a>

#### get_actor_descs

```python
@classmethod
def get_actor_descs(cls) -> Optional[Array[ActorDesc]]
```

X.get_actor_descs() -> Array[ActorDesc] or None
Gets all the actor descriptors into the provided array, recursing into actor containers.

Returns:
    Array[ActorDesc] or None: True if the operation was successful.

    out_actor_descs (Array[ActorDesc]):

<a id="unreal.WorldDataLayers"></a>