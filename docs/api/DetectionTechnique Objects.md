## DetectionTechnique Objects

```python
class DetectionTechnique(EnumBase)
```

Detection method used for placing a notify / marker in the track

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: FootstepAnimEventsModifier.h

<a id="unreal.DetectionTechnique.PASS_THROUGH_REFERENCE_BONE"></a>

#### PASS_THROUGH_REFERENCE_BONE

0: Create anim event when foot bone passes through a given reference bone.

Note that the translation vector of the reference bone will be used as the normal vector for the detection plane
used to determine if the foot bone has crossed the reference bone.

<a id="unreal.DetectionTechnique.FOOT_BONE_REACHES_GROUND"></a>

#### FOOT_BONE_REACHES_GROUND

1: Create anim event when foot bone reaches the ground level within a given threshold.

Note that this will only be true if the foot bone position goes from NOT being within the threshold to being
WITHIN the ground threshold.

<a id="unreal.DetectionTechnique.FOOT_BONE_SPEED"></a>

#### FOOT_BONE_SPEED

2: Create anim event when foot bone translation speed is below a given threshold and nearly zero.

Note that the foot bone translation speed is normalize therefore when a footstep occurs
the speed will be very close to zero.

<a id="unreal.SplineType"></a>