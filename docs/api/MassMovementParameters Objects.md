## MassMovementParameters Objects

```python
class MassMovementParameters(MassConstSharedFragment)
```

Mass Movement Parameters

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassMovement
- **File**: MassMovementFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_desired_speed`` (float):  [Read-Write] Default desired speed (cm/s).
- ``default_desired_speed_variance`` (float):  [Read-Write] How much default desired speed is varied randomly.
- ``height_smoothing_time`` (float):  [Read-Write] The time it takes the entity position to catchup to the requested height.
- ``max_acceleration`` (float):  [Read-Write] 200..600 Smaller steering maximum acceleration makes the steering more \"calm\" but less opportunistic, may not find solution, or gets stuck.
- ``max_speed`` (float):  [Read-Write] Maximum speed (cm/s).
- ``movement_styles`` (Array[MassMovementStyleParameters]):  [Read-Write] List of supported movement styles for this configuration.

<a id="unreal.MassMovementParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MassReplicationParameters"></a>