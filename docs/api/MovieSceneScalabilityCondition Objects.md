## MovieSceneScalabilityCondition Objects

```python
class MovieSceneScalabilityCondition(MovieSceneCondition)
```

Condition on whether the current engine scalability settings fulfill a given constraint.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneScalabilityCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_force_true`` (bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.
- ``group`` (MovieSceneScalabilityConditionGroup):  [Read-Write]
- ``invert`` (bool):  [Read-Write] If true, inverts the result of the condition check.
- ``level`` (MovieSceneScalabilityConditionLevel):  [Read-Write]
- ``operator`` (MovieSceneScalabilityConditionOperator):  [Read-Write]

<a id="unreal.MovieSceneSpawnableBindingBase"></a>