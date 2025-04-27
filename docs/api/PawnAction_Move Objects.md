## PawnAction_Move Objects

```python
class PawnAction_Move(PawnAction)
```

Pawn Action Move

**C++ Source:**

- **Module**: AIModule
- **File**: PawnAction_Move.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceptable_radius`` (float):  [Read-Write]
- ``allow_new_same_class_instance`` (bool):  [Read-Write] if this is FALSE and we're trying to push a new instance of a given class,
      but the top of the stack is already an instance of that class ignore the attempted push
- ``allow_strafe`` (bool):  [Read-Write]
- ``always_notify_on_finished`` (bool):  [Read-Write] if set, action will call OnFinished notify even when ending as FailedToStart
- ``filter_class`` (type(Class)):  [Read-Write] "None" will result in default filter being used
- ``goal_actor`` (Actor):  [Read-Write]
- ``goal_location`` (Vector):  [Read-Write]
- ``replace_active_same_class_instance`` (bool):  [Read-Write] if this is TRUE, when we try to push a new instance of an action who has the
      same class as the action on the top of the stack, pop the one on the stack, and push the new one
      NOTE: This trumps bAllowNewClassInstance (e.g. if this is true and bAllowNewClassInstance
      is false the active instance will still be replaced)
- ``should_pause_movement`` (bool):  [Read-Write] this is a temporary solution to allow having movement action running in background while there's
      another action on top doing its thing
  note: should go away once AI resource locking comes on-line

<a id="unreal.PawnAction_Move.goal_actor"></a>

#### goal_actor

```python
@property
def goal_actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.PawnAction_Move.goal_actor"></a>

#### goal_actor

```python
@goal_actor.setter
def goal_actor(value: Actor) -> None
```

<a id="unreal.PawnAction_Move.goal_location"></a>

#### goal_location

```python
@property
def goal_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PawnAction_Move.goal_location"></a>

#### goal_location

```python
@goal_location.setter
def goal_location(value: Vector) -> None
```

<a id="unreal.PawnAction_Move.acceptable_radius"></a>

#### acceptable_radius

```python
@property
def acceptable_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.PawnAction_Move.acceptable_radius"></a>

#### acceptable_radius

```python
@acceptable_radius.setter
def acceptable_radius(value: float) -> None
```

<a id="unreal.PawnAction_Move.filter_class"></a>

#### filter_class

```python
@property
def filter_class() -> Class
```

(type(Class)):  [Read-Write] "None" will result in default filter being used

<a id="unreal.PawnAction_Move.filter_class"></a>

#### filter_class

```python
@filter_class.setter
def filter_class(value: Class) -> None
```

<a id="unreal.PawnAction_Move.allow_strafe"></a>

#### allow_strafe

```python
@property
def allow_strafe() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PawnAction_Move.allow_strafe"></a>

#### allow_strafe

```python
@allow_strafe.setter
def allow_strafe(value: bool) -> None
```

<a id="unreal.PawnAction_Repeat"></a>