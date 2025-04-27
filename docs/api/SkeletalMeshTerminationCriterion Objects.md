## SkeletalMeshTerminationCriterion Objects

```python
class SkeletalMeshTerminationCriterion(EnumBase)
```

Enum specifying the reduction type to use when simplifying skeletal meshes with internal tool

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshReductionSettings.h

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_NUM_OF_TRIANGLES"></a>

#### SMTC_NUM_OF_TRIANGLES

0: Triangle count criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_NUM_OF_VERTS"></a>

#### SMTC_NUM_OF_VERTS

1: Vertex cont criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_TRIANGLE_OR_VERT"></a>

#### SMTC_TRIANGLE_OR_VERT

2: Simplification will continue until either Triangle or Vertex count criteria is met.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_NUM_OF_TRIANGLES"></a>

#### SMTC_ABS_NUM_OF_TRIANGLES

3: Triangle count criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_NUM_OF_VERTS"></a>

#### SMTC_ABS_NUM_OF_VERTS

4: Vertex cont criterion will be used for simplification.

<a id="unreal.SkeletalMeshTerminationCriterion.SMTC_ABS_TRIANGLE_OR_VERT"></a>

#### SMTC_ABS_TRIANGLE_OR_VERT

5: Simplification will continue until either Triangle or Vertex count criteria is met.

<a id="unreal.SkeletalMeshOptimizationType"></a>