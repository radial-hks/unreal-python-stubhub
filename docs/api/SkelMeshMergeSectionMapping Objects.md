## SkelMeshMergeSectionMapping Objects

```python
class SkelMeshMergeSectionMapping(StructBase)
```

Info to map all the sections from a single source skeletal mesh to
a final section entry in the merged skeletal mesh

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshMerge.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``section_i_ds`` (Array[int32]):  [Read-Write] indices to final section entries of the merged skel mesh

<a id="unreal.SkelMeshMergeSectionMapping.__init__"></a>

#### __init__

```python
def __init__(section_i_ds: Array[int] = []) -> None
```

<a id="unreal.SkelMeshMergeSectionMapping.section_i_ds"></a>

#### section_i_ds

```python
@property
def section_i_ds() -> Array[int]
```

(Array[int32]):  [Read-Write] indices to final section entries of the merged skel mesh

<a id="unreal.SkelMeshMergeSectionMapping.section_i_ds"></a>

#### section_i_ds

```python
@section_i_ds.setter
def section_i_ds(value: Array[int]) -> None
```

<a id="unreal.SkelMeshMergeMeshUVTransforms"></a>