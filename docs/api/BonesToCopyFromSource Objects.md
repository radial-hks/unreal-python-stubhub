## BonesToCopyFromSource Objects

```python
class BonesToCopyFromSource(EnumBase)
```

EBones to Copy from Source

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

<a id="unreal.BonesToCopyFromSource.ALL_BONES"></a>

#### ALL_BONES

0: Copy all bones from the source mesh to the target, regardless of whether they're bound or not.

<a id="unreal.BonesToCopyFromSource.ONLY_BOUND_AND_PARENTS"></a>

#### ONLY_BOUND_AND_PARENTS

1: Keep only bones that are actually bound to the target mesh, including all parent bones up to the root.

<a id="unreal.BonesToCopyFromSource.ONLY_BOUND_AND_ROOT"></a>

#### ONLY_BOUND_AND_ROOT

2: Keep only bones that are actually bound to the target mesh and the root bone. Any existing bones between
the two will not be copied. Bound bones will have their parent as either the root bone or another bound bone.

<a id="unreal.GeometryScriptBooleanOperation"></a>