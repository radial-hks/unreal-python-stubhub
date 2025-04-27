## SkelMeshMergeUVTransformMapping Objects

```python
class SkelMeshMergeUVTransformMapping(StructBase)
```

Info to map all the sections about how to transform their UVs

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshMerge.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``uv_transforms_per_mesh`` (Array[SkelMeshMergeMeshUVTransforms]):  [Read-Write] UV coordinates transform datam one entry for each Skeletal Mesh.

<a id="unreal.SkelMeshMergeUVTransformMapping.__init__"></a>

#### __init__

```python
def __init__(
        uv_transforms_per_mesh: Array[SkelMeshMergeMeshUVTransforms] = []
) -> None
```

<a id="unreal.SkelMeshMergeUVTransformMapping.uv_transforms_per_mesh"></a>

#### uv_transforms_per_mesh

```python
@property
def uv_transforms_per_mesh() -> Array[SkelMeshMergeMeshUVTransforms]
```

(Array[SkelMeshMergeMeshUVTransforms]):  [Read-Write] UV coordinates transform datam one entry for each Skeletal Mesh.

<a id="unreal.SkelMeshMergeUVTransformMapping.uv_transforms_per_mesh"></a>

#### uv_transforms_per_mesh

```python
@uv_transforms_per_mesh.setter
def uv_transforms_per_mesh(
        value: Array[SkelMeshMergeMeshUVTransforms]) -> None
```

<a id="unreal.SkeletalMaterial"></a>