## SkelMeshMergeMeshUVTransforms Objects

```python
class SkelMeshMergeMeshUVTransforms(StructBase)
```

Skel Mesh Merge Mesh UVTransforms

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshMerge.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``uv_transforms`` (Array[Transform]):  [Read-Write] A list of how UVs should be transformed on a given mesh, where index represents a specific UV channel.

<a id="unreal.SkelMeshMergeMeshUVTransforms.__init__"></a>

#### \_\_init\_\_

```python
def __init__(uv_transforms: Array[Transform] = []) -> None
```

<a id="unreal.SkelMeshMergeMeshUVTransforms.uv_transforms"></a>

#### uv\_transforms

```python
@property
def uv_transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] A list of how UVs should be transformed on a given mesh, where index represents a specific UV channel.

<a id="unreal.SkelMeshMergeMeshUVTransforms.uv_transforms"></a>

#### uv\_transforms

```python
@uv_transforms.setter
def uv_transforms(value: Array[Transform]) -> None
```

<a id="unreal.SkelMeshMergeUVTransformMapping"></a>