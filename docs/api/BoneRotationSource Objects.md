## BoneRotationSource Objects

```python
class BoneRotationSource(EnumBase)
```

Enum for specifying the source of a bone's rotation.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.BoneRotationSource.BRS_KEEP_COMPONENT_SPACE_ROTATION"></a>

#### BRS\_KEEP\_COMPONENT\_SPACE\_ROTATION

0: Don't change rotation at all.

<a id="unreal.BoneRotationSource.BRS_KEEP_LOCAL_SPACE_ROTATION"></a>

#### BRS\_KEEP\_LOCAL\_SPACE\_ROTATION

1: Keep forward direction vector relative to the parent bone.

<a id="unreal.BoneRotationSource.BRS_COPY_FROM_TARGET"></a>

#### BRS\_COPY\_FROM\_TARGET

2: Copy rotation of target to bone.

<a id="unreal.InterpolationBlend"></a>