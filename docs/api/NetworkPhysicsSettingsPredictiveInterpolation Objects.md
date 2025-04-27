## NetworkPhysicsSettingsPredictiveInterpolation Objects

```python
class NetworkPhysicsSettingsPredictiveInterpolation(StructBase)
```

Network Physics Settings Predictive Interpolation

**C++ Source:**

- **Module**: Engine
- **File**: NetworkPhysicsSettingsComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``correct_connected_bodies`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.CorrectConnectedBodies -- When true, transform corrections will also apply to any connected physics object.
- ``correct_connected_bodies_friction`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.CorrectConnectedBodiesFriction -- When true, transform correction on any connected physics object will also recalculate their friction.
- ``disable_soft_snap`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.DisableSoftSnap -- When true, predictive interpolation will not use softsnap to correct the replication with when velocity fails. Hardsnap will still eventually kick in if replication can't reach the target.
- ``override_correct_connected_bodies`` (bool):  [Read-Write]
- ``override_correct_connected_bodies_friction`` (bool):  [Read-Write]
- ``override_disable_soft_snap`` (bool):  [Read-Write]
- ``override_pos_correction_time_base`` (bool):  [Read-Write]
- ``override_pos_correction_time_min`` (bool):  [Read-Write]
- ``override_pos_correction_time_multiplier`` (bool):  [Read-Write]
- ``override_pos_interpolation_time_multiplier`` (bool):  [Read-Write]
- ``override_post_resim_wait_for_update`` (bool):  [Read-Write]
- ``override_rot_correction_time_base`` (bool):  [Read-Write]
- ``override_rot_correction_time_min`` (bool):  [Read-Write]
- ``override_rot_correction_time_multiplier`` (bool):  [Read-Write]
- ``override_rot_interpolation_time_multiplier`` (bool):  [Read-Write]
- ``override_skip_velocity_rep_on_pos_early_out`` (bool):  [Read-Write]
- ``override_soft_snap_pos_strength`` (bool):  [Read-Write]
- ``override_soft_snap_rot_strength`` (bool):  [Read-Write]
- ``override_soft_snap_to_source`` (bool):  [Read-Write]
- ``pos_correction_time_base`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.PosCorrectionTimeBase -- Base time to correct positional offset over. RoundTripTime * PosCorrectionTimeMultiplier is added on top of this.
- ``pos_correction_time_min`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.PosCorrectionTimeMin -- Min time to correct positional offset over. DeltaSeconds is added on top of this.
- ``pos_correction_time_multiplier`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.PosCorrectionTimeMultiplier -- Multiplier to adjust how much of RoundTripTime to add to positional offset correction.
- ``pos_interpolation_time_multiplier`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.InterpolationTimeMultiplier -- Multiplier to adjust the interpolation time which is based on the sendrate of state data from the server.
- ``post_resim_wait_for_update`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.PostResimWaitForUpdate -- After a resimulation, wait for replicated states that correspond to post-resim state before processing replication again.
- ``rot_correction_time_base`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.RotCorrectionTimeBase -- Base time to correct rotational offset over. RoundTripTime * RotCorrectionTimeMultiplier is added on top of this.
- ``rot_correction_time_min`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.RotCorrectionTimeMin -- Min time to correct rotational offset over. DeltaSeconds is added on top of this.
- ``rot_correction_time_multiplier`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.RotCorrectionTimeMultiplier -- Multiplier to adjust how much of RoundTripTime to add to rotational offset correction.
- ``rot_interpolation_time_multiplier`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.RotInterpolationTimeMultiplier -- Multiplier to adjust the rotational interpolation time which is based on the sendrate of state data from the server.
- ``skip_velocity_rep_on_pos_early_out`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.SkipVelocityRepOnPosEarlyOut -- If true, don't run linear velocity replication if position can early out but angular can't early out.
- ``soft_snap_pos_strength`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.SoftSnapPosStrength -- Value in percent between 0.0 - 1.0 representing how much to softsnap each tick of the remaining positional distance.
- ``soft_snap_rot_strength`` (float):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.SoftSnapRotStrength -- Value in percent between 0.0 - 1.0 representing how much to softsnap each tick of the remaining rotational distance.
- ``soft_snap_to_source`` (bool):  [Read-Write] Overrides CVar: np2.PredictiveInterpolation.SoftSnapToSource -- If true, softsnap will be performed towards the source state of the current target instead of the predicted state of the current target.

<a id="unreal.NetworkPhysicsSettingsPredictiveInterpolation.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NetworkPhysicsSettingsResimulation"></a>