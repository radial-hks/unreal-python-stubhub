## AnimPhysSphericalLimit Objects

```python
class AnimPhysSphericalLimit(StructBase)
```

Anim Phys Spherical Limit

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``driving_bone`` (BoneReference):  [Read-Write] Bone to attach the sphere to
- ``limit_radius`` (float):  [Read-Write] Radius of the sphere
- ``limit_type`` (SphericalLimitType):  [Read-Write] Whether to lock bodies inside or outside of the sphere
- ``sphere_local_offset`` (Vector):  [Read-Write] Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space

<a id="unreal.AnimPhysSphericalLimit.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimPhysPlanarLimit"></a>