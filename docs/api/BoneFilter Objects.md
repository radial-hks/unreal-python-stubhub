## BoneFilter Objects

```python
class BoneFilter(StructBase)
```

Bone Filter

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshLODSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Write] Name of Bone Name
- ``exclude_self`` (bool):  [Read-Write] * Do not include the joint specified
  *
  * This option will work differently based on EBoneFilterActionOption
  * If EBoneFilterActionOption is Remove, it will exclude itself and only remove children
  * For example, if you specify hand, it will only include children of hand(all fingers),
  * not the hand itself if this is true
  *
  * But if the EBoneFilterActionOption is Keep, it will exclude itself but include all parents of it
  * You can't remove joint without children removed, and you can't keep without your parents

<a id="unreal.BoneFilter.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InputAxisProperties"></a>