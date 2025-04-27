## MovieSceneSpawnableDirectorBlueprintBinding Objects

```python
class MovieSceneSpawnableDirectorBlueprintBinding(
        MovieSceneSpawnableBindingBase)
```

Custom binding type that uses a Director Blueprint endpoint to allow the user to define how to spawn an actor for this binding.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneSpawnableDirectorBlueprintBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuously_respawn`` (bool):  [Read-Write] When enabled, this spawnable will always be respawned if it gets destroyed externally. When disabled, this object will only ever be spawned once for each binding lifetime section even if destroyed externally.
- ``dynamic_binding`` (MovieSceneDynamicBinding):  [Read-Write] Director Blueprint defined binding info
- ``spawn_ownership`` (SpawnOwnership):  [Read-Write] * The spawn ownership setting for this spawnable, allowing spawnables to potentially outlast the lifetime of their sub sequence or sequence altogether.

<a id="unreal.MovieSceneTestSequence"></a>