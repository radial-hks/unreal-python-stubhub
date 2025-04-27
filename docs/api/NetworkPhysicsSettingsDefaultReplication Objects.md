## NetworkPhysicsSettingsDefaultReplication Objects

```python
class NetworkPhysicsSettingsDefaultReplication(StructBase)
```

Network Physics Settings Default Replication

**C++ Source:**

- **Module**: Engine
- **File**: NetworkPhysicsSettingsComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``correct_connected_bodies`` (bool):  [Read-Write] Overrides CVar: p.DefaultReplication.CorrectConnectedBodies -- When true, transform corrections will also apply to any connected physics object.
- ``correct_connected_bodies_friction`` (bool):  [Read-Write] Overrides CVar: p.DefaultReplication.CorrectConnectedBodiesFriction -- When true, transform correction on any connected physics object will also recalculate their friction.
- ``hardsnap_in_physics_thread`` (bool):  [Read-Write] Overrides CVar: p.DefaultReplication.Legacy.HardsnapInPT -- If default replication is used and it's running the legacy flow through Game Thread, allow hardsnapping to be performed on Physics Thread if async physics is enabled.
- ``max_linear_hard_snap_distance`` (float):  [Read-Write] Overrides CVar: p.MaxLinearHardSnapDistance -- Hardsnap if distance between current position and extrapolated target position is larger than this value.
- ``override_correct_connected_bodies`` (bool):  [Read-Write]
- ``override_correct_connected_bodies_friction`` (bool):  [Read-Write]
- ``override_default_legacy_hardsnap_in_pt`` (bool):  [Read-Write]
- ``override_max_linear_hard_snap_distance`` (bool):  [Read-Write]

<a id="unreal.NetworkPhysicsSettingsDefaultReplication.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NetworkPhysicsSettingsPredictiveInterpolation"></a>