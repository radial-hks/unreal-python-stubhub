## BoneRotationSource Objects

```python
class BoneRotationSource(EnumBase)
```

Enum for specifying the source of a bone's rotation.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.BoneRotationSource.BRS_KEEP_COMPONENT_SPACE_ROTATION"></a>

#### BRS_KEEP_COMPONENT_SPACE_ROTATION

0: Don't change rotation at all.

<a id="unreal.BoneRotationSource.BRS_KEEP_LOCAL_SPACE_ROTATION"></a>

#### BRS_KEEP_LOCAL_SPACE_ROTATION

1: Keep forward direction vector relative to the parent bone.

<a id="unreal.BoneRotationSource.BRS_COPY_FROM_TARGET"></a>

#### BRS_COPY_FROM_TARGET

2: Copy rotation of target to bone.

<a id="unreal.InterpolationBlend"></a>