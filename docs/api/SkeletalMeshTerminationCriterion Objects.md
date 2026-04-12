## SkeletalMeshTerminationCriterion Objects

```python
class SkeletalMeshTerminationCriterion(EnumBase)
```

Enum specifying the reduction type to use when simplifying skeletal meshes with internal tool

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshReductionSettings.h

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_NUM_OF_TRIANGLES"></a>

#### SMTC\_NUM\_OF\_TRIANGLES

0: Triangle count criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_NUM_OF_VERTS"></a>

#### SMTC\_NUM\_OF\_VERTS

1: Vertex cont criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_TRIANGLE_OR_VERT"></a>

#### SMTC\_TRIANGLE\_OR\_VERT

2: Simplification will continue until either Triangle or Vertex count criteria is met.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_NUM_OF_TRIANGLES"></a>

#### SMTC\_ABS\_NUM\_OF\_TRIANGLES

3: Triangle count criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_NUM_OF_VERTS"></a>

#### SMTC\_ABS\_NUM\_OF\_VERTS

4: Vertex cont criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_TRIANGLE_OR_VERT"></a>

#### SMTC\_ABS\_TRIANGLE\_OR\_VERT

5: Simplification will continue until either Triangle or Vertex count criteria is met.

<a id="unreal.SkeletalMeshOptimizationType"></a>