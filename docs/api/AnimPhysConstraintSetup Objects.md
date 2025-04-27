## AnimPhysConstraintSetup Objects

```python
class AnimPhysConstraintSetup(StructBase)
```

Constraint setup struct, holds data required to build a physics constraint

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_constraint_type`` (AnimPhysAngularConstraintType):  [Read-Write] Method to use when constraining angular motion
- ``angular_limits_max`` (Vector):  [Read-Write]
- ``angular_limits_min`` (Vector):  [Read-Write]
- ``angular_target`` (Vector):  [Read-Write] The axis to align the angular spring constraint to in the animation pose.
  This typically points down the bone - so values of (1.0, 0.0, 0.0) are common,
  but you can pick other values to align the spring to a different direction.
  Note: This is affected by the Angular Spring Constant.
- ``angular_target_axis`` (AnimPhysTwistAxis):  [Read-Write] The axis in the simulation pose to align to the Angular Target.
  This is typically the axis pointing along the bone.
  Note: This is affected by the Angular Spring Constant.
- ``cone_angle`` (float):  [Read-Write] Angle to use when constraining using a cone
- ``linear_axes_max`` (Vector):  [Read-Write] Maximum linear movement per-axis (Set zero here and in the min limit to lock)
- ``linear_axes_min`` (Vector):  [Read-Write] Minimum linear movement per-axis (Set zero here and in the max limit to lock)
- ``linear_x_limit_type`` (AnimPhysLinearConstraintType):  [Read-Write] Whether to limit the linear X axis
- ``linear_y_limit_type`` (AnimPhysLinearConstraintType):  [Read-Write] Whether to limit the linear Y axis
- ``linear_z_limit_type`` (AnimPhysLinearConstraintType):  [Read-Write] Whether to limit the linear Z axis
- ``twist_axis`` (AnimPhysTwistAxis):  [Read-Write] Axis to consider for twist when constraining angular motion (forward axis)

<a id="unreal.AnimPhysConstraintSetup.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SocketReference"></a>