## MassMovementStyleParameters Objects

```python
class MassMovementStyleParameters(StructBase)
```

Movement style parameters. A movement style abstracts movement properties for specific style. Behaviors can refer to specific styles when handling speeds.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassMovement
- **File**: MassMovementTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desired_speeds`` (Array[MassMovementStyleSpeedParameters]):  [Read-Write] Array of desired speeds (cm/s) assigned to agents based on probability.
- ``style`` (MassMovementStyleRef):  [Read-Write] Style of the movement

<a id="unreal.MassMovementStyleParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ZoneGraphDataHandle"></a>