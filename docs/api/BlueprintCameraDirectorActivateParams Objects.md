## BlueprintCameraDirectorActivateParams Objects

```python
class BlueprintCameraDirectorActivateParams(StructBase)
```

Parameter struct for activating the Blueprint camera director evaluator.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraDirector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``evaluation_context_owner`` (Object):  [Read-Write] The owner (if any) of the evaluation context we are running inside of.

<a id="unreal.BlueprintCameraDirectorActivateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(evaluation_context_owner: Object = None) -> None
```

<a id="unreal.BlueprintCameraDirectorActivateParams.evaluation_context_owner"></a>

#### evaluation\_context\_owner

```python
@property
def evaluation_context_owner() -> Object
```

(Object):  [Read-Write] The owner (if any) of the evaluation context we are running inside of.

<a id="unreal.BlueprintCameraDirectorActivateParams.evaluation_context_owner"></a>

#### evaluation\_context\_owner

```python
@evaluation_context_owner.setter
def evaluation_context_owner(value: Object) -> None
```

<a id="unreal.BlueprintCameraDirectorDeactivateParams"></a>