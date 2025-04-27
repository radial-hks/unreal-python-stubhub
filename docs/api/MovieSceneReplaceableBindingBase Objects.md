## MovieSceneReplaceableBindingBase Objects

```python
class MovieSceneReplaceableBindingBase(MovieSceneCustomBinding)
```

The base class for custom replaceable bindings. A replaceable binding uses an internal custom spawnable at editor time to produce a preview object,
while in editor will use some other mechanism to dynamically bind an object to the track. Different replaceable types can choose different combinations
of how to create a spawnable for preview vs. how to dynamically bind an object at runtime.
UMovieSceneReplaceableActorBinding as an example is the simplest type of replaceable binding and provides no method for binding at runtime and relies on the LevelSequenceActor's Binding Override
mechanism to bind an actor at runtime.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneReplaceableBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preview_spawnable`` (MovieSceneSpawnableBindingBase):  [Read-Only] Optional Editor-only preview object

<a id="unreal.MovieSceneReplaceableBindingBase.preview_spawnable"></a>

#### preview_spawnable

```python
@property
def preview_spawnable() -> MovieSceneSpawnableBindingBase
```

(MovieSceneSpawnableBindingBase):  [Read-Only] Optional Editor-only preview object

<a id="unreal.MovieSceneReplaceableActorBinding"></a>