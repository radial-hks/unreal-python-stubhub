## MovieScenePlatformCondition Objects

```python
class MovieScenePlatformCondition(MovieSceneCondition)
```

Condition on whether the platform running the executable matches one of the given platforms.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieScenePlatformCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_force_true`` (bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.
- ``invert`` (bool):  [Read-Write] If true, inverts the result of the condition check.
- ``valid_platforms`` (Array[Name]):  [Read-Write]

<a id="unreal.MovieSceneCustomBinding"></a>