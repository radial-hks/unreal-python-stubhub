## BlueprintCameraDirectorEvaluationParams Objects

```python
class BlueprintCameraDirectorEvaluationParams(StructBase)
```

Parameter struct for running the Blueprint camera director evaluator.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraDirector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta_time`` (float):  [Read-Write] The elapsed time since the last evaluation.
- ``evaluation_context_owner`` (Object):  [Read-Write] The owner (if any) of the evaluation context we are running inside of.

<a id="unreal.BlueprintCameraDirectorEvaluationParams.__init__"></a>

#### __init__

```python
def __init__(delta_time: float = 0.000000,
             evaluation_context_owner: Object = None) -> None
```

<a id="unreal.BlueprintCameraDirectorEvaluationParams.delta_time"></a>

#### delta_time

```python
@property
def delta_time() -> float
```

(float):  [Read-Write] The elapsed time since the last evaluation.

<a id="unreal.BlueprintCameraDirectorEvaluationParams.delta_time"></a>

#### delta_time

```python
@delta_time.setter
def delta_time(value: float) -> None
```

<a id="unreal.BlueprintCameraDirectorEvaluationParams.evaluation_context_owner"></a>

#### evaluation_context_owner

```python
@property
def evaluation_context_owner() -> Object
```

(Object):  [Read-Write] The owner (if any) of the evaluation context we are running inside of.

<a id="unreal.BlueprintCameraDirectorEvaluationParams.evaluation_context_owner"></a>

#### evaluation_context_owner

```python
@evaluation_context_owner.setter
def evaluation_context_owner(value: Object) -> None
```

<a id="unreal.CameraDirectorStateTreeEvaluationData"></a>