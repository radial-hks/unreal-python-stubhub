## ConstraintSubsystem Objects

```python
class ConstraintSubsystem(EngineSubsystem)
```

Constraint Subsystem

**C++ Source:**

- **Module**: Constraints
- **File**: ConstraintSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_constraint_added_to_system_bp`` (OnConstraintAddedToSystem):  [Read-Write] BP Delegate fired when constraints are added
- ``on_constraint_removed_from_system_bp`` (OnConstraintRemovedFromSystem):  [Read-Write] BP Delegate fired when constraints are removed

<a id="unreal.ConstraintSubsystem.on_constraint_added_to_system_bp"></a>

#### on_constraint_added_to_system_bp

```python
@property
def on_constraint_added_to_system_bp() -> OnConstraintAddedToSystem
```

(OnConstraintAddedToSystem):  [Read-Write] BP Delegate fired when constraints are added

<a id="unreal.ConstraintSubsystem.on_constraint_added_to_system_bp"></a>

#### on_constraint_added_to_system_bp

```python
@on_constraint_added_to_system_bp.setter
def on_constraint_added_to_system_bp(value: OnConstraintAddedToSystem) -> None
```

<a id="unreal.ConstraintSubsystem.on_constraint_removed_from_system_bp"></a>

#### on_constraint_removed_from_system_bp

```python
@property
def on_constraint_removed_from_system_bp() -> OnConstraintRemovedFromSystem
```

(OnConstraintRemovedFromSystem):  [Read-Write] BP Delegate fired when constraints are removed

<a id="unreal.ConstraintSubsystem.on_constraint_removed_from_system_bp"></a>

#### on_constraint_removed_from_system_bp

```python
@on_constraint_removed_from_system_bp.setter
def on_constraint_removed_from_system_bp(
        value: OnConstraintRemovedFromSystem) -> None
```

<a id="unreal.ConstraintsActor"></a>