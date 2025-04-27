## MovieSceneSpawnableChaosCacheBinding Objects

```python
class MovieSceneSpawnableChaosCacheBinding(MovieSceneSpawnableActorBinding)
```

* An override of UMovieSceneSpawnableActorBinding that adds some custom behavior on Spawn

**C++ Source:**

- **Plugin**: ChaosCaching
- **Module**: ChaosCaching
- **File**: MovieSceneSpawnableChaosCacheBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_template`` (Actor):  [Read-Only]
- ``continuously_respawn`` (bool):  [Read-Write] When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each binding lifetime section even if destroyed externally.
- ``level_name`` (Name):  [Read-Write] Name of level to spawn into
- ``net_addressable_name`` (bool):  [Read-Write] When enabled, the actor will be spawned with a unique name so that it can be addressable between clients and servers.
- ``spawn_ownership`` (SpawnOwnership):  [Read-Write] * The spawn ownership setting for this spawnable, allowing spawnables to potentially outlast the lifetime of their sub sequence or sequence altogether.

<a id="unreal.ChaosCacheCollection"></a>