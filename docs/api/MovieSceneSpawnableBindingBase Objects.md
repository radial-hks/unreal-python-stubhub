## MovieSceneSpawnableBindingBase Objects

```python
class MovieSceneSpawnableBindingBase(MovieSceneCustomBinding)
```

The base class for custom spawnable bindings. A spawnable binding will spawn an object upon resolution or return a cached previously spawned object.
UMovieSceneSpawnableActorBinding is the reimplementation of previous FMovieSceneSpawnable features and spawns an actor based on a saved template and actor class.
Otherwise, projects are free to implement their own Spawnable bindings by overriding this class.
In doing so, they could choose to just override GetSpawnObjectClass, PostSpawnObject, and PreDestroyObject for example to do custom post-spawn setup on a character mesh,
or they could choose to fully override SpawnObject and DestroySpawnedObject and do their own custom logic for spawning completely.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSpawnableBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuously_respawn`` (bool):  [Read-Write] When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each binding lifetime section even if destroyed externally.
- ``spawn_ownership`` (SpawnOwnership):  [Read-Write] * The spawn ownership setting for this spawnable, allowing spawnables to potentially outlast the lifetime of their sub sequence or sequence altogether.

<a id="unreal.MovieSceneSpawnableBindingBase.spawn_ownership"></a>

#### spawn_ownership

```python
@property
def spawn_ownership() -> SpawnOwnership
```

(SpawnOwnership):  [Read-Write] * The spawn ownership setting for this spawnable, allowing spawnables to potentially outlast the lifetime of their sub sequence or sequence altogether.

<a id="unreal.MovieSceneSpawnableBindingBase.spawn_ownership"></a>

#### spawn_ownership

```python
@spawn_ownership.setter
def spawn_ownership(value: SpawnOwnership) -> None
```

<a id="unreal.MovieSceneSpawnableBindingBase.continuously_respawn"></a>

#### continuously_respawn

```python
@property
def continuously_respawn() -> bool
```

(bool):  [Read-Write] When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each binding lifetime section even if destroyed externally.

<a id="unreal.MovieSceneSpawnableBindingBase.continuously_respawn"></a>

#### continuously_respawn

```python
@continuously_respawn.setter
def continuously_respawn(value: bool) -> None
```

<a id="unreal.MovieSceneSpawnableActorBindingBase"></a>