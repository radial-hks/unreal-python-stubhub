## PawnAction_Wait Objects

```python
class PawnAction_Wait(PawnAction)
```

uses system timers rather then ticking

**C++ Source:**

- **Module**: AIModule
- **File**: PawnAction_Wait.h

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

<a id="unreal.Controller"></a>