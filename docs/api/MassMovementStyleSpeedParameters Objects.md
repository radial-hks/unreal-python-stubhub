## MassMovementStyleSpeedParameters Objects

```python
class MassMovementStyleSpeedParameters(StructBase)
```

Movement style consists of multiple speeds which are assigned to agents based on agents unique ID.
Same speed is assigned consistently for the same ID.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassMovement
- **File**: MassMovementTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``probability`` (float):  [Read-Write] Probability to assign this speed.
- ``speed`` (float):  [Read-Write] Desired speed
- ``variance`` (float):  [Read-Write] How much default desired speed is varied randomly.

<a id="unreal.MassMovementStyleSpeedParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ConstraintDrive"></a>