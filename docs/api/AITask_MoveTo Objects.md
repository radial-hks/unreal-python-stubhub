## AITask_MoveTo Objects

```python
class AITask_MoveTo(AITask)
```

AITask Move To

**C++ Source:**

- **Module**: AIModule
- **File**: AITask_MoveTo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_move_finished`` (MoveTaskCompletedSignature):  [Read-Write]
- ``on_request_failed`` (GenericGameplayTaskDelegate):  [Read-Write]
- ``owner_controller`` (AIController):  [Read-Write]

<a id="unreal.AITask_MoveTo.on_request_failed"></a>

#### on_request_failed

```python
@property
def on_request_failed() -> GenericGameplayTaskDelegate
```

(GenericGameplayTaskDelegate):  [Read-Write]

<a id="unreal.AITask_MoveTo.on_request_failed"></a>

#### on_request_failed

```python
@on_request_failed.setter
def on_request_failed(value: GenericGameplayTaskDelegate) -> None
```

<a id="unreal.AITask_MoveTo.on_move_finished"></a>

#### on_move_finished

```python
@property
def on_move_finished() -> MoveTaskCompletedSignature
```

(MoveTaskCompletedSignature):  [Read-Write]

<a id="unreal.AITask_MoveTo.on_move_finished"></a>

#### on_move_finished

```python
@on_move_finished.setter
def on_move_finished(value: MoveTaskCompletedSignature) -> None
```

<a id="unreal.AITask_RunEQS"></a>