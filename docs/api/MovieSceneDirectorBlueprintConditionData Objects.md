## MovieSceneDirectorBlueprintConditionData Objects

```python
class MovieSceneDirectorBlueprintConditionData(StructBase)
```

Data for a director blueprint condition endpoint call.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneDirectorBlueprintCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_context_pin_name`` (Name):  [Read-Write] Pin name for passing the condition context params
- ``payload_variables`` (Map[Name, MovieSceneDirectorBlueprintConditionPayloadVariable]):  [Read-Write] Array of payload variables to be added to the generated function
- ``weak_endpoint`` (Object):  [Read-Write] Endpoint node in the sequence director

<a id="unreal.MovieSceneDirectorBlueprintConditionData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneDynamicBinding"></a>