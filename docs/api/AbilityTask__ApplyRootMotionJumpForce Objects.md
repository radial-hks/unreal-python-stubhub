## AbilityTask\_ApplyRootMotionJumpForce Objects

```python
class AbilityTask_ApplyRootMotionJumpForce(AbilityTask_ApplyRootMotion_Base)
```

Applies force to character's movement

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_ApplyRootMotionJumpForce.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_finish`` (ApplyRootMotionJumpForceDelegate):  [Read-Write]
- ``on_landed`` (ApplyRootMotionJumpForceDelegate):  [Read-Write]

<a id="unreal.AbilityTask_ApplyRootMotionJumpForce.on_finish"></a>

#### on\_finish

```python
@property
def on_finish() -> ApplyRootMotionJumpForceDelegate
```

(ApplyRootMotionJumpForceDelegate):  [Read-Write]

<a id="unreal.AbilityTask_ApplyRootMotionJumpForce.on_finish"></a>

#### on\_finish

```python
@on_finish.setter
def on_finish(value: ApplyRootMotionJumpForceDelegate) -> None
```

<a id="unreal.AbilityTask_ApplyRootMotionJumpForce.on_landed"></a>

#### on\_landed

```python
@property
def on_landed() -> ApplyRootMotionJumpForceDelegate
```

(ApplyRootMotionJumpForceDelegate):  [Read-Write]

<a id="unreal.AbilityTask_ApplyRootMotionJumpForce.on_landed"></a>

#### on\_landed

```python
@on_landed.setter
def on_landed(value: ApplyRootMotionJumpForceDelegate) -> None
```

<a id="unreal.AbilityTask_ApplyRootMotionJumpForce.finish"></a>

#### finish

```python
def finish() -> None
```

x.finish() -> None
Finish

<a id="unreal.AbilityTask_ApplyRootMotionMoveToActorForce"></a>