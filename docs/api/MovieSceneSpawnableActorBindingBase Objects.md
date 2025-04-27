## MovieSceneSpawnableActorBindingBase Objects

```python
class MovieSceneSpawnableActorBindingBase(MovieSceneSpawnableBindingBase)
```

The base class for actor-specific spawnable bindings. Contains a default implementation that can handle spawning an Actor from provided Actor class and optional Actor template.
Can be overridden in C++ or blueprint to provide an Actor class and to add custom PostSpawnObject behavior such as mesh setup based on an asset.
The below UMovieSceneSpawnableActorBinding class implements this base class and replicates the old FMovieSceneSpawnable behavior by using a specified Actor template to spawn an Actor and can be used out of the box.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneSpawnableActorBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuously_respawn`` (bool):  [Read-Write] When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each binding lifetime section even if destroyed externally.
- ``level_name`` (Name):  [Read-Write] Name of level to spawn into
- ``net_addressable_name`` (bool):  [Read-Write] When enabled, the actor will be spawned with a unique name so that it can be addressable between clients and servers.
- ``spawn_ownership`` (SpawnOwnership):  [Read-Write] * The spawn ownership setting for this spawnable, allowing spawnables to potentially outlast the lifetime of their sub sequence or sequence altogether.

<a id="unreal.MovieSceneSpawnableActorBindingBase.net_addressable_name"></a>

#### net_addressable_name

```python
@property
def net_addressable_name() -> bool
```

(bool):  [Read-Write] When enabled, the actor will be spawned with a unique name so that it can be addressable between clients and servers.

<a id="unreal.MovieSceneSpawnableActorBindingBase.net_addressable_name"></a>

#### net_addressable_name

```python
@net_addressable_name.setter
def net_addressable_name(value: bool) -> None
```

<a id="unreal.MovieSceneSpawnableActorBindingBase.level_name"></a>

#### level_name

```python
@property
def level_name() -> Name
```

(Name):  [Read-Write] Name of level to spawn into

<a id="unreal.MovieSceneSpawnableActorBindingBase.level_name"></a>

#### level_name

```python
@level_name.setter
def level_name(value: Name) -> None
```

<a id="unreal.MovieSceneSpawnableActorBinding"></a>