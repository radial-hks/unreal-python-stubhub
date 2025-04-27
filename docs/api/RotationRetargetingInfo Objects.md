## RotationRetargetingInfo Objects

```python
class RotationRetargetingInfo(StructBase)
```

The FRotationRetargetingInfo is used to provide all of the
settings required to perform rotational retargeting on a single
transform.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: CommonAnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clamp`` (bool):  [Read-Write] If set to true the value for the easing will be clamped between 0.0 and 1.0
- ``custom_curve`` (RuntimeFloatCurve):  [Read-Write] Custom curve mapping to apply if bApplyCustomCurve is true
- ``easing_type`` (EasingFuncType):  [Read-Write] The easing to use - pick linear if you don't want to apply any easing
- ``easing_weight`` (float):  [Read-Write] The amount of easing to apply (value should be 0.0 to 1.0)
- ``enabled`` (bool):  [Read-Write] Set to true this enables retargeting
- ``flip_easing`` (bool):  [Read-Write] If set to true the interpolation value for the easing will be flipped (1.0 - Value)
- ``rotation_component`` (RotationComponent):  [Read-Write] The rotation component to perform retargeting with
- ``source`` (Transform):  [Read-Write] The source transform of the frame of reference. The rotation is made relative to this space
- ``source_maximum`` (float):  [Read-Write] The maximum value of the source angle in degrees
- ``source_minimum`` (float):  [Read-Write] The minimum value of the source angle in degrees
- ``target`` (Transform):  [Read-Write] The target transform to project the rotation. In most cases this is the same as Source
- ``target_maximum`` (float):  [Read-Write] The target value of the target angle in degrees (can be the same as SourceMaximum)
- ``target_minimum`` (float):  [Read-Write] The minimum value of the target angle in degrees (can be the same as SourceMinimum)
- ``twist_axis`` (Vector):  [Read-Write] In case the rotation component is SwingAngle or TwistAngle this vector is used as the twist axis
- ``use_absolute_angle`` (bool):  [Read-Write] If set to true the angle will be always positive, thus resulting in mirrored rotation both ways

<a id="unreal.RotationRetargetingInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RuntimeFloatCurve"></a>