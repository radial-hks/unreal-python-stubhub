## PoseSearchFeatureChannel_FilterCrashingLegs Objects

```python
class PoseSearchFeatureChannel_FilterCrashingLegs(PoseSearchFeatureChannel)
```

the idea is to calculate the angle between the direction from LeftThigh position to RightThigh position and the direction from LeftFoot position to RightFoot position, and divide it by PI to have values in range [-1,1]
the number (called 'CrashingLegsValue' calculated in ComputeCrashingLegsValue) is gonna be
0 if the feet are aligned with the thighs (for example in an idle standing position)
0.5 if the right foot is exactly in front of the left foot (for example when a character is running  following a line)
-0.5 if the left foot is exactly in front of the right foot
close to 1 or -1 if the feet (and so the legs) are completely crossed
at runtime we'll match the CrashingLegsValue and also filter by discarding pose candidates that don't respect the 'AllowedTolerance' between query and database values (happening in IsFilterValid)

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchFeatureChannel_FilterCrashingLegs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allowed_tolerance`` (float):  [Read-Write] if AllowedTolerance is zero the filter is disabled
- ``input_query_pose`` (InputQueryPose):  [Read-Write]
- ``left_foot`` (BoneReference):  [Read-Write]
- ``left_thigh`` (BoneReference):  [Read-Write]
- ``right_foot`` (BoneReference):  [Read-Write]
- ``right_thigh`` (BoneReference):  [Read-Write]
- ``sample_role`` (Name):  [Read-Write]
- ``weight`` (float):  [Read-Write]

<a id="unreal.PoseSearchFeatureChannel_GroupBase"></a>