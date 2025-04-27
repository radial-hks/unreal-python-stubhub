## PhysicsReplicationResimulationSettings Objects

```python
class PhysicsReplicationResimulationSettings(StructBase)
```

Default settings for physics replication using EPhysicsReplicationMode::Resimulation

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_resimulation_error_angular_velocity_threshold`` (bool):  [Read-Write] Enable angular velocity error threshold to trigger resimulation
- ``enable_resimulation_error_linear_velocity_threshold`` (bool):  [Read-Write] Enable linear velocity error threshold to trigger resimulation
- ``enable_resimulation_error_position_threshold`` (bool):  [Read-Write] Enable positional error threshold to trigger resimulation
- ``enable_resimulation_error_rotation_threshold`` (bool):  [Read-Write] Enable rotational error threshold to trigger resimulation
- ``resimulation_error_angular_velocity_threshold`` (float):  [Read-Write] Velocity degrees / second before a state discrepancy triggers a resimulation
- ``resimulation_error_linear_velocity_threshold`` (float):  [Read-Write] Velocity difference in centimeters / second before a state discrepancy triggers a resimulation
- ``resimulation_error_position_threshold`` (float):  [Read-Write] Distance in centimeters before a state discrepancy triggers a resimulation
- ``resimulation_error_rotation_threshold`` (float):  [Read-Write] Rotation difference in degrees before a state discrepancy triggers a resimulation

<a id="unreal.PhysicsReplicationResimulationSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SkeletalMeshOptimizationSettings"></a>