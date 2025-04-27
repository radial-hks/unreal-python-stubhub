## SkeletalMeshSamplingRegionBoneFilter Objects

```python
class SkeletalMeshSamplingRegionBoneFilter(StructBase)
```

Filter to include or exclude bones and their associated triangles from a sampling region.

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshSampling.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_to_children`` (bool):  [Read-Write] If true, this filter will apply to all children of this bone as well.
- ``bone_name`` (Name):  [Read-Write]
- ``include_or_exclude`` (bool):  [Read-Write] If true, this filter will include bones. If false, it will exclude them.

<a id="unreal.SkeletalMeshSamplingRegionBoneFilter.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraSystemVisibilityCullingSettings"></a>