## BlueprintCameraDirectorDeactivateParams Objects

```python
class BlueprintCameraDirectorDeactivateParams(StructBase)
```

Parameter struct for deactivating the Blueprint camera director evaluator.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraDirector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``evaluation_context_owner`` (Object):  [Read-Write] The owner (if any) of the evaluation context we were running inside of.

<a id="unreal.BlueprintCameraDirectorDeactivateParams.__init__"></a>

#### __init__

```python
def __init__(evaluation_context_owner: Object = None) -> None
```

<a id="unreal.BlueprintCameraDirectorDeactivateParams.evaluation_context_owner"></a>

#### evaluation_context_owner

```python
@property
def evaluation_context_owner() -> Object
```

(Object):  [Read-Write] The owner (if any) of the evaluation context we were running inside of.

<a id="unreal.BlueprintCameraDirectorDeactivateParams.evaluation_context_owner"></a>

#### evaluation_context_owner

```python
@evaluation_context_owner.setter
def evaluation_context_owner(value: Object) -> None
```

<a id="unreal.BlueprintCameraDirectorEvaluationParams"></a>