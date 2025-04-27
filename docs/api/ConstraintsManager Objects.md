## ConstraintsManager Objects

```python
class ConstraintsManager(Object)
```

UConstraintsManager
This object gathers the different static/nonanimated constraints of the level and is held by the ConstraintsActor (unique in the level)
Note in 5.4 all of the constraints are owned by the subsystem, so need to get that to get at animated constraints

**C++ Source:**

- **Module**: Constraints
- **File**: ConstraintsManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_constraint_added_bp`` (OnConstraintAdded):  [Read-Write] BP Delegate fired when constraints are added
- ``on_constraint_removed_bp`` (OnConstraintRemoved):  [Read-Write] BP Delegate fired when constraints are removed

<a id="unreal.ConstraintsManager.on_constraint_added_bp"></a>

#### on_constraint_added_bp

```python
@property
def on_constraint_added_bp() -> OnConstraintAdded
```

(OnConstraintAdded):  [Read-Write] BP Delegate fired when constraints are added

<a id="unreal.ConstraintsManager.on_constraint_added_bp"></a>

#### on_constraint_added_bp

```python
@on_constraint_added_bp.setter
def on_constraint_added_bp(value: OnConstraintAdded) -> None
```

<a id="unreal.ConstraintsManager.on_constraint_removed_bp"></a>

#### on_constraint_removed_bp

```python
@property
def on_constraint_removed_bp() -> OnConstraintRemoved
```

(OnConstraintRemoved):  [Read-Write] BP Delegate fired when constraints are removed

<a id="unreal.ConstraintsManager.on_constraint_removed_bp"></a>

#### on_constraint_removed_bp

```python
@on_constraint_removed_bp.setter
def on_constraint_removed_bp(value: OnConstraintRemoved) -> None
```

<a id="unreal.ConstraintsScriptingLibrary"></a>