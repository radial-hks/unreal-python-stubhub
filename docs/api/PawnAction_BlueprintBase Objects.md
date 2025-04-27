## PawnAction_BlueprintBase Objects

```python
class PawnAction_BlueprintBase(PawnAction)
```

Pawn Action Blueprint Base

**C++ Source:**

- **Module**: AIModule
- **File**: PawnAction_BlueprintBase.h

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

<a id="unreal.PawnAction_BlueprintBase.action_tick"></a>

#### action_tick

```python
def action_tick(controlled_pawn: Pawn, delta_seconds: float) -> None
```

x.action_tick(controlled_pawn, delta_seconds) -> None
Action Tick

Args:
    controlled_pawn (Pawn): 
    delta_seconds (float):

<a id="unreal.PawnAction_BlueprintBase.action_start"></a>

#### action_start

```python
def action_start(controlled_pawn: Pawn) -> None
```

x.action_start(controlled_pawn) -> None
Blueprint interface

Args:
    controlled_pawn (Pawn):

<a id="unreal.PawnAction_BlueprintBase.action_resume"></a>

#### action_resume

```python
def action_resume(controlled_pawn: Pawn) -> None
```

x.action_resume(controlled_pawn) -> None
Action Resume

Args:
    controlled_pawn (Pawn):

<a id="unreal.PawnAction_BlueprintBase.action_pause"></a>

#### action_pause

```python
def action_pause(controlled_pawn: Pawn) -> None
```

x.action_pause(controlled_pawn) -> None
Action Pause

Args:
    controlled_pawn (Pawn):

<a id="unreal.PawnAction_BlueprintBase.action_finished"></a>

#### action_finished

```python
def action_finished(controlled_pawn: Pawn,
                    with_result: PawnActionResult) -> None
```

x.action_finished(controlled_pawn, with_result) -> None
Action Finished

Args:
    controlled_pawn (Pawn): 
    with_result (PawnActionResult):

<a id="unreal.PawnAction_Move"></a>