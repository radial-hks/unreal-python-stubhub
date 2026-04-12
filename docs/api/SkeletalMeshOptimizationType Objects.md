## SkeletalMeshOptimizationType Objects

```python
class SkeletalMeshOptimizationType(EnumBase)
```

Enum specifying the reduction type to use when simplifying skeletal meshes with Simmplygon

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshReductionSettings.h

<a id="unreal.SkeletalMeshOptimizationType.SMOT_NUM_OF_TRIANGLES"></a>

#### SMOT\_NUM\_OF\_TRIANGLES

0: Triangle requirement will be used for simplification.

<a id="unreal.SkeletalMeshOptimizationType.SMOT_MAX_DEVIATION"></a>

#### SMOT\_MAX\_DEVIATION

1: Accuracy requirement will be used for simplification.

<a id="unreal.SkeletalMeshOptimizationType.SMOT_TRIANGLE_OR_DEVIATION"></a>

#### SMOT\_TRIANGLE\_OR\_DEVIATION

2: Simplification will continue until either Triangle or Accuracy requirement is met.

<a id="unreal.SkeletalMeshOptimizationImportance"></a>