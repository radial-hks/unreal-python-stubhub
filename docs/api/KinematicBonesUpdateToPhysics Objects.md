## KinematicBonesUpdateToPhysics Objects

```python
class KinematicBonesUpdateToPhysics(EnumBase)
```

This enum defines how you'd like to update bones to physics world.
      If bone is simulating, you don't have to waste time on updating bone transform from kinematic.
      But also sometimes you don't like fixed bones to be updated by animation data.

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshComponent.h

<a id="unreal.KinematicBonesUpdateToPhysics.SKIP_SIMULATING_BONES"></a>

#### SKIP_SIMULATING_BONES

0: Update any bones that are not simulating.

<a id="unreal.KinematicBonesUpdateToPhysics.SKIP_ALL_BONES"></a>

#### SKIP_ALL_BONES

1: Skip physics update from kinematic changes.

<a id="unreal.PhysicsTransformUpdateMode"></a>