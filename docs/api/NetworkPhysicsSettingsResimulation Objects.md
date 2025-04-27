## NetworkPhysicsSettingsResimulation Objects

```python
class NetworkPhysicsSettingsResimulation(StructBase)
```

Network Physics Settings Resimulation

**C++ Source:**

- **Module**: Engine
- **File**: NetworkPhysicsSettingsComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ang_vel_stability_multiplier`` (float):  [Read-Write] Overrides CVar: np2.Resim.AngVelStabilityMultiplier -- Recommended range between 0.0-1.0. Lower value means more stable angular velocity corrections.
- ``override_ang_vel_stability_multiplier`` (bool):  [Read-Write]
- ``override_pos_stability_multiplier`` (bool):  [Read-Write]
- ``override_resimulation_error_angular_velocity_threshold`` (bool):  [Read-Write]
- ``override_resimulation_error_linear_velocity_threshold`` (bool):  [Read-Write]
- ``override_resimulation_error_position_threshold`` (bool):  [Read-Write]
- ``override_resimulation_error_rotation_threshold`` (bool):  [Read-Write]
- ``override_rot_stability_multiplier`` (bool):  [Read-Write]
- ``override_runtime_correct_connected_bodies`` (bool):  [Read-Write]
- ``override_runtime_correction_enabled`` (bool):  [Read-Write]
- ``override_runtime_velocity_correction`` (bool):  [Read-Write]
- ``override_vel_stability_multiplier`` (bool):  [Read-Write]
- ``pos_stability_multiplier`` (float):  [Read-Write] Overrides CVar: np2.Resim.PosStabilityMultiplier -- Recommended range between 0.0-1.0. Lower value means more stable positional corrections.
- ``resimulation_error_angular_velocity_threshold`` (float):  [Read-Write] Overrides Project Settings -> Physics -> Replication -> Physics Prediction -> Resimulation Error Angular Velocity Threshold -- Degrees / second that the object is allowed to desync from the server before triggering a resimulation, within this threshold runtime correction can be performed if RuntimeCorrectionEnabled is true.
- ``resimulation_error_linear_velocity_threshold`` (float):  [Read-Write] Overrides Project Settings -> Physics -> Replication -> Physics Prediction -> Resimulation Error Linear Velocity Threshold -- Velocity difference in centimeters / second that the object is allowed to desync from the server before triggering a resimulation, within this threshold runtime correction can be performed if RuntimeCorrectionEnabled is true.
- ``resimulation_error_position_threshold`` (float):  [Read-Write] Overrides Project Settings -> Physics -> Replication -> Physics Prediction -> Resimulation Error Position Threshold -- Distance that the object is allowed to desync from the server before triggering a resimulation, within this threshold runtime correction can be performed if RuntimeCorrectionEnabled is true.
- ``resimulation_error_rotation_threshold`` (float):  [Read-Write] Overrides Project Settings -> Physics -> Replication -> Physics Prediction -> Resimulation Error Rotation Threshold -- Rotation difference in degrees that the object is allowed to desync from the server before triggering a resimulation, within this threshold runtime correction can be performed if RuntimeCorrectionEnabled is true.
- ``rot_stability_multiplier`` (float):  [Read-Write] Overrides CVar: np2.Resim.RotStabilityMultiplier -- Recommended range between 0.0-1.0. Lower value means more stable rotational corrections.
- ``runtime_correct_connected_bodies`` (bool):  [Read-Write] Overrides CVar: np2.Resim.RuntimeCorrectConnectedBodies -- If true runtime position and rotation correction will also shift transform of any connected physics objects. Used if RuntimeCorrectionEnabled is true.
- ``runtime_correction_enabled`` (bool):  [Read-Write] Overrides CVar: np2.Resim.RuntimeCorrectionEnabled -- Apply positional and rotational runtime corrections while within resim trigger distance.
- ``runtime_velocity_correction`` (bool):  [Read-Write] Overrides CVar: np2.Resim.RuntimeVelocityCorrection -- Apply linear and angular velocity corrections in runtime while within resim trigger distance. Used if RuntimeCorrectionEnabled is true.
- ``vel_stability_multiplier`` (float):  [Read-Write] Overrides CVar: np2.Resim.VelStabilityMultiplier -- Recommended range between 0.0-1.0. Lower value means more stable linear velocity corrections.

<a id="unreal.NetworkPhysicsSettingsResimulation.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NetworkPhysicsSettingsNetworkPhysicsComponent"></a>