## MovieSceneDirectorBlueprintCondition Objects

```python
class MovieSceneDirectorBlueprintCondition(MovieSceneCondition)
```

Condition class allowing users to create a director blueprint endpoint in the Sequence to evaluate a condition.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneDirectorBlueprintCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_frequency`` (MovieSceneConditionCheckFrequency):  [Read-Write]
- ``director_blueprint_condition_data`` (MovieSceneDirectorBlueprintConditionData):  [Read-Write]
- ``editor_force_true`` (bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.
- ``invert`` (bool):  [Read-Write] If true, inverts the result of the condition check.
- ``scope`` (MovieSceneConditionScope):  [Read-Write]

<a id="unreal.MovieScenePlatformCondition"></a>