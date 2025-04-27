## CustomBoneAttributeLookup Objects

```python
class CustomBoneAttributeLookup(EnumBase)
```

Method used when retrieving a attribute value

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshComponent.h

<a id="unreal.CustomBoneAttributeLookup.BONE_ONLY"></a>

#### BONE_ONLY

0: Only look for the attribute using the provided bone (name)

<a id="unreal.CustomBoneAttributeLookup.IMMEDIATE_PARENT"></a>

#### IMMEDIATE_PARENT

1: Look for the attribute using the provided bone (name) and its direct parent bone

<a id="unreal.CustomBoneAttributeLookup.PARENT_HIERARCHY"></a>

#### PARENT_HIERARCHY

2: Look for the attribute using the provided bone (name) and its direct bone parent hierarchy up and until the root bone

<a id="unreal.RootMotionMode"></a>