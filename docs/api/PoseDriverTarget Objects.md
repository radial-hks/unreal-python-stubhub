## PoseDriverTarget Objects

```python
class PoseDriverTarget(StructBase)
```

Information about each target in the PoseDriver

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseDriver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_custom_curve`` (bool):  [Read-Write] If we should apply a custom curve mapping to how this target activates
- ``bone_transforms`` (Array[PoseDriverTransform]):  [Read-Write] Translation of this target
- ``custom_curve`` (RichCurve):  [Read-Write] Custom curve mapping to apply if bApplyCustomCurve is true
- ``distance_method`` (RBFDistanceMethod):  [Read-Write] Override for the distance method to use for each target
- ``driven_name`` (Name):  [Read-Write] Name of item to drive - depends on DriveOutput setting.
  If DriveOutput is DrivePoses, this should be the name of a pose in the assigned PoseAsset
  If DriveOutput is DriveCurves, this is the name of the curve (morph target, material param etc) to drive
- ``function_type`` (RBFFunctionType):  [Read-Write] Override for the function method to use for each target
- ``is_hidden`` (bool):  [Read-Write] If we should hide this pose from the UI
- ``target_rotation`` (Rotator):  [Read-Write] Rotation of this target
- ``target_scale`` (float):  [Read-Write] Scale applied to this target's function - a larger value will activate this target sooner

<a id="unreal.PoseDriverTarget.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimPhysBodyDefinition"></a>