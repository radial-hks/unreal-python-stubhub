## AnimPhysBodyDefinition Objects

```python
class AnimPhysBodyDefinition(StructBase)
```

Anim Phys Body Definition

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bound_bone`` (BoneReference):  [Read-Only]
- ``box_extents`` (Vector):  [Read-Write] Extents of the box to use for simulation
- ``collision_type`` (AnimPhysCollisionType):  [Read-Write] Resolution method for planar limits
- ``constraint_setup`` (AnimPhysConstraintSetup):  [Read-Write] Data describing the constraints we will apply to the body
- ``local_joint_offset`` (Vector):  [Read-Write] Vector relative to the body being simulated to attach the constraint to
- ``sphere_collision_radius`` (float):  [Read-Write] Radius to use if CollisionType is set to CustomSphere

<a id="unreal.AnimPhysBodyDefinition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimPhysSphericalLimit"></a>