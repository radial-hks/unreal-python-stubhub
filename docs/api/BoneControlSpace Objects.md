## BoneControlSpace Objects

```python
class BoneControlSpace(EnumBase)
```

Enum for controlling which reference frame a controller is applied in.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.BoneControlSpace.BCS_WORLD_SPACE"></a>

#### BCS\_WORLD\_SPACE

0: Set absolute position of bone in world space.

<a id="unreal.BoneControlSpace.BCS_COMPONENT_SPACE"></a>

#### BCS\_COMPONENT\_SPACE

1: Set position of bone in SkeletalMeshComponent's reference frame.

<a id="unreal.BoneControlSpace.BCS_PARENT_BONE_SPACE"></a>

#### BCS\_PARENT\_BONE\_SPACE

2: Set position of bone relative to parent bone.

<a id="unreal.BoneControlSpace.BCS_BONE_SPACE"></a>

#### BCS\_BONE\_SPACE

3: Set position of bone in its own reference frame.

<a id="unreal.AnimInterpolationType"></a>