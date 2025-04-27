## OutputTargetMeshBones Objects

```python
class OutputTargetMeshBones(EnumBase)
```

EOutput Target Mesh Bones

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

<a id="unreal.OutputTargetMeshBones.SOURCE_BONES"></a>

#### SOURCE_BONES

0: When transferring weights, the SourceMesh bone attriubtes will be copied over to the TargetMesh, replacing any
existing one, and transferred weights will be indexing the copied bone attributes.

<a id="unreal.OutputTargetMeshBones.TARGET_BONES"></a>

#### TARGET_BONES

1: When transferring weights, if the TargetMesh has bone attributes, then the transferred SourceMesh weights will be
reindexed with respect to the TargetMesh bones. In cases where a transferred SourceMesh weight refers to a bone
not present in the TargetMesh bone attributes, then that weight is simply skipped, and an error message with
information about the bone will be printed to the Output Log. For best results, the TargetMesh bone attributes
should be a superset of all the bones that are indexed by the transferred weights.

<a id="unreal.BonesToCopyFromSource"></a>