## MovieSceneReplaceableDirectorBlueprintBinding Objects

```python
class MovieSceneReplaceableDirectorBlueprintBinding(
        MovieSceneReplaceableBindingBase)
```

Custom binding type that uses a Director Blueprint endpoint to allow the user to define at runtime how to resolve this binding.
User can use any desired custom spawnable type as the preview within Sequencer, such as a MovieSceneSpawnableDirectorBlueprintBinding for another endpoint
for spawning, or a MovieSceneSpawnableActorBinding to spawn from an actor template.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneReplaceableDirectorBlueprintBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_binding`` (MovieSceneDynamicBinding):  [Read-Write] Director Blueprint defined binding info
- ``preview_spawnable`` (MovieSceneSpawnableBindingBase):  [Read-Only] Optional Editor-only preview object
- ``preview_spawnable_type`` (type(Class)):  [Read-Write] Preview Spawnable Type to use for this replaceable

<a id="unreal.MovieSceneReplaceableDirectorBlueprintBinding.preview_spawnable_type"></a>

#### preview_spawnable_type

```python
@property
def preview_spawnable_type() -> Class
```

(type(Class)):  [Read-Write] Preview Spawnable Type to use for this replaceable

<a id="unreal.MovieSceneReplaceableDirectorBlueprintBinding.preview_spawnable_type"></a>

#### preview_spawnable_type

```python
@preview_spawnable_type.setter
def preview_spawnable_type(value: Class) -> None
```

<a id="unreal.MovieSceneRotatorSection"></a>