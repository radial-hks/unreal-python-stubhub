## PawnAction Objects

```python
class PawnAction(Object)
```

Things to remember:
* Actions are created paused

**C++ Source:**

- **Module**: AIModule
- **File**: PawnAction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_new_same_class_instance`` (bool):  [Read-Write] if this is FALSE and we're trying to push a new instance of a given class,
      but the top of the stack is already an instance of that class ignore the attempted push
- ``always_notify_on_finished`` (bool):  [Read-Write] if set, action will call OnFinished notify even when ending as FailedToStart
- ``replace_active_same_class_instance`` (bool):  [Read-Write] if this is TRUE, when we try to push a new instance of an action who has the
      same class as the action on the top of the stack, pop the one on the stack, and push the new one
      NOTE: This trumps bAllowNewClassInstance (e.g. if this is true and bAllowNewClassInstance
      is false the active instance will still be replaced)
- ``should_pause_movement`` (bool):  [Read-Write] this is a temporary solution to allow having movement action running in background while there's
      another action on top doing its thing
  note: should go away once AI resource locking comes on-line

<a id="unreal.PawnAction.allow_new_same_class_instance"></a>

#### allow_new_same_class_instance

```python
@property
def allow_new_same_class_instance() -> bool
```

(bool):  [Read-Only] if this is FALSE and we're trying to push a new instance of a given class,
    but the top of the stack is already an instance of that class ignore the attempted push

<a id="unreal.PawnAction.replace_active_same_class_instance"></a>

#### replace_active_same_class_instance

```python
@property
def replace_active_same_class_instance() -> bool
```

(bool):  [Read-Write] if this is TRUE, when we try to push a new instance of an action who has the
    same class as the action on the top of the stack, pop the one on the stack, and push the new one
    NOTE: This trumps bAllowNewClassInstance (e.g. if this is true and bAllowNewClassInstance
    is false the active instance will still be replaced)

<a id="unreal.PawnAction.replace_active_same_class_instance"></a>

#### replace_active_same_class_instance

```python
@replace_active_same_class_instance.setter
def replace_active_same_class_instance(value: bool) -> None
```

<a id="unreal.PawnAction.should_pause_movement"></a>

#### should_pause_movement

```python
@property
def should_pause_movement() -> bool
```

(bool):  [Read-Write] this is a temporary solution to allow having movement action running in background while there's
    another action on top doing its thing
note: should go away once AI resource locking comes on-line

<a id="unreal.PawnAction.should_pause_movement"></a>

#### should_pause_movement

```python
@should_pause_movement.setter
def should_pause_movement(value: bool) -> None
```

<a id="unreal.PawnAction.always_notify_on_finished"></a>

#### always_notify_on_finished

```python
@property
def always_notify_on_finished() -> bool
```

(bool):  [Read-Write] if set, action will call OnFinished notify even when ending as FailedToStart

<a id="unreal.PawnAction.always_notify_on_finished"></a>

#### always_notify_on_finished

```python
@always_notify_on_finished.setter
def always_notify_on_finished(value: bool) -> None
```

<a id="unreal.PawnAction.get_action_priority"></a>

#### get_action_priority

```python
def get_action_priority() -> AIRequestPriority
```

x.get_action_priority() -> AIRequestPriority
Blueprint interface

Returns:
    AIRequestPriority:

<a id="unreal.PawnAction.finish"></a>

#### finish

```python
def finish(with_result: PawnActionResult) -> None
```

x.finish(with_result) -> None
Finish

Args:
    with_result (PawnActionResult):

<a id="unreal.PawnAction.create_action_instance"></a>

#### create_action_instance

```python
@classmethod
def create_action_instance(cls, world_context_object: Object,
                           action_class: Class) -> PawnAction
```

X.create_action_instance(world_context_object, action_class) -> PawnAction
Create Action Instance
deprecated: PawnActions have been deprecated and are no longer being supported. It will get removed in following UE5 releases. Use GameplayTasks or AITasks instead.

Args:
    world_context_object (Object): 
    action_class (type(Class)): 

Returns:
    PawnAction:

<a id="unreal.PawnActionsComponent"></a>