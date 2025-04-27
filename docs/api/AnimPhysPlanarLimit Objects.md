## AnimPhysPlanarLimit Objects

```python
class AnimPhysPlanarLimit(StructBase)
```

Anim Phys Planar Limit

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``driving_bone`` (BoneReference):  [Read-Write] When using a driving bone, the plane transform will be relative to the bone transform
- ``plane_transform`` (Transform):  [Read-Write] Transform of the plane, this is either in component-space if no DrivinBone is specified
  or in bone-space if a driving bone is present.

<a id="unreal.AnimPhysPlanarLimit.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AngularRangeLimit"></a>