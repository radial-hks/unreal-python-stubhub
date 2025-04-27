## MovieSceneReplaceableActorBinding Objects

```python
class MovieSceneReplaceableActorBinding(MovieSceneReplaceableBindingBase)
```

* An implementation of UMovieSceneReplaceableBindingBase that uses UMovieSceneSpawnableActorBinding as the preview spawnable,
* and has no implementation of ResolveRuntimeBindingInternal, relying instead of Sequencer's built in BindingOverride mechanism for binding at runtime.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneReplaceableActorBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preview_spawnable`` (MovieSceneSpawnableBindingBase):  [Read-Only] Optional Editor-only preview object

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase"></a>