## AnimLegIKDefinition Objects

```python
class AnimLegIKDefinition(StructBase)
```

Per foot definitions

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_LegIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_knee_twist_correction`` (bool):  [Read-Write] Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation.
- ``enable_rotation_limit`` (bool):  [Read-Write] If enabled, we prevent the leg from bending backwards and enforce a min compression angle
- ``fk_foot_bone`` (BoneReference):  [Read-Write]
- ``foot_bone_forward_axis`` (AxisType):  [Read-Write] Forward Axis for Foot bone.
- ``hinge_rotation_axis`` (AxisType):  [Read-Write] Hinge Bones Rotation Axis. This is essentially the plane normal for (hip - knee - foot).
- ``ik_foot_bone`` (BoneReference):  [Read-Write]
- ``min_rotation_angle`` (float):  [Read-Write] Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,
  and forces at least this angle between Parent and Child bone.
- ``num_bones_in_limb`` (int32):  [Read-Write]
- ``twist_offset_curve_name`` (Name):  [Read-Write] Name of the curve to use as the twist offset angle(in degrees).
  This is useful for injecting knee motion, while keeping the IK chain's goal/hand and root/hip locked in place.
  Reasonable values are usually between -+15 degrees, although this is depends on how far in/out the knee is in the original pose.

<a id="unreal.AnimLegIKDefinition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Axis"></a>